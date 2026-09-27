#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

WEB_DIR = "/home/ramis/projectAnti/Хакатоны/MAX_Образование/web"
STUDENT_DIR = os.path.join(WEB_DIR, "student")
TEACHER_DIR = os.path.join(WEB_DIR, "teacher")

from build_multipage import student_header, teacher_header

def wrap_student_page(active_tab, title, main_content):
    header = student_header(active_tab)
    return f'''<!DOCTYPE html>
<html lang="ru" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} • Кабинет Ученика МАХ</title>
  <script src="../shared/tailwindcss.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../shared/theme.css">
</head>
<body class="min-h-screen bg-[#0C0D11] text-[#E2E8F0] antialiased selection:bg-[#D4AF37] selection:text-black">
  {header}
  <main class="w-full px-4 sm:px-6 lg:px-8 py-5 space-y-6">
    {main_content}
  </main>

  <!-- МОДАЛКА ЗАДАЧИ-ДВОЙНИКА -->
  <div id="twinModal" class="hidden fixed inset-0 bg-black/80 backdrop-blur-md z-50 flex items-center justify-center p-4">
    <div class="max-w-md w-full cockpit-card rounded-3xl p-8 space-y-5 shadow-2xl">
      <div class="flex items-center justify-between">
        <span class="text-xs uppercase tracking-wider text-[#D4AF37] font-semibold">Задача-Двойник для тренировки в боте</span>
        <button onclick="closeTwinModal()" class="text-sm text-[#71717A] hover:text-white">✕</button>
      </div>
      <div class="space-y-2">
        <h3 class="text-2xl font-bold text-white">Задача №318-Б: 1/4 + 5/6</h3>
        <p class="text-xs text-[#94A3B8] leading-relaxed">
          Та же математическая структура (знаменатели 4 и 6, НОК = 12), но новый числитель. Отправь решение в бот МАХ для проверки!
        </p>
      </div>
      <button onclick="closeTwinModal(); alert('Задача-двойник №318-Б отправлена в твой чат с ботом МАХ!')" class="w-full py-3.5 rounded-xl btn-primary-white text-xs font-bold">
        Отправить задачу в бот МАХ
      </button>
    </div>
  </div>

  <script src="./app.js"></script>
</body>
</html>
'''

def wrap_teacher_page(active_tab, title, main_content):
    header = teacher_header(active_tab)
    return f'''<!DOCTYPE html>
<html lang="ru" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} • Кабинет Учителя МАХ</title>
  <script src="../shared/tailwindcss.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../shared/theme.css">
</head>
<body class="min-h-screen bg-[#0C0D11] text-[#E2E8F0] antialiased selection:bg-[#10B981] selection:text-black">
  {header}
  <main class="w-full px-4 sm:px-6 lg:px-8 py-5 space-y-6">
    {main_content}
  </main>
  <script src="./app.js"></script>
</body>
</html>
'''

# ==================== STUDENT PAGES ====================

