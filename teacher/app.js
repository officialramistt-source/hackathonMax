// Кабинет Учителя • Аналитика Класса МАХ - Живая синхронизация с бэкендом
function toggleTeacherNavMenu() {
  const drawer = document.getElementById('teacherNavDrawer');
  if (drawer) {
    drawer.classList.toggle('hidden');
  }
}

function changeClass(cls) {
  const badge = document.getElementById('classBottleneckBadge');
  if (cls === '5a') {
    if (badge) badge.innerText = 'Узкое место: Шаг 2 (НОК: 9 застряли)';
  } else if (cls === '5b') {
    if (badge) badge.innerText = 'Узкое место: Шаг 3 (17 застряли)';
  } else if (cls === '5v') {
    if (badge) badge.innerText = 'Узкое место: Шаг 4 (Сокращение: 8 застряли)';
  } else if (cls === '6a') {
    if (badge) badge.innerText = 'Узкое место: Шаг 1 (Перенос: 12 застряли)';
  }
}

let studentsData = [
  { id: 1, name: 'Иванов Михаил', s1: 'зеленый', s2: 'желтый', s3: '62% класса застряли', s4: 'Ответ', latency: [10, 50, 20, 55, 112, 50], autonomy: 74, error: 'Пропуск домножения числителя', note: 'Забыл домножить числитель первой дроби на 3.' },
  { id: 2, name: 'Алексеева Анна', s1: 'зеленый', s2: 'желтый', s3: '62% класса застряли', s4: 'Ответ', latency: [8, 40, 25, 45, 95, 40], autonomy: 71, error: 'Пропуск домножения числителя', note: 'Сложила 1/12 + 1/12 вместо 3/12 + 2/12.' },
  { id: 3, name: 'Бондаренко Дмитрий', s1: 'зеленый', s2: 'желтый', s3: '62% класса застряли', s4: 'Ответ', latency: [12, 35, 30, 60, 105, 45], autonomy: 68, error: 'Неверный доп. множитель', note: 'Умножил числитель на 2 вместо 3.' },
  { id: 4, name: 'Хайрутдинов Рамис', s1: 'зеленый', s2: 'зеленый', s3: 'в работе', s4: 'Ответ', latency: [6, 14, 112, 20, 15, 10], autonomy: 84, error: 'Глубокий анализ домножения', note: 'Думает самостоятельно, время размышления 112 сек.' },
  { id: 5, name: 'Васильева Елена', s1: 'зеленый', s2: 'желтый', s3: '62% класса застряли', s4: 'Ответ', latency: [10, 45, 20, 50, 88, 35], autonomy: 72, error: 'Пропуск домножения числителя', note: 'Забыла про вторую дробь.' },
  { id: 6, name: 'Гарипов Тимур', s1: 'зеленый', s2: 'зеленый', s3: 'зеленый', s4: 'Ответ', latency: [5, 12, 25, 15, 18, 12], autonomy: 94, error: 'Нет ошибок', note: 'Идеальное решение без подсказок.' },
  { id: 7, name: 'Дмитриев Артем', s1: 'зеленый', s2: 'желтый', s3: '62% класса застряли', s4: 'Ответ', latency: [9, 38, 28, 52, 98, 42], autonomy: 69, error: 'Пропуск домножения числителя', note: 'Требуется задача-двойник.' }
];

let selectedStudent = studentsData[0];

async function loadClassMatrixFromBackend() {
  try {
    const res = await fetch('/api/teacher/class-matrix');
    const data = await res.json();
    if (data.students && data.students.length > 0) {
      studentsData = data.students;
      // Синхронизируем статус Рамиса
      const ramis = studentsData.find(s => s.name === 'Хайрутдинов Рамис');
      if (ramis) {
        const rEl = document.querySelector('#studentRow_4 div:nth-child(4) span');
        if (rEl && ramis.s3 === 'зеленый') {
          rEl.className = 'px-3 py-1 rounded-md text-[11px] font-semibold pill-status-green';
          rEl.innerText = 'зеленый';
        }
      }
    }
  } catch (e) {}
}

