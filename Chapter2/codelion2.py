# 변수에 대하여 배우는 문서

import random

lunch = random.choice(["된장찌개", "피자", "제육볶음"]) # lunch는 이름표, = 뒤는 이름표에 대한 내용물
lunch = "냉장고" # 이렇게 하면 윗줄에서 lunch에 넣은 음식들은 자동으로 지워지고 냉장고가 채워짐
dinner = random.choice(["김밥", "쫄면", "돈까스"])

print(lunch) # 이렇게 하면 변수 lunch 안 내용물이 출력됨