import random as rnd


def bubble_sort(random_list):
    for i in range(len(random_list)-1):
        for j in range(len(random_list)-1-i):
           if random_list[j] > random_list[j+1]:
                temp=random_list[j+1]
                random_list[j+1]=random_list[j]
                random_list[j]=temp
    return random_list






if __name__=="__main__":
    random_list = []
    #rnd.seed(1)
    for num in range(0,10):
        random_list.append(rnd.randint(1,46))
    print("랜덤생성{}".format(random_list))

    sorted_list= bubble_sort(random_list)
    print("정령된 리스트 {}".format(sorted_list))