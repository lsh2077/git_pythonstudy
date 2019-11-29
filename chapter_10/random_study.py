import random

print(random.random())
print(random.randrange(0,11,2))#1~10 짝수
print(random.randrange(1,101,2))#1~100 홀수


dic1 =random.randint(1,6)
dic2 =random.randint(1,6)

print('주사위 두개의 숫자 : {0},{1}'.format (dic1,dic2))


menu = [ '비빔','된장','볶음','불고','스파','피자','탕수']
print(random.choice(menu))


print((random.sample([1,2,3,4,5],2)))