#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-page builder for Student Analytics and Teacher Cockpit
Updated with Ramis's exact chosen titles:
Учитель: Мониторинг класса, Разбор ученика, План урока, Быстрая помощь
Ученик: Главная, Темы и проблемы, Разбор ошибок, История в боте, План Тренировок, Шпаргалки и правила
"""
import os

WEB_DIR = "/home/ramis/projectAnti/Хакатоны/MAX_Образование/web"
STUDENT_DIR = os.path.join(WEB_DIR, "student")
TEACHER_DIR = os.path.join(WEB_DIR, "teacher")

# --- HTML TEMPLATES ---

def student_header(active_tab):
    tabs = [
        ("index.html", "🏠 Главная"),
        ("topics.html", "🗺️ Темы и проблемы"),
        ("bottleneck.html", "🔍 Разбор ошибок"),
        ("history.html", "📱 История в боте"),
        ("planner.html", "📅 План Тренировок"),
        ("tools.html", "🧮 Шпаргалки и правила")
    ]
    tabs_html = ""
    for href, label in tabs:
        is_active = (href == active_tab)
        bg_class = "bg-[#D4AF37] text-black font-bold shadow-md" if is_active else "text-[#94A3B8] hover:text-white hover:bg-[#1D1E26] font-medium"
        tabs_html += f'<a href="{href}" class="px-3.5 py-1.5 rounded-xl text-xs transition-all {bg_class}">{label}</a>\n'

    drawer_links = ""
    for href, label in tabs:
        is_active = (href == active_tab)
        drawer_bg = "bg-[#D4AF37] text-black font-bold" if is_active else "bg-[#16171D] text-[#CBD5E1] hover:bg-[#20222D]"
        drawer_links += f'<a href="{href}" class="w-full flex items-center gap-3 p-3 rounded-xl {drawer_bg} text-xs transition-all">{label}</a>\n'

    return f'''
  <!-- ВЫДВИЖНОЕ МЕНЮ НАВИГАЦИИ -->
  <div id="navMenuDrawer" class="hidden fixed inset-0 z-50 flex">
    <div onclick="toggleNavMenu()" class="fixed inset-0 bg-black/70 backdrop-blur-sm"></div>
    <div class="relative w-80 max-w-[85vw] h-full bg-[#111216] p-6 shadow-2xl flex flex-col justify-between z-10">
      <div class="space-y-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2.5">
            <div class="w-8 h-8 rounded-xl bg-[#1D1E26] flex items-center justify-center font-bold text-xs text-[#D4AF37]">МАХ</div>
            <span class="font-bold text-sm text-white">Кабинет Ученика</span>
          </div>
          <button onclick="toggleNavMenu()" class="text-xl text-[#71717A] hover:text-white p-1 rounded-lg">✕</button>
        </div>
        <nav class="space-y-2">
          {drawer_links}
        </nav>
      </div>
      <div class="pt-4 space-y-3">
        <a href="../teacher/index.html" class="w-full flex items-center justify-center gap-2 p-3 rounded-xl btn-primary-white text-xs font-bold">
          <span>В Кабинет Учителя</span> <span>→</span>
        </a>
        <div class="text-[11px] text-[#71717A] text-center">Платформа МАХ.Образование • 5 «Б» класс</div>
      </div>
    </div>
  </div>

  <!-- ШАПКА КАБИНЕТА С ВКЛАДКАМИ -->
  <header class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 px-6 py-4 rounded-2xl cockpit-surface shadow-xl">
    <div class="flex items-center gap-4">
      <button onclick="toggleNavMenu()" title="Открыть меню" class="p-2 rounded-xl bg-[#1A1C24] text-white hover:bg-[#252836] transition-all flex items-center gap-1.5 text-xs font-medium">
        <span class="text-base">☰</span>
        <span class="hidden sm:inline">Разделы</span>
      </button>
      <div>
        <h1 class="text-base font-bold tracking-wide text-white">Кабинет Ученика • Аналитика МАХ</h1>
        <p class="text-xs text-[#94A3B8]">Мониторинг знаний и пробелов • Решение задач в боте @max_math_bot</p>
      </div>
    </div>

    <!-- ГОРИЗОНТАЛЬНЫЕ ВКЛАДКИ РАЗДЕЛОВ -->
    <nav class="hidden xl:flex items-center gap-1.5 p-1 rounded-2xl bg-[#14151D]">
      {tabs_html}
    </nav>

    <div class="flex items-center gap-4 text-xs">
      <span class="text-[11px] px-3 py-1.5 rounded-full bg-[#142E23] text-[#10B981] font-semibold hidden lg:inline-block">
        ● Бот МАХ активен
      </span>
      <a href="../teacher/index.html" class="text-[#94A3B8] hover:text-[#D4AF37] transition-all hidden sm:flex items-center gap-1">
        <span>Кабинет Учителя</span> <span>→</span>
      </a>
      <div class="flex items-center gap-2 pl-2">
        <div class="w-8 h-8 rounded-full bg-[#1D1E26] flex items-center justify-center font-bold text-xs text-white">РХ</div>
        <span class="text-white font-medium hidden md:inline">Рамис Х.</span>
      </div>
    </div>
  </header>
'''

def teacher_header(active_tab):
    tabs = [
        ("index.html", "👥 Мониторинг класса"),
        ("diagnostics.html", "🔍 Разбор ученика"),
        ("planner.html", "⏱️ План урока"),
        ("actions.html", "⚡ Быстрая помощь")
    ]
    tabs_html = ""
    for href, label in tabs:
        is_active = (href == active_tab)
        bg_class = "bg-white text-black font-bold shadow-md" if is_active else "text-[#94A3B8] hover:text-white hover:bg-[#1D1E26] font-medium"
        tabs_html += f'<a href="{href}" class="px-3.5 py-1.5 rounded-xl text-xs transition-all {bg_class}">{label}</a>\n'

    drawer_links = ""
    for href, label in tabs:
        is_active = (href == active_tab)
        drawer_bg = "bg-white text-black font-bold" if is_active else "bg-[#16171D] text-[#CBD5E1] hover:bg-[#20222D]"
        drawer_links += f'<a href="{href}" class="w-full flex items-center gap-3 p-3 rounded-xl {drawer_bg} text-xs transition-all">{label}</a>\n'

    return f'''
  <!-- ВЫДВИЖНОЕ МЕНЮ НАВИГАЦИИ УЧИТЕЛЯ -->
  <div id="teacherNavDrawer" class="hidden fixed inset-0 z-50 flex">
    <div onclick="toggleTeacherNavMenu()" class="fixed inset-0 bg-black/70 backdrop-blur-sm"></div>
    <div class="relative w-80 max-w-[85vw] h-full bg-[#111216] p-6 shadow-2xl flex flex-col justify-between z-10">
      <div class="space-y-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2.5">
            <div class="w-8 h-8 rounded-xl bg-[#1D1E26] flex items-center justify-center font-bold text-xs text-[#10B981]">МАХ</div>
            <span class="font-bold text-sm text-white">Кабинет Учителя</span>
          </div>
          <button onclick="toggleTeacherNavMenu()" class="text-xl text-[#71717A] hover:text-white p-1 rounded-lg">✕</button>
        </div>
        <nav class="space-y-2">
          {drawer_links}
        </nav>
      </div>
      <div class="pt-4 space-y-3">
        <a href="../student/index.html" class="w-full flex items-center justify-center gap-2 p-3 rounded-xl btn-primary-white text-xs font-bold">
          <span>В Кабинет Ученика</span> <span>→</span>
        </a>
        <div class="text-[11px] text-[#71717A] text-center">Платформа МАХ.Образование • 5 класс</div>
      </div>
    </div>
  </div>

  <!-- ШАПКА КАБИНЕТА УЧИТЕЛЯ С ВКЛАДКАМИ -->
  <header class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 px-6 py-4 rounded-2xl cockpit-surface shadow-xl">
    <div class="flex items-center gap-4">
      <button onclick="toggleTeacherNavMenu()" title="Открыть меню" class="p-2 rounded-xl bg-[#1A1C24] text-white hover:bg-[#252836] transition-all flex items-center gap-1.5 text-xs font-medium">
        <span class="text-base">☰</span>
        <span class="hidden sm:inline">Разделы</span>
      </button>
      <div>
        <h1 class="text-base font-bold tracking-wide text-white">Кабинет Учителя • Аналитика МАХ</h1>
        <p class="text-xs text-[#94A3B8]">Мониторинг решений класса в реальном времени • Синхронизация с ботами МАХ</p>
      </div>
    </div>

    <!-- ГОРИЗОНТАЛЬНЫЕ ВКЛАДКИ РАЗДЕЛОВ -->
    <nav class="hidden lg:flex items-center gap-1.5 p-1 rounded-2xl bg-[#14151D]">
      {tabs_html}
    </nav>

    <div class="flex items-center gap-3 text-xs">
      <!-- ВЫБОР КЛАССА -->
      <div class="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-[#1D1E26] text-xs shadow-inner">
        <span class="text-[#71717A] text-[11px]">Класс:</span>
        <select id="classSelector" onchange="changeClass(this.value)" class="bg-transparent text-white font-bold cursor-pointer focus:outline-none pr-1">
          <option value="5b" class="bg-[#111216] text-white" selected>5 «Б» (28 уч.)</option>
          <option value="5a" class="bg-[#111216] text-white">5 «А» (26 уч.)</option>
          <option value="5v" class="bg-[#111216] text-white">5 «В» (29 уч.)</option>
          <option value="6a" class="bg-[#111216] text-white">6 «А» (27 уч.)</option>
        </select>
      </div>

      <span id="classBottleneckBadge" class="text-[11px] px-3 py-1.5 rounded-full bg-[#3B1818] text-[#EF4444] font-semibold hidden md:inline-block">
        Узкое место: Шаг 3 (17 застряли)
      </span>
      <a href="../student/index.html" class="text-[#94A3B8] hover:text-white transition-all hidden sm:flex items-center gap-1">
        <span>Ученик</span> <span>→</span>
      </a>
      <div class="flex items-center gap-2 pl-1">
        <div class="w-8 h-8 rounded-full bg-[#1D1E26] flex items-center justify-center font-bold text-xs text-white">МИ</div>
        <span class="text-white font-medium hidden md:inline">Марья Ив.</span>
      </div>
    </div>
  </header>
'''

print("Updated build_multipage.py templates with Ramis's chosen titles.")
