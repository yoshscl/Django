__author__ = 'yschellekens'

from abc import ABCMeta, abstractmethod
import time

class test:

      def __init__(self,TestName,StartDate,totalAvailableGeos): ''',clientID,clientName,selectedChannel,testStatus,actionToDo,successMetric,endDate,significance,power,,selectedGeos,
                 spendDatabyGeo,salesDatabyGeo,estimationOfCost,estimationOfRoas,estimationOfVarRoas):'''
      self.TestName = TestName
         # self.clientID = clientID
         #self.selectedGeos=selectedGeos
        #self.totalAvailableGeos=totalAvailableGeos
        #self.actionToDo=actionToDo
      self.StartDate=StartDate
      self.totalAvailableGeos=totalAvailableGeos
        #self.selected=totalAvailableGeos


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

''' def createJsonForSimulation(self):
       incremental = datetime.timedelta(days=30)
       return self.StartDate+incremental

    @abstractmethod
    def boostGeos(self, amount):
        #this method will be done implemented in each subclass also depend on whether it will be done by algorithm or determined boost
        #for this we need max bid, boost, action,
        pass

    def getSpentData(self): #not sure we need this
        self.balance += amount
        return self.balance


    def computeExtraSpent(self): #overide for non simple test
        #need time frame of test, geos that are 'test' geo's, and thier spent
        self.balance += amount
        return self.balance

    def computeEstVar(self, amount): #overide for non simple test
        self.balance += amount
        return self.balance

     def computeRoas(self, amount):#overide for non simple test
        self.balance += amount
        return self.balance

    def standerize(self, amount):#overide for non simple test
        self.balance += amount
        return self.balance

    def load(self, amount):
        #load the most updates roas , spent assestment, var assestment into test & test arcive,
        return self.balance

    def save(self, amount):
       #save the most updates roas , spent assestment, var assestment into test & test arcive,
        return self.balance '''


myList=[1,2,3,4,5,6,7,8]
test1=test('yahoo test','2012-05-12',myList)
test1.RandGeos()