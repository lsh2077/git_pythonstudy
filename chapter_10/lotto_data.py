from chapter_04.bubblesort import bubble_sort
import  operator

file_path = "lotto_번호통계.csv"

def lotte_date():
    with open(file_path, 'r') as f:
        head = f.readline()
        all_list=[]
        line = f.readline()
        while line:
            num_list = line.split(',')
            for i in num_list:
                all_list.append(int(i))
            line = f.readline()
    return all_list


def printdict(all_list):
    all_dict={}
    for i in range(1,46):
        print("{}의 갯수:{}".format(i,all_list.count(i)))
        dict_info={i:all_list.count(i)}
        all_dict.update(dict_info)
    return all_dict

def num_rank(all_dict):
    #dict_all=sorted(all_dict.items())#딕셔너리를 리스트구조로 변경

    dict_all=sorted(all_dict.items(),
                    key=operator.itemgetter(1),
                    reverse= True) #리스트로 변환하면서 내림정렬로 정렬

    for i in range(len(dict_all)):
        print("{}위\n{}의 갯수 : {}".format(i+1,dict_all[i][0],dict_all[i][1]))



if __name__=="__main__":
    all_list=lotte_date()
    bubble_sort(all_list)
    all_dict=printdict(all_list)
    num_rank(all_dict)