import random as rnd


def bubble_sort(random_list):
    print(random_list)

if __name__=="__main__":
    random_list = []
    rnd.seed(1)
    for num in range(0,10):
        random_list.append(rnd.randint(1,46))
    print(random_list)

    sorted_list= bubble_sort(random_list)
    print("정령된 리스트 {}".format(sorted_list))