#!/usr/bin/env bash
echo "========================================================"
echo "  Запуск МАХ.Образование • School Mathematic"
echo "========================================================"
echo "Сервер запускается на http://localhost:8080 ..."
if which xdg-open > /dev/null 2>&1; then
  xdg-open http://localhost:8080 &
elif which open > /dev/null 2>&1; then
  open http://localhost:8080 &
fi
python3 server.py
