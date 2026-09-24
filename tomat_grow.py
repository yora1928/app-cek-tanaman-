"""
TOMAT GROW - Entry point.
Dapat dijalankan langsung (python tomat_grow.py) atau dikompilasi menjadi .exe.
"""
import os
import sys
import socket
import threading
import time
import webbrowser
from pathlib import Path


def _base_dir() -> Path:
    """Direktori kerja aplikasi (sebelah EXE, atau direktori script)."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).parent


def _find_free_port(start=5000, end=5100):
    for p in range(start, end):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", p))
                return p
            except OSError:
                continue
    raise RuntimeError("Tidak ada port bebas antara 5000-5099.")


def _open_browser(url, delay=2.0):
    def worker():
        time.sleep(delay)
        try:
            webbrowser.open(url)
        except Exception:
            pass
    threading.Thread(target=worker, daemon=True).start()


def main():
    base = _base_dir()
    print("=" * 60)
    print("  TOMAT GROW - Sistem Monitoring Tanaman Tomat")
    print("=" * 60)

    from tg_core import create_app
    app = create_app(base)

    port = _find_free_port(5000, 5100)
    url = f"http://127.0.0.1:{port}"

    # Buat akun admin bila database kosong
    with app.app_context():
        pass

    print(f"  Aplikasi berjalan di: {url}")
    print("  Browser akan dibuka otomatis...")
    print("  Login default -> username: admin | password: admin123")
    print("  Tutup jendela ini untuk menghentikan aplikasi.")
    print("=" * 60)

    _open_browser(url, delay=1.5)

    try:
        from waitress import serve
        serve(app, host="127.0.0.1", port=port, threads=4, _quiet=True)
    except ImportError:
        # Fallback bila waitress tidak tersedia
        app.run(host="127.0.0.1", port=port, debug=False, use_reloader=False)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAplikasi dihentikan.")
    except Exception as e:
        print(f"\n[ERROR] {e}")
        input("Tekan Enter untuk keluar...")
