for x in range(30): # x는 0부터 29까지이다
    print(x)

foods = ["된장찌개", "피자", "제육볶음"]    
print(foods[0])
print(foods[1])
print(foods[2]) # 이렇게 다 출력하려면 귀찮고 힘드니까

for x in range(3):
    print(foods[x]) # 이렇게 for 이용하기

for x in foods:
    print(x) # 리스트에서 foods 값을 모두 출력하는 코드



information = {"고향": "수원", "취미": "영화관람", "좋아하는 음식": "국수"}
for x, y in information.items():
    print(x)
    print(y) # 딕셔너리에서 information 값을 모두 출력하는 코드
