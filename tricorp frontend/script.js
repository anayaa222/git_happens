// ═══════════════════════════════════════════════════════════
//  SYMPTOM DATABASE
// ═══════════════════════════════════════════════════════════
const SYMPTOM_DB = {
  // PRIMARY SYMPTOMS (shown on screen 1)
  primary: [
    { id:'chest_pain',      label:'Chest Pain',        icon:'💔', weight:90 },
    { id:'shortness_breath',label:'Shortness of Breath',icon:'🫁', weight:85 },
    { id:'headache',        label:'Headache',           icon:'🤕', weight:40 },
    { id:'fever',           label:'Fever',              icon:'🌡️', weight:55 },
    { id:'nausea',          label:'Nausea / Vomiting',  icon:'🤢', weight:45 },
    { id:'abdominal_pain',  label:'Abdominal Pain',     icon:'🫃', weight:65 },
    { id:'dizziness',       label:'Dizziness / Fainting',icon:'😵', weight:70 },
    { id:'back_pain',       label:'Back Pain',          icon:'🦴', weight:50 },
    { id:'joint_pain',      label:'Joint / Limb Pain',  icon:'🦵', weight:45 },
    { id:'cough',           label:'Cough',              icon:'😮‍💨', weight:35 },
    { id:'fatigue',         label:'Severe Fatigue',     icon:'😴', weight:50 },
    { id:'rash',            label:'Skin Rash',          icon:'🔴', weight:40 },
    { id:'bleeding',        label:'Bleeding',           icon:'🩸', weight:88 },
    { id:'numbness',        label:'Numbness / Tingling',icon:'⚡', weight:75 },
    { id:'vision',          label:'Vision Problems',    icon:'👁️', weight:72 },
    { id:'swelling',        label:'Swelling',           icon:'🫧', weight:55 },
  ],

  // RELATED SYMPTOMS per primary + their weights
  related: {
    chest_pain: [
      { id:'arm_pain',       label:'Pain radiating to arm',    weight:85 },
      { id:'jaw_pain',       label:'Jaw / neck pain',          weight:82 },
      { id:'sweating',       label:'Cold sweats',              weight:80 },
      { id:'palpitations',   label:'Heart palpitations',       weight:75 },
      { id:'breath_short2',  label:'Difficulty breathing',     weight:70 },
      { id:'nausea_chest',   label:'Nausea / indigestion',     weight:60 },
      { id:'fatigue_chest',  label:'Sudden extreme fatigue',   weight:65 },
      { id:'anxiety',        label:'Sense of doom / anxiety',  weight:55 },
    ],
    shortness_breath: [
      { id:'wheeze',         label:'Wheezing',                 weight:70 },
      { id:'blue_lips',      label:'Blue lips or fingertips',  weight:90 },
      { id:'chest_tight',    label:'Chest tightness',          weight:75 },
      { id:'rapid_breath',   label:'Rapid breathing (>20/min)',weight:72 },
      { id:'cough_blood',    label:'Coughing up blood',        weight:92 },
      { id:'ankle_swell',    label:'Ankle swelling',           weight:60 },
      { id:'fever_breath',   label:'Fever',                    weight:50 },
      { id:'confusion',      label:'Confusion / drowsiness',   weight:85 },
    ],
    headache: [
      { id:'stiff_neck',     label:'Stiff neck',               weight:88 },
      { id:'light_sensitive',label:'Light sensitivity',        weight:65 },
      { id:'vision_blur',    label:'Blurred vision',           weight:72 },
      { id:'vomit',          label:'Vomiting',                 weight:60 },
      { id:'confusion2',     label:'Confusion',                weight:85 },
      { id:'fever_head',     label:'Fever',                    weight:70 },
      { id:'worst_headache', label:'"Worst headache of life"', weight:95 },
      { id:'weakness_head',  label:'Weakness on one side',     weight:90 },
    ],
    fever: [
      { id:'chills',         label:'Chills / rigors',          weight:60 },
      { id:'rash_fever',     label:'Skin rash',                weight:72 },
      { id:'confusion_fever',label:'Confusion / altered state',weight:90 },
      { id:'petechiae',      label:'Tiny red/purple spots',    weight:92 },
      { id:'joint_fever',    label:'Joint pain',               weight:55 },
      { id:'throat',         label:'Sore throat',              weight:40 },
      { id:'dysuria',        label:'Painful urination',        weight:50 },
      { id:'neck_stiff2',    label:'Neck stiffness',           weight:88 },
    ],
    nausea: [
      { id:'blood_vomit',    label:'Blood in vomit',           weight:92 },
      { id:'severe_pain',    label:'Severe abdominal pain',    weight:75 },
      { id:'diarrhea',       label:'Diarrhea',                 weight:45 },
      { id:'jaundice',       label:'Yellowing of skin/eyes',   weight:80 },
      { id:'dehydrated',     label:'Signs of dehydration',     weight:65 },
      { id:'head_nausea',    label:'Headache',                 weight:50 },
      { id:'can_not_eat',    label:'Unable to keep fluids down',weight:70 },
      { id:'fever_nausea',   label:'Fever',                    weight:55 },
    ],
    abdominal_pain: [
      { id:'rigid_abd',      label:'Rigid / board-like belly', weight:92 },
      { id:'blood_stool',    label:'Blood in stool',           weight:88 },
      { id:'localized',      label:'Pain in lower-right',      weight:80 },
      { id:'rebound',        label:'Pain worsens on release',  weight:85 },
      { id:'fever_abd',      label:'Fever',                    weight:65 },
      { id:'vomit_abd',      label:'Vomiting',                 weight:60 },
      { id:'bloat',          label:'Severe bloating',          weight:55 },
      { id:'no_stool',       label:'No bowel movement 3+ days',weight:70 },
    ],
    dizziness: [
      { id:'syncope',        label:'Fainting / loss of consc.',weight:88 },
      { id:'speech_slur',    label:'Slurred speech',           weight:92 },
      { id:'facial_drop',    label:'Facial drooping',          weight:95 },
      { id:'arm_weak',       label:'Arm / leg weakness',       weight:90 },
      { id:'heart_diz',      label:'Heart palpitations',       weight:70 },
      { id:'vision_diz',     label:'Double or blurred vision', weight:72 },
      { id:'stand_diz',      label:'Worsens on standing',      weight:50 },
      { id:'head_diz',       label:'Headache',                 weight:55 },
    ],
    back_pain: [
      { id:'tearing_back',   label:'Tearing / ripping sensation',weight:92 },
      { id:'leg_numb',       label:'Leg numbness / weakness',  weight:85 },
      { id:'bladder_back',   label:'Loss of bladder control',  weight:90 },
      { id:'fever_back',     label:'Fever + back pain',        weight:75 },
      { id:'flank_pain',     label:'Flank / kidney area pain', weight:70 },
      { id:'trauma',         label:'Recent trauma / fall',     weight:80 },
      { id:'shoot_leg',      label:'Pain shoots to legs',      weight:65 },
      { id:'worse_lying',    label:'Worse when lying down',    weight:55 },
    ],
    joint_pain: [
      { id:'joint_red',      label:'Joint redness / warmth',   weight:65 },
      { id:'joint_fever',    label:'Fever',                    weight:70 },
      { id:'joint_swell',    label:'Joint swelling',           weight:60 },
      { id:'multiple_joints',label:'Multiple joints affected', weight:65 },
      { id:'morning_stiff',  label:'Morning stiffness > 1hr',  weight:55 },
      { id:'skin_rash_j',    label:'Skin rash',                weight:60 },
      { id:'fatigue_j',      label:'Severe fatigue',           weight:50 },
      { id:'recent_bite',    label:'Recent insect bite',       weight:72 },
    ],
    cough: [
      { id:'cough_blood2',   label:'Blood in sputum',          weight:92 },
      { id:'breath_cough',   label:'Shortness of breath',      weight:75 },
      { id:'chest_cough',    label:'Chest pain when coughing', weight:70 },
      { id:'night_sweat',    label:'Night sweats',             weight:65 },
      { id:'weight_loss',    label:'Unintended weight loss',   weight:72 },
      { id:'high_fever_c',   label:'High fever (>39°C)',       weight:65 },
      { id:'stridor',        label:'Crowing / stridor sound',  weight:88 },
      { id:'week_cough',     label:'Persistent > 3 weeks',     weight:60 },
    ],
    fatigue: [
      { id:'chest_fat',      label:'Chest pain',               weight:85 },
      { id:'breath_fat',     label:'Shortness of breath',      weight:75 },
      { id:'confusion_fat',  label:'Confusion',                weight:88 },
      { id:'pale',           label:'Pale / white complexion',  weight:70 },
      { id:'dark_urine',     label:'Dark urine',               weight:72 },
      { id:'no_appetite',    label:'Loss of appetite',         weight:55 },
      { id:'swollen_lymph',  label:'Swollen lymph nodes',      weight:68 },
      { id:'bruising',       label:'Easy bruising / bleeding', weight:75 },
    ],
    rash: [
      { id:'rash_fever2',    label:'Fever',                    weight:65 },
      { id:'rash_spread',    label:'Rapidly spreading',        weight:80 },
      { id:'rash_blister',   label:'Blistering',               weight:72 },
      { id:'rash_breath',    label:'Difficulty breathing',     weight:92 },
      { id:'rash_throat',    label:'Throat swelling',          weight:92 },
      { id:'rash_pus',       label:'Pus / infection signs',    weight:70 },
      { id:'rash_nopress',   label:'Does not blanch on press',  weight:90 },
      { id:'rash_pain',      label:'Painful to touch',         weight:65 },
    ],
    bleeding: [
      { id:'bleed_cont',     label:'Cannot stop bleeding',     weight:95 },
      { id:'bleed_dark',     label:'Dark / coffee-ground blood',weight:90 },
      { id:'bleed_anus',     label:'Rectal bleeding',          weight:85 },
      { id:'bleed_cough',    label:'Coughing up blood',        weight:92 },
      { id:'bleed_urine',    label:'Blood in urine',           weight:75 },
      { id:'bleed_dizzy',    label:'Dizziness / fainting',     weight:88 },
      { id:'bleed_pale',     label:'Pale / clammy skin',       weight:85 },
      { id:'bleed_rapid',    label:'Rapid heart rate',         weight:80 },
    ],
    numbness: [
      { id:'numb_face',      label:'Facial numbness',          weight:88 },
      { id:'numb_sudden',    label:'Sudden onset',             weight:90 },
      { id:'numb_weak',      label:'Muscle weakness',          weight:85 },
      { id:'numb_speech',    label:'Speech difficulty',        weight:92 },
      { id:'numb_vision',    label:'Visual changes',           weight:85 },
      { id:'numb_bladder',   label:'Bladder/bowel issues',     weight:90 },
      { id:'numb_coord',     label:'Loss of coordination',     weight:88 },
      { id:'numb_pain',      label:'Pain along nerve path',    weight:65 },
    ],
    vision: [
      { id:'vis_sudden',     label:'Sudden onset',             weight:92 },
      { id:'vis_curtain',    label:'"Curtain" over vision',    weight:90 },
      { id:'vis_headache',   label:'Severe headache',          weight:85 },
      { id:'vis_double',     label:'Double vision',            weight:80 },
      { id:'vis_flash',      label:'Flashing lights / floaters',weight:72 },
      { id:'vis_pain',       label:'Eye pain',                 weight:68 },
      { id:'vis_red',        label:'Red eye',                  weight:55 },
      { id:'vis_nausea',     label:'Nausea / vomiting',        weight:60 },
    ],
    swelling: [
      { id:'swell_face',     label:'Face / tongue swelling',   weight:95 },
      { id:'swell_breath',   label:'Difficulty breathing',     weight:92 },
      { id:'swell_both',     label:'Both legs equally swollen',weight:65 },
      { id:'swell_red',      label:'Red, warm skin',           weight:65 },
      { id:'swell_pitting',  label:'Pitting (leaves indent)',  weight:60 },
      { id:'swell_tender',   label:'Tender to touch',          weight:70 },
      { id:'swell_fever',    label:'Fever',                    weight:65 },
      { id:'swell_sudden',   label:'Sudden onset swelling',    weight:80 },
    ],
  },

  // CONCERN AREAS per primary
  concerns: {
    chest_pain:       'Cardiac / Cardiovascular',
    shortness_breath: 'Respiratory / Cardiac',
    headache:         'Neurological',
    fever:            'Infectious / Systemic',
    nausea:           'Gastrointestinal',
    abdominal_pain:   'Gastrointestinal / Surgical',
    dizziness:        'Neurological / Cardiac',
    back_pain:        'Musculoskeletal / Spinal',
    joint_pain:       'Rheumatological',
    cough:            'Respiratory / Pulmonary',
    fatigue:          'Haematological / Systemic',
    rash:             'Dermatological / Allergic',
    bleeding:         'Haematological / Surgical',
    numbness:         'Neurological',
    vision:           'Ophthalmological / Neurological',
    swelling:         'Cardiovascular / Allergic',
  }
};

