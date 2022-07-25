# AIMaskingMonitoring

### test multi user request
`python multi_req_tets.py`  
graph 필요 시:  
`python multi_req_tets.py > time_log.txt`

```
# 1회 요청 당 paragraph 수
paragraph_count = 100
# 유저 수
user_count = 100
# request 20번 정도면 queing 지연 시간이 최댓값으로 수렴한다고 판단
req_count = 20
```

### log graph
`python plot.py`