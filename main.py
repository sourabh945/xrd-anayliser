import pandas as pd
import os
import numpy as np
import shutil
import matplotlib.pyplot as plt  
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
        left_index = np.searchsorted(self.angle,range[0],side='left')
        right_index = np.searchsorted(self.angle,range[1],side='right')
        return self.angle[left_index:right_index] , self.intensity[left_index:right_index]
    
    def local_maxima(self,range) -> float:
        x,y = self.peak_separator(range)
        max_index = np.argmax(y)
        return x[max_index],y[max_index]
    
    def maxima(self) -> float:
        return self.angle[np.argmax(self.intensity)] , self.intensity[np.argmax(self.intensity)]
    
    def all_peak(self) -> list:
        


if __name__ == "__main__":
    loaded = open_file("data.csv",separator='\t')
    angle = np.array(loaded[0])
    intensity = np.array(loaded[1])
    
    # data = xrd_data(angle,intensity)
    # print(data.maxima())
    # c ,d = data.peak_separator([10,15])
    # a = plot(angle,intensity)
    # a.show()
    
    # print(np.searchsorted(angle,10))

    
    

# a.show()