// ═══════════════════════════════════════════════════════════
//  STATE
// ═══════════════════════════════════════════════════════════
let state = {
  primarySymptom: null,
  relatedSymptoms: [],
  severity: 5,
  duration: null,
  score: 0,
  category: null,
  token: null,
};

// ═══════════════════════════════════════════════════════════
//  RENDER PRIMARY SYMPTOMS
// ═══════════════════════════════════════════════════════════
function renderPrimary(filter = '') {
  const grid = document.getElementById('primaryGrid');
  const list = SYMPTOM_DB.primary.filter(s =>
    !filter || s.label.toLowerCase().includes(filter.toLowerCase())
  );
  grid.innerHTML = list.map(s => `
    <div class="sym-chip ${state.primarySymptom?.id === s.id ? 'selected' : ''}"
         onclick="selectPrimary('${s.id}')">
      <div class="sym-chip-dot"></div>
      <span>${s.icon} ${s.label}</span>
    </div>
  `).join('');
}

function filterSymptoms() {
  const q = document.getElementById('symSearch').value;
  renderPrimary(q);
}

function selectPrimary(id) {
  const sym = SYMPTOM_DB.primary.find(s => s.id === id);
  state.primarySymptom = sym;
  renderPrimary(document.getElementById('symSearch').value);
  document.getElementById('s1Next').disabled = false;
}

