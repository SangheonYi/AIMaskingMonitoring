from transformers import ElectraTokenizerFast, ElectraForTokenClassification, TokenClassificationPipeline
from kiwipiepy import Kiwi

kiwi=Kiwi()
tokenizer = ElectraTokenizerFast.from_pretrained("./model")
model = ElectraForTokenClassification.from_pretrained("./model")
sentence_count = 100
sentences = "특히 둘째 출산 후 몸무게가 63kg까지 치솟았다고 밝혔지만 체중 증가가 무색할 정도로 변함없는 비주얼을 자랑해 감탄을 안겼다." * sentence_count
splitted_text = list(kiwi.split_into_sents(sentences))
text_list = [splitted_line.text for splitted_line in splitted_text]
inputs = tokenizer(text_list, 
        return_tensors='pt',
        truncation=True, 
        padding=True)
print(model(**inputs))