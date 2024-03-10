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

class ProcessPlotter:
#     def __init__(self) -> None:
#         self.x = []
#         self.y = []

#     def terminate(self):
#         plt.close('all')

#     def call_back(self):
#         while self.pipe.poll():
#             command = self.pipe.recv()
#             if command is None:
#                 self.terminate()
#                 return False
#             else:
#                 self.x.append(command[0])
#                 self.y.append(command[1])
#                 self.ax.plot(self.x, self.y, 'ro')
#         self.fig.canvas.draw()
#         return True
    
#     def __call__(self, pipe):
#         print('starting plotter...')

#         self.pipe = pipe
#         self.fig, self.ax = plt.subplots()
#         timer = self.fig.canvas.new_timer(interval=1000)
#         timer.add_callback(self.call_back)
#         timer.start()

# #         print('...done')
#         plt.show()

# class Plot:
#     def __init__(self):
#         self.plot_pipe, plotter_pipe = mp.Pipe()
#         self.plotter = ProcessPlotter()
#         self.plot_process = mp.Process(
#             target=self.plotter, args=(plotter_pipe,), daemon=True)
#         self.plot_process.start()

#     def plot(self,given_data, finished=False):
#         send = self.plot_pipe.send
#         if finished:
#             send(None)
#         else:
#             data = given_data
            # send(data)