# 1. student/index.html (Главная)
student_index_content = '''
    <!-- ИНФО-БАННЕР АРХИТЕКТУРЫ РАЗДЕЛЕНИЯ СРЕД -->
    <div class="p-4 rounded-2xl bg-[#141724] flex flex-col md:flex-row items-start md:items-center justify-between gap-3 shadow-lg">
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-xl bg-[#1F2438] flex items-center justify-center text-lg">📱</div>
        <div>
          <div class="text-xs font-bold text-white">Среда решения задач — Чат-бот МАХ (@max_math_bot)</div>
          <div class="text-[11px] text-[#94A3B8]">Здесь ты изучаешь свою аналитику: какие темы освоены, на каких шагах возникают задержки и что повторить перед уроком.</div>
        </div>
      </div>
      <a href="https://max.mail.ru" target="_blank" class="px-5 py-2.5 rounded-xl btn-primary-white text-xs font-bold whitespace-nowrap shadow-md hover:scale-105 transition-all">
        💬 Открыть диалог в боте МАХ ↗
      </a>
    </div>

    <!-- ОСНОВНАЯ СЕТКА ГЛАВНОЙ (РАЗДЕЛЫ КАБИНЕТА) -->
    <div class="grid grid-cols-12 gap-6">

      <!-- ЛЕВАЯ КОЛОНКА (70%): КАРТОЧКИ КЛЮЧЕВЫХ РАЗДЕЛОВ -->
      <div class="col-span-12 lg:col-span-8 grid grid-cols-1 md:grid-cols-2 gap-5">

        <!-- КАРТОЧКА 1: ТЕМЫ И ПРОБЛЕМЫ -->
        <a href="topics.html" class="p-6 rounded-3xl cockpit-card hover:bg-[#181A22] transition-all space-y-4 group block">
          <div class="flex items-center justify-between">
            <span class="text-2xl">🗺️</span>
            <span class="text-[11px] font-bold text-[#EF4444] bg-[#3B1818] px-2.5 py-1 rounded-lg">1 зона риска</span>
          </div>
          <div class="space-y-1">
            <h2 class="text-sm font-bold text-white group-hover:text-[#D4AF37] transition-all">Темы и проблемы</h2>
            <p class="text-xs text-[#94A3B8]">4 темы 5 класса: дроби, НОК, сокращение. Сложение с разными знаменателями освоено на 58%.</p>
          </div>
          <div class="w-full h-1.5 rounded-full bg-[#121319] overflow-hidden">
            <div class="h-full bg-[#EF4444] rounded-full" style="width: 58%"></div>
          </div>
          <div class="text-xs font-bold text-[#D4AF37] flex items-center gap-1">
            <span>Открыть Темы и проблемы</span> <span>→</span>
          </div>
        </a>

        <!-- КАРТОЧКА 2: РАЗБОР ОШИБОК -->
        <a href="bottleneck.html" class="p-6 rounded-3xl cockpit-card hover:bg-[#181A22] transition-all space-y-4 group block">
          <div class="flex items-center justify-between">
            <span class="text-2xl">🔍</span>
            <span class="text-[11px] font-mono-code text-[#D4AF37] bg-[#2A2312] px-2.5 py-1 rounded-lg">Пример: 1/4 + 1/6</span>
          </div>
          <div class="space-y-1">
            <h2 class="text-sm font-bold text-white group-hover:text-[#D4AF37] transition-all">Разбор ошибок</h2>
            <p class="text-xs text-[#94A3B8]">Почему ответ 1/12 + 1/12 был неверным, и как правильно домножать числители (3/12 + 2/12 = 5/12).</p>
          </div>
          <div class="p-2.5 rounded-xl bg-[#221618] text-[11px] text-[#EF4444]">
            Ошибки домножения: 3 за неделю
          </div>
          <div class="text-xs font-bold text-[#D4AF37] flex items-center gap-1">
            <span>Изучить Разбор ошибок</span> <span>→</span>
          </div>
        </a>

        <!-- КАРТОЧКА 3: ИСТОРИЯ В БОТЕ -->
        <a href="history.html" class="p-6 rounded-3xl cockpit-card hover:bg-[#181A22] transition-all space-y-4 group block">
          <div class="flex items-center justify-between">
            <span class="text-2xl">📱</span>
            <span class="text-[11px] font-mono-code text-[#10B981] bg-[#142E23] px-2.5 py-1 rounded-lg">3 сессии</span>
          </div>
          <div class="space-y-1">
            <h2 class="text-sm font-bold text-white group-hover:text-[#D4AF37] transition-all">История в боте</h2>
            <p class="text-xs text-[#94A3B8]">Лог последних решенных примеров (#318, #317, #315) с точным временем размышления по каждому шагу.</p>
          </div>
          <div class="p-2.5 rounded-xl bg-[#121319] text-[11px] text-[#CBD5E1]">
            Последняя сессия: Задача №318 (Пауза 112с)
          </div>
          <div class="text-xs font-bold text-[#D4AF37] flex items-center gap-1">
            <span>Смотреть Историю</span> <span>→</span>
          </div>
        </a>

        <!-- КАРТОЧКА 4: ПЛАН ТРЕНИРОВОК -->
        <a href="planner.html" class="p-6 rounded-3xl cockpit-card hover:bg-[#181A22] transition-all space-y-4 group block">
          <div class="flex items-center justify-between">
            <span class="text-2xl">📅</span>
            <span class="text-[11px] font-mono-code text-[#F59E0B] bg-[#382D12] px-2.5 py-1 rounded-lg">Спринт 16:30</span>
          </div>
          <div class="space-y-1">
            <h2 class="text-sm font-bold text-white group-hover:text-[#D4AF37] transition-all">План Тренировок</h2>
            <p class="text-xs text-[#94A3B8]">План тренировки в боте перед контрольной: серия из 3 задач-двойников на домножение. Дедлайн: 16:30.</p>
          </div>
          <div class="p-2.5 rounded-xl bg-[#121319] text-[11px] text-[#F59E0B]">
            До дедлайна осталось 18 минут
          </div>
          <div class="text-xs font-bold text-[#D4AF37] flex items-center gap-1">
            <span>Открыть План Тренировок</span> <span>→</span>
          </div>
        </a>

      </div>

      <!-- ПРАВАЯ КОЛОНКА (30%): ДИАГНОСТИКА МЫШЛЕНИЯ И ШПАРГАЛКИ -->
      <div class="col-span-12 lg:col-span-4 space-y-5">

        <div class="cockpit-card rounded-3xl p-6 space-y-5">
          <div class="flex items-center justify-between">
            <h2 class="text-sm font-bold text-white tracking-wide">Диагностика Мышления</h2>
            <button onclick="toggleMetricHelp()" class="text-xs text-[#D4AF37] hover:underline">ℹ️ Смысл</button>
          </div>

          <!-- Спарклайн времени размышления -->
          <div class="space-y-2">
            <div class="flex items-center justify-between text-xs">
              <span class="text-[#94A3B8]">Где уходит время в боте</span>
              <span class="text-[#D4AF37] font-mono-code font-bold">Пик: 112 сек</span>
            </div>
            <div class="p-3.5 rounded-2xl bg-[#121319] space-y-1">
              <canvas id="latencyCanvas" width="260" height="70" class="w-full h-16"></canvas>
              <div class="flex justify-between text-[10px] text-[#71717A] font-mono-code">
                <span>Сравн (6с)</span>
                <span>НОК (14с)</span>
                <span class="text-[#D4AF37] font-bold">Домнож (112с)</span>
                <span>Слож (8с)</span>
              </div>
            </div>
          </div>

          <!-- Индекс самостоятельности -->
          <div class="flex items-center justify-between p-3.5 rounded-2xl bg-[#14151D]">
            <div class="space-y-0.5">
              <div class="text-[10px] uppercase text-[#71717A] font-bold">Самостоятельность</div>
              <div class="text-xs text-white font-medium">84% без подсказок</div>
            </div>
            <div class="w-12 h-12 rounded-xl bg-[#1D1E26] flex items-center justify-center font-bold text-sm text-[#10B981]">
              84%
            </div>
          </div>

          <a href="tools.html" class="w-full py-3 px-4 rounded-xl btn-primary-white text-xs font-bold text-center block shadow-md">
            🧮 Шпаргалки и правила к боту →
          </a>
        </div>

      </div>

    </div>
'''

