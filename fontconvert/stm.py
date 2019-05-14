#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from bijoy2unicode import converter
test = converter.Unicode()

def convert(txt):
  import re

  txt = txt.replace('\\u09aa\\u09cd\\u09b0\\u09ac\\u09b1\\u0995\\u09cd\\u09b7\\u09a3',
                                                                                       'প্রশিক্ষন')
  txt = txt.replace('\\u09ac\\u09ab\\u09ad\\u09be\\u09a8\\u09ae\\u09b3\\u09a8\\u09be',
                    ' বিমানসেনা')
  txt = txt.replace('\\u09a8\\u09af\\u09be', 'দ্যো')
  txt = txt.replace('\\u09ad\\u09a8\\u09cd\\u09a4\\u09cd\\u09b0\\u09a3\\u09be\\u09b0\\u09df',
                                             'মন্ত্রণালয়')
  txt = txt.replace('\\u09a1\\u09ab\\u09ac\\u09be\\u0997',
                                             'বিভাগ')
  txt = txt.replace('\\u09aa\\u09cd\\u09b0\\u0995\\u09a8\\u09b2\\u09cd\\u09aa\\u09af',
                    'প্রকল্পের')
  txt = txt.replace('\\u09a1\\u09b1\\u09a8\\u09af\\u09be\\u09a8\\u09be\\u09ad',
                    'শিরোনাম')
  txt = txt.replace('\\u09a8\\u09af\\u09be',
                               'রো')
  txt = txt.replace('\\u09b8\\u09b3',
                               'সে')
  txt = txt.replace('\\u09ac\\u09be',
                    'ভা')

  txt = txt.replace('\\u0981', 'ঁ')
  txt = txt.replace('\\u0982', 'ং')
  txt = txt.replace('\\u0983', 'ঃ')


  txt = txt.replace('\\u0985','অ')
  #txt = txt.replace('\\u0986', 'আ')
  txt = txt.replace('\\u0986', 'ই')
  #txt = txt.replace('\\u0988',
  #                             'ঈ')
  txt = txt.replace('\\u0988',
                               'উ')
  txt = txt.replace('\\u0989',
                    'উ')
  txt = txt.replace('\\u098a',
                               'ঊ')
  txt = txt.replace('\\u098b',
                               'ঋ')
  txt = txt.replace('\\u098c', 'ঌ')
  txt = txt.replace('\\u098f',
                              'এ')
  txt = txt.replace('\\u0990',
                               'ঐ')
  txt = txt.replace('\\u0993',
                               'ও')
  txt = txt.replace('\\u0994',
                               'ঔ')

  txt = txt.replace('\\u0995',
                               'ক')
  txt = txt.replace('\\u0996',
                    'খ')
  txt = txt.replace('\\u0997',
                    'গ')
  txt = txt.replace('\\u0998',
                    'ঘ')
  txt = txt.replace('\\u0999',

                    'ঙ')
  txt = txt.replace('\\u099a',

                    'চ')
  txt = txt.replace('\\u099b',

                    'ছ')
  txt = txt.replace('\\u099c',
                    'জ')
  txt = txt.replace('\\u099d',

                    'ঝ')
  txt = txt.replace('\\u099e',

                    'ঞ')
  txt = txt.replace('\\u099f',

                    'ট')
  txt = txt.replace('\\u09a0',

                    'ঠ')
  txt = txt.replace('\\u09a1',

                    'শ')
  txt = txt.replace('\\u09a2',

                    'ঢ')
  txt = txt.replace('\\u09a3',

                    'ণ')
  txt = txt.replace('\\u09a4',

                    'ত')
  txt = txt.replace('\\u09a5',

                    'থ')
  txt = txt.replace('\\u09a6',

                    'দ')
  txt = txt.replace('\\u09a7',

                    'ধ')
  txt = txt.replace('\\u09a8',

                    'ন')
  #txt = txt.replace('\\u09aa',

   #                 'প')
  txt = txt.replace('\\u09a9',

                    'প')
  txt = txt.replace('\\u09aa',

                    'ফ')
  txt = txt.replace('\\u09ac',

                    'ব')
  txt = txt.replace('\\u09ac',

                    'ভ')
  txt = txt.replace('\\u09ae',

                    'ম')
  txt = txt.replace('\\u09af',

                    'র')
  txt = txt.replace('\\u09b0',

                    'র')
  txt = txt.replace('\\u09b2',

                    'ল')
  txt = txt.replace('\\u09b6',

                    '')
  txt = txt.replace('\\u09b7',

                    'ষ')
  txt = txt.replace('\\u09b8',

                    'স')
  txt = txt.replace('\\u09b3',

                    'স')
  txt = txt.replace('\\u09b9',

                    'হ')
  txt = txt.replace('\\u09b4',

                    'হ')
  txt = txt.replace('\\u09bc',
                    '়')
  txt = txt.replace('\\u09be',
                    'া')
  txt = txt.replace('\\u09b1',
                    'ি')
  txt = txt.replace('\\u09ab',
                    'ি')
  txt = txt.replace('\\u09bf',
                    'ি')
  txt = txt.replace('\\u09c0',
                    'ী')
  txt = txt.replace('\\u09c1',
                    'ু')
  txt = txt.replace('\\u09c2',
                    'ূ')
  txt = txt.replace('\\u09c3',
                    'ৃ')
  txt = txt.replace('\\u09c4',
                    'ৄ')
  txt = txt.replace('\\u09ad',
                    'ম')
  txt = txt.replace('\\u09c7',
                    'ে')
  txt = txt.replace('\\u09c8',
                    'ৈ')
  txt = txt.replace('\\u09cb',
                    'ো')
  txt = txt.replace('\\u09cc',
                    'ৌ')
  txt = txt.replace('\\u09cd',
                    '্')
  txt = txt.replace('\\u09d7',
                    'ৗ')
  txt = txt.replace('\\u09dc',
                    'ড়')
  txt = txt.replace('\\u09dd',
                    'ঢ়')
  txt = txt.replace('\\u09df',
                    'য়')
  txt = txt.replace('\\u09e0', 'ৠ')
  txt = txt.replace('\\u09e1', 'ৡ')
  txt = txt.replace('\\u09e2', 'ৢ')
  txt = txt.replace('\\u09e3', 'ৣ')
  txt = txt.replace('\\u09e6', '০')
  txt = txt.replace('\\u09e7', '১')
  txt = txt.replace('\\u09e8', '২')
  txt = txt.replace('\\u09e9', '৩')
  txt = txt.replace('\\u09ea', '৪')
  txt = txt.replace('\\u09eb', '৫')
  txt = txt.replace('\\u09ec', '৬')
  txt = txt.replace('\\u09ed', '৭')
  txt = txt.replace('\\u09ee', '৮')
  txt = txt.replace('\\u09ef', '৯')
  txt = txt.replace('\\u09f0', 'ৰ')
  txt = txt.replace('\\u09f1', 'ৱ')
  txt = txt.replace('\\u09f2', '৲')
  txt = txt.replace('\\u09f3', '৳')
  txt = txt.replace('\\u09f4', '৴')
  txt = txt.replace('\\u09f5', '৵')
  txt = txt.replace('\\u09f6', '৶')
  txt = txt.replace('\\u09f7', '৷')
  txt = txt.replace('\\u09f8', '৸')
  txt = txt.replace('\\u09f9', '৹')
  txt = txt.replace('\\u09fa', '৺')

  txt = txt.replace('\\u0964',
                               '।')


  #txt = txt.dumps(txt.decode("utf-8"), indent=4, ensure_ascii=False)
  #toUnicode = test.convertBijoyToUnicode(txt)
  #txt=iconv('UTF-8', 'windows-1252', txt)
  return txt
  