// ═══════════════════════════════════════════════════════════
//  RENDER RELATED SYMPTOMS
// ═══════════════════════════════════════════════════════════
function renderRelated() {
  const list = SYMPTOM_DB.related[state.primarySymptom.id] || [];
  const grid = document.getElementById('relatedGrid');
  grid.innerHTML = list.map(s => `
    <div class="sym-chip ${state.relatedSymptoms.find(r=>r.id===s.id) ? 'selected' : ''}"
         onclick="toggleRelated('${s.id}')">
      <div class="sym-chip-dot"></div>
      <span>${s.label}</span>
    </div>
  `).join('');
  updateRelCount();
}

function toggleRelated(id) {
  const list = SYMPTOM_DB.related[state.primarySymptom.id];
  const sym = list.find(s => s.id === id);
  const idx = state.relatedSymptoms.findIndex(s => s.id === id);
  if (idx >= 0) state.relatedSymptoms.splice(idx, 1);
  else state.relatedSymptoms.push(sym);
  renderRelated();
  checkS2();
}

function updateRelCount() {
  document.getElementById('relCount').textContent = state.relatedSymptoms.length;
}

// ═══════════════════════════════════════════════════════════
//  SEVERITY + DURATION
// ═══════════════════════════════════════════════════════════
function updateSeverity() {
  const val = document.getElementById('severitySlider').value;
  state.severity = parseInt(val);
  document.getElementById('severityVal').textContent = val;
  const pct = ((val - 1) / 9) * 100;
  document.getElementById('severityFill').style.width = pct + '%';
  const fill = document.getElementById('severityFill');
  if (val <= 3) fill.style.background = 'var(--green)';
  else if (val <= 6) fill.style.background = 'var(--amber)';
  else fill.style.background = 'var(--red)';
}