# 2. student/topics.html (Темы и проблемы)
student_topics_content = '''
    <div class="flex items-center justify-between">
      <div>
        <h2 class="text-xl font-bold text-white tracking-wide">🗺️ Темы и проблемы (5 класс: Обыкновенные дроби)</h2>
        <p class="text-xs text-[#94A3B8]">Автоматическая диагностика на основе твоих ответов в чат-боте МАХ.</p>
      </div>
      <a href="index.html" class="text-xs text-[#94A3B8] hover:text-white transition-all flex items-center gap-1">
        <span>← Назад на Главную</span>
      </a>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-5 pt-2">

      <!-- ТЕМА 1 (ЗОНА РИСКА) -->
      <div class="p-6 rounded-3xl bg-[#221618] space-y-4 shadow-xl">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2.5">
            <span class="text-sm font-bold text-white">1. Сложение дробей с разными знаменателями</span>
            <span class="text-[11px] font-bold text-[#EF4444] bg-[#3B1818] px-2.5 py-0.5 rounded-md">Зона риска</span>
          </div>
          <span class="text-xs font-mono-code font-bold text-[#EF4444]">58% освоено</span>
        </div>
        <div class="w-full h-2.5 rounded-full bg-[#181922] overflow-hidden">
          <div class="h-full bg-[#EF4444] rounded-full" style="width: 58%"></div>
        </div>
        <div class="p-4 rounded-2xl bg-[#1A1214] text-xs text-[#E2E8F0] space-y-2 leading-relaxed">
          <span class="text-[#EF4444] font-semibold text-xs">⚠️ Точный диагноз ошибки (Шаг 3):</span>
          <p class="text-[#CBD5E1] text-[11px]">
            Ты правильно находишь общий знаменатель НОК = 12, но забываешь умножить числители на дополнительные множители (пишешь 1/12 вместо 3/12). 3 ошибки за неделю.
          </p>
        </div>
        <div class="flex items-center justify-between pt-1">
          <a href="bottleneck.html" class="px-4 py-2 rounded-xl btn-primary-white text-xs font-bold shadow-md">
            Изучить разбор этой ошибки →
          </a>
          <span class="text-[11px] text-[#94A3B8]">Рекомендован спринт из 3 задач</span>
        </div>
      </div>

      <!-- ТЕМА 2 (ОСВОЕНО) -->
      <div class="p-6 rounded-3xl cockpit-card space-y-4 shadow-xl">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2.5">
            <span class="text-sm font-bold text-white">2. Поиск общего знаменателя (НОК)</span>
            <span class="text-[11px] font-bold text-[#10B981] bg-[#142E23] px-2.5 py-0.5 rounded-md">Освоено</span>
          </div>
          <span class="text-xs font-mono-code font-bold text-[#10B981]">92% освоено</span>
        </div>
        <div class="w-full h-2.5 rounded-full bg-[#121319] overflow-hidden">
          <div class="h-full bg-[#10B981] rounded-full" style="width: 92%"></div>
        </div>
        <div class="p-4 rounded-2xl bg-[#121319] text-xs text-[#CBD5E1] space-y-1">
          <span class="text-[#10B981] font-semibold">✓ Отличная скорость:</span>
          <p class="text-[11px] text-[#94A3B8]">Быстро находишь НОК чисел 4 и 6, 3 и 5. Среднее время ответа в боте: 14 секунд. Алгоритм разложения усвоен прочно.</p>
        </div>
      </div>

      <!-- ТЕМА 3 (ОТЛИЧНО) -->
      <div class="p-6 rounded-3xl cockpit-card space-y-4 shadow-xl">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2.5">
            <span class="text-sm font-bold text-white">3. Сравнение и анализ долей</span>
            <span class="text-[11px] font-bold text-[#10B981] bg-[#142E23] px-2.5 py-0.5 rounded-md">Отлично</span>
          </div>
          <span class="text-xs font-mono-code font-bold text-[#10B981]">98% освоено</span>
        </div>
        <div class="w-full h-2.5 rounded-full bg-[#121319] overflow-hidden">
          <div class="h-full bg-[#10B981] rounded-full" style="width: 98%"></div>
        </div>
        <div class="p-4 rounded-2xl bg-[#121319] text-xs text-[#CBD5E1] space-y-1">
          <span class="text-[#10B981] font-semibold">✓ Интуитивное понимание:</span>
          <p class="text-[11px] text-[#94A3B8]">Моментально определяешь равенство или различие долей. Среднее время ответа в боте: 6 секунд.</p>
        </div>
      </div>

      <!-- ТЕМА 4 (В ПРОЦЕССЕ) -->
      <div class="p-6 rounded-3xl cockpit-card space-y-4 shadow-xl">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2.5">
            <span class="text-sm font-bold text-white">4. Сокращение дробей и выделение целой части</span>
            <span class="text-[11px] font-bold text-[#F59E0B] bg-[#382D12] px-2.5 py-0.5 rounded-md">В процессе</span>
          </div>
          <span class="text-xs font-mono-code font-bold text-[#F59E0B]">65% освоено</span>
        </div>
        <div class="w-full h-2.5 rounded-full bg-[#121319] overflow-hidden">
          <div class="h-full bg-[#F59E0B] rounded-full" style="width: 65%"></div>
        </div>
        <div class="p-4 rounded-2xl bg-[#121319] text-xs text-[#CBD5E1] space-y-1">
          <span class="text-[#F59E0B] font-semibold">⚠️ Требует закрепления:</span>
          <p class="text-[11px] text-[#94A3B8]">Иногда оставляешь ответ в виде 6/12 вместо 1/2. Запланировано в следующем тренировочном спринте.</p>
        </div>
      </div>

    </div>
'''

