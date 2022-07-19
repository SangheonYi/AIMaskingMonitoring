# locustfile.py
from locust import HttpUser, task, between
short_text = "오늘 11kg 간다. 우리가 강의를 이상헌 듣는다. 농협은 일요일 쉰다."
paragraph_count = 100
user_count = 0
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
class LocustUser(HttpUser):
    host = "http://localhost:5000"
    wait_time = between(1, 2)
    count = 0
    def __init__(self, *args, **kwargs):
        global user_count
        super().__init__(*args, **kwargs)
        user_count += 1
        self.user_id = user_count
        print(f"user{user_count} init!")

    @task
    def home(self):
        resp = self.client.post('/pii_demo', json=body).json()
        # self.client.get('/pii_demo')
        self.count += 1
        proc = resp["process"]
        print(f"{self.user_id} got {self.count} from {proc}")