import traceback

class TrainInfo():

  def __init__(self):
      self.cars = []

  def addcar(self):
    try:
      cardic = {}
      carid = int(input("please enter the cars id number: "))
      cardic['carid'] = carid
      cartype = input("enter the car type: ")
      cardic['cartype'] = cartype
    except KeyError:
      print("something went wrong entering the key into the dic.", traceback.print_exc())
    except ValueError:
      print('something went wrong', traceback.print_exc())
    else:
      self.cars.append(cardic)
      print(self.cars[0]['cartype'])