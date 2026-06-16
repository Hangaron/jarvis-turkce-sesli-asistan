# -*- coding: utf-8 -*-
"""
J.A.R.V.I.S. Local Command Bridge
Geliştirici: Emirhan "Hangaronn" Vardar
Açıklama: HTML arayüzünden gelen istekleri dinleyen ve yerel uygulamaları çalıştıran mikro HTTP Sunucu.
"""

import http.server
import socketserver
import json
import sys
import subprocess

PORT = 8080

class JarvisBridgeHandler(http.server.BaseHTTPRequestHandler):
    
    def end_headers(self):
        # CORS yetkilerini tanımlama (HTML dosyamızın bu sunucuya erişebilmesi için gereklidir)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        # CORS ön uçuş (pre-flight) isteklerini kabul et
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path == "/status":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {"status": "online", "message": "JARVIS Python Bridge aktif, sizi dinliyor efendim."}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/execute":
            # Gelen veriyi okuma ve çözümleme
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                command = data.get("command", "").lower().strip()
                
                # Komut yürütme ve sonuç oluşturma
                message = self.launch_app(command)
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                
                response = {"status": "success", "message": message}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {"status": "error", "error": str(e)}
                self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def launch_app(self, app_name):
        is_win = sys.platform.startswith('win')
        is_mac = sys.platform.startswith('darwin')

        # İşletim sistemine göre uygulamaları eşleştirme ve çalıştırma
        if app_name == "notepad":
            if is_win:
                subprocess.Popen(["notepad.exe"])
            elif is_mac:
                subprocess.Popen(["open", "-a", "TextEdit"])
            else:
                subprocess.Popen(["gedit"])
            return "Not Defteri başarıyla başlatıldı, Efendim."

        elif app_name == "chrome":
            if is_win:
                # Windows'ta default tarayıcı yerine direkt Chrome çalıştırmayı dener
                try:
                    subprocess.Popen(["cmd", "/c", "start", "chrome"])
                except:
                    subprocess.Popen(["cmd", "/c", "start", "https://www.google.com"])
            elif is_mac:
                subprocess.Popen(["open", "-a", "Google Chrome"])
            else:
                subprocess.Popen(["google-chrome"])
            return "Chrome tarayıcınız açılıyor, Efendim."

        elif app_name == "calculator":
            if is_win:
                subprocess.Popen(["calc.exe"])
            elif is_mac:
                subprocess.Popen(["open", "-a", "Calculator"])
            else:
                subprocess.Popen(["gnome-calculator"])
            return "Hesap makineniz açılıyor, Efendim."

        elif app_name == "paint":
            if is_win:
                subprocess.Popen(["mspaint.exe"])
            elif is_mac:
                subprocess.Popen(["open", "-a", "Preview"])
            else:
                subprocess.Popen(["gimp"])
            return "Çizim aracı başlatıldı, Efendim."

        elif app_name == "explorer":
            if is_win:
                subprocess.Popen(["explorer.exe"])
            elif is_mac:
                subprocess.Popen(["open", "."])
            else:
                subprocess.Popen(["xdg-open", "."])
            return "Dosya yöneticisi ekranınıza yansıtılıyor, Efendim."

        else:
            return f"'{app_name}' komutu anlaşıldı fakat bu yerel uygulama köprü üzerinde tanımlı değil, Efendim."

# Sunucuyu başlatma logu ve döngüsü
if __name__ == "__main__":
    print("="*60)
    print("J.A.R.V.I.S. YEREL SİSTEM KÖPRÜSÜ BAŞLATILIYOR...")
    print(f"Geliştirici: Emirhan 'Hangaronn' Vardar")
    print(f"Sunucu adresi: http://localhost:{PORT}")
    print("="*60)
    
    # TCP sunucusunu çalıştırma
    try:
        with socketserver.TCPServer(("", PORT), JarvisBridgeHandler) as httpd:
            print("[SİSTEM]: Köprü aktif. Tarayıcıdan gelecek komutlar bekleniyor...")
            print("Kapatmak için CTRL+C tuşlarına basın.")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[SİSTEM]: Köprü kapatılıyor. İyi günler dilerim, Sir.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[HATA]: Sunucu başlatılamadı: {e}")