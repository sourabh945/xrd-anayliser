from matplotlib import pyplot as plt
from sys import argv
import pandas as pd

filename = argv[1]


with open(filename,"r") as file:
    data = pd.read_csv(filename,sep="\t",header=None)
    file.close()

plt.plot(data[0],data[1])

plt.xlabel("angle")
plt.ylabel("intensity")
plt.ion()
while True:
    plt.show()
