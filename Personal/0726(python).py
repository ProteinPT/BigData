#조건문 실습
cel=30
if cel >0:
    print('아이스아메리카노')


cel_1=-10
if cel_1>0:
    print('아이스 아메리카노')
else:
    print('따뜻한 아메리카노')

cel_2=0
if cel_2 >0:
    print('아이스 아메리카노')
elif cel_2==0:
    print('미지근 아메리카노')
else:
    print('따뜻한 아메리카노')

whether='맑음'
cel_3=40

if whether=='맑음':
    if cel_3 >0:
        print('아이스 아메리카노')
    elif cel_3 ==0:
        print('미지근 아메리카노')
    else:
        print('따뜻한 아메리카노')
else:
    print('카푸치노')

eng_s=90
math_s=90
if eng_s >= 90 and math_s >= 90:
    print('용돈인상')
elif eng_s <= 80 and math_s <= 80:
    print('용돈삭감')
else:
    print('용돈동결')

eng_s1=90
math_s1=70
if eng_s1 >=90 or math_s1 >=90:
    print('용돈인상')
elif eng_s1 <= 80 or math_s1 <= 80:
    print('용돈삭감')
else:
    print('용돈동결')

#반복문 실습
math_score=[80,90,70,65,85,100,90,80,75,80]
re_math=[]
for s in math_score:
    if s <100:
        new=s+5
    else:
        new=s
    re_math.append(new)
print(re_math)

# score 리스트 -> s 변수
# s변수 + 5 -> new 변수
# new 변수 append함수 _> new_score 리스트

# 한줄로 표현하여 새로운 컨테이너 타입을 만드는 방법 = 컴프리핸션
# [수행문1 if 조건문 else 수행문2 for 변수 in 리스트]
# 수행문1= if 조건문을 만족할 경우 수행문
# 수행문2= else 조건문을 만족할 경우 수행문
re_math2=[s+5 if s <100 else s for s in math_score]
print(re_math2)


#while문
math_score=[80,90,70,65,85,100,90,80,75,80]
new_score=[]
index=0

while(index < len(math_score)):
    if math_score[index] <100:
        new=math_score[index]+5
    else:
        new=math_score[index]
    new_score.append(new)
    index= index+1

print(new_score)
