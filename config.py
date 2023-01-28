#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5696138411:AAE2hRzQZeWwtBUqz6Lvt-KWyj6FBc4Y860")
    API_ID = int(os.environ.get("API_ID", "952608"))
    API_HASH = os.environ.get("API_HASH", "8d8d0ad8e3d4bcd54420190f57da78ad")
    AUTH_USERS = "818269274"

