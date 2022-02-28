# Gerekli Kurulumlar
import os
import logging
import random
from sorular import Şiir_LİST, Söz_LİST , Sorular_LİST
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# ============================ #

B_TOKEN = os.getenv("BOT_TOKEN") # AAHW96z6cR0UbiWSnbQjzC3v0NMASseJB90
API_ID = os.getenv("OWNER_API_ID") # 16280281

API_HASH = os.getenv("OWNER_API_HASH") #92660d5c054828213fa405ebe0dc105 
OWNER_ID.append(818300528)

MOD = None

# Log Kaydı Alalım
logging.basicConfig(level=logging.INFO)

# Komutlar İcin Botu Tanıtma
K_G = Client(
	"Pyrogram Bot",
	bot_token=AAHW96z6cR0UbiWSnbQjzC3v0NMASseJB90,
	api_id=16280281
,
	api_hash=92660d5c054828213fa405ebe0dc105,
	)

# Start Buttonu İcin Def Oluşturalım :)
def button():
	BUTTON=[[InlineKeyboardButton(text="??????? Sahibim ",url="t.me/kartalgolgolgoll")]]
	BUTTON+=[[InlineKeyboardButton(text="?? Open Source ??",url="https://github.com/tknilknur/TeriGaliyanBot")]]
	return InlineKeyboardMarkup(BUTTON)

# Kullanıcı Start Komutunu Kullanınca Selam'layalım :)
@K_G.on_message(filters.command("start"))
async def _(client, message):
	user = message.from_user # Kullanıcın Kimliğini Alalım

	await message.reply_text(text="**Merhaba {}!**\n\n__Ben Pyrogram Api İle Yazılmış Eğlence Botuyum :)__\n\n**Repom =>** [Open Source](https://github.com/AkinYoungSoftware/TgEglenceBot)\nDoğruluk mu? Cesaret mi? Oyun Komutu => /dc".format(
		user.mention, # Kullanıcı'nın Adı
		),
	disable_web_page_preview=True, # Etiketin Önizlemesi Olmaması İcin Kullanıyoruz
	reply_markup=button() # Buttonlarımızı Ekleyelim
	)

# terigaliyan Komutu İcin Olan Buttonlar
def d_or_c(user_id):
	BUTTON = [[InlineKeyboardButton(text="? Sözler", callback_data = " ".join(["söz_data",str(user_id)]))]]
	BUTTON += [[InlineKeyboardButton(text="?? Şiir", callback_data = " ".join(["şiir_data",str(user_id)]))]]
	return InlineKeyboardMarkup(BUTTON)
        BUTTON += [[InlineKeyboardButton(text="?? Sorular", callback_data = " ".join(["soru_data",str(user_id)]))]]]
	return InlineKeyboardMarkup(BUTTON)

# terigaliyan Komutunu Oluşturalım
@K_G.on_message(filters.command("Sözler"))
async def _(client, message):
	user = message.from_user

	await message.reply_text(text="{} İstediğini Seç!".format(user.mention),
		reply_markup=d_or_c(user.id)
		)

# Buttonlarımızı Yetkilendirelim
@K_G.on_callback_query()
async def _(client, callback_query):
	şiir_soru=random.choice(Şiir_LİST) # Random Bir Şiir seçelim
	söz_soru=random.choice(Söz_LİST) # Random Bir Söz Seçelim
	soru_soru=random.choice(Soru_LİST) # Random Bir Söz Seçelim
	user = callback_query.from_user # Kullanıcın Kimliğini Alalım

	c_q_d, user_id = callback_query.data.split() # Buttonlarımızın Komutlarını Alalım


	if str(user.id) == str(user_id):
		# Kullanıcının Doğruluk Sorusu İstemiş İse Bu Kısım Calışır
		if söz_q_soru_q_şiir == "şiir_data":
			await callback_query.answer(text="Şiir İstediniz", show_alert=False) # İlk Ekranda Uyarı Olarak Gösterelim
			await client.delete_messages(
				chat_id=callback_query.message.chat.id,
				message_ids=callback_query.message.message_id) # Eski Mesajı Silelim

			await callback_query.message.reply_text("**{user} Şiir İstedi:** __{şiir_soru}__".format(user=user.mention, şiir_soru=şiir_soru)) # Sonra Kullanıcıyı Etiketleyerek Sorusunu Gönderelim
			return

		if şiir_q_söz_q_soru == "söz_data":
			await callback_query.answer(text="Söz İstediniz", show_alert=False)
			await client.delete_messages(
				chat_id=callback_query.message.chat.id,
				message_ids=callback_query.message.message_id)
			await callback_query.message.reply_text("**{user} Söz İstedi:** __{söz_soru}__".format(user=user.mention, söz_soru=söz_soru))
			return
                 if şiir_q_söz_q_soru == "soru_data":
			await callback_query.answer(text="Soru İstediniz", show_alert=False)
			await client.delete_messages(
				chat_id=callback_query.message.chat.id,
				message_ids=callback_query.message.message_id)
			await callback_query.message.reply_text("**{user} Söz İstedi:** __{soru_soru}__".format(user=user.mention, soru_soru=soru_soru))
			return

	# Buttonumuza Tıklayan Kisi Komut Calıştıran Kişi Değil İse Uyarı Gösterelim
	else:
		await callback_query.answer(text="Komutu Kullanan Kişi Sen Değilsin!!", show_alert=False)
		return

############################
    # Sudo islemleri #
@K_G.on_message(filters.command("cekle"))
async def _(client, message):
  global MOD
  user = message.from_user
  
  if user.id not in OWNER_ID:
    await message.reply_text("**[?]** **Sen Yetkili Birisi degilsin!!**")
    return
  MOD="cekle"
  await message.reply_text("**[?]** **Eklenmesini istedigin Cesaret Sorunu Giriniz!**")
  
@K_G.on_message(filters.command("dekle"))
async def _(client, message):
  global MOD
  user = message.from_user
  
  if user.id not in OWNER_ID:
    await message.reply_text("**[?]** **Sen Yetkili Birisi degilsin!!**")
    return
  MOD="cekle"
  await message.reply_text("**[?]** **Eklenmesini istedigin Dogruluk Sorunu Giriniz!**")

@K_G.on_message(filters.private)
async def _(client, message):
  global MOD
  global Şiir_LİST
  global Söz_LİST
  global Soru_LİST
  
  user = message.from_user
  
  if user.id in OWNER_ID:
    if MOD=="cekle":
     Şiir_LİST.append(str(message.text))
      MOD=None
      await message.reply_text("**[?]** __Metin Şiir Eklendi!__")
      return
    if MOD=="dekle":
      Söz_LİST.append(str(message.text))
      MOD=None
      await message.reply_text("**[?]** __Metin Söz Eklendi!__")
      return
   if MOD=="dekle":
      Soru_LİST.append(str(message.text))
      MOD=None
      await message.reply_text("**[?]** __Metin  Sorusu Eklendi!__")
      return
############################

K_G.run() # Botumuzu Calıştıralım :)
