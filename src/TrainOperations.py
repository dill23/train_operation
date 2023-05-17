 

__version__ = "0.0.1"
__author__ = "Dylan Hilse"
import train_info as ti

def main():
  train = ti.TrainInfo()
  train.addcar()
  train.saveinfo()

if __name__ == '__main__':
  main()