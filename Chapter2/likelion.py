# 차집합/변수의 내용을 바꿔 다시 그 변수에 넣는 법을 배우는 문서

set_lunch = set(["된장찌개", "피자", "제육볶음", "짜장면"])
item = "짜장면"

# set_lunch - item # 집합에서 문자열을 빼는 것은 오류!
# set_lunch - set([item]) # 문자열에서 리스트로, 리스트에서 집합으로 바꿔서 빼야 정상!

print(set_lunch - set([item])) # 짜장면 뺀 것을 출력하라는 코드지, 진짜 짜장면을 빼라는 코드가 아님
set_lunch = set_lunch - set([item]) # 이렇게 해야 짜장면이 빠짐
print(set_lunch)