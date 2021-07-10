#!/usr/bin/env python
# coding: utf-8

# # <파이썬 셋과 딕셔너리>
# 1. 파이썬 셋
# 2. 파이썬 셋과 집합연산
# 3. 파이썬 딕셔너리

# In[27]:


list_=[1,2,3,4,5,6]
list_.append("Python")
list_


# In[28]:


list_.append([7,8,9])
list_


# ## remove() / pop() 함수
# 셋의 지정된 원소/ 마지막 원소 제거
# (https://blockdmask.tistory.com/451)

# In[29]:


x=0
while True:
    x+= 3
    print(x)
    if x> 100 and x% 3== 0 :
     break


# In[30]:


set1= set({'a','b','c','d','e'})
set1


# In[31]:


set1.remove('a')
set1


# In[32]:


set1.pop()
set1


# In[33]:


set1


# In[34]:


a=[1,2,3]
a.pop()
a


# ## 파이썬 셋 집합연산
# - `교집합` = & / intersection() 함수
# - `합집합`= | / union() 함수
# - `차집합`= - /difference() 함수
# - `대칭 차집합`= ^ / symmetric_diffrence() 함수

# In[35]:


중간고사= {
    "수학":90,
    "영어":80,
}
중간고사


# In[36]:


중간고사['국어']= 85
중간고사


# In[37]:


중간고사['영어']


# In[38]:


중간고사['영어']= 100
중간고사


# In[39]:


list(중간고사.keys())


# In[40]:


list(중간고사.values())


# In[41]:


list(중간고사.items())


# In[42]:


중간고사.keys()


# In[43]:


중간고사.values()


# In[44]:


중간고사.items()


# In[45]:


중간고사.pop('국어')


# In[46]:


중간고사


# In[47]:


중간고사['국어']=100


# In[48]:


중간고사


# In[49]:


중간고사.items()


# # <파이썬 조건문>
# 
# 1. 파이썬 비교연산자와 논리연산자
# 2. 파이썬 조건문
# 3. 파이썬 중첩/복합 조건문

# 
# ## 1.비교연산자와 논리연산자
# ---

# In[50]:


x= 10; y=5
x <y


# In[51]:


x!= y


# In[52]:


y!= x


# In[53]:


x== y


# 
# ## 2. 파이썬 조건문
# ---
# **들여쓰기 중요 !!!**

# In[54]:


점수=50
if 점수 > 60:
    print('합격')
else:
    print('불합격')


# In[55]:


점수=100
if 점수 >70:
    print('합격')
else:
    print('불합격')


# In[56]:


x,y=10,10
if x > y:
    print('x가 y보다 큽니다')
elif x < y:
    print('y가 x보다 큽니다')
elif x ==y :
    print('x와 y가 같습니다')


# In[57]:


x,y=10,10
if x > y:
    print('x가 y보다 큽니다')
elif x < y:
    print('y가 x보다 큽니다')
else:
    print('x와 y가 같습니다')


# 
# ## 3. 중첩/복합 조건문
# ---

# In[58]:


회원=True
입장료= 0
나이=59
if 회원:
    if 나이>6 and 나이<13:
       입장료= 2500
    elif 나이 >14 and 나이 <=59:
       입장료=5000
else :
    if 나이>6 and 나이<13 :
       입장료=5000
    elif 나이>14 and 나이 <=59:
       입장료=10000
print(f'입장료는{입장료:,} 입니다.')


# In[59]:


회원=False
입장료= 0
나이=59
if 회원:
    if 나이>6 and 나이<13:
       입장료= 2500
    elif 나이 >14 and 나이 <=59:
       입장료=5000
else :
    if 나이>6 and 나이<13 :
       입장료=5000
    elif 나이>14 and 나이 <=59:
       입장료=10000
print(f'입장료는{입장료:,} 입니다.')


# In[60]:


admissionFee= 0
age= 19
person= True

if age <=6 or age >=60 :
    admissionFee=0
elif age >6 and age <14 :
    admissionFee=5000
elif age >13 and age <60 :
    admissionFee=10000

if person:
    admissionFee=int(admissionFee*0.5)

print(f'입장료는 {admissionFee:,}원 입니다')


# In[61]:


admissionFee= 0
age= 19
person= False

if age <=6 or age >=60 :
    admissionFee=0
elif age >6 and age <14 :
    admissionFee=5000
elif age >13 and age <60 :
    admissionFee=10000

if person:
    admissionFee=int(admissionFee*0.5)

print(f'입장료는 {admissionFee:,}원 입니다')


# # <파이썬 반복문>
# 1. for 반복문
# 2. while 반복문
# 3. 리스트 컴프리핸션

