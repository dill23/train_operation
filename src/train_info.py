import json
import os
from  cryptography.fernet import Fernet

class TrainInfo():

  def __init__(self):
      if os.path.exists("savejson.json") == True:
          self.TrainFile = open("savejson.json", "r")
      elif os.path.exists("savejson.json") == False:
          TrainFile = open("savejson.json", 'w')
          TrainFile.close()
          self.TrainFile = open("savejson.json", "r")
      self.Train = json.load(self.TrainFile)
      
  def maketrain(self):
      try:
        train = {
          'cars' : {}
        }
        trainName = input("Please enter a name for the train. Thanks!: ")
        classtrain = input('Please enter the class # of the train. ')
        traincompany = input('what company would be running this train?')
        train['class'] = classtrain
        train['company'] = traincompany
      except ValueError:
          print("something went wrong.")
      else:
        #train[trainName] = trainName
        self.Train[trainName] = train
  def addcar(self):
    count = 1
    while True:  
      try:
        trainName = input("Please enter the name for the train: ")
        train = {}
        carid = int(input("please enter the cars id number or enter -1 to quit.: "))
        if carid == -1:
          break
        
        print(count)
        caridkey = 'carid' + str(count)
        cartypekey = 'cartype' + str(count)
        carbrandkey = 'carbrand' + str(count)
        print(caridkey, cartypekey, carbrandkey)
        train[caridkey] = carid
        cartype = input("enter the car type: ")
        train[cartypekey] = cartype
        carbrand = input('enter the name of the manufacturer: ')
        train[carbrandkey] = carbrand
        count += 1
        print(train)
        self.Train[trainName]['cars'].update(train)
      except KeyError:
        print("something went wrong entering the key into the dic, keyError")
      except ValueError:
        print('something went wrong, ValueError')
        

  def deleteTrain(self):
      try:
          train = self.Train
          trainName = input("enter tha name of the train you want to delete: ")
          sure = input("are you sure Y or N: ").upper()
          if sure == 'Y':
            del train[trainName]
      except KeyError:
          print('something went wrong')
      else:
          self.Train = train

  def saveinfo(self):
    with open('savejson.json','w') as savefile:
      output = json.dumps(self.Train, indent=2)
      savefile.write(output)
      self.TrainFile.close()
