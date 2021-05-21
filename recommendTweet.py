#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy

def tweet(tweetDir):
    CK = 'F9775TKQrUgwws9uJm7qr0bw9'
    CS = 'UDPVHjwVMaOf3HMHJ2U68s2ssPxv5Kf9LAePW3O2x2n3baSV7V'
    AT = '1384009908178198529-g8yEdNsWEhlsxCEsjqIhOaoAdFnLUP'
    AS = 'RLT6juFbVbPcHHe3V9ERbjSvYmeZmc68Ppcrlb3OPUftr'

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    print(tweetDir)

    api.update_with_media(filename=tweetDir["thumbnail"],status=tweetDir["message"])

