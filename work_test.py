from transformers import ElectraTokenizerFast, ElectraForTokenClassification
    
tokenizer = ElectraTokenizerFast.from_pretrained("./model")
model = ElectraForTokenClassification.from_pretrained("./model")
sentence_count = 1
sentences = ["특히 둘째 출산 후 몸무게가 63kg까지 치솟았다고 밝혔지만 체중 증가가 무색할 정도로 변함없는 비주얼을 자랑해 감탄을 안겼다."] * sentence_count

inputs = tokenizer(sentences, 
            return_tensors='pt')
print(model(**inputs))