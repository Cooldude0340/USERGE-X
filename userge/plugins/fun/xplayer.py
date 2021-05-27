"""X - MUSIC PLAYER"""

# Copyright (C) 2021 USERGE-X

#

# Author : github.com/code-rgb [TG : @deleteduser420]

#          Plugin Help Written by -> @iTz_Black007

#

# This program is free software: you can redistribute it and/or modify

# it under the terms of the GNU General Public License as

# published by the Free Software Foundation, either version 3 of the

# License, or (at your option) any later version.

#

# This program is distributed in the hope that it will be useful,

# but WITHOUT ANY WARRANTY; without even the implied warranty of

# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

# GNU General Public License for more details.

#

# You should have received a copy of the GNU General Public License

# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import asyncio

import os

import re

from functools import wraps

from math import floor

from random import shuffle

from signal import SIGTERM

from typing import Dict, List, Optional, Set, Union

import youtube_dl

from pyrogram import filters

from pyrogram.errors import PeerIdInvalid, UserNotParticipant

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from userge import Config, Message, get_collection, pool, userge

from userge.plugins.bot.alive import _parse_arg

from userge.plugins.bot.utube_inline import BASE_YT_URL, get_yt_video_id, get_ytthumb

from userge.plugins.misc.upload import check_thumb

from userge.plugins.utils.songlink import find_url_from_msg, ge
