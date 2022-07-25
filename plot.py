import matplotlib.pyplot as pl
import statistics
import torch

def draw_graph(graph, data, target):
  x_size = len(data)
  margin = x_size // 400
  graph.set_xlim(-margin, x_size + margin)
  graph.plot(range(x_size), data[:x_size])
  graph.set_title(f"{target} log {round(statistics.mean(data), 3)}")
  
def parse_serv_log():
  with open('../ai-masking-server/logs/ai-masking-daemon.log', 'r', encoding='utf-8') as file:
    data = []
    for line in file:
      splited = line.split()
      if 'spent' in splited:
        data.append(float(splited[-1]))
  return data

def parse_cli_log():
  with open('time_log.txt', 'r', encoding='utf-8') as file:
    data = []
    for line in file.readlines():
      if '😀'in line:
        continue
      splited = line.split()
      if "from" in splited:
        data.append(float(splited[3]))
  return data

def draw_log(target):
  with open(target + '_log.txt', 'r', encoding='utf-8') as file:
    splited = file.readline().split(', ')
    data = [float(e) for e in splited if e]
  return data

axis = pl.subplots(2, 1, figsize=(20, 10))[1]
pl.subplots_adjust(left=0.03, bottom=0.05, right=0.98, top=0.98, wspace=1, hspace=0.1)

# data = draw_log('memory')
# draw_graph(axis[0], data, 'memory')
# data = draw_log('time')
# draw_graph(axis[1], data, 'time')
data = parse_serv_log()
draw_graph(axis[0], data, 'server')
data = parse_cli_log()
draw_graph(axis[1], data, 'client')

pl.savefig('test.png')
