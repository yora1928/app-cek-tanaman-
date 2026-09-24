@echo off
REM ============================================================
REM  TOMAT GROW - Script build EXE
REM  Jalankan file ini di Windows setelah install Python 3.10+
REM ============================================================
setlocal

echo.
echo ============================================================
echo   TOMAT GROW - Build EXE
echo ============================================================
echo.

where python >nul 2>nul
if errorlevel 1 (
  echo [ERROR] Python tidak ditemukan. Install Python 3.10+ dulu.
  pause & exit /b 1
)

REM Buat virtual environment bila belum ada
if not exist "venv\Scripts\python.exe" (
  echo [1/5] Membuat virtual environment...
  python -m venv venv
) else (
  echo [1/5] Virtual environment sudah ada.
)

call venv\Scripts\activate.bat

echo [2/5] Upgrade pip...
python -m pip install --upgrade pip >nul

echo [3/5] Install dependensi...
pip install -r requirements.txt
pip install pyinstaller

echo [4/5] Bersihkan build lama...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo [5/5] Build EXE...
pyinstaller --clean --noconfirm tomat_grow.spec

echo.
echo ============================================================
echo  SELESAI
echo.
echo  Hasil build ada di:  dist\TOMAT-GROW\TOMAT-GROW.exe
echo.
echo  Cara pakai:
echo    1. Copy folder  dist\TOMAT-GROW  ke mana saja.
echo    2. Dobel klik  TOMAT-GROW.exe
echo    3. Browser akan terbuka otomatis.
echo ============================================================
pause
endlocal
