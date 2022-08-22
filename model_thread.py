import os
from transformers import ElectraTokenizerFast, ElectraForTokenClassification
import time
import torch

MODEL_DIR = './model'
TOKENIZER_DIR = './model'
short_text = "오늘 11kg 간다. 우리가 강의를 이상헌 듣는다. 농협은 일요일 쉰다."
# print(torch.get_num_threads(), torch.get_num_interop_threads())
torch.set_num_threads(8) # set 2 spent:  19.297 # default spent:  9.544 # set 8 spent: 9.584
# torch.set_num_interop_threads(1)
# print(torch.get_num_threads(), torch.get_num_interop_threads())

tokenizer = ElectraTokenizerFast.from_pretrained(TOKENIZER_DIR)
model = ElectraForTokenClassification.from_pretrained(MODEL_DIR)
model.train()
repeat_count = 1000

avg = 0
def inference(input_tokenizer):
    global avg
    start = time.time()
    # inputs = tokenizer(input_tokenizer, return_tensors="pt")
    inputs = {'input_ids': torch.tensor([[   2, 6451, 6307, 4011, 4060, 9379,   18, 6233, 4070, 7911, 4110, 6264,
         4243, 2440, 4034, 4176,   18, 9720, 4112, 9622, 2987, 4176,   18,    3],
        [   2, 6451, 6307, 4011, 4060, 9379,   18, 6233, 4070, 7911, 4110, 6264,
         4243, 2440, 4034, 4176,   18, 9720, 4112, 9622, 2987, 4176,   18,    3],
        [   2, 6451, 6307, 4011, 4060, 9379,   18, 6233, 4070, 7911, 4110, 6264,
         4243, 2440, 4034, 4176,   18, 9720, 4112, 9622, 2987, 4176,   18,    3],
        [   2, 6451, 6307, 4011, 4060, 9379,   18, 6233, 4070, 7911, 4110, 6264,
         4243, 2440, 4034, 4176,   18, 9720, 4112, 9622, 2987, 4176,   18,    3],
        [   2, 6451, 6307, 4011, 4060, 9379,   18, 6233, 4070, 7911, 4110, 6264,
         4243, 2440, 4034, 4176,   18, 9720, 4112, 9622, 2987, 4176,   18,    3],
        [   2, 6451, 6307, 4011, 4060, 9379,   18, 6233, 4070, 7911, 4110, 6264,
         4243, 2440, 4034, 4176,   18, 9720, 4112, 9622, 2987, 4176,   18,    3],
        [   2, 6451, 6307, 4011, 4060, 9379,   18, 6233, 4070, 7911, 4110, 6264,
         4243, 2440, 4034, 4176,   18, 9720, 4112, 9622, 2987, 4176,   18,    3],
        [   2, 6451, 6307, 4011, 4060, 9379,   18, 6233, 4070, 7911, 4110, 6264,
         4243, 2440, 4034, 4176,   18, 9720, 4112, 9622, 2987, 4176,   18,    3],
        [   2, 6451, 6307, 4011, 4060, 9379,   18, 6233, 4070, 7911, 4110, 6264,
         4243, 2440, 4034, 4176,   18, 9720, 4112, 9622, 2987, 4176,   18,    3],
        [   2, 6451, 6307, 4011, 4060, 9379,   18, 6233, 4070, 7911, 4110, 6264,
         4243, 2440, 4034, 4176,   18, 9720, 4112, 9622, 2987, 4176,   18,    3]]), 
         'token_type_ids': torch.tensor([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), 
        'attention_mask': torch.tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]),
        }
    model(**inputs)
    avg += round(time.time() - start, 3)
for i in range(repeat_count):
    input_tokenizer = [short_text for _ in range(1)]
    inference(input_tokenizer)
print("spent: ", round(avg / repeat_count, 3))

# start = time.time()
# for i in input_tokenizer:
#     inference(i)
# print("spent: ", round(time.time() - start, 3))