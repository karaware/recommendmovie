#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import random

CK = 'F9775TKQrUgwws9uJm7qr0bw9'
CS = 'UDPVHjwVMaOf3HMHJ2U68s2ssPxv5Kf9LAePW3O2x2n3baSV7V'
AT = '1384009908178198529-g8yEdNsWEhlsxCEsjqIhOaoAdFnLUP'
AS = 'RLT6juFbVbPcHHe3V9ERbjSvYmeZmc68Ppcrlb3OPUftr'

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

#lists = [0, 1, 2, 3, 4]
#print(random.choice(lists))

message = "【自作おすすめ動画】"
message += "\n"
message += "https://youtu.be/ObYjX0vOveA"
message += "\n"
message += "豆苗の成長を動画にしました！"
message += "\n"
message += "新芽がフリフリ動きながら伸びていく姿がかわいいです！"
message += "\n"
message += "#家庭菜園 #水耕栽培 #豆苗"

thumbnailPath = '/home/pi/script/recommendmovie/thumbnail/beens_01.png'

lists = [{"thumbnail" : thumbnailPath, "message" : message}]
choiceMovie = random.choice(lists)
print(choiceMovie)

#api.update_with_media(filename=thumbnailPath,status=message)
api.update_with_media(filename=choiceMovie["thumbnail"],status=choiceMovie["message"])

