#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

print "put your string"
str = raw_input()

print "put your spilt char"

spilt_char = raw_input()

str_ret = str.split(spilt_char)

print len(str_ret)