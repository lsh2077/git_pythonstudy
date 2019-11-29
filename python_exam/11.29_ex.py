from chapter_04.bubblesort import bubble_sort
import  operator
import  numpy as np

def load_data():
    with open("Gettysburg_Address.txt") as f:
        out_line=f.readline()
        data=[]
        in_line = f.readline()
        while in_line:
            data_line= in_line.split()
            for i in range(len(data_line)):
                data.append(data_line[i])
            in_line = f.readline()
    data=[strip.strip(',.-') for strip in data]

    all_dict={}
    set_data=set(data)
    for i in set_data:
        data_cnt=data.count(i)
        if data_cnt > 2:
            dict_save={i:data_cnt}
            all_dict.update(dict_save)

    rank_data = sorted(all_dict.items(),
                      key=operator.itemgetter(1),
                      reverse=True)
    for i in range(len(rank_data)):
        print("{}위  {}의 갯수 : {}".format(i+1,rank_data[i][0],rank_data[i][1]))


def lamda_ex(x,y,str):
    if str =='+':
        a=lambda x, y: x + y
        print("{}{}{}={}".format(x,str,y,a(x, y)))
    elif str == '-':
        a = lambda x, y: x - y
        print("{}{}{}={}".format(x,str,y,a(x, y)))
    elif str == '/':
        a = lambda x, y: x / y
        print("{}{}{}={}".format(x,str,y,a(x, y)))
    elif str == '*':
        a = lambda x, y: x * y
        print("{}{}{}={}".format(x,str,y,a(x, y)))
    elif str == '**':
        a = lambda x, y: x**y
        print("{}{}{}={}".format(x,str,y,a(x, y)))


def woodman():
    cnt=1
    while 1 :
        print("나무꾼이 나무를 {}번찍었습니다".format(cnt))
        cnt=cnt+1
        if cnt >10:
            print("나무가 넘어갑니다")
            break

def array_nife(arr,commands):
    for i in range(len(commands)):
        nife_arr=arr[(commands[i][0]-1):(commands[i][1])]
        nife_list=list(nife_arr)
        sort_nife_list=bubble_sort(nife_list)
        point_list=sort_nife_list[(commands[i][2]-1)]
        print("{}를 {}번째부터 {}쨰까지 자른 후 정렬합니다. {}의 {}째 숫자를 {}입니다.".format(
            arr,commands[i][0],commands[i][1],sort_nife_list,commands[i][2],point_list
        ))


if __name__=="__main__":

    print("1번")
    load_data()

    print("2번")
    lamda_ex(2, 3,'+')
    lamda_ex(2, 3, '-')
    lamda_ex(2, 3, '*')
    lamda_ex(2, 3, '/')
    lamda_ex(2, 3, '**')

    print("3번")
    woodman()

    print("4번")
    arr_list=[1,5,2,6,3,7,4]
    arr=np.array(arr_list)
    commands=[[2,5,3],[4,4,1],[1,7,3]]
    array_nife(arr,commands)