# ## 1. for 반복문
# ---

# In[62]:


for st in ['Hello','World','Python']:
    print(st)


# In[63]:


score={'국어':95, '영어':80, '수학':100 }
for item in score.keys() :
    print(item)


# In[64]:


score={'국어':95, '영어':80, '수학':100 }
for item in score.values() :
    print(item)


# In[65]:


for key, value in score.items():
    print(f'{key}과목 점수는 {value}점 입니다.')


# In[66]:


for a in range(2,10):
    for i in range(1,10):
        ans= a * i
        print(f'{a}*{i}={ans}')
    if a == 9 :
        print(f'구구단 {a}단 끝')
    else :
        print(f'구구단 {a}단 끝')  
        print(f'구구단 {a+1}단 시작')
        
else :
    print('구구단이 끝났습니다.')
            
        


# ## 2. while 반복문
# ---

# In[67]:


a=0
while a <10 :
    print(a)
    a += 1
else :
    print(f'a가 {a}이므로 종료합니다.')


# In[68]:


x =0
while True:  #무한루프
    x += 3                   #실행코드
    print(x)
    if x>100 and x % 3 == 0: #종료조건
        break


# In[69]:


a=0
while a<10 :
    print(a)
    a +=1
else :
    print(f'a가 {a}이므로 종료합니다.')


# ## 3. 리스트 컴프리핸션(List Comprehension)
# ---
# **리스트 각 원소들에 대해 연산을 수행**

# In[70]:


list1= list(range(1,15))
print(list1)


# In[71]:


list2= [i*2 for i in list1]
print(list2)


# ## [표현식 for 변수 in 리스트 객체 if 조건식]
# - 리스트 원소들 필터링하여 연산 수행

# In[72]:


print(list1)


# In[73]:


list3 =[i**2 for i in list1 if i %2 == 1]
list3


# # <파이썬 함수>
# 1. 파이썬 함수
# 2. 사용자 정의함수
# 3. 함수의 매개변수

# ## 2. 사용자 정의함수
# ---

# In[74]:


def add1() :
    print('더하기 함수입니다')
add1()


# In[75]:


def add2(x,y) :
    print(x+y)
add2(100,145)


# In[76]:


def add3():
    x,y=156,172
    return x+y
re= add3()
print(re)


# In[77]:


def add4(x,y) :   #파라미터, 매개변수
    return x+y
re_= add4(189,192)  #인자(값 value)
print(re_)


# In[78]:


def square(x,y) :   #(사용자 정의) 제곱함수 
    x= x**2
    y= y**2
    return x,y     #return값이 있어야지

sq=square(2,3)
print(sq)


# ## 3. 함수의 매개변수
# ---

# `가변 매개변수`
# - 매개변수 앞에 *를 붙여서 정의
# - 무조건 마지막에 와야함.
# - def 함수명(a,*b) :
#       #print(a,b)

# In[79]:


def changeble(x,y,*z):
    print(x,y,z)


# In[81]:


changeble(1,2,3,4,5)


# In[82]:


changeble(1,2,3,4)


# In[83]:


changeble(1,2)


# In[84]:


changeble(1,2,3,4,5,6)


# # <파이썬 모듈>
# 1. 파이썬 모듈
# 2. 사용자 정의 모듈

# ## 1. 파이썬 모듈
# ---
# - 기본모듈
# - 사용자정의 모듈
# - 3rd party 모듈

# In[85]:


get_ipython().system('pip list')


# In[86]:


help('matplotlib')


# In[87]:


import os #지금 현재 디렉토리 반환
os.getcwd()


# In[88]:


import numpy as np
np.absolute(-3)


# In[89]:


np.sqrt(16) #제곱근


# ### 모듈 import
# - import [모듈명] as [Alias명]  #Alias = 줄임말 변수이름
# - from [패키지명] import[모듈명]
# - from [모듈명] import [클래스명|함수명]

# In[90]:


from scipy import stats
stats.hmean([1,2,3])


# In[91]:


from datetime import datetime
now= datetime.now()
now


# In[92]:


now.month


# In[93]:


now.day


# In[94]:


import sys
sys.path


# # <파이썬 파일 입출력>
# 1. 파일 입력
# 2. 파일 출력
# 3. 파일 시스템

# ## 파일 읽기
# 1. 파일 객체 생성
# - `파일객체= open(파일경로/파일명, 모드)`
# 2. 파일 읽기(라인단위)
# - `for 변수 in 파일객체`
# 3. 파일객체 닫기
# - `파일객체.close()`

# In[98]:


fr= open('myprint.txt./Documents/Python,'r')


# In[ ]:




