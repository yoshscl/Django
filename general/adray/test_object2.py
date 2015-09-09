__author__ = 'yschellekens'

from abc import ABCMeta, abstractmethod
import time
import datetime
from datetime import date
from random import shuffle
import json
import os
import random

class test:
    def __init__(self, TestName, StartDate, totalAvailableGeos):
        self.TestName = TestName
        self.StartDate = StartDate
        self.totalAvailableGeos = totalAvailableGeos

    def RandGeos(self):
        shuffle(self.totalAvailableGeos)
        n = len(self.totalAvailableGeos)
        splt = int(n / 2)
        test = self.totalAvailableGeos[0:splt]
        print(test)
        return test;

    def computeTestLenght(self):
        incremental = datetime.timedelta(days=30)
        return self.StartDate + incremental
'''
    def createJsonFile(self):
        str =" var statesData ={'type':'FeatureCollection','features':["
        f = open('us-states.txt')
        for line in iter(f):
          line=line[:-2]
          dict=json.loads(line)
          dict['Test'] = random.randint(0,1) # to change at the future using rand geo's
          str_new=json.dumps(dict)
          str_new=str_new+','
          str=str+str_new
      f.close()

      str=str[:-1]
      str=str+']};'
      text_file = open("Output.js", "w")
      text_file.write(str)
      text_file.close()
     return None
'''

