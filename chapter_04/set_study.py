#로또번호생성기를 작성하고 당첨 번호에 따라 순위를 구하는 프로그램

import random as rnd
from chapter_04.bubblesort import bubble_sort

def lotto_bubble_sort(random_list):
    for i in range(len(random_list)-2):
        for j in range(len(random_list)-2-i):
           if random_list[j] > random_list[j+1]:
                temp=random_list[j+1]
                random_list[j+1]=random_list[j]
                random_list[j]=temp
    return random_list

def lotto_generator():
    lotto_num = set()
    while len(lotto_num)<6:
        lotto_num.add(rnd.randint(1,46))
    return lotto_num

def lotto_winning():
    #rnd.seed(1)
    lotto_winning_num = set()
    while len(lotto_winning_num) < 7:
        lotto_winning_num.add(rnd.randint(1, 46))
    lotto_winning_num=lotto_bubble_sort(list(lotto_winning_num))
    return lotto_winning_num

def lotto_grade(list1,list2):
    count1=0
    count2=0
    for i in range(0,6):
        count1 += list1.count(list2[i])
    count2 +=list1.count(list2[6])
    if count1==6: print("1등")
    elif count1==5 and count2==1: print("2등")
    elif count1==5:print("3등")
    elif count1==5: print("4등")
    elif count1==4: print("5등")
    else: print("꽝")


if __name__=="__main__":
    #rnd.seed(1)
    set_lotto=[]
    for i in range(0,5):
        set_lotto.append(list(lotto_generator()))
        print("로또번호{}".format(bubble_sort(set_lotto[i]),end='\t'))
    winning_lotto=lotto_winning()
    print("당첨자 번호{}".format([winning_lotto[i] for i in range(0,6)]),end='   ')
    print("보너스 번호:{}".format(winning_lotto[6]))
    for i in range(0,5):
        print("로또번호{}".format(bubble_sort(set_lotto[i]),end='\t'))
        lotto_grade(set_lotto[i],winning_lotto)