# 3. student/bottleneck.html (Разбор ошибок)
student_bottleneck_content = '''
    <div class="flex items-center justify-between">
      <div>
        <h2 class="text-xl font-bold text-white tracking-wide">🔍 Разбор ошибок: Домножение Числителя</h2>
        <p class="text-xs text-[#94A3B8]">Почему ответ 1/12 + 1/12 был неверным, и как правильно мыслить на Шаге 3.</p>
      </div>
      <a href="index.html" class="text-xs text-[#94A3B8] hover:text-white transition-all flex items-center gap-1">
        <span>← Назад на Главную</span>
      </a>
    </div>

    <!-- КАРТОЧКА СОПОСТАВЛЕНИЯ -->
    <div class="cockpit-card rounded-3xl p-7 space-y-6">
      <div class="flex items-center justify-between">
        <span class="text-xs uppercase tracking-wider text-[#D4AF37] font-semibold">Пример: 1/4 + 1/6</span>
        <span class="text-xs text-[#94A3B8]">Задача №318 из учебника</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
        <!-- КАК ОТВЕТИЛ В БОТЕ -->
        <div class="p-6 rounded-2xl bg-[#261517] space-y-3">
          <span class="text-[#EF4444] font-bold uppercase tracking-wider text-[11px]">❌ Как ты ответил в боте МАХ:</span>
          <div class="font-mono-code text-lg text-white font-bold">1/12 + 1/12 = 2/12</div>
          <p class="text-xs text-[#94A3B8] leading-relaxed">
            Знаменатели стали 12, а числители остались единицами. В итоге дробь 1/4 превратилась в 1/12, то есть уменьшилась в 3 раза! Пропорция нарушена.
          </p>
        </div>

        <!-- КАК ПРАВИЛЬНО МЫСЛИТЬ -->
        <div class="p-6 rounded-2xl bg-[#142E23] space-y-3">
          <span class="text-[#10B981] font-bold uppercase tracking-wider text-[11px]">✓ Как правильно мыслить:</span>
          <div class="font-mono-code text-lg text-white font-bold">3/12 + 2/12 = 5/12</div>
          <p class="text-xs text-[#94A3B8] leading-relaxed">
            Знаменатель 4 вырос в 3 раза (до 12) -> числитель 1 тоже умножаем на 3 (получаем 3/12)! Знаменатель 6 вырос в 2 раза -> числитель умножаем на 2 (получаем 2/12)!
          </p>
        </div>
      </div>

      <div class="flex flex-wrap items-center gap-3 pt-2">
        <button onclick="showPizzaRule()" class="py-3 px-5 rounded-xl btn-secondary-dark text-xs font-semibold hover:text-[#D4AF37]">
          🍕 Правило Пиццы (почему доли должны быть равны)
        </button>
        <button onclick="runRamisCalc()" class="py-3 px-5 rounded-xl btn-secondary-dark text-xs font-semibold hover:text-[#D4AF37]">
          🧮 Проверить расчет НОК (Закон Рамиса)
        </button>
        <button onclick="requestTwinProblem()" class="py-3 px-5 rounded-xl btn-primary-white text-xs font-bold">
          🔄 Запросить задачу-двойник в бот МАХ
        </button>
      </div>
    </div>
'''

# 4. student/history.html (История в боте)
student_history_content = '''
    <div class="flex items-center justify-between">
      <div>
        <h2 class="text-xl font-bold text-white tracking-wide">📱 История в боте МАХ (@max_math_bot)</h2>
        <p class="text-xs text-[#94A3B8]">Синхронизировано по API. Все ответы, задержки размышления и статус помощи.</p>
      </div>
      <a href="index.html" class="text-xs text-[#94A3B8] hover:text-white transition-all flex items-center gap-1">
        <span>← Назад на Главную</span>
      </a>
    </div>

    <div class="cockpit-card rounded-3xl p-7 space-y-4">
      <div class="space-y-3 text-xs">

        <!-- СЕССИЯ 1 -->
        <div class="p-4 rounded-2xl bg-[#1F1718] flex flex-col md:flex-row items-start md:items-center justify-between gap-3">
          <div class="space-y-1">
            <div class="font-bold text-white flex items-center gap-2">
              <span class="text-sm">Задача №318: 1/4 + 1/6</span>
              <span class="text-[10px] text-[#EF4444] bg-[#3B1818] px-2 py-0.5 rounded font-mono-code font-bold">Пауза на Шаге 3</span>
            </div>
            <div class="text-[#94A3B8]">Пауза 112 сек на домножении числителей. Получена наводящая подсказка бота о равенстве долей.</div>
          </div>
          <div class="text-left md:text-right">
            <div class="text-[#F59E0B] font-bold font-mono-code text-sm">84% автономия</div>
            <div class="text-[10px] text-[#71717A]">Сегодня, 16:22</div>
          </div>
        </div>

        <!-- СЕССИЯ 2 -->
        <div class="p-4 rounded-2xl bg-[#121319] flex flex-col md:flex-row items-start md:items-center justify-between gap-3">
          <div class="space-y-1">
            <div class="font-bold text-white flex items-center gap-2">
              <span class="text-sm">Задача №317: 1/2 + 1/4</span>
              <span class="text-[10px] text-[#10B981] bg-[#142E23] px-2 py-0.5 rounded font-mono-code font-bold">Решено чисто</span>
            </div>
            <div class="text-[#94A3B8]">Базовые дроби, общий знаменатель 4 найден с первой попытки за 4 минуты.</div>
          </div>
          <div class="text-left md:text-right">
            <div class="text-[#10B981] font-bold font-mono-code text-sm">95% автономия</div>
            <div class="text-[10px] text-[#71717A]">Сегодня, 16:15</div>
          </div>
        </div>

        <!-- СЕССИЯ 3 -->
        <div class="p-4 rounded-2xl bg-[#121319] flex flex-col md:flex-row items-start md:items-center justify-between gap-3">
          <div class="space-y-1">
            <div class="font-bold text-white flex items-center gap-2">
              <span class="text-sm">Задача №315: 3/8 + 1/8</span>
              <span class="text-[10px] text-[#10B981] bg-[#142E23] px-2 py-0.5 rounded font-mono-code font-bold">Решено мгновенно</span>
            </div>
            <div class="text-[#94A3B8]">Одинаковые знаменатели: 3 + 1 = 4/8 -> сокращение до 1/2. Автономия 100%.</div>
          </div>
          <div class="text-left md:text-right">
            <div class="text-[#10B981] font-bold font-mono-code text-sm">100% автономия</div>
            <div class="text-[10px] text-[#71717A]">Вчера, 17:40</div>
          </div>
        </div>

      </div>
    </div>
'''

# 5. student/planner.html (План Тренировок)
student_planner_content = '''
    <div class="flex items-center justify-between">
      <div>
        <h2 class="text-xl font-bold text-white tracking-wide">📅 План Тренировок</h2>
        <p class="text-xs text-[#94A3B8]">Тайм-менеджмент и подготовка к контрольной работе в боте МАХ.</p>
      </div>
      <a href="index.html" class="text-xs text-[#94A3B8] hover:text-white transition-all flex items-center gap-1">
        <span>← Назад на Главную</span>
      </a>
    </div>

    <div class="cockpit-card rounded-3xl p-7 space-y-6">
      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2">
        <div class="space-y-1">
          <span class="text-xs text-[#D4AF37] font-bold uppercase tracking-wider">Текущий тренировочный спринт</span>
          <div class="text-base font-bold text-white">Домножение числителей при сложении дробей</div>
        </div>
        <div class="px-4 py-2 rounded-xl bg-[#382D12] text-[#F59E0B] font-mono-code font-bold text-xs">
          Дедлайн: 16:30 (осталось 18 мин)
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs">
        <div class="p-4 rounded-2xl bg-[#121319] space-y-1">
          <div class="text-[10px] uppercase text-[#71717A] font-bold">Задач в серии</div>
          <div class="text-white font-bold text-sm">3 задачи-двойника</div>
          <div class="text-[11px] text-[#94A3B8]">Решено: 1 из 3</div>
        </div>
        <div class="p-4 rounded-2xl bg-[#121319] space-y-1">
          <div class="text-[10px] uppercase text-[#71717A] font-bold">Баланс времени</div>
          <div class="text-white font-bold text-sm">План: 20 мин / Факт: 12 мин</div>
          <div class="text-[11px] text-[#10B981]">Идешь с опережением графика</div>
        </div>
        <div class="p-4 rounded-2xl bg-[#121319] space-y-1">
          <div class="text-[10px] uppercase text-[#71717A] font-bold">Уведомление в МАХ</div>
          <div class="text-white font-bold text-sm">За 10 мин до конца</div>
          <div class="text-[11px] text-[#F59E0B]">Пуш придет в 16:20</div>
        </div>
      </div>

      <div class="pt-2">
        <a href="https://max.mail.ru" target="_blank" class="w-full py-4 px-4 rounded-2xl btn-primary-white text-xs font-bold text-center block shadow-lg hover:scale-[1.01] transition-all">
          🚀 Запустить тренировочную серию в боте МАХ (@max_math_bot)
        </a>
      </div>
    </div>
'''

# 6. student/tools.html (Шпаргалки и правила)
student_tools_content = '''
    <div class="flex items-center justify-between">
      <div>
        <h2 class="text-xl font-bold text-white tracking-wide">🧮 Шпаргалки и правила к боту МАХ</h2>
        <p class="text-xs text-[#94A3B8]">Наглядные правила, калькулятор Закона Рамиса и связь с учителем.</p>
      </div>
      <a href="index.html" class="text-xs text-[#94A3B8] hover:text-white transition-all flex items-center gap-1">
        <span>← Назад на Главную</span>
      </a>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-5 pt-2">

      <div class="p-6 rounded-3xl cockpit-card space-y-4">
        <div class="text-2xl">🍕</div>
        <h3 class="text-base font-bold text-white">Правило Пиццы (Наглядные доли)</h3>
        <p class="text-xs text-[#94A3B8] leading-relaxed">
          Нельзя складывать кусок от пиццы на 4 части и кусок от пиццы на 6 частей — они разного размера! Сначала разрежем обе пиццы на 12 одинаковых кусочков: 1/4 = 3/12, 1/6 = 2/12. Теперь 3 + 2 = 5 кусочков из 12!
        </p>
        <button onclick="showPizzaRule()" class="px-4 py-2.5 rounded-xl btn-secondary-dark text-xs font-semibold">
          Показать наглядную анимацию
        </button>
      </div>

      <div class="p-6 rounded-3xl cockpit-card space-y-4">
        <div class="text-2xl">🧮</div>
        <h3 class="text-base font-bold text-white">Калькулятор НОК (Закон Рамиса)</h3>
        <p class="text-xs text-[#94A3B8] leading-relaxed">
          Человек строит математическую логику и понимает доли, а рутинный счет столбиком машина берет на себя. Введи знаменатели и мгновенно получи НОК с множителями.
        </p>
        <button onclick="runRamisCalc()" class="px-4 py-2.5 rounded-xl btn-secondary-dark text-xs font-semibold">
          Рассчитать для 4 и 6 (НОК = 12)
        </button>
      </div>

      <div class="p-6 rounded-3xl cockpit-card space-y-4">
        <div class="text-2xl">🔄</div>
        <h3 class="text-base font-bold text-white">Задача-Двойник в бот</h3>
        <p class="text-xs text-[#94A3B8] leading-relaxed">
          Сгенерировать параллельную задачу (например, 1/4 + 5/6) с той же структурой, чтобы проверить себя без подсказок ГДЗ.
        </p>
        <button onclick="requestTwinProblem()" class="px-4 py-2.5 rounded-xl btn-primary-white text-xs font-bold">
          Отправить задачу-двойник в бот
        </button>
      </div>

      <div class="p-6 rounded-3xl cockpit-card space-y-4">
        <div class="text-2xl">🙋</div>
        <h3 class="text-base font-bold text-white">Вопрос Учительнице в МАХ</h3>
        <p class="text-xs text-[#94A3B8] leading-relaxed">
          Застрял на шаге? Отправь точечный вопрос Марье Ивановне прямо в мессенджер МАХ вместе с контекстом твоей текущей задачи.
        </p>
        <button onclick="askTeacher()" class="px-4 py-2.5 rounded-xl btn-secondary-dark text-xs font-semibold">
          Отправить вопрос учительнице
        </button>
      </div>

    </div>
'''

# ==================== TEACHER PAGES ====================

