print('Hello World!!')
a = 10
b = 20
print(a + b)

print(a * b)

print(a/b)

score=[80, 90, 100]
print(score[1])

print(len(score))

fruit=['apple','banana','strawberry','grape']
print(fruit[1])
print(len(fruit))
print(fruit[-1])
print(fruit[1:3])
print(fruit[0:2])

fruit.insert(1,'watermelon')
print(fruit)

fruit.append('orange')
print(fruit)

vegetable=['carrot','toamto','onion']
vegetable.extend(fruit)
print(vegetable)

print(fruit+vegetable)

'''특정 값 삭제는 remove()
    특정 위치 삭제는 del
    리스트는 남겨두지만 아이템 모두 삭제는 clear()'''

print(fruit)
fruit.remove('watermelon')
print(fruit)

del fruit[1]
print(fruit)

vegetable.clear()
print(vegetable)

vegetable.insert(0,'obj')
print(vegetable)
vegetable.append('mola')
vegetable.extend(fruit)
print(vegetable)

vegetable.sort()
print(vegetable)

# 2. 튜플: 소괄호()안에 여러개의 아이템을 콤마로 연결하여 만든 자료형, 아이템 선택하여 변경, 추가, 삭제 불가능

fruit_tuple=('apple','banana','strawberry')
print(fruit_tuple)
#fruit_tuple.insert(1,'c')   아이텀 추가 삭제 수정 불가능

fruit_tuple=list(fruit_tuple)
print(fruit_tuple)
fruit_tuple.append('a')
fruit_tuple= tuple(fruit_tuple)
print(fruit_tuple)

# 3. 세트: 중괄호 {} 순서x, 변경 추가 가능
fruit_set={'apple','banana','strawberry'}
fruit_set.add('d')
print(fruit_set)
print(fruit_set)

vegetable_set={'a','b','c'}
vegetable_set.update(fruit_set)
print(vegetable_set)

# 4. 딕셔너리: 중괄호{}, 여러개의 키(key), 값(value) 쌍을 가지는 아이템을 콤마로 연결하여 만든 자료형
my_dic={
    'name':'jaeyeong',
    'age':26,
    'height':174,
    'weight':72
}

print(my_dic)
print(my_dic.keys())
print(my_dic.values())

my_dic['age']=20
print(my_dic)

my_dic.update({'height':190})
print(my_dic)
my_dic['height']=200
print(my_dic)
my_dic.update({'name':'yeong'})
print(my_dic)
my_dic['name']='jang'
print(my_dic)

my_dic.popitem()
print(my_dic)

my_dic.pop('age')
print(my_dic)

my_dic.clear()
print(my_dic)


