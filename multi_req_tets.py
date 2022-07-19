import requests
import threading
import time

host = 'http://127.0.0.1:5000'
short_text = "오늘 11kg 간다. 우리가 강의를 이상헌 듣는다. 농협은 일요일 쉰다."
paragraph_count = 100
user_count = 100
req_count = 100
body = {
        "batches":
        [
            {
                "path": "./xyz/Downloads",
                "text": [short_text for _ in range(paragraph_count)],
            },
        ],
        "labels": [],
        "options": {
            "word": "False"
        }
    }
one_req_spent_avg = 0
total_spent = 0
responsed_count = 0

def req():
    global total_spent
    global responsed_count
    global one_req_spent_avg
    for i in range(req_count):
        start = time.time()
        response = requests.post(f'{host}/pii_demo',json=body).json()
        total_spent += time.time() - start
        responsed_count += 1
        one_req_spent_avg = round(total_spent / responsed_count, 3)
        print(f"took {one_req_spent_avg} from {response['process']}")
    
threads = []
e2e_start = time.time()
for i in range(user_count):
    t = threading.Thread(target=req)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
print(f'paragraph_count: {paragraph_count} user_count: {user_count} req_count: {req_count}')
print(f'total req sum: {round(total_spent, 3)} avg: {one_req_spent_avg}, e2e took: {round(time.time() - e2e_start, 3)}')