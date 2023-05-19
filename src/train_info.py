import json
import os

class TrainInfo():

  def __init__(self):
      if os.path.exists("savejson.json") == True:
          TrainFile = open("savejson.json", "r")
      else:
          TrainFile = open("savejson.json", 'xr')
      self.Train = json.load(TrainFile)
      
  def maketrain(self):
      try:
        train = {}
        trainName = input("Please enter a name for the train. Thanks!: ")
      except ValueError:
          print("something went wrong.")
      else:
        train[trainName] = trainName
        self.Train[trainName] = train
  def addcar(self):
    while True:  
      try:
        trainName = input("Please enter the name for the train: ")
        train = self.Train
        carid = int(input("please enter the cars id number or enter -1 to quit.: "))
        if carid == -1:
          break 
        train[trainName]['carid'] = carid
        cartype = input("enter the car type: ")
        train[trainName]['cartype'] = cartype
        carbrand = input('enter the name of the manufacturer: ')
        train[trainName]['carbrand'] = carbrand
      except KeyError:
        print("something went wrong entering the key into the dic, keyError")
      except ValueError:
        print('something went wrong, ValueError')

  def saveinfo(self):
    with open('savejson.json','w') as savefile:
      output = json.dumps(self.Train, indent=2)
      savefile.write(output)
      print(self.Train)
  