function selectDuration(el, val) {
  document.querySelectorAll('.dur-btn').forEach(b => b.classList.remove('selected'));
  el.classList.add('selected');
  state.duration = val;
  checkS2();
}

function checkS2() {
  document.getElementById('s2Next').disabled = !state.duration;
}

// ═══════════════════════════════════════════════════════════
//  SCORING ENGINE
// ═══════════════════════════════════════════════════════════
function calculateScore() {
  let score = 0;

  // 1. Primary symptom base weight (contributes up to 35 pts)
  const primaryWeight = state.primarySymptom.weight;
  score += (primaryWeight / 100) * 35;

  // 2. Related symptoms (each contributes weighted share, up to 35 pts total)
  if (state.relatedSymptoms.length > 0) {
    const allRelated = SYMPTOM_DB.related[state.primarySymptom.id];
    const maxPossible = allRelated.reduce((s, r) => s + r.weight, 0);
    const selected = state.relatedSymptoms.reduce((s, r) => s + r.weight, 0);
    score += (selected / maxPossible) * 35;
  }

  // 3. Severity (up to 20 pts)
  score += ((state.severity - 1) / 9) * 20;

  // 4. Duration modifier (up to 10 pts)
  const durationScore = {
    'sudden': 10, '<1h': 9, '1-6h': 7, '6-24h': 5,
    '1-3d': 4, '3-7d': 3, '>7d': 2, 'chronic': 1,
  };
  score += (durationScore[state.duration] || 3);

  return Math.min(100, Math.max(0, Math.round(score)));
}

