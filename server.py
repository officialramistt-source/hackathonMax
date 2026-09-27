#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
School Mathematic API & Static Server
Backend для платформ Ученика и Учителя хакатона МАХ
"""

import os
import json
import time
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

PORT = 8080
WEB_DIR = os.path.dirname(os.path.abspath(__file__))

# База состояния в памяти
STATE = {
    "currentProblem": {
        "id": 318,
        "title": "Задача №318: 1/4 + 1/6",
        "fractions": ["1/4", "1/6"],
        "commonDenominator": 12,
        "multipliers": [3, 2],
        "scaledFractions": ["3/12", "2/12"],
        "finalAnswer": "5/12"
    },
    "student": {
        "id": "STU-09551-RAMIS",
        "name": "Рамис Хайрутдинов",
        "class": "5 «Б»",
        "currentStep": 3,
        "thinkingTimeSec": 112,
        "autonomyIndex": 84,
        "focusCategory": "Домножение числителя (Шаг 3)",
        "stepsStatus": {
            "step1": {"status": "completed", "time": 6, "val": "4 ≠ 6"},
            "step2": {"status": "completed", "time": 14, "val": "НОК = 12"},
            "step3": {"status": "in_progress", "time": 112, "val": ""},
            "step4": {"status": "pending", "time": 0, "val": ""}
        },
        "recentTwin": None
    },
    "classMatrix": [
        {"id": 1, "name": "Иванов Михаил", "s1": "зеленый", "s2": "желтый", "s3": "62% класса застряли", "s4": "Ответ", "latency": 112, "autonomy": 74, "error": "Пропуск домножения числителя"},
        {"id": 2, "name": "Алексеева Анна", "s1": "зеленый", "s2": "желтый", "s3": "62% класса застряли", "s4": "Ответ", "latency": 95, "autonomy": 71, "error": "Пропуск домножения числителя"},
        {"id": 3, "name": "Бондаренко Дмитрий", "s1": "зеленый", "s2": "желтый", "s3": "62% класса застряли", "s4": "Ответ", "latency": 105, "autonomy": 68, "error": "Неверный доп. множитель"},
        {"id": 4, "name": "Хайрутдинов Рамис", "s1": "зеленый", "s2": "зеленый", "s3": "в работе", "s4": "Ответ", "latency": 112, "autonomy": 84, "error": "Глубокий анализ домножения"},
        {"id": 5, "name": "Васильева Елена", "s1": "зеленый", "s2": "желтый", "s3": "62% класса застряли", "s4": "Ответ", "latency": 88, "autonomy": 72, "error": "Пропуск домножения числителя"},
        {"id": 6, "name": "Гарипов Тимур", "s1": "зеленый", "s2": "зеленый", "s3": "зеленый", "s4": "Ответ", "latency": 18, "autonomy": 94, "error": "Нет ошибок"},
        {"id": 7, "name": "Дмитриев Артем", "s1": "зеленый", "s2": "желтый", "s3": "62% класса застряли", "s4": "Ответ", "latency": 98, "autonomy": 69, "error": "Пропуск домножения числителя"}
    ],
    "twinsGenerated": []
}

class CockpitHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def _send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == '/api/status':
            return self._send_json({'status': 'online', 'server': 'School Mathematic Engine', 'time': time.time()})

        elif path == '/api/student/state':
            return self._send_json(STATE['student'])

        elif path == '/api/teacher/class-matrix':
            return self._send_json({
                'totalStudents': 28,
                'stuckStep3': 17,
                'solvedAlone': 9,
                'students': STATE['classMatrix']
            })

        elif path == '/api/problem/current':
            return self._send_json(STATE['currentProblem'])

        # Иначе раздаем статические файлы (HTML, CSS, JS)
        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(length) if length > 0 else b'{}'
        
        try:
            body = json.loads(post_data.decode('utf-8'))
        except Exception:
            body = {}

        if path == '/api/student/submit-step':
            step = body.get('step', 3)
            answer = body.get('answer', '').strip().replace(' ', '')
            thinking_time = body.get('thinkingTime', 112)

            if step == 3:
                # Валидация домножения
                if answer in ['3/12+2/12', '2/12+3/12', '5/12']:
                    STATE['student']['currentStep'] = 4
                    STATE['student']['autonomyIndex'] = 88
                    STATE['student']['stepsStatus']['step3'] = {'status': 'completed', 'time': thinking_time, 'val': '3/12 + 2/12'}
                    STATE['student']['stepsStatus']['step4'] = {'status': 'in_progress', 'time': 0, 'val': ''}
                    
                    # Обновляем в матрице учителя
                    for st in STATE['classMatrix']:
                        if st['name'] == 'Хайрутдинов Рамис':
                            st['s3'] = 'зеленый'
                            st['autonomy'] = 88

                    return self._send_json({
                        'success': True,
                        'step': 3,
                        'status': 'passed',
                        'message': 'Верно! Дроби приведены к общему знаменателю: 3/12 + 2/12.',
                        'nextStep': 4,
                        'newAutonomy': 88
                    })
                else:
                    return self._send_json({
                        'success': False,
                        'step': 3,
                        'status': 'error',
                        'message': 'Ошибка домножения. Вспомни: 12 : 4 = 3 (числитель 1×3=3), 12 : 6 = 2 (числитель 1×2=2).'
                    })

            elif step == 4:
                if answer == '5/12':
                    STATE['student']['stepsStatus']['step4'] = {'status': 'completed', 'time': 18, 'val': '5/12'}
                    STATE['student']['autonomyIndex'] = 92
                    for st in STATE['classMatrix']:
                        if st['name'] == 'Хайрутдинов Рамис':
                            st['s4'] = '5/12 ✓'
                    return self._send_json({
                        'success': True,
                        'step': 4,
                        'status': 'completed',
                        'message': '🎉 Задача №318 полностью решена! Ответ 5/12 зафиксирован в журнале учителя.'
                    })
                else:
                    return self._send_json({
                        'success': False,
                        'step': 4,
                        'status': 'error',
                        'message': 'Сложи числители: 3 + 2 = 5. Знаменатель остается 12. Ответ: 5/12.'
                    })

        elif path == '/api/teacher/generate-twin':
            twin = {
                'id': len(STATE['twinsGenerated']) + 1,
                'problem': '1/4 + 5/6',
                'commonDenominator': 12,
                'targetStudentsCount': 17,
                'timestamp': time.time()
            }
            STATE['twinsGenerated'].append(twin)
            STATE['student']['recentTwin'] = twin
            return self._send_json({
                'success': True,
                'twin': twin,
                'message': 'Задача-двойник 1/4 + 5/6 успешно сгенерирована и отправлена 17 ученикам.'
            })

        elif path == '/api/teacher/send-sticker':
            student_id = body.get('studentId', 1)
            sticker_text = body.get('text', 'Отличное понимание НОК!')
            return self._send_json({
                'success': True,
                'studentId': student_id,
                'sticker': sticker_text,
                'delivered': True
            })

        elif path == '/api/student/ask-question':
            q_text = body.get('question', 'Подсказка по Шагу 3')
            return self._send_json({
                'success': True,
                'question': q_text,
                'receivedByTeacher': True
            })

        return self._send_json({'error': 'Endpoint not found'}, status=404)

if __name__ == '__main__':
    server = ThreadingHTTPServer(('0.0.0.0', PORT), CockpitHandler)
    print(f'School Mathematic Backend Server running on http://localhost:{PORT}')
    server.serve_forever()
