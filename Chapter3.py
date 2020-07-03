money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")




money = True

if money:
    
    print("택시를")

    print("타고")

    print("가라")





money = 2000

card = True

if money >= 3000 or card:

    print("택시를 타고 가라")

else:

    print("걸어가라")






'a' in ('a', 'b', 'c')

'j' not in 'python'


pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:

    print("택시를 타고 가라")

else:

    print("걸어가라")






pocket = ['paper', 'money', 'cellphone']

if 'money' in pocket:

    pass

else:

    print("카드를 꺼내라")







score = 30
message = "success" if score >= 60 else "failure"








treeHit = 0

while treeHit < 10:

    treeHit = treeHit +1

    print("나무를 %d번 찍었습니다." % treeHit)

    if treeHit == 10:

        print("나무 넘어갑니다.")







prompt = """

1. Add
2. Del
3. List
4. Quit

Enter number: """




number = 0
while number != 4:
    print(prompt)
    number = int(input())



coffee = 10

money = 300

while money:

    print("돈을 받았으니 커피를 줍니다.")

    coffee = coffee -1

    print("남은 커피의 양은 %d개입니다." % coffee)

    if coffee == 0:

        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")

        break






a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a, end='')





while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")






test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)






a = [(1,2), (3,4), (5,6)]

for (first, last) in a:

    print(first + last) 






marks = [90, 25, 67, 45, 80]

number = 0

for mark in marks:

    number = number +1

    if mark >= 60:

        print("%d번 학생은 합격입니다." % number)

    else:

        print("%d번 학생은 불합격입니다." % number)








marks = [90, 25, 67, 45, 80]

number = 0

for mark in marks:

    number = number +1

    if mark < 60:

        continue

    print("%d번 학생 축하합니다. 합격입니다." % number)







a = range(10)
a

add = 0

for i in range(1, 11):

    add = add + i

print(add)


add = 0

for i in range(1, 11):

    add += i

print(add)





for i in range(2,10):

    for j in range(1, 10):

        print(i, "x", j, "=", i*j, end=" ")

    print('')






a = [1,2,3,4]

result = []

for num in a:

    result.append(num*3)

print(result)





a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)





for i in range(1, 101):

    print(i, end=' ')



result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)



i = 0

while True:
    i += 1
    if i > 5: break
    print("*" * i)



A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in A:
    total += score
    
average = total / len(A)
print(average)



