#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6314089749:AAFgCoL2hxCd11lhVq_tqL3NJtem6Ao0bds")
    API_ID = int(os.environ.get("API_ID", "12606917"))
    API_HASH = os.environ.get("API_HASH", "f25113b8c17dca6fa7abda53a86bd4f7")
    AUTH_USERS = "5318243282"