function getCategory(score) {
  if (score >= 65) return 'A';
  if (score >= 35) return 'B';
  return 'C';
}

function generateToken() {
  const d = new Date();
  const pad = n => String(n).padStart(2, '0');
  const timeStr = pad(d.getHours()) + pad(d.getMinutes());
  const rand = Math.floor(1 + Math.random() * 999);
  return { prefix: state.category + '-', num: timeStr + String(rand).padStart(3,'0') };
}

// ═══════════════════════════════════════════════════════════
//  NAVIGATION
// ═══════════════════════════════════════════════════════════
function showScreen(n) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById('screen' + n).classList.add('active');
  window.scrollTo({ top: 0, behavior: 'smooth' });
  updateSteps(n);
}

function updateSteps(n) {
  for (let i = 1; i <= 4; i++) {
    const node = document.getElementById('s' + i);
    node.classList.remove('active', 'done');
    if (i < n) node.classList.add('done');
    else if (i === n) node.classList.add('active');
    if (i < 4) {
      const line = document.getElementById('sl' + i);
      line.classList.toggle('done', i < n);
    }
  }
}

function goToScreen2() {
  document.getElementById('selectedPrimaryLabel').textContent = state.primarySymptom.label;
  state.relatedSymptoms = [];
  renderRelated();
  showScreen(2);
}

function goToScreen3() {
  showScreen(3);
  runAnalysis();
}

function goBack(n) {
  showScreen(n);
}

// ═══════════════════════════════════════════════════════════
//  ANALYSIS ANIMATION
// ═══════════════════════════════════════════════════════════
function runAnalysis() {
  const stages = [
    { text: 'Mapping primary symptom profile…', pct: 15, delay: 400 },
    { text: 'Cross-referencing related symptoms…', pct: 35, delay: 900 },
    { text: 'Evaluating severity indicators…', pct: 55, delay: 1500 },
    { text: 'Applying duration weighting…', pct: 72, delay: 2000 },
    { text: 'Calculating risk score…', pct: 88, delay: 2600 },
    { text: 'Assigning priority category…', pct: 100, delay: 3200 },
  ];
  stages.forEach(stage => {
    setTimeout(() => {
      document.getElementById('analyzeStatus').textContent = stage.text;
      document.getElementById('analyzeProgress').style.width = stage.pct + '%';
    }, stage.delay);
  });
  setTimeout(() => {
    state.score = calculateScore();
    state.category = getCategory(state.score);
    state.token = generateToken();
    renderResult();
    showScreen(4);
  }, 3800);
}

