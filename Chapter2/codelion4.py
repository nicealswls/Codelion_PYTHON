# 딕셔너리와 리스트 배우기

information = {"고향": "수원", "취미": "영화관람", "좋아하는 음식": "국수"} # 딕셔너리
foods = ["된장찌개", "피자", "제윢볶음"] # 리스트

print(information.get("고향")) # 딕셔너리 출력 방식
information["특기"] = "피아노" # 딕셔너리에 값 추가하는 법
information["사는 곳"] = "서울"
del information["좋아하는 음식"] # 딕셔너리 값 지우기
print(information)
print(len(information)) # 몇 개의 정보가 있는지 알려 줌

# information.clear() >> 딕셔너리 다 비우는 코드
# print(information) >> 출력하면 텅 비어 있을 것임


print(foods[0]) # 리스트에서 맨앞 값 출력, 리스트에서는 가장 처음이 0
print(foods[-1]) # 음수는 뒤에서부터 반대로 접근함
foods.append("김밥") # 리스트에서 값 추가
del foods[1] # 딕셔너리랑 비슷함. 리스트에서 두 번째 값 삭제하는 코드
print(foods)