from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_message_text = """
Hello {} \U0001F60E I am GpyTranslatorBot AKA Gipy \ud83e\udd16

Send any text which you would like to translate for English.

**Available commands:**
/donate - Support developers
/help - Show this help message
/language - Set your main language

If you have questions about this bot or bots' development__ - Contact @MrCentimetreLK

Enjoy! ☺"""

start_message_reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "➕ Add me to a Group ➕",  url="http://t.me/GpyTranslatorBot?startgroup=tr")
        ],
        [
            InlineKeyboardButton(
                "🆘 Help",  callback_data="help"),
            InlineKeyboardButton(
                "Credits 💚",  callback_data=b"Credits")
        ],
        [
            InlineKeyboardButton(
                "📣 Channel",  url="https://t.me/CentiProjects"),
            InlineKeyboardButton(
                "Group 👥",  url="https://t.me/joinchat/VBrSurucLQFgJ_r2"),
        ]
    ]
)

credits = """Development 🧑‍💻
 • @MrCentimetreLK
 • @itayki
 • @rojserbest

Inspiration 👨🏻‍🏫
 • @DavideGalilei"""

help_text = """
**GpyTranslate Bot**

GpyTranslate is a word 'G+Py+Translate' which means 'Google Python Translate'. A bot to help you translate text (with emojis) to few Languages from any other language in world.

GpyTranslator Bot is able to detect a wide variety of languages because he is a grand son of Google Translate API.

You can use GpyTranslator Bot in his private chat. But GpyTranslator Bot is not available for Telegram Group & Channel.

**How To**
Just send copied text or forward message with other language to GpyTranslator Bot and you'll receive a translation of the message in the language of your choice. Send /language command to know which language is available.

---
Find a problem? Send to @MrCentimetre

coded by @MrCentimetreLK and @itayki by using @DavideGalilei's Library with 💚
"""

donate_text = """
It's just a command \ud83d\ude09 But you can contact my father - @MrCentimetreLK
"""

language_text = """
**Languages**

__Select the language you want to translate.__

•/lang (language code) 

Example: ```/lang en``` 

List of language codes: https://cloud.google.com/translate/docs/languages

Send the relevant command. \ud83e\udd20")
"""
