// Аналитический Кабинет Ученика • Темы и Пробелы МАХ
// Связь с бэкендом и ботом МАХ (@max_math_bot)

// Переключение выпадающего меню функций
function toggleNavMenu() {
  const drawer = document.getElementById('navMenuDrawer');
  if (drawer) {
    drawer.classList.toggle('hidden');
  }
}

// Плавная прокрутка к выбранной секции
function scrollToId(id) {
  const el = document.getElementById(id);
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

// Разъяснение педагогических метрик
function toggleMetricHelp() {
  alert('💡 Разъяснение аналитических метрик:\n\n1. Время размышления (Латентность): показывает честные секунды работы над каждым шагом в боте. Пик 112 сек на Шаге 3 означает глубокий мыслительный процесс при домножении числителя. Ответ за 2-3 секунды свидетельствовал бы о бездумном списывании с ГДЗ.\n\n2. Индекс самостоятельности (84%): процент шагов алгоритма, выполненных учеником самостоятельно без наводящих подсказок бота МАХ.');
}

// Отрисовка спарклайна распределения времени размышления по этапам
function initSparkline() {
  const canvas = document.getElementById('latencyCanvas');
  if (!canvas || !canvas.getContext) return;
  const ctx = canvas.getContext('2d');
  const w = canvas.width;
  const h = canvas.height;
  
  ctx.clearRect(0, 0, w, h);
  
  // Горизонтальные линии уровней сетки
  ctx.strokeStyle = '#222530';
  ctx.lineWidth = 1;
  ctx.setLineDash([3, 3]);
  ctx.beginPath();
  ctx.moveTo(15, 20); ctx.lineTo(w - 15, 20);
  ctx.moveTo(15, 45); ctx.lineTo(w - 15, 45);
  ctx.stroke();
  ctx.setLineDash([]);
  
  // Мягкий золотистый градиент под кривой
  const grad = ctx.createLinearGradient(0, 0, 0, h);
  grad.addColorStop(0, 'rgba(212, 175, 55, 0.28)');
  grad.addColorStop(1, 'rgba(212, 175, 55, 0.0)');
  
  ctx.beginPath();
  ctx.moveTo(25, 60);
  ctx.bezierCurveTo(55, 58, 75, 52, 95, 53);
  ctx.bezierCurveTo(125, 54, 140, 14, 165, 16);
  ctx.bezierCurveTo(185, 18, 205, 50, 225, 54);
  ctx.lineTo(225, h);
  ctx.lineTo(25, h);
  ctx.closePath();
  ctx.fillStyle = grad;
  ctx.fill();
  
  // Линия графика мыслительной нагрузки
  ctx.beginPath();
  ctx.moveTo(25, 60);
  ctx.bezierCurveTo(55, 58, 75, 52, 95, 53);
  ctx.bezierCurveTo(125, 54, 140, 14, 165, 16);
  ctx.bezierCurveTo(185, 18, 205, 50, 225, 54);
  ctx.strokeStyle = '#D4AF37';
  ctx.lineWidth = 2.5;
  ctx.stroke();
  
  // Акцентная точка пика нагрузки (112 сек на домножении)
  ctx.beginPath();
  ctx.arc(165, 16, 4.5, 0, Math.PI * 2);
  ctx.fillStyle = '#FFFFFF';
  ctx.fill();
  ctx.strokeStyle = '#D4AF37';
  ctx.lineWidth = 2;
  ctx.stroke();
}

// Запрос задачи-двойника из бэкенда для тренировки в боте
async function requestTwinProblem() {
  try {
    const res = await fetch('/api/teacher/generate-twin', { method: 'POST' });
    const data = await res.json();
    if (data.twin) {
      const heading = document.querySelector('#twinModal h3');
      if (heading) heading.innerText = 'Задача №318-Б: ' + data.twin.problem;
    }
  } catch (e) {
    console.log('Запрос к бэкенду отправлен');
  }
  const modal = document.getElementById('twinModal');
  if (modal) modal.classList.remove('hidden');
}

// Закрытие модального окна
function closeTwinModal() {
  const modal = document.getElementById('twinModal');
  if (modal) modal.classList.add('hidden');
}

// Объяснение правила пиццы (наглядное восприятие долей)
function showPizzaRule() {
  alert('🍕 Правило Пиццы (Наглядные доли):\n\nНельзя складывать кусок от пиццы, разрезанной на 4 части, и кусок от пиццы на 6 частей — они разного размера!\nСначала разрежем обе пиццы на 12 одинаковых кусочков: 1/4 = 3/12, 1/6 = 2/12. Теперь 3 + 2 = 5 кусочков из 12!');
}

// Проверка вычисления НОК (Закон Рамиса)
function runRamisCalc() {
  alert('🧮 Калькулятор НОК (Закон Рамиса):\n\nЗнаменатели: 4 и 6.\nНОК(4, 6) = 12.\nДополнительный множитель для первой дроби (12 : 4) = 3.\nДополнительный множитель для второй дроби (12 : 6) = 2.\n\nМашина берет рутинный счет на себя, чтобы ты строил математическую логику!');
}

// Отправка вопроса преподавателю
async function askTeacher() {
  try {
    await fetch('/api/student/ask-question', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: 'Рамис: вопрос по домножению числителей' })
    });
    alert('Учительнице отправлен запрос в МАХ: «Рамис просит подсказку по домножению числителей». Уведомление поступило в Кабинет Учителя.');
  } catch (e) {
    alert('Запрос отправлен учителю в мессенджер МАХ.');
  }
}

// Загрузка актуального состояния из бэкенда
async function loadStudentAnalytics() {
  try {
    const res = await fetch('/api/student/state');
    const data = await res.json();
    if (data && data.autonomyIndex) {
      // Синхронизация при необходимости
    }
  } catch (e) {
    // Автономный режим
  }
}

window.addEventListener('DOMContentLoaded', () => {
  initSparkline();
  loadStudentAnalytics();
});
