import json

class TrainInfo():

  def __init__(self):
      self.Train = {}

  def addcar(self):
    while True:  
      try:
        cardic = {}
        trainName = input("Please enter a name for the train. Thanks!: ")
        carid = int(input("please enter the cars id number or enter -1 to quit.: "))
        if carid == -1:
          break 
        cardic['carid'] = carid
        cartype = input("enter the car type: ")
        cardic['cartype'] = cartype
        carbrand = input('enter the name of the manufacturer: ')
        cardic['carbrand'] = carbrand
      except KeyError:
        print("something went wrong entering the key into the dic, keyError")
      except ValueError:
        print('something went wrong, ValueError')
      else:
        self.Train[trainName] = cardic

  def saveinfo(self):
    with open('savejson.json','w') as savefile:
      output = json.dumps(self.Train, indent=2)
      savefile.write(output)
      print(self.Train)
  