#로또번호생성기를 작성하고 당첨 번호에 따라 순위를 구하는 프로그램

import random as rnd
from chapter_04.bubblesort import bubble_sort



def lotto_generator():
    lotto_num = set()
    while len(lotto_num)<6:
        lotto_num.add(rnd.randint(1,46))
    return lotto_num



if __name__=="__main__":
    rnd.seed(1)
    set_lotto= list(lotto_generator())
    print("로또 번호: {}".format(bubble_sort(set_lotto))) #정렬된 결과
