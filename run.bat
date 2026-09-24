@echo off
setlocal
cd /d "%~dp0"
if not exist "venv\Scripts\python.exe" (
  echo Membuat virtual environment...
  python -m venv venv
  if errorlevel 1 (
    echo Gagal membuat virtual environment. Pastikan Python 3.10+ terpasang.
    pause
    exit /b 1
  )
  call venv\Scripts\activate.bat
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt
) else (
  call venv\Scripts\activate.bat
)
python tomat_grow.py
pause
