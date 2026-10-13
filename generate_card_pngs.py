import os
import sys
import time
import subprocess
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8765
WORKSPACE_DIR = r"c:\PROJECT\Prototype CaKades"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

class QuietHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WORKSPACE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

def run_server(httpd):
    httpd.serve_forever()

def capture(url, out_path, width, height, scale=1):
    # Command for headless chrome
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--hide-scrollbars",
        f"--window-size={width},{height}",
        f"--force-device-scale-factor={scale}",
        f"--screenshot={out_path}",
        url
    ]
    subprocess.run(cmd, check=True)
    time.sleep(1)

def main():
    httpd = HTTPServer(('127.0.0.1', PORT), QuietHandler)
    server_thread = threading.Thread(target=run_server, args=(httpd,), daemon=True)
    server_thread.start()
    print(f"HTTP server running on http://127.0.0.1:{PORT}")
    time.sleep(1)

    targets = [
        (
            f"http://127.0.0.1:{PORT}/print_card_front.html",
            os.path.join(WORKSPACE_DIR, "Kartu_Pintar_Depan_Alif_Setiawan.png"),
            840, 530, 1
        ),
        (
            f"http://127.0.0.1:{PORT}/print_card_back.html",
            os.path.join(WORKSPACE_DIR, "Kartu_Pintar_Belakang_QR_Tegalpingen.png"),
            840, 530, 1
        ),
        (
            f"http://127.0.0.1:{PORT}/print_sticker.html",
            os.path.join(WORKSPACE_DIR, "Stiker_Pintu_Barcode_Alif_Setiawan.png"),
            380, 550, 2
        )
    ]

    for url, out_path, w, h, s in targets:
        print(f"Capturing {out_path} ({w}x{h} @ {s}x)...")
        capture(url, out_path, w, h, s)
        if os.path.exists(out_path):
            size_kb = os.path.getsize(out_path) / 1024
            print(f"  -> SUCCESS: {os.path.basename(out_path)} ({size_kb:.1f} KB)")
        else:
            print(f"  -> FAILED: {out_path}")

    httpd.shutdown()
    print("All captures completed.")

if __name__ == "__main__":
    main()
