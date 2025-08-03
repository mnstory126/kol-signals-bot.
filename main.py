import pytz
import json                                             from apscheduler.schedulers.blocking import BlockingScheduler
from scanner import fetch_new_tokens
from ai_filter import is_potential_pump, ai_scan        from telegram_bot import send_signal
from config import TELEGRAM_CHAT_ID                     
known_tokens = set()                                    
def scan_and_send():
    tokens = fetch_new_tokens()
    for token in tokens:
        if isinstance(token, str):                                  try:
                token = json.loads(token)                           except:
                print("Lewatkan token karena tidak bisa dibaca:", token)
                continue                                
        if not isinstance(token, dict):
            continue
                                                                try:
            name = token.get("name")
            address = token.get("address")
            supply = float(token.get("supply", 0))
            marketcap = float(token.get("marketcap", 1))

            if address in known_tokens:
                continue
            known_tokens.add(address)

            if supply / marketcap >= 0.1 and ai_scan(token):
                send_signal(token)                                      print(f"[✅] Signal sent for: {name} ({address})")
                                                                except Exception as e:
            print("Error:", e)
                                                        scheduler = BlockingScheduler(timezone=pytz.utc)
scheduler.add_job(scan_and_send, 'interval', seconds=60)print("🚀 KOL Signals Bot Started.")
scheduler.start()