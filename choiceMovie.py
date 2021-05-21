#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import tweetList

def choiceMovie():
    tweetDir = random.choice(tweetList.lists)
    
    return tweetDir

