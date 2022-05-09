# 익명 게시판 최종본(두 가지의 데이터 저장 방식을 이용함. 두 가지 방식을 비교해서 공부하기)

# 데이터를 저장하는 법: 1. 온전히 딕셔너리만 쓰기 2. 리스트 안에 딕셔너리 담아서 쓰기
# 1. 온전히 딕셔너리만 쓰기: {"취미는 무엇입니까": "영화 보기입니다", "특기는 무엇입니까": "댄스입니다"}
                         # : 앞은 Key       # : 뒤는 value
# 2. 리스트 안에 딕셔너리 담아서 쓰기: [{"질문": "취미는 무엇입니까", "답변": "영화 보기입니다"} {"질문": "특기는 무엇입니까", "답변": "댄스입니다"}]                         
                         # "질문"이 key, "취미는 무엇입니까"가 value



# 1. 온전히 딕셔너리만 쓰는 방법
total_dictionary = {} # 현재는 빈 딕셔너리 

while True: # 들여쓰기 중요
    question = input("질문을 입력해 주세요: ")
    if question == "q": # ==은 좌우가 같은지 비교함
        break
    else:
        total_dictionary[question] = "" # totle_dictionary key에 question이 들어가고, value에는 빈 문자열이 들어감

for i in total_dictionary:
    print(i)    
    answer = input("답변을 입력해 주세요: ")   
    total_dictionary[i] = answer # value에 사용자가 입력한 answer이 들어감

print(total_dictionary)    















# 2. 리스트 안에 딕셔너리 담아서 쓰는 방법
total_list = []

while True:
    question = input("질문을 입력해 주세요: ")
    if question == "q":
        break
    else:
        total_list.append({"질문": question, "답변": ""}) # 답변 뒤 빈곳을 나중에 사용자가 입력한 데이터로 바꿀 것임.

for i in total_list:
    print(i["질문"]) # print(i)로 하면 프로그램 돌렸을 때 리스트 전체가 나와 버림. 질문만 뽑는 코드
    answer = input("답변을 입력해 주세요: ")
    i["답변"] = answer # answr라는 변수가 i라는 딕셔너리에 답변이라는 key를 가진 value로 들어감
    
print(total_list)    