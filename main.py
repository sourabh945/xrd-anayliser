import pandas as pd
import os
import numpy as np
import shutil
import matplotlib.pyplot as plt  
import csv
from scipy import optimize

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

def funcgauss(x,y0,a,mean,sigma) -> float:
    '''Gaussian equation'''
    return y0+(a/(sigma*np.sqrt(2*np.pi)))*np.exp(-(x-mean)**2/(2*sigma*sigma))

def generate_gaussian__(xrange:list,y0:float,a:float,mean:float,sigma:float,number_of_points_:int=1000):
    if number_of_points_ <= 0 :
        print("Invalid number of points")
        return []
    else:
        interval__ = abs(xrange[1] - xrange[0])/(number_of_points_)
        return [i for i in np.arange(xrange[0],xrange[1],interval__)] , [funcgauss(i,y0,a,mean,sigma) for i in np.arange(xrange[0],xrange[1],interval__)] 

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
    def plot_with_fit(self,x__,y__,xlabel="x",ylabel="y"):
        self.plot_object.plot(x__,y__)
        self.show(xlabel,ylabel)

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
    lambdak1 = 15.406
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
    
    def all_peak(self,baseline:float,width:float) -> list:
        result_ = []
        last_value_ = 0
        slope = True
        for i in range(0,len(self.angle)):
            if self.intensity[i] > baseline:
                if self.intensity[i] < last_value_ and slope:
                    result_.append((self.angle[i],self.intensity[i]))
                    slope = False
                elif self.intensity[i] > last_value_:
                    slope = True
                last_value_ = self.intensity[i]
            else:
                pass
        result__ = [result_[0]]
        checked = set()
        for i in range(1,len(result_)):
            if result_[i][0] - result__[-1][0] < width:
                if result_[i][1] > result__[-1][1]:
                    result__[-1] = result_[i]
            else:
                result__.append(result_[i])
        return result__
    
    def fit_peak__(self,range):
        x_seg ,y_seg = self.peak_separator(range)
        meanest,_ = self.local_maxima(range)
        sigest = meanest - min(x_seg)
        popt, pcov = optimize.curve_fit(funcgauss,x_seg,y_seg,p0 = [min(y_seg),max(y_seg),meanest,sigest])
        y0,a,mean,sigma = popt
        return y0,a,mean,sigma

    def single_fit_peak(self,range):
        y0,a,mean,sigma = self.fit_peak__(range)
        return generate_gaussian__(range,y0,a,mean,sigma)
    
    def fwhm_of_peak(self,range):
        _,_,_,sigma = self.fit_peak__(range)
        # return (sigma*2*np.sqrt(2*np.log(2)))*np.pi/180
        return sigma*2.35
    
        
    def peak_finder(self,tols):
        peak__ = []
        min_hight , base_line = tols
        result__angle= []
        result__intensity = []
        peak_is_on = False
        for i in range(0,len(self.intensity)):
            if self.intensity[i] > base_line:
                result__angle.append(self.angle[i])
                result__intensity.append(self.intensity[i])
                peak_is_on = True
            if self.intensity[i] <= base_line and peak_is_on:
                if result__intensity[np.argmax(np.array(result__intensity))] > min_hight:
                    peak__.append((result__angle,result__intensity))
                result__angle = []
                result__intensity = []
                peak_is_on = False
        return peak__

    def all_peak(self,tols):
        peak__ = []
        self.all_peak_finder_rec([0,len(self.angle)-1],tols,peak__)
        return peak__
    
    def crystal_size_of_single_peak(self,range):
        lambdak1 = 15.406
        fwhm_ = []
        index__ = len(range)
        print(index__)
        data_ = self.all_peak(500,0.3)
        for i in range:
            fwhm_.append(abs(self.fwhm_of_peak(i)))
        print(fwhm_)
        d_ = []
        sum = 0 
        for i,j in enumerate(fwhm_):
            d_.append(0.9*lambdak1/j*np.sin(data_[i][0]*np.pi/360))
            sum = sum + (0.9*lambdak1/j*np.cos(data_[i][0]*np.pi/360))
        print(d_)
        return sum/len(d_)
        


if __name__ == "__main__":
    loaded = open_file("ABCD.csv",separator='\t')
    angle = np.array(loaded[0])
    intensity = np.array(loaded[1])
    
    data = xrd_data(angle,intensity)

    peaks = data.peak_finder((1500,300))
    print(len(peaks))
    
    plot1 = plot(peaks[0][0],peaks[0][1])
    plot1.show()


    # print(data.all_peak(500,0.3))
    # list = [[21,23],[30,33],[38,39.5],[44.4,45],[45,46],[50.5,51.2],[55,57],[65,66.4],[74,74.5],[74.5,75.5],[79,79.5]]
    # print(data.crystal_size_of_single_peak(list))

    # while(True):
    #     exec(input(">>\t"))

    # plot1 = plot(angle,intensity)
    # fit_x,fit_y = data.single_fit_peak([28.5,29.16])
    # plot1.plot_with_fit(fit_x,fit_y)
    # print(data.all_peak(1000,0.5))
    # print(data.fit_peak([30,32]))
    # print(data.maxima())
    # c ,d = data.peak_separator([10,15])
    # a = plot(angle,intensity)
    # a.show()
    
    # print(np.searchsorted(angle,10))

    
    

# a.show()