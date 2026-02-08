from bot import Bot
from flask import Flask
import threading
import os

# Render-এর জন্য ছোট একটি ওয়েব সার্ভার
app_web = Flask(__name__)

@app_web.route('/')
def health_check():
    return "Bot is alive and running!"

def run_flask():
    # Render সাধারণত 10000 পোর্ট ব্যবহার করে
    port = int(os.environ.get("PORT", 10000))
    app_web.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    # Flask সার্ভারটি আলাদা একটি থ্রেডে চালু করা হচ্ছে
    threading.Thread(target=run_flask, daemon=True).start()
    
    # আপনার আসল বট চালু করা হচ্ছে
    app = Bot()
    app.run()
