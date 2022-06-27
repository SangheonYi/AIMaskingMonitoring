import unittest
import requests
import matplotlib.pyplot as pl

sample_str = "특히 둘째 출산 후 몸무게가 63kg까지 치솟았다고 밝혔지만 체중 증가가 무색할 정도로 변함없는 비주얼을 자랑해 감탄을 안겼다.\n"
req_count = 1000
sentence_count = 1000
host = 'http://localhost:5000'

def draw_log(graph, target):
    with open(target + '_log.txt', 'r', encoding='utf-8') as file:
        splited = file.readline().split(', ')
        data = [float(e) for e in splited if e]
        x_size = len(data)
        margin = x_size // 400
        graph.set_xlim(-margin, x_size + margin)
        graph.plot(range(x_size), data[:x_size])
        graph.set_title(target + ' log')

def draw_by_unittest():
    print("log_draw")
    axis = pl.subplots(2, 1, figsize=(50, 10))[1]
    pl.subplots_adjust(left=0.01, bottom=0.05, right=1, top=1, wspace=1, hspace=0.1)
    draw_log(axis[0], 'memory')
    draw_log(axis[1], 'time')
    pl.savefig(f'{sentence_count}request{req_count}times.png')
    print(f'{sentence_count}request{req_count}times.png is saved')

def stamp_memory():
    with open('memory_log.txt', 'a', encoding='utf-8') as memory_log:
                memory = requests.get(host + '/process_memory').text 
                memory_log.write(f'{memory}, ')

class pii_demo_test(unittest.TestCase):
    def setUp(self):
        self.request_body = {
            "lines": [sample_str for _ in range(sentence_count)]
            }
        self.headers = {
            'content-type': "application/json",
            "Connection": "close"
        }
        print('request lines:', len(self.request_body["lines"]))

    def test_memory(self):
        stamp_memory()
        for i in range(req_count):
            print(f'request count: {i}')
            resp = requests.post(host + '/pii_demo', json=self.request_body, headers=self.headers).json()
            spent = resp['spent'] 
            with open('time_log.txt', 'a', encoding='utf-8') as time_log:
                time_log.write(f'{spent}, ')
            stamp_memory()
        draw_by_unittest()

if __name__ == '__main__':
    with open('memory_log.txt', 'w', encoding='utf-8') as memory_log:
        print('reset memory log')
    with open('time_log.txt', 'w', encoding='utf-8') as time_log:
        print('reset time log')
    unittest.main()