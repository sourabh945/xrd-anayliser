import pandas as pd
import os
import numpy as np
import shutil

import csv

def open_file(filepath,type="csv",separator=";") -> None:
    try:
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
    except Exception as error:
        print(error)

class plot:  
    def __init__(self,x,y) -> None:
        import matplotlib.pyplot as plt  
        self.plot_object = plt
        self.x = x
        self.y = y
    def show(self,xlabel="x",ylabel="y"):
        self.plot_object.xlabel(xlabel)
        self.plot_object.ylabel(ylabel)
        self.plot_object.plot(self.x,self.y)
        self.plot_object.show()
    def save(self,name):
        self.plot_object.plot(self.x,self.y)
        self.plot_object.savefig(f"/plots/{name}.png")

def export_csv(filename,*args) -> bool:
    try:
        with open(filename,"w") as file:
            writer = csv.writer(file)
            data = []
            for i in args:
                data.append(list(i))
            row = data.__len__()
            col = data[0].__len__()
            for i in range(0,col):
                temp = []
                for j in range(0,row):
                    temp.append(data[j][i])
                writer.writerow(temp)
        return True
    except Exception as error:
        print(error)
        return False
    
class xrd_data:
    def __init__(self,angle,intensity) -> None:
        self.angle = angle
        self.intensity = intensity
    def peak_separator(self,range) -> list:
        left_index = np.searchsorted(self.x,range[0],side='left')
        right_index = np.searchsorted(self.x,range[1],side='right')
        data = []
        temp 
        return 
    

angle = np.array(open_file("data.csv",separator="\t")[0])
intensity = np.array(open_file("data.csv",separator="\t")[1])

a = plot(angle,intensity)
# a.show()
print(np.searchsorted(angle,10))
b = plot([0,1,2,3],[0,2,4,6])
# b.show()

# a.show()