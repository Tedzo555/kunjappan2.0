
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils import temp
from database.ia_filterdb import unpack_new_file_id

# https://github.com/EvamariaTG/EvaMaria/blob/e325a1d8ef484ecc67bad74e1a02173ee0505801/plugins/genlink.py#L23

@Client.on_message(filters.private & filters.command(['add_file', 'filestore']))
async def gen_link_s(bot, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply('Reply to a message to get a shareable link.')

    file_type = replied.media
    if file_type not in ["video", 'audio', 'document']:
        return await message.reply("__**Reply to a Supported Media**__")

    file_id, ref = unpack_new_file_id((getattr(replied, file_type)).file_id)
    url = f"https://t.me/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}"
    await message.reply(f"**Here is your Link:**\n`{url}")
