__author__ = 'yschellekens'

from abc import ABCMeta, abstractmethod
import time
import datetime
from datetime import date
from random import shuffle

class test:

    def __init__(self, TestName,StartDate,totalAvailableGeos):
     self.TestName = TestName
     self.StartDate=StartDate
     self.totalAvailableGeos=totalAvailableGeos


    def RandGeos(self):
      shuffle(self.totalAvailableGeos)
      n = len(self.totalAvailableGeos)
      splt=int(n/2)
      test=self.totalAvailableGeos[0:splt]
      print(test)
      return test;


    def computeTestLenght(self):
       incremental = datetime.timedelta(days=30)
       return self.StartDate+incremental

myList=[1,2,3,4,5,6,7,8]
day = datetime.date.today()
test1=test('yahoo test',day,myList)
test2=test1.RandGeos()
print(test1.computeTestLenght())