// ═══════════════════════════════════════════════════════════
//  RENDER RESULT
// ═══════════════════════════════════════════════════════════
function renderResult() {
  const { score, category, token } = state;

  // Colors
  const colors = {
    A: { main: 'var(--red)',   glow: 'rgba(239,68,68,0.15)',   cls: 'cat-A' },
    B: { main: 'var(--amber)', glow: 'rgba(245,158,11,0.15)',  cls: 'cat-B' },
    C: { main: 'var(--green)', glow: 'rgba(34,197,94,0.15)',   cls: 'cat-C' },
  };
  const c = colors[category];

  // Token
  document.getElementById('tokenPrefix').textContent = token.prefix;
  document.getElementById('tokenNum').textContent = token.num;
  document.getElementById('tokenDisplay').style.setProperty('--glow-color', c.glow);
  document.getElementById('tokenNum').style.color = c.main;

  // Category badge
  const badge = document.getElementById('catBadge');
  badge.className = 'category-badge ' + c.cls;
  badge.textContent = {
    A: '⚠ Category A — High Priority',
    B: '◆ Category B — Moderate Priority',
    C: '✓ Category C — Low Priority',
  }[category];

  document.getElementById('catDesc').textContent = {
    A: 'Score: ' + score + '/100 — Immediate clinical assessment required',
    B: 'Score: ' + score + '/100 — Timely evaluation recommended',
    C: 'Score: ' + score + '/100 — Routine evaluation, stable condition',
  }[category];

  // Score meter
  const fill = document.getElementById('scoreFill');
  setTimeout(() => {
    fill.style.width = score + '%';
    fill.style.background = c.main;
    fill.style.boxShadow = `0 0 12px ${c.glow}`;
  }, 100);

  // Animated score counter
  let displayed = 0;
  const target = score;
  const interval = setInterval(() => {
    displayed = Math.min(displayed + 2, target);
    document.getElementById('scoreDisplay').textContent = displayed + ' / 100';
    if (displayed >= target) clearInterval(interval);
  }, 20);

  // Info cells
  document.getElementById('concernArea').textContent =
    SYMPTOM_DB.concerns[state.primarySymptom.id] || 'General';
  document.getElementById('symCount').textContent =
    (1 + state.relatedSymptoms.length) + ' symptoms';

  const durLabels = {
    'sudden':'Sudden onset','<1h':'< 1 hour','1-6h':'1–6 hours',
    '6-24h':'6–24 hours','1-3d':'1–3 days','3-7d':'3–7 days',
    '>7d':'> 1 week','chronic':'Chronic'
  };
  document.getElementById('durFactor').textContent = durLabels[state.duration] || '—';
  document.getElementById('sevRating').textContent = state.severity + ' / 10';

  // Symptom tags
  const summDiv = document.getElementById('symSummary');
  summDiv.innerHTML = `<div class="sym-tag primary">⭐ ${state.primarySymptom.icon} ${state.primarySymptom.label}</div>`;
  state.relatedSymptoms.forEach(s => {
    summDiv.innerHTML += `<div class="sym-tag">${s.label}</div>`;
  });

  // Dispatch box
  const dispatch = {
    A: {
      icon: '🚨',
      bg: 'rgba(239,68,68,0.1)', border: 'rgba(239,68,68,0.25)',
      title: 'Proceed to Nurse Station A immediately',
      sub: 'Station A is equipped for high-priority cases. Please go now — a nurse has been alerted with token ' + token.prefix + token.num,
      btnBg: 'var(--red)', btnColor: '#fff',
    },
    B: {
      icon: '⚡',
      bg: 'rgba(245,158,11,0.08)', border: 'rgba(245,158,11,0.25)',
      title: 'Proceed to Nurse Station B',
      sub: 'Station B handles moderate-priority cases. Please wait briefly if a nurse is with another patient. Token: ' + token.prefix + token.num,
      btnBg: 'var(--amber)', btnColor: '#000',
    },
    C: {
      icon: '✅',
      bg: 'rgba(34,197,94,0.08)', border: 'rgba(34,197,94,0.2)',
      title: 'Proceed to Nurse Station C',
      sub: 'Station C handles routine assessments. Please have a seat and wait to be called. Token: ' + token.prefix + token.num,
      btnBg: 'var(--green)', btnColor: '#000',
    },
  }[category];

  const box = document.getElementById('dispatchBox');
  box.style.background = dispatch.bg;
  box.style.border = '1px solid ' + dispatch.border;
  document.getElementById('dispatchIcon').textContent = dispatch.icon;
  document.getElementById('dispatchTitle').textContent = dispatch.title;
  document.getElementById('dispatchSub').textContent = dispatch.sub;
  const btn = document.getElementById('dispatchBtn');
  btn.style.background = dispatch.btnBg;
  btn.style.color = dispatch.btnColor;
}

// ═══════════════════════════════════════════════════════════
//  RESET
// ═══════════════════════════════════════════════════════════
function resetAll() {
  state = { primarySymptom: null, relatedSymptoms: [], severity: 5, duration: null };
  document.getElementById('symSearch').value = '';
  document.getElementById('severitySlider').value = 5;
  document.getElementById('severityVal').textContent = 5;
  document.getElementById('severityFill').style.width = '50%';
  document.getElementById('severityFill').style.background = 'var(--blue)';
  document.getElementById('s1Next').disabled = true;
  document.getElementById('s2Next').disabled = true;
  document.getElementById('analyzeProgress').style.width = '0%';
  renderPrimary();
  showScreen(1);
}

// ═══════════════════════════════════════════════════════════
//  INIT
// ═══════════════════════════════════════════════════════════
renderPrimary();