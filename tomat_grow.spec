# -*- mode: python ; coding: utf-8 -*-
"""
Spec PyInstaller untuk TOMAT GROW.
Strategi anti-deteksi antivirus:
  1. Gunakan mode --onedir (bukan --onefile) → lebih jarang di-flag.
  2. Jangan aktifkan UPX → UPX sering memicu heuristik AV.
  3. Sertakan version_info → EXE resmi, tidak kosong.
  4. Aktifkan bootloader resmi (default, jangan dimodifikasi).
  5. Nama file EXE deskriptif, bukan acak.
"""

import sys
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

hiddenimports = [
    'sqlalchemy', 'sqlalchemy.sql.default_comparator',
    'sqlalchemy.ext.baked',
    'flask', 'flask_login', 'flask_sqlalchemy', 'werkzeug',
    'waitress',
    'reportlab', 'reportlab.pdfbase._fontdata',
    'matplotlib', 'matplotlib.backends.backend_agg',
    'PIL', 'PIL.Image',
]

hiddenimports += collect_submodules('sqlalchemy')
hiddenimports += collect_submodules('waitress')

datas = []
datas += collect_data_files('reportlab')
datas += collect_data_files('matplotlib', include_py_files=False)

a = Analysis(
    ['tomat_grow.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter', 'test', 'unittest',
        'matplotlib.backends.backend_qt5agg',
        'matplotlib.backends.backend_tkagg',
        'matplotlib.backends.backend_qtagg',
        'PyQt5', 'PyQt6', 'PySide2', 'PySide6',
    ],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='TOMAT-GROW',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,                 # ← WAJIB: jangan gunakan UPX
    console=True,              # console=True lebih aman dari AV
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='version_info.txt',
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,                 # ← WAJIB
    upx_exclude=[],
    name='TOMAT-GROW',
)
