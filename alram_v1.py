#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import def_alram

if __name__ == '__main__':
  # POPKON
  Process(target=def_alram.popkontv, args=("[pop_bj]", "[name]")).start()
  
  # PANDA
  Process(target=def_alram.pandatv, args=("[panda_bj]", "[name]", "[id]")).start()
