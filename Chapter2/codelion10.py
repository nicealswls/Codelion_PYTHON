# Chapter 2에서 [오늘은 뭐 드실?] 메뉴 자판기 최종본임

import random
import time

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"] # 리스트, 메뉴 추가는 리스트를 이용함(이유는 그냥)

while True:
    print(lunch)
    item = input("음식을 추가해 주세요: ")
    if(item == "q"):
        break
    else:
        lunch.append(item)
print(lunch)        



set_lunch = set(lunch) # 리스트를 집합으로 만듦(순서 파괴됨), 메뉴 삭제는 집합을 이용함(이유는 그냥. 삭제는 집합이 더 편해서)
while True:
    print(set_lunch)
    item = input("음식을 삭제해 주세요: ")
    if(item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item]) # item은 문자열이기 때문에 먼저 리스트로 바꾸고(대괄호 이용), 그 후 집합으로 바꾸어서 빼야 한다


print(set_lunch, "중에서 선택합니다.")     
print("5")
time.sleep(1) # 1초 쉼 # import 까먹기 말기
print("4")
time.sleep(1) 
print("3")
time.sleep(1) 
print("2")
time.sleep(1)
print("1")
time.sleep(1) 


# random.choice는 오직 리스트에서만 동작함! 그래서 set_lunch를 리스트로 바꾼 거임.
print(random.choice(list(set_lunch))) # import 까먹기 말기
