import torch
import timeit
import matplotlib.pyplot as pl
import statistics
import torch

def draw_graph(graph, data, target):
  x_size = len(data)
  margin = x_size // 400
  graph.set_xlim(-margin, x_size + margin)
  graph.plot(range(x_size), data[:x_size])
  graph.set_title(f"{target} log {round(statistics.mean(data), 3)}")

runtimes = []
threads = [1] + [t for t in range(2, 49, 2)]
for t in threads:
    torch.set_num_threads(t)
    r = timeit.timeit(setup = "import torch; x = torch.randn(1024, 1024); y = torch.randn(1024, 1024)", stmt="torch.mm(x, y)", number=100)
    runtimes.append(r)

axis = pl.subplots(1, 1, figsize=(20, 10))[1]
pl.subplots_adjust(left=0.03, bottom=0.05, right=0.98, top=0.98, wspace=1, hspace=0.1)
draw_graph(axis, runtimes, 'thread')
pl.savefig('tune.png')