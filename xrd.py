import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np
import pandas as pd
import os
import shutil
import random
from sys import argv
from csv import reader,writer
import multiprocessing as mp
from threading import Thread 
import powerxrd


if len(argv) == 0:
    print("Please pass the path of file")
    os._exit(status=1)

try:
    path = argv[1]
except Exception as error:
    print(error)
    os._exit(status=1)


try:
    separator = argv[2]
except:
    separator = ","

_,extension = os.path.splitext(path)

try:
    if extension.lower() == ".csv":
        with open(path,'r') as file:
            data = pd.read_csv(file,sep=separator,header=None)
            angle = np.array(data[0])
            intensity = np.array(data[1])
            del data
            file.close()
    else:
        base_name , _  = os.path.splitext(path)
        shutil.copy2(path,f'{base_name}+.csv')
        with open(path,'r') as file:
            data = pd.read_csv(file,sep=separator,header=None)
            angle = np.array(data[0])
            intensity = np.array(data[1])
            del data
            file.close()
except Exception as error:
    if path not in set(os.listdir()):
        print(f"Sorry file {path} is not current dir :{os.curdir()}")
        os._exit(1)
    else:
        print(error)
        os._exit(1)

class plot:
    if "Plots" not in set(os.listdir("./")):
        os.mkdir("./Plots/")
    def __init__(self,x,y,xlabel='x',ylabel='y') -> None:
        self.plot = plt.plot(x,y)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
    def save(self,name):
        plt.savefig(f"./Plots/{name}.png")