# 1. teacher/index.html (Мониторинг класса)
teacher_index_content = '''
    <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
      <div>
        <h2 class="text-xl font-bold text-white tracking-wide">👥 Мониторинг Класса (28 учеников)</h2>
        <p class="text-xs text-[#94A3B8]">Мониторинг этапов решения в боте МАХ в реальном времени • Синхронизация каждые 3 сек.</p>
      </div>
      <div class="flex items-center gap-3">
        <button onclick="generateTwinProblemForClass()" class="px-4 py-2 rounded-xl btn-primary-white text-xs font-bold shadow-md">
          ⚡ Сгенерировать задачу-двойник 17 застрявшим
        </button>
      </div>
    </div>

    <!-- АЛЕРТ УЗКОГО МЕСТА УРОКА -->
    <div class="p-4 rounded-2xl bg-[#2A1517] flex items-center justify-between shadow-lg">
      <div class="flex items-center gap-3">
        <span class="text-xl">⚠️</span>
        <div>
          <div class="text-xs font-bold text-[#EF4444]">Узкое место урока: Шаг 3 (Домножение числителей)</div>
          <div class="text-[11px] text-[#94A3B8]">62% класса (17 из 28 учеников) забыли домножить числитель первой дроби на 3.</div>
        </div>
      </div>
      <a href="diagnostics.html?id=1" class="px-4 py-2 rounded-xl bg-[#3B1818] text-[#EF4444] font-bold text-xs hover:bg-[#4E2020] transition-all">
        Разбор учеников →
      </a>
    </div>

    <!-- ТАБЛИЦА МОНИТОРИНГА КЛАССА С ДИНАМИЧЕСКИМИ ШАГАМИ -->
    <div class="cockpit-card rounded-3xl p-6 space-y-4">
      <div class="grid grid-cols-12 px-4 py-2 text-[11px] font-bold uppercase tracking-wider text-[#71717A]">
        <div class="col-span-4">Ученик</div>
        <div class="col-span-2 text-center">1. Анализ долей</div>
        <div class="col-span-2 text-center">2. Общий знаменатель</div>
        <div class="col-span-2 text-center">3. Домножение ⚠️</div>
        <div class="col-span-2 text-center">4. Ответ</div>
      </div>

      <div class="space-y-2 text-xs" id="studentsMatrixContainer">
        <!-- Иванов Михаил -->
        <a href="diagnostics.html?id=1" class="grid grid-cols-12 items-center px-4 py-3 rounded-2xl bg-[#222432] text-xs shadow-md block">
          <div class="col-span-4 font-bold text-white flex items-center gap-2">
            <span>Иванов Михаил</span>
            <span class="text-[#D4AF37]">★</span>
          </div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-green">Пройдено</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-yellow">НОК = 12</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-red">62% застряли</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-green">Сдано</span></div>
        </a>

        <!-- Алексеева Анна -->
        <a href="diagnostics.html?id=2" class="grid grid-cols-12 items-center px-4 py-3 rounded-2xl cockpit-card-elevated text-xs hover:bg-[#20222D] block transition-all">
          <div class="col-span-4 font-bold text-white">Алексеева Анна</div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-green">Пройдено</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-yellow">НОК = 12</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-red">62% застряли</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-green">Сдано</span></div>
        </a>

        <!-- Бондаренко Дмитрий -->
        <a href="diagnostics.html?id=3" class="grid grid-cols-12 items-center px-4 py-3 rounded-2xl cockpit-card-elevated text-xs hover:bg-[#20222D] block transition-all">
          <div class="col-span-4 font-bold text-white">Бондаренко Дмитрий</div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-green">Пройдено</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-yellow">НОК = 12</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-red">62% застряли</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-green">Сдано</span></div>
        </a>

        <!-- Хайрутдинов Рамис -->
        <a href="diagnostics.html?id=4" class="grid grid-cols-12 items-center px-4 py-3 rounded-2xl cockpit-card-elevated text-xs hover:bg-[#20222D] block transition-all">
          <div class="col-span-4 font-bold text-[#D4AF37]">Хайрутдинов Рамис</div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-green">Пройдено</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-green">НОК = 12</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-yellow">в работе</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-green">Сдано</span></div>
        </a>

        <!-- Гарипов Тимур -->
        <a href="diagnostics.html?id=6" class="grid grid-cols-12 items-center px-4 py-3 rounded-2xl cockpit-card-elevated text-xs hover:bg-[#20222D] block transition-all">
          <div class="col-span-4 font-bold text-white">Гарипов Тимур</div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-green">Пройдено</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-green">НОК = 12</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-green">Пройдено</span></div>
          <div class="col-span-2 text-center"><span class="px-3 py-1 rounded-md text-[11px] font-semibold pill-status-green">Сдано</span></div>
        </a>
      </div>
    </div>
'''

