# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import filters
from pyrogram.types import Message

from DaisyXMusic.services.callsmusic.callsmusic import client as USER


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
       "Hi there, This is the music assistant service of @VenomMusicBot .\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **IF YOU ARE UNABLE TO ADD ASSISTANT OR HAVE PROBLEM REGARDING MUSIC BOT KINDLY CONTACT @R2K_VENOM** \n\n **⚠️ Note : if you are unable to add music assistant in  private groups just make the group public for one minute and send the group link here or in @R2K_VENOM dm and after the music assistant joins you can make your group private again** \n\n **❗if you need any help just ask here @CrackMonkey**")
  return
