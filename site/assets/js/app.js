/* =========================================================================
   PICCARDO · comportamenti di interfaccia
   Vanilla, nessuna dipendenza. Ogni modulo esce silenziosamente se il
   componente non è presente nella pagina.
   ========================================================================= */
(() => {
  'use strict';

  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const RIDOTTO = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Header: sfondo allo scroll + nascondi scendendo ---------------- */
  const header = $('.header');
  if (header) {
    let last = 0, ticking = false;
    const onScroll = () => {
      const y = window.scrollY;
      header.classList.toggle('is-stuck', y > 12);
      if (!$('.drawer.is-open')) {
        header.classList.toggle('is-hidden', y > 420 && y > last && !header.matches(':focus-within'));
      }
      last = y;
      ticking = false;
    };
    addEventListener('scroll', () => {
      if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
    }, { passive: true });
    onScroll();
  }

  /* ---- Mega menu ------------------------------------------------------ */
  $$('.nav__item.has-mega').forEach(item => {
    const btn = $('.nav__link', item);
    let timer;
    const apri  = () => { clearTimeout(timer); chiudiTutti(item); item.classList.add('is-open'); btn?.setAttribute('aria-expanded', 'true'); };
    const chiudi = () => { item.classList.remove('is-open'); btn?.setAttribute('aria-expanded', 'false'); };
    const chiudiTutti = (tranne) => $$('.nav__item.is-open').forEach(o => { if (o !== tranne) { o.classList.remove('is-open'); $('.nav__link', o)?.setAttribute('aria-expanded', 'false'); } });

    item.addEventListener('mouseenter', apri);
    item.addEventListener('mouseleave', () => { timer = setTimeout(chiudi, 130); });
    btn?.addEventListener('click', e => { e.preventDefault(); item.classList.contains('is-open') ? chiudi() : apri(); });
    item.addEventListener('focusin', apri);
    item.addEventListener('focusout', e => { if (!item.contains(e.relatedTarget)) chiudi(); });
  });
  addEventListener('keydown', e => {
    if (e.key === 'Escape') $$('.nav__item.is-open').forEach(o => o.classList.remove('is-open'));
  });

  /* ---- Drawer mobile -------------------------------------------------- */
  const burger = $('.burger'), drawer = $('.drawer');
  if (burger && drawer) {
    burger.addEventListener('click', () => {
      const aperto = drawer.classList.toggle('is-open');
      burger.classList.toggle('is-open', aperto);
      burger.setAttribute('aria-expanded', String(aperto));
      document.body.style.overflow = aperto ? 'hidden' : '';
      if (aperto) header?.classList.remove('is-hidden');
    });
    $$('.drawer__head').forEach(h => {
      h.addEventListener('click', () => {
        const g = h.closest('.drawer__group');
        const era = g.classList.contains('is-open');
        $$('.drawer__group').forEach(x => { x.classList.remove('is-open'); $('.drawer__head', x)?.setAttribute('aria-expanded', 'false'); });
        if (!era) { g.classList.add('is-open'); h.setAttribute('aria-expanded', 'true'); }
      });
    });
    $$('.drawer a').forEach(a => a.addEventListener('click', () => {
      drawer.classList.remove('is-open');
      burger.classList.remove('is-open');
      document.body.style.overflow = '';
    }));
  }

  /* ---- Barra sticky mobile: compare dopo il primo scroll -------------- */
  const bar = $('.mobile-bar');
  if (bar) {
    const mostra = () => bar.classList.toggle('is-in', window.scrollY > 260);
    addEventListener('scroll', mostra, { passive: true });
    mostra();
  }

  /* ---- Reveal allo scroll --------------------------------------------- */
  const daRivelare = $$('[data-reveal]');
  if (daRivelare.length) {
    if (RIDOTTO || !('IntersectionObserver' in window)) {
      daRivelare.forEach(el => el.classList.add('is-in'));
    } else {
      const io = new IntersectionObserver((voci, obs) => {
        voci.forEach(v => {
          if (!v.isIntersecting) return;
          v.target.classList.add('is-in');
          obs.unobserve(v.target);
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      daRivelare.forEach(el => io.observe(el));
    }
  }
  /* scaglionamento automatico dei figli di un gruppo */
  $$('[data-stagger]').forEach(g => {
    const passo = Number(g.dataset.stagger) || 70;
    Array.from(g.children).forEach((c, i) => {
      if (c.hasAttribute('data-reveal')) c.style.setProperty('--d', `${i * passo}ms`);
    });
  });

  /* ---- Contatori ------------------------------------------------------ */
  const contatori = $$('[data-count]');
  if (contatori.length) {
    const anima = el => {
      const fine = parseFloat(el.dataset.count);
      const dec = (el.dataset.count.split('.')[1] || '').length;
      const pre = el.dataset.pre || '', post = el.dataset.post || '';
      // data-plain: niente separatore delle migliaia (anni, codici)
      const fmt = n => el.hasAttribute('data-plain')
        ? n.toFixed(dec).replace('.', ',')
        : n.toLocaleString('it-IT', { minimumFractionDigits: dec, maximumFractionDigits: dec });
      if (RIDOTTO) { el.textContent = pre + fmt(fine) + post; return; }
      const durata = 1500, t0 = performance.now();
      const tick = t => {
        const p = Math.min(1, (t - t0) / durata);
        const e = 1 - Math.pow(1 - p, 3);
        el.textContent = pre + fmt(fine * e) + post;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };
    const io = new IntersectionObserver((v, o) => v.forEach(x => {
      if (x.isIntersecting) { anima(x.target); o.unobserve(x.target); }
    }), { threshold: 0.5 });
    contatori.forEach(c => io.observe(c));
  }

  /* ---- Tab per intenzione --------------------------------------------- */
  $$('[data-tabs]').forEach(root => {
    const tabs = $$('[role="tab"]', root);
    const pannelli = $$('[role="tabpanel"]', root);
    const attiva = (i, focus = false) => {
      tabs.forEach((t, k) => {
        t.setAttribute('aria-selected', String(k === i));
        t.tabIndex = k === i ? 0 : -1;
      });
      pannelli.forEach((p, k) => p.hidden = k !== i);
      if (focus) tabs[i].focus();
    };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => attiva(i));
      t.addEventListener('keydown', e => {
        const m = { ArrowRight: 1, ArrowLeft: -1, Home: -Infinity, End: Infinity }[e.key];
        if (m === undefined) return;
        e.preventDefault();
        const n = !isFinite(m) ? (m < 0 ? 0 : tabs.length - 1) : (i + m + tabs.length) % tabs.length;
        attiva(n, true);
      });
    });
    attiva(0);
  });

  /* ---- Slider prima / dopo -------------------------------------------- */
  $$('.ba').forEach(ba => {
    let attivo = false;
    let anim = null;

    const sposta = p => {
      ba.style.setProperty('--pos', p + '%');
      ba.setAttribute('aria-valuenow', Math.round(p));
    };
    // Il primo contatto ferma qualunque dimostrazione in corso: da lì in poi
    // il cursore appartiene a chi guarda.
    const preso = () => {
      if (ba.classList.contains('is-touched')) return;
      ba.classList.add('is-touched');
      if (anim) { cancelAnimationFrame(anim); anim = null; }
    };
    const imposta = clientX => {
      const r = ba.getBoundingClientRect();
      sposta(Math.max(2, Math.min(98, ((clientX - r.left) / r.width) * 100)));
    };
    const giu = e => { preso(); attivo = true; imposta((e.touches ? e.touches[0] : e).clientX); };
    const muovi = e => { if (attivo) imposta((e.touches ? e.touches[0] : e).clientX); };
    const su = () => { attivo = false; };

    ba.addEventListener('mousedown', giu);
    ba.addEventListener('touchstart', giu, { passive: true });
    addEventListener('mousemove', muovi);
    addEventListener('touchmove', muovi, { passive: true });
    addEventListener('mouseup', su);
    addEventListener('touchend', su);
    ba.addEventListener('mousemove', e => {
      if (('ontouchstart' in window)) return;
      preso();
      imposta(e.clientX);
    });

    ba.tabIndex = 0;
    ba.setAttribute('role', 'slider');
    ba.setAttribute('aria-label', 'Confronta prima e dopo');
    ba.setAttribute('aria-valuemin', '0');
    ba.setAttribute('aria-valuemax', '100');
    ba.setAttribute('aria-valuenow', '50');
    ba.addEventListener('focus', preso);
    ba.addEventListener('keydown', e => {
      const d = { ArrowLeft: -4, ArrowRight: 4, Home: -100, End: 100 }[e.key];
      if (d === undefined) return;
      e.preventDefault();
      preso();
      const cur = parseFloat(getComputedStyle(ba).getPropertyValue('--pos')) || 50;
      sposta(Math.max(2, Math.min(98, cur + d)));
    });

    /* Dimostrazione automatica: quando il confronto entra nello schermo il
       cursore fa una passata sola, così si capisce che è mobile senza
       leggerlo da nessuna parte. */
    if (!ba.hasAttribute('data-autohint') || RIDOTTO || !('IntersectionObserver' in window)) return;

    const tappe = [[0, 50], [.30, 76], [.72, 26], [1, 50]];
    const passata = () => {
      const durata = 2000, t0 = performance.now();
      const frame = ora => {
        if (ba.classList.contains('is-touched')) { anim = null; return; }
        const k = Math.min(1, (ora - t0) / durata);
        let i = 1;
        while (i < tappe.length - 1 && k > tappe[i][0]) i++;
        const [k0, p0] = tappe[i - 1], [k1, p1] = tappe[i];
        const f = (k - k0) / (k1 - k0);
        const e = f < .5 ? 2 * f * f : 1 - Math.pow(-2 * f + 2, 2) / 2;
        sposta(p0 + (p1 - p0) * e);
        anim = k < 1 ? requestAnimationFrame(frame) : null;
      };
      anim = requestAnimationFrame(frame);
    };

    const osserva = new IntersectionObserver(voci => {
      voci.forEach(v => {
        if (!v.isIntersecting) return;
        osserva.disconnect();
        setTimeout(passata, 320);
      });
    }, { threshold: .55 });
    osserva.observe(ba);
  });

  /* ---- Accordion ------------------------------------------------------ */
  $$('.acc').forEach(acc => {
    const solouno = acc.hasAttribute('data-single');
    $$('.acc__btn', acc).forEach(btn => {
      btn.addEventListener('click', () => {
        const item = btn.closest('.acc__item');
        const era = item.classList.contains('is-open');
        if (solouno) $$('.acc__item', acc).forEach(i => {
          i.classList.remove('is-open');
          $('.acc__btn', i)?.setAttribute('aria-expanded', 'false');
        });
        item.classList.toggle('is-open', !era);
        btn.setAttribute('aria-expanded', String(!era));
      });
    });
  });

  /* ---- Tariffario: ricerca + filtro categoria ------------------------- */
  const tabella = $('#tariffario');
  if (tabella) {
    const input = $('#tariff-q');
    const chip = $$('[data-tariff-cat]');
    let cat = 'tutte';

    const filtra = () => {
      const q = (input?.value || '').trim().toLowerCase();
      let visibiliPerCat = {};
      $$('.tariff-row', tabella).forEach(r => {
        const testo = r.dataset.nome.toLowerCase();
        const okQ = !q || testo.includes(q);
        const okC = cat === 'tutte' || r.dataset.cat === cat;
        const ok = okQ && okC;
        r.classList.toggle('is-hidden', !ok);
        if (ok) visibiliPerCat[r.dataset.cat] = true;
      });
      $$('.tariff-cat', tabella).forEach(h => h.classList.toggle('is-hidden', !visibiliPerCat[h.dataset.cat]));
      const vuoto = $('#tariff-empty');
      if (vuoto) vuoto.hidden = Object.keys(visibiliPerCat).length > 0;
    };

    input?.addEventListener('input', filtra);
    chip.forEach(c => c.addEventListener('click', () => {
      cat = c.dataset.tariffCat;
      chip.forEach(x => x.setAttribute('aria-pressed', String(x === c)));
      filtra();
    }));
  }

  /* ---- Calcolatore finanziamento -------------------------------------- */
  const calc = $('#calc');
  if (calc) {
    const range = $('#calc-importo', calc);
    const outImporto = $('#calc-importo-val', calc);
    const outRata = $('#calc-rata', calc);
    const outNota = $('#calc-nota', calc);
    const bottoni = $$('[data-mesi]', calc);
    let mesi = 36;

    const euro = n => n.toLocaleString('it-IT', { maximumFractionDigits: 0 });

    const aggiorna = () => {
      const imp = Number(range.value);
      const pct = ((imp - range.min) / (range.max - range.min)) * 100;
      range.style.setProperty('--fill', pct + '%');
      outImporto.textContent = euro(imp) + ' €';
      // Tasso 0 fino a 5.000 €. Oltre: tasso agevolato, stima prudenziale TAN 4,9%.
      let rata;
      if (imp <= 5000) {
        rata = imp / mesi;
        outNota.textContent = 'Tasso 0 · TAN 0%, importo fino a 5.000 €';
      } else {
        const i = 0.049 / 12;
        rata = (imp * i) / (1 - Math.pow(1 + i, -mesi));
        outNota.textContent = 'Tasso agevolato · stima indicativa su TAN 4,9%';
      }
      outRata.textContent = euro(Math.round(rata));
    };

    range.addEventListener('input', aggiorna);
    bottoni.forEach(b => b.addEventListener('click', () => {
      mesi = Number(b.dataset.mesi);
      bottoni.forEach(x => x.setAttribute('aria-pressed', String(x === b)));
      aggiorna();
    }));
    aggiorna();
  }

  /* ---- Drawer scheda persona ------------------------------------------ */
  const pd = $('#person-drawer');
  if (pd) {
    const panel = $('.person-drawer__panel', pd);
    const body = $('.person-drawer__body', pd);
    let ultimoTrigger = null;

    const apri = (btn) => {
      const src = document.getElementById(btn.dataset.person);
      if (!src) return;
      body.innerHTML = src.innerHTML;
      pd.classList.add('is-open');
      document.body.style.overflow = 'hidden';
      ultimoTrigger = btn;
      panel.scrollTop = 0;
      $('.person-drawer__close', pd)?.focus();
    };
    const chiudi = () => {
      pd.classList.remove('is-open');
      document.body.style.overflow = '';
      ultimoTrigger?.focus();
    };

    $$('[data-person]').forEach(b => b.addEventListener('click', () => apri(b)));
    $('.person-drawer__bd', pd)?.addEventListener('click', chiudi);
    $('.person-drawer__close', pd)?.addEventListener('click', chiudi);
    addEventListener('keydown', e => { if (e.key === 'Escape' && pd.classList.contains('is-open')) chiudi(); });
  }

  /* ---- Scrollspy nav ad ancore ---------------------------------------- */
  const anav = $('.anchor-nav');
  if (anav && 'IntersectionObserver' in window) {
    const link = $$('a', anav);
    const sezioni = link.map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
    const io = new IntersectionObserver(voci => {
      voci.forEach(v => {
        if (!v.isIntersecting) return;
        link.forEach(a => a.classList.toggle('is-active', a.getAttribute('href') === '#' + v.target.id));
      });
    }, { rootMargin: '-25% 0px -65% 0px' });
    sezioni.forEach(s => io.observe(s));
  }

  /* ---- Form: validazione + invio simulato ----------------------------- */
  $$('form[data-validate]').forEach(form => {
    const mostraErrore = (campo, msg) => {
      const wrap = campo.closest('.field');
      if (!wrap) return;
      wrap.classList.add('field--error');
      const e = $('.field__err', wrap);
      if (e) e.textContent = msg;
    };
    const pulisci = campo => campo.closest('.field')?.classList.remove('field--error');

    $$('input, textarea, select', form).forEach(c => c.addEventListener('input', () => pulisci(c)));

    form.addEventListener('submit', e => {
      e.preventDefault();
      let ok = true, primo = null;

      $$('[required]', form).forEach(campo => {
        const v = campo.type === 'checkbox' ? campo.checked : campo.value.trim();
        if (!v) { mostraErrore(campo, 'Campo obbligatorio'); ok = false; primo ||= campo; return; }
        if (campo.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(campo.value)) {
          mostraErrore(campo, 'Indirizzo email non valido'); ok = false; primo ||= campo;
        }
        if (campo.type === 'tel' && campo.value.replace(/\D/g, '').length < 8) {
          mostraErrore(campo, 'Numero di telefono non valido'); ok = false; primo ||= campo;
        }
      });

      if (!ok) { primo?.focus(); return; }

      const btn = $('button[type="submit"]', form);
      if (btn) { btn.disabled = true; btn.textContent = 'Invio in corso…'; }

      // Segnaposto: in produzione qui va l'endpoint reale (vedi docs/05).
      setTimeout(() => {
        const ok = form.parentElement.querySelector('.form-success');
        if (ok) { form.hidden = true; ok.classList.add('is-on'); ok.scrollIntoView({ behavior: RIDOTTO ? 'auto' : 'smooth', block: 'center' }); }
      }, 700);
    });
  });

  /* ---- Upload panoramica ---------------------------------------------- */
  $$('.file-drop').forEach(drop => {
    const input = $('input[type="file"]', drop);
    const eti = $('[data-file-label]', drop);
    if (!input) return;
    const nomi = files => Array.from(files).map(f => `${f.name} · ${(f.size / 1048576).toFixed(1)} MB`).join(', ');
    input.addEventListener('change', () => { if (input.files.length && eti) eti.textContent = nomi(input.files); });
    ['dragenter', 'dragover'].forEach(t => drop.addEventListener(t, e => { e.preventDefault(); drop.classList.add('is-over'); }));
    ['dragleave', 'drop'].forEach(t => drop.addEventListener(t, e => { e.preventDefault(); drop.classList.remove('is-over'); }));
    drop.addEventListener('drop', e => {
      if (!e.dataTransfer?.files.length) return;
      input.files = e.dataTransfer.files;
      if (eti) eti.textContent = nomi(input.files);
    });
  });

  /* ---- Anno corrente nel footer --------------------------------------- */
  $$('[data-year]').forEach(el => el.textContent = new Date().getFullYear());

  /* ---- Stato "aperto ora" --------------------------------------------- */
  $$('[data-open-now]').forEach(el => {
    const ora = new Date();
    const g = ora.getDay();              // 0 dom … 6 sab
    const m = ora.getHours() * 60 + ora.getMinutes();
    const aperto = g >= 1 && g <= 6 && m >= 8 * 60 && m < 20 * 60 + 30;
    el.innerHTML = aperto
      ? '<span class="dot"></span> Aperto ora · fino alle 20:30'
      : '<span class="dot" style="background:var(--muted-2);box-shadow:none;animation:none"></span> Chiuso ora · riapre lunedì–sabato alle 8:00';
    if (!aperto) el.style.color = 'var(--muted)';
  });
})();
