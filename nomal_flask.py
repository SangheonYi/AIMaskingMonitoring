from flask import Flask, request
from transformers import ElectraTokenizerFast, ElectraForTokenClassification
import os, psutil
from kiwipiepy import Kiwi

process = psutil.Process(os.getpid())
count = 0
start_memory = 0

app = Flask(__name__)
model = None
tokenizer = None
kiwi = None

def init_pipeline():
    global tokenizer
    global model
    global kiwi

    # init kiwi
    kiwi=Kiwi()
    tokenizer = ElectraTokenizerFast.from_pretrained("./model")
    model = ElectraForTokenClassification.from_pretrained("./model")

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
    splitted_text = kiwi.split_into_sents(text)
    inputs = [splitted_line.text for splitted_line in splitted_text]
    inputs = tokenizer(inputs, 
            return_tensors='pt')
    print(f"result len: {len(model(**inputs))}")
    return "done"

if __name__ == '__main__':
    init_pipeline()
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)