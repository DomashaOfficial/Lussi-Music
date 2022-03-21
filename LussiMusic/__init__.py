#
# Copyright (C) 2022 by DomashaOfficial@Github, < https://github.com/DomashaOfficial >.
#
# This file is part of < https://github.com/DomashaOfficial/Lussi-Music > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DomashaOfficial/Lussi-Music/blob/master/LICENSE >
#
# All rights reserved.

from LussiMusic.core.bot import YukkiBot
from LussiMusic.core.dir import dirr
from LussiMusic.core.git import git
from LussiMusic.core.userbot import Userbot
from LussiMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = YukkiBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