# 2. teacher/diagnostics.html (Разбор ученика)
teacher_diagnostics_content = '''
    <div class="flex items-center justify-between">
      <div>
        <h2 class="text-xl font-bold text-white tracking-wide">🔍 Разбор Ученика</h2>
        <p class="text-xs text-[#94A3B8]">Глубокий анализ мыслительного процесса, задержек и уровня самостоятельности.</p>
      </div>
      <a href="index.html" class="text-xs text-[#94A3B8] hover:text-white transition-all flex items-center gap-1">
        <span>← Назад в Мониторинг</span>
      </a>
    </div>

    <!-- СЕЛЕКТОР УЧЕНИКОВ -->
    <div class="flex flex-wrap gap-2 pt-1">
      <button onclick="selectStudent(1)" class="px-3.5 py-1.5 rounded-xl bg-white text-black text-xs font-bold shadow-md">Иванов Михаил</button>
      <button onclick="selectStudent(2)" class="px-3.5 py-1.5 rounded-xl bg-[#1D1E26] text-[#CBD5E1] text-xs font-medium hover:bg-[#262835]">Алексеева Анна</button>
      <button onclick="selectStudent(3)" class="px-3.5 py-1.5 rounded-xl bg-[#1D1E26] text-[#CBD5E1] text-xs font-medium hover:bg-[#262835]">Бондаренко Дмитрий</button>
      <button onclick="selectStudent(4)" class="px-3.5 py-1.5 rounded-xl bg-[#1D1E26] text-[#D4AF37] text-xs font-bold hover:bg-[#262835]">Хайрутдинов Рамис</button>
      <button onclick="selectStudent(6)" class="px-3.5 py-1.5 rounded-xl bg-[#1D1E26] text-[#CBD5E1] text-xs font-medium hover:bg-[#262835]">Гарипов Тимур</button>
    </div>

    <div class="grid grid-cols-12 gap-6 pt-2">

      <!-- ЛЕВАЯ КОЛОНКА (65%): СПАРКЛАЙН + ДИАГНОЗ -->
      <div class="col-span-12 lg:col-span-8 cockpit-card rounded-3xl p-7 space-y-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3.5">
            <div class="w-12 h-12 rounded-2xl bg-[#1D1E26] flex items-center justify-center font-bold text-sm text-[#10B981]">УЧ</div>
            <div>
              <div id="diagStudentName" class="text-base font-bold text-white">Иванов Михаил</div>
              <div class="text-xs text-[#71717A]">5 «Б» класс • Анализ решения задачи №318</div>
            </div>
          </div>
          <span id="diagStudentCategory" class="px-3 py-1 rounded-lg text-xs font-bold text-[#EF4444] bg-[#3B1818]">
            Пропуск домножения числителя
          </span>
        </div>

        <!-- График времени размышления -->
        <div class="space-y-2">
          <div class="flex items-center justify-between text-xs">
            <span class="text-[#94A3B8]">Кривая времени размышления по шагам (сек)</span>
            <span class="text-white font-mono-code font-bold">100 / 50 / 0 сек</span>
          </div>
          <div class="p-4 rounded-2xl bg-[#121319]">
            <canvas id="teacherLatencyCanvas" width="400" height="90" class="w-full h-24"></canvas>
          </div>
        </div>

        <div class="p-4 rounded-2xl bg-[#14151D] text-xs text-[#CBD5E1] space-y-1.5">
          <span class="text-[#D4AF37] font-semibold">⏱️ Зачем учителю этот график:</span>
          <p class="leading-relaxed text-[#94A3B8] text-[11px]">
            Задержка > 100 сек на Шаге 3 означает, что ученик застрял именно на домножении. Учитель видит конкретный затык и отправляет точечную подсказку, не тратя время на весь пример. А время менее 3 сек указывает на бездумное списывание с ГДЗ.
          </p>
        </div>

        <div class="p-4 rounded-2xl bg-[#181922] text-xs space-y-1">
          <span class="text-white font-semibold">Педагогическая заметка:</span>
          <p id="diagStudentNote" class="text-[#94A3B8] text-[11px]">Забыл домножить числитель первой дроби на 3. Требуется формирующий стикер.</p>
        </div>
      </div>

      <!-- ПРАВАЯ КОЛОНКА (35%): ИНДЕКС И БЫСТРЫЕ ДЕЙСТВИЯ -->
      <div class="col-span-12 lg:col-span-4 space-y-5">

        <div class="cockpit-card rounded-3xl p-6 space-y-5">
          <h3 class="text-sm font-bold text-white tracking-wide">Индекс Самостоятельности</h3>
          <div class="flex items-center justify-center py-2">
            <div class="w-28 h-28 rounded-full bg-[#1D1E26] flex items-center justify-center shadow-inner">
              <div class="w-22 h-22 rounded-full bg-[#121319] flex items-center justify-center">
                <span id="diagStudentAutonomyCircle" class="text-2xl font-bold text-white">74%</span>
              </div>
            </div>
          </div>
          <div class="text-[11px] text-[#94A3B8] text-center">
            Показывает процент шагов, решенных учеником самостоятельно без готовых ответов из сети.
          </div>
        </div>

        <div class="cockpit-card rounded-3xl p-6 space-y-3">
          <h3 class="text-sm font-bold text-white tracking-wide">Действия для этого ученика</h3>
          <button onclick="generateTwinProblemForClass()" class="w-full py-3 px-3.5 rounded-xl btn-primary-white text-xs font-bold text-left shadow-md">
            🔄 Отправить задачу-двойник в МАХ
          </button>
          <button onclick="sendFormativeSticker()" class="w-full py-2.5 px-3.5 rounded-xl btn-secondary-dark text-xs font-medium text-left">
            🏷️ Отправить формирующий стикер
          </button>
          <button onclick="triggerMiniLesson()" class="w-full py-2.5 px-3.5 rounded-xl btn-secondary-dark text-xs font-medium text-left">
            📋 Запустить карточку 3-минутки
          </button>
        </div>

      </div>

    </div>
'''

# 3. teacher/planner.html (План урока)
teacher_planner_content = '''
    <div class="flex items-center justify-between">
      <div>
        <h2 class="text-xl font-bold text-white tracking-wide">⏱️ План Урока (45 минут)</h2>
        <p class="text-xs text-[#94A3B8]">Тайм-менеджмент 45-минутного урока в 5 классе с интеграцией бота МАХ.</p>
      </div>
      <a href="index.html" class="text-xs text-[#94A3B8] hover:text-white transition-all flex items-center gap-1">
        <span>← Назад в Мониторинг</span>
      </a>
    </div>

    <div class="cockpit-card rounded-3xl p-7 space-y-6">
      <div class="flex items-center justify-between">
        <span class="text-xs uppercase tracking-wider text-[#D4AF37] font-semibold">5 «Б» класс • Урок математики</span>
        <span class="text-xs font-mono-code text-white">Текущий тайминг: <b class="text-[#10B981]">22 мин из 45</b></span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
        <div class="p-5 rounded-2xl bg-[#142E23] space-y-1.5">
          <div class="text-[10px] uppercase text-[#10B981] font-bold">1. Теория и правила</div>
          <div class="text-white font-bold text-sm">10 мин (Завершено ✓)</div>
          <div class="text-[11px] text-[#94A3B8]">Разбор правила равенства долей на доске.</div>
        </div>

        <div class="p-5 rounded-2xl bg-[#222432] space-y-1.5">
          <div class="text-[10px] uppercase text-[#D4AF37] font-bold">2. Практикум в боте МАХ</div>
          <div class="text-white font-bold text-sm">20 мин (Идет — 12 мин)</div>
          <div class="text-[11px] text-[#94A3B8]">Ученики решают задачи по шагам в мессенджере.</div>
        </div>

        <div class="p-5 rounded-2xl bg-[#14151D] space-y-1.5">
          <div class="text-[10px] uppercase text-[#71717A] font-bold">3. Разбор узких мест</div>
          <div class="text-white font-bold text-sm">15 мин (Ожидает)</div>
          <div class="text-[11px] text-[#94A3B8]">Фокус на домножении первой дроби на 3.</div>
        </div>
      </div>

      <div class="flex flex-wrap items-center gap-3 pt-2">
        <button onclick="alert('Уведомление отправлено всем 28 ученикам в мессенджер МАХ!')" class="py-3 px-5 rounded-xl btn-primary-white text-xs font-bold shadow-md">
          🔔 Отправить напоминание о дедлайне в МАХ
        </button>
        <button onclick="alert('Спринт продлен на 5 минут. Таймеры в ботах обновлены.')" class="py-3 px-5 rounded-xl btn-secondary-dark text-xs font-semibold">
          ⏱️ Продлить спринт (+5 мин)
        </button>
      </div>
    </div>
'''

