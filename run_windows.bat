@echo off
chcp 65001 > nul
echo ========================================================
echo   Запуск МАХ.Образование • School Mathematic
echo ========================================================
echo Сервер запускается на http://localhost:8080 ...
timeout /t 1 > nul
start http://localhost:8080
python server.py
if errorlevel 1 (
    echo.
    echo [ОШИБКА] Python не найден в PATH. Убедитесь, что Python 3 установлен.
    pause
)
