 

__version__ = "0.0.6"
__author__ = "Dylan Hilse"
import train_info as ti
#import network.network
#import network.client

def main():
  train = ti.TrainInfo()
  train.maketrain()
  train.addcar()
  #train.deleteTrain()
  train.saveinfo()
  #network.start()
 
if __name__ == '__main__':
    main()