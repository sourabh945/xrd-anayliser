import pandas as pd
import os
import numpy as np
import shutil
import matplotlib.pyplot as plt

def open_file(filepath,type="csv",separator=";") -> None:
    if type == "csv":
        with open(filepath,'r') as file:
            data = pd.read_csv(file,sep=separator,header=None)
            file.close()
        return data
    else:
        base_name , _  = os.path.splitext(filepath)
        shutil.copy2(filepath,f'{base_name}.csv')
        with open(filepath,'r') as file:
            data = pd.read_csv(file,sep=separator,header=None)
            file.close()
        return data

class plot:    
    def __init__(self,x,y) -> None:
        self.plot_object = plt
        self.plot_object.ion()
        self.plot_object.plot(x,y)
    def show(self,xlabel="x",ylabel="y"):
        self.plot_object.xlabel(xlabel)
        self.plot_object.ylabel(ylabel)
        self.plot_object.show()
    def save(self,name):
        self.plot_object.savefig(f"/plots/{name}.png")

def 

angle = np.array(open_file("data.csv",separator="\t")[0])
intensity = np.array(open_file("data.csv",separator="\t")[1])

a = plot(angle,intensity)
a.show()

print(plt.isinteractive())