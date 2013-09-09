#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json 
import android

def sendJoke():
    droid = android.Android()
    
    droid.smsSend("10086","TEST")
        
sendJoke()