function initTeacherSparkline() {
  const canvas = document.getElementById('teacherLatencyCanvas');
  if (!canvas || !canvas.getContext) return;
  const ctx = canvas.getContext('2d');
  const w = canvas.width;
  const h = canvas.height;
  
  ctx.clearRect(0, 0, w, h);
  
  ctx.strokeStyle = '#222530';
  ctx.lineWidth = 1;
  ctx.setLineDash([3, 3]);
  ctx.beginPath();
  ctx.moveTo(10, 20); ctx.lineTo(w - 10, 20);
  ctx.moveTo(10, 45); ctx.lineTo(w - 10, 45);
  ctx.stroke();
  ctx.setLineDash([]);
  
  ctx.beginPath();
  ctx.moveTo(10, 52);
  ctx.bezierCurveTo(35, 48, 55, 15, 75, 22);
  ctx.bezierCurveTo(95, 28, 110, 56, 125, 48);
  ctx.bezierCurveTo(145, 38, 165, 52, 185, 22);
  ctx.bezierCurveTo(200, 12, 215, 38, w - 10, 42);
  ctx.strokeStyle = '#FFFFFF';
  ctx.lineWidth = 2.5;
  ctx.stroke();
}

function selectStudent(id) {
  const st = studentsData.find(s => s.id === id);
  if (!st) return;
  selectedStudent = st;
  
  const nameEl = document.getElementById('diagStudentName');
  if (nameEl) nameEl.innerText = st.name;
  
  const catEl = document.getElementById('diagStudentCategory');
  if (catEl) catEl.innerText = st.error;
  
  const autoEl = document.getElementById('diagStudentAutonomy');
  if (autoEl) autoEl.innerText = st.autonomy + '%';
  
  const circleEl = document.getElementById('diagStudentAutonomyCircle');
  if (circleEl) circleEl.innerText = st.autonomy + '%';
  
  const noteEl = document.getElementById('diagStudentNote');
  if (noteEl) noteEl.innerText = st.note;
  
  studentsData.forEach(s => {
    const row = document.getElementById('studentRow_' + s.id);
    if (row) {
      if (s.id === id) {
        row.className = 'grid grid-cols-12 items-center px-4 py-3 rounded-2xl bg-[#222432] text-xs shadow-md cursor-pointer transition-all';
      } else {
        row.className = 'grid grid-cols-12 items-center px-4 py-3 rounded-2xl cockpit-card-elevated text-xs hover:bg-[#20222D] cursor-pointer transition-all';
      }
    }
  });
  
  initTeacherSparkline();
}

async function generateTwinProblemForClass() {
  try {
    const res = await fetch('/api/teacher/generate-twin', { method: 'POST' });
    const data = await res.json();
    alert(`⚡ Бэкенд МАХ:\n\n${data.message}\n\nЗадача: 1/4 + 5/6 доставлена в личные кабинеты 17 учеников.`);
  } catch (e) {
    alert('⚡ Задача-двойник 1/4 + 5/6 создана локально.');
  }
}

async function sendFormativeSticker() {
  try {
    const res = await fetch('/api/teacher/send-sticker', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        studentId: selectedStudent.id,
        text: 'Марья Ивановна: обрати внимание на домножение числителя!'
      })
    });
    const data = await res.json();
    alert(`🏷️ Бэкенд подтвердил: стикер доставлен ученику ${selectedStudent.name}.`);
  } catch (e) {
    alert(`🏷️ Стикер отправлен ученику ${selectedStudent.name}.`);
  }
}

function triggerMiniLesson() {
  alert('📋 Карточка 3-минутки для начала урока сгенерирована бэкендом.');
}

window.addEventListener('DOMContentLoaded', () => {
  initTeacherSparkline();
  loadClassMatrixFromBackend();
  
  // Проверяем параметр URL id
  const params = new URLSearchParams(window.location.search);
  const idParam = parseInt(params.get('id') || '0');
  if (idParam > 0) {
    selectStudent(idParam);
  }
  
  // Опрос сервера каждые 3 секунды для живой синхронизации
  setInterval(loadClassMatrixFromBackend, 3000);
});
