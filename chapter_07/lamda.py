res= (lambda x:x**2)(3)
print(res)


mysquare = lambda x:x**2

print((mysquare(9)))

scores=[90,80,95,85]
score_sum=0
subject_num=0
for score in scores:
    score_sum=score_sum+score
    subject_num=subject_num+1

average =score_sum/subject_num

print("총점:%d, 평균:%d"%(score_sum,average))


list1 = [1,2,3,4,5]
e=lambda x:x**2
for i in list1:
    print(e(i),end=' ')

print()
[print (i**2,end= ' ') for i in list1]
print("---------------------------------")
for i in list1:
    if i%2==1:
        print(e(i),end=' ')
print()
[print (i**2,end= ' ') for i in list1 if i%2==1]

