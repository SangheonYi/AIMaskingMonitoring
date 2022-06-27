import matplotlib.pyplot as pl

def draw_log(graph, target):
      with open(target + '_log.txt', 'r', encoding='utf-8') as file:
        splited = file.readline().split(', ')
        data = [float(e) for e in splited if e]
        x_size = len(data)
        margin = x_size // 400
        graph.set_xlim(-margin, x_size + margin)
        graph.plot(range(x_size), data[:x_size])
        graph.set_title(target + ' log')


axis = pl.subplots(2, 1, figsize=(50, 10))[1]
pl.subplots_adjust(left=0.02, bottom=0.05, right=0.98, top=1, wspace=1, hspace=0.1)

draw_log(axis[0], 'memory')

draw_log(axis[1], 'time')
pl.savefig('test.png')
