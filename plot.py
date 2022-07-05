import matplotlib.pyplot as pl
import statistics
import torch

def draw_log(graph, target):
      with open(target + '_log.txt', 'r', encoding='utf-8') as file:
        splited = file.readline().split(', ')
        data = [float(e) for e in splited if e]
        x_size = len(data)
        margin = x_size // 400
        graph.set_xlim(-margin, x_size + margin)
        graph.plot(range(x_size), data[:x_size])
        graph.set_title(f"{torch.__version__} {target} log {round(statistics.mean(data), 3)}")


axis = pl.subplots(2, 1, figsize=(20, 10))[1]
pl.subplots_adjust(left=0.03, bottom=0.05, right=0.98, top=0.98, wspace=1, hspace=0.1)

draw_log(axis[0], 'memory')

draw_log(axis[1], 'time')
pl.savefig('test.png')
