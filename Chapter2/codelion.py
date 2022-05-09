# 자료를 저장하는 방법 1 - 리스트

import random # random을 정의해 줘야 함
import time # time.sleep 쓰기 위해 time 불러온 거임

for X in range(30): # X가 0부터 29일 때까지 : 이후 코드를 반복하라
    print(random.choice(["된장찌개", "피자", "제육볶음", "치킨", "떡볶이"])) # python은 들여쓰기 중요함

while True:
    print(random.choice(["된장찌개","치킨","떡볶이","라면","감자튀김"]))
    break # 반복(루프)를 멈추는 코드. 멈추고 싶은 위치에 작성하면 됨.
    print("이 문장도 반복되나")
    time.sleep(1) # 1초마다 쉰다는 코드

# 터미널에서 코드 루프를 멈추는 키: Ctrl + C    