# 4. teacher/actions.html (Быстрая помощь)
teacher_actions_content = '''
    <div class="flex items-center justify-between">
      <div>
        <h2 class="text-xl font-bold text-white tracking-wide">⚡ Быстрая Помощь</h2>
        <p class="text-xs text-[#94A3B8]">Точечные формирующие воздействия на класс и экспорт аналитики.</p>
      </div>
      <a href="index.html" class="text-xs text-[#94A3B8] hover:text-white transition-all flex items-center gap-1">
        <span>← Назад в Мониторинг</span>
      </a>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-5 pt-2">

      <div class="p-6 rounded-3xl cockpit-card space-y-4">
        <div class="text-2xl">🔄</div>
        <h3 class="text-base font-bold text-white">Задача-Двойник 17 ученикам</h3>
        <p class="text-xs text-[#94A3B8] leading-relaxed">
          Мгновенно разослать параллельный пример (1/4 + 5/6) всем 17 ученикам, которые застряли на домножении числителей.
        </p>
        <button onclick="generateTwinProblemForClass()" class="px-4 py-2.5 rounded-xl btn-primary-white text-xs font-bold">
          Сгенерировать и отправить классу
        </button>
      </div>

      <div class="p-6 rounded-3xl cockpit-card space-y-4">
        <div class="text-2xl">🏷️</div>
        <h3 class="text-base font-bold text-white">Отправка Формирующего Стикера</h3>
        <p class="text-xs text-[#94A3B8] leading-relaxed">
          Отправить ободряющий стикер с подсказкой («Обрати внимание на домножение числителя») выбранному ученику в чат МАХ.
        </p>
        <button onclick="sendFormativeSticker()" class="px-4 py-2.5 rounded-xl btn-secondary-dark text-xs font-semibold">
          Отправить стикер выбранному
        </button>
      </div>

      <div class="p-6 rounded-3xl cockpit-card space-y-4">
        <div class="text-2xl">📋</div>
        <h3 class="text-base font-bold text-white">Карточка 3-минутки</h3>
        <p class="text-xs text-[#94A3B8] leading-relaxed">
          Сгенерировать экспресс-разбор типичной ошибки на проектор для демонстрации всему классу в конце спринта.
        </p>
        <button onclick="triggerMiniLesson()" class="px-4 py-2.5 rounded-xl btn-secondary-dark text-xs font-semibold">
          Вывести 3-минутку на проектор
        </button>
      </div>

      <div class="p-6 rounded-3xl cockpit-card space-y-4">
        <div class="text-2xl">📄</div>
        <h3 class="text-base font-bold text-white">Экспорт Аналитики Класса</h3>
        <p class="text-xs text-[#94A3B8] leading-relaxed">
          Выгрузка детального отчета по 28 ученикам (время размышления, % автономии, типичные ошибки) для завуча и родителей.
        </p>
        <button onclick="alert('Отчет экспортирован в формате PDF/Excel.')" class="px-4 py-2.5 rounded-xl btn-secondary-dark text-xs font-semibold">
          Экспортировать отчет в PDF
        </button>
      </div>

    </div>
'''

# WRITE FILES
files_to_write = [
    (os.path.join(STUDENT_DIR, "index.html"), wrap_student_page("index.html", "Главная", student_index_content)),
    (os.path.join(STUDENT_DIR, "topics.html"), wrap_student_page("topics.html", "Темы и проблемы", student_topics_content)),
    (os.path.join(STUDENT_DIR, "bottleneck.html"), wrap_student_page("bottleneck.html", "Разбор ошибок", student_bottleneck_content)),
    (os.path.join(STUDENT_DIR, "history.html"), wrap_student_page("history.html", "История в боте", student_history_content)),
    (os.path.join(STUDENT_DIR, "planner.html"), wrap_student_page("planner.html", "План Тренировок", student_planner_content)),
    (os.path.join(STUDENT_DIR, "tools.html"), wrap_student_page("tools.html", "Шпаргалки и правила", student_tools_content)),

    (os.path.join(TEACHER_DIR, "index.html"), wrap_teacher_page("index.html", "Мониторинг Класса", teacher_index_content)),
    (os.path.join(TEACHER_DIR, "diagnostics.html"), wrap_teacher_page("diagnostics.html", "Разбор Ученика", teacher_diagnostics_content)),
    (os.path.join(TEACHER_DIR, "planner.html"), wrap_teacher_page("planner.html", "План Урока", teacher_planner_content)),
    (os.path.join(TEACHER_DIR, "actions.html"), wrap_teacher_page("actions.html", "Быстрая Помощь", teacher_actions_content)),
]

for path, content in files_to_write:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated with exact chosen titles: {path}")

print("All 10 multi-page files updated successfully!")
