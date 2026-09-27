#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

with open("/home/ramis/projectAnti/Хакатоны/MAX_Образование/web/build_multipage.py", "r", encoding="utf-8") as f:
    content = f.read()

# Добавляем селектор классов в teacher_header
old_str = '''      <span class="text-[11px] px-3 py-1.5 rounded-full bg-[#3B1818] text-[#EF4444] font-semibold hidden md:inline-block">
        Узкое место: Шаг 3 (17 застряли)
      </span>'''

new_str = '''      <!-- ВЫБОР КЛАССА -->
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
      </span>'''

content = content.replace(old_str, new_str)

with open("/home/ramis/projectAnti/Хакатоны/MAX_Образование/web/build_multipage.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated build_multipage.py with class switcher.")
