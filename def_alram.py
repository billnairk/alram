#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, telegram, time, os
from bs4 import BeautifulSoup
bot = telegram.Bot(token='[텔레그램 Token 값]')

def popkontv(pop_bj, name):
  check = None
  first = 0
  while True:
    Channel = requests.get(f'https://www.popkontv.com/ch/default.asp?mcid={pop_bj}&mcPartnerCode=P-00001')
    time.sleep(1)
    html = BeautifulSoup(Channel.text, 'html.parser')
    status = html.find("span", {"class" : "ic ic_on"})
    first, check, status = pop_Brodcast(check, status, name, first)
    time.sleep(9)

def pandatv(panda_bj, name, id):
  check = None
  first = 0
  while True:
    Channel = requests.get(f'https://www.pandalive.co.kr/channel/{panda_bj}/notice')
    time.sleep(1)
    html = BeautifulSoup(Channel.text, 'html.parser')
    status = html.find("a", {"class" : "v_box"}).find("span", {"class" : "txt_c"}).string
    first, check, status = panda_Brodcast(check, status, name, first)
    time.sleep(9)

def pop_Brodcast(check, status, name, first):
  # 방송 ON/OFF 비교
  if check != status:
    check = status
    # 프로그램 첫 실행시 메세지 보내지 않음
    if first != 0:
      if check is not None:
        txt = (f"{name} 🔥") # 방송 ON
        bot.sendMessage(['Chat_id'], txt)
      else:
        txt = (f"{name} ❄") 
        bot.sendMessage(['Chat_id'], txt)
  # first 변수 값이 계속 증가하는 것을 방지
  if first < 1:
    first += 1
  return first, check, status

def panda_Brodcast(check, status, name, first):
  if check != status:
    check = status
    if first != 0:
      if check == "시청하기":
        txt = (f"{name} 🔥")
        bot.sendMessage(['Chat_id'], txt)
      else:
        txt = (f"{name} ❄")
        bot.sendMessage(['Chat_id'], txt)
  if first < 1:
    first += 1
  return first, check, status

# 🥳 🌹 🔥 🌟 ⭐ ☀ 🎉 ❄ 🪄