# FIRE IT DAY 1 #
# 🔥 FIRE ORDER – Day 1: Linux + Git + Python + Telegram Bot

Цей репозиторій — частина системи FIRE ORDER 💀  
Ціль: стати мільйонером через стабільність, технічні навички та медіа.

---

## 📚 Урок складається з 4 частин:

### 🖥 1. Linux-команда
Перший практичний крок — базова команда в Linux:
```bash
ls
cd
nano
Мета: розуміння структури директорій та базова CLI-навігація.

🔧 2. Git: Перший commit
bash
Копировать
Редактировать
git init
git add .
git commit -m "Day 1 setup"
git push origin main
Якщо виникає помилка типу rejected (fetch first) — використовуй git pull --rebase origin main

🤖 3. Python: Telegram-бот
Використана бібліотека:

bash
Копировать
Редактировать
pip install pyTelegramBotAPI
bot.py — базовий код:
python
Копировать
Редактировать
import telebot

TOKEN = 'ТУТ_ВСТАВ_ТОКЕН'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я DeutschNinjaBot 🤖")

bot.polling()
Запуск:

bash
Копировать
Редактировать
python bot.py
🌐 4. GitHub upload
Фінальні кроки для документації:

bash
Копировать
Редактировать
git add README.md
git commit -m "Add README + Day 1 summary"
git push
🔁 Завдання на День 1:
Компонент	Прогрес ✅
Linux команда	✅ ls, cd, nano
Git init + push	✅ перший commit
Python скрипт	✅ bot.py
Telegram-бот	✅ /start відповідає
README файл	✅ опис всього уроку
GitHub upload	✅ все залито

📈 Наступні кроки:
Додати команду /word — слово + приклад

Створити клавіатуру (InlineButtons)

Зробити логіку для вивчення німецької

🔥 FIRE ORDER – SYSTEM
Цей урок — частина системи FIRE ORDER:

Німецька → C1

Знайомства / події

Робота / 10 дзвінків в день

Контент / TikTok / Shorts

IT-напрям / GitHub / боти

Спорт / зал

Антилінь-система / нагадування

🤖 Автор:
Yurii – 23 роки, Німеччина 🇩🇪
Ціль: 1 000 000 $ через IT + Контент + Робота + Мова
