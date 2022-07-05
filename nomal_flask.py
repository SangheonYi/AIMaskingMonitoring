from flask import Flask, request
from transformers import ElectraTokenizerFast, ElectraForTokenClassification, TokenClassificationPipeline
import os, psutil

process = psutil.Process(os.getpid())
count = 0
start_memory = 0

app = Flask(__name__)
pipeline = None

def init_pipeline():
    global pipeline

    # init config
    tokenizer = ElectraTokenizerFast.from_pretrained("./model")
    model = ElectraForTokenClassification.from_pretrained("./model")
    pipeline = TokenClassificationPipeline(
        model=model, tokenizer=tokenizer, framework='pt')

@app.route('/process_memory', methods=['GET'])
def get_process_memory():
    global start_memory
    memory = round(process.memory_info().rss / 1024 ** 2, 3)
    if count == 1:
        start_memory = memory
    print("memory usages:", memory)
    print("memory start, end, differencies:", start_memory, memory, round(memory - start_memory, 3))
    return str(memory)

@app.route('/pii_demo', methods=['POST'])
def pii_demo():
    text = request.get_json(silent=True)["text"]
    
    result = pipeline(text)
    print(result)
    print(f'result len: {len(result)}')
    return "done"

if __name__ == '__main__':
    init_pipeline()
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)