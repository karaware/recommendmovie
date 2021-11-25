#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy

def tweet(tweetDir):
    CK = 'XXXXX'
    CS = 'XXXXX'
    AT = 'XXXXX'
    AS = 'XXXXX'

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    print(tweetDir)

    api.update_with_media(filename=tweetDir["thumbnail"],status=tweetDir["message"])

