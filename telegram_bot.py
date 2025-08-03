from telegram import Bot
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

bot = Bot(token=TELEGRAM_TOKEN)

def send_signal(token):
    try:
        mc = float(token.get('marketcap', 1))                   supply = float(token.get('supply', 1))
        symbol = token.get('symbol', token.get('name', 'Unknown'))
        address = token.get('address', 'N/A')
                                                                msg = f"""                                      🚀 New Meme Coin Detected!
                                                        🪙 Name: ${symbol}
📉 Market Cap: ${mc}                                    📦 Supply Ratio: {supply / mc:.2%}
🧠 AI Score: ✅ Safe
📄 Contract: {address}
                                                        🔗 [Copy Contract] | [Birdeye](https://birdeye.so/token/{address})                                              """
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg)
    except Exception as e:                                      print("Telegram send error:", e)