from BanAllBot import app,START_IMG,BOT_USERNAME,BOT_NAME,LOG
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , CallbackQuery 

START_MSG="""
ʜᴇʏ **{}** , ɪ ᴀᴍ {},
ɪ ʜᴀᴠᴇ sᴏᴍᴇ ɪɴᴛᴇʀᴇsᴛɪɴɢ ᴘʟᴜɢɪɴs ʏᴏᴜ sʜᴏᴜʟᴅ ᴛʀʏ ɪᴛ ʙʏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ.
ᴀᴅᴅ ᴍᴇ ɪɴ ᴏᴛʜᴇʀs ɢʀᴏᴜᴘ ᴛᴏ ᴅᴇsᴛʀᴏʏ ɪᴛ.
"""
START_BUTTONS=InlineKeyboardMarkup (
      [
      [
         InlineKeyboardButton (text="➕ ᴀᴅᴅ ᴍᴇ ➕",url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
      ],
      [
         InlineKeyboardButton (text="ʜᴇʟᴘ",callback_data="help_back")
      ]
      ]
)

HELP_MSG="""
**ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs**

⨷ /banall : ʙᴀɴ-ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

⨷ /unbanall : ᴜɴʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

⨷ /kickall : ᴋɪᴄᴋ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

⨷ /muteall : ᴍᴜᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ

⨷ /unmuteall : ᴜɴᴍᴜᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ(sᴛɪʟʟ ᴡɪʟʟ ᴛʜᴇ ʟɪsᴛ ɪɴ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴍᴇᴍʙᴇʀs ʙᴜᴛ ᴀʟʟ ʀᴇsᴛʀɪᴄᴛɪᴏɴs ᴡɪʟʟ ɢᴏ)

⨷/unpinall : ᴜɴᴘɪɴ ᴀʟʟ ᴍᴇssᴀɢᴇs ɪɴ ᴀ ɢʀᴏᴜᴘ.

ᴄʀᴇᴀᴛᴇᴅ ʙʏ: [ᴍ ᴀ ʀ ᴄ ᴏ ⌯ ❰ 𝗟𝗚𝗗 ❱](https://t.me/IM4RC0)
"""




@app.on_message(filters.command("start"))
async def start(_,msg):
    await msg.reply_photo(
     photo=START_IMG,
     caption=START_MSG.format(msg.from_user.mention,BOT_NAME),
     reply_markup=START_BUTTONS)

@app.on_callback_query(filters.regex("help_back"))
async def help_back(_,callback_query: CallbackQuery):
    query=callback_query.message
    await query.edit_caption(HELP_MSG)    



if __name__ == "__main__":
    LOG.info("started")
    app.run()
