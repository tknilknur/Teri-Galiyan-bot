
----

<div align="center">
  <img src="https://github.com/AkinYoungSoftware/TerigaliyanBot/raw/master/logo.png" width="300" height="300">
  <h1>Telegram Kültür Botu</h1>
</div>
<p align="center">
        <a href="https://telegram.dog/@terigaliyan_bot">~Bot~</a>
</p>

----

# Bot Hakkında
**Pyrogram Bot Api Kullanılarak yazılmış basit telegram genel kültür botu!**

# Heroku'da Clonlamak

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AkinYoungSoftware/TgEglenceBot)

## Alanları Doldurma
* ``BOT_TOKEN``:AAHW96z6cR0UbiWSnbQjzC3v0NMASseJB90,
* ``OWNER_API_ID``: 16280281,
* ``OWNER_API_HASH``: 92660d5c054828213fa405ebe0dc1056,

# Örnek Start Komutu
```python
from pyrogram import Client, filters

K_G = Client(
    "Pyrogram Bot,
    bot_token=AAHW96z6cR0UbiWSnbQjzC3v0NMASseJB90,
    api_id=16280281,
    api_hash=YOUR_API_HASH 92660d5c054828213fa405ebe0dc1056
    )

@K_G.on_message(filters.command("start"))
async def _(client, message):
    await message.reply_text(text="Merhaba")
```

# İletişim
Şikayet, bağış v.b. için benim ile telegram'dan iletişime geç [@kartalgolgolgoll](https://t.me/kartalgolgolgoll])

