from matplotlib import pyplot as plt
from sys import argv

import json

def graph(x,y,xlabel,ylabel):
    plt.xlabel(xlabel=xlabel)
    plt.ylabel(ylabel=ylabel)
    plt.plot(x,y)
    plt.show()

filename=argv[1]

with open("./.temp/{filename}.json") as file:
    data = list(json.load(file))
    file.close()

graph(data[0],data[1],argv[2],argv[3])