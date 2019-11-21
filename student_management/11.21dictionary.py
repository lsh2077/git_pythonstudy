"""
list,tuple,dictionry,set 에서 하나를 선택하여 아래 프로그램을 작성하시오.
-->dictionary, 하나
student_management 패키지 추가
학생 정보는 : 학생번호, 학생명, 국어, 영어, 수학 ,총점 ,평균
1 학생목록 2학생추가 3학생 수정 4학생 삭제 5 종료 메뉴추가
2 프로그램 수행시 먼저 student_list.txt 리스트 파일을 읽어와 수행
3각각 메뉴별 수행되도록 작성
4종료시 학생 목록이 studen_list.txt에 저장

5. 프린터하여 출
#split() --()공간으로 쪼개

"""
save_dict={}
def first_act():
    global save_dict
    try:
        f=open("student_list.txt","r")
        line = f.readline()
        while line:
            line_list = line.split()
            upload_dict={line_list[0]:{"학생이름":line_list[1],"국어점수":line_list[2],"수학점수":line_list[3],"영어점수":line_list[4]}}
            save_dict.update(upload_dict)
            line = f.readline()
    except FileNotFoundError as e:
        print("해당파일이 존재하지않음", e,sep='\n')
    finally:
        f.close()


def switch():
    while 1:
        a = input("--------menu--------\n 1.학생 목록\n 2.학생 추가\n 3.학생 수정\n 4.학생 삭제\n 5.종료\n*수행작업을 선택해주세요:")
        if a == "1":
            student_list()
            continue
        elif a == "2":
            student_add()
            student_edit_list1()
            continue
        elif a == "3":
            student_edit()
            continue
        elif a == "4":
            student_delete()
            student_edit_list1()
            continue
        elif a == "5":
            exit_save()
            return
        else: continue

def student_list():
    global save_dict
    for i in save_dict.keys():
        print("{}".format(i),end=' ')
        sumscore=int(save_dict[i]["국어점수"])+int(save_dict[i]["수학점수"])+int(save_dict[i]["영어점수"])
        averagescore = sumscore / 3
        for a, b in save_dict[i].items():
            print("{} : {}".format(a, b),end=' ')
        print("총점: {} 평균: {:.1f}".format(sumscore,averagescore))


def student_edit_list1():
    global save_dict
    for i in save_dict.keys():
        print("{}".format(i), end=' ')
        for a, b in save_dict[i].items():
            print("{} : {}".format(a, b), end=' ')
        print()
def student_edit_list2(i):
    print("선택된학생:\n{}".format(i), end=' ')
    for a, b in save_dict[i].items():
        print("{} : {}".format(a, b), end=' ')
    print()

def student_add():
    global save_dict

    while 1:
        sign = 0
        no=input("입력할 학생번호?(종료:0):")
        for i in save_dict.keys():
            if no==i :
                print("중복하는사람이있습니다 다시 입력해주세요")
                sign = 1
        if sign == 0: break
        if no == '0': return

    name=input("입력할 학생이름?(종료:0):")
    if name == '0': return
    kor=input("입력할 국어점수?(종료:0):")
    if kor == '0': return
    math=input("입력할 수학점수?(종료:0):")
    if math == '0': return
    eng=input("입력할 영어점수?(종료:0):")
    if eng == '0': return
    upload_dict = {no: {"학생이름": name, "국어점수": kor, "수학점수": math, "영어점수": eng}}
    save_dict.update(upload_dict)


def student_edit():
    global save_dict
    student_edit_list1()

    while 1:
        sign = 0
        no=input("수정할 학생번호?(종료:0):")
        for i in save_dict.keys():
            if no==i :
                area=i
                sign = 1
        if sign == 1: break
        print("존재하지않는 번호입니다.")
        if no=='0' : return

    while 1:
        student_edit_list2(area)
        a=input("--------edit--------\n 1.이름\n 2.국어점수\n 3.수학점수\n 4.영어점수\n 5.다른학생선택\n 6.종료\n*수행작업을 선택해주세요:")
        if a == "1":
            name = input("수정할 학생이름?(종료:0):")
            if name == '0': return
            save_dict[area]["학생이름"]=name
            continue
        elif a == "2":
            kor = input("입력할 국어점수?(종료:0):")
            if kor == '0': return
            save_dict[area]["국어점수"] = kor
            continue
        elif a == "3":
            math = input("입력할 수학점수?(종료:0):")
            if math == '0': return
            save_dict[area]["수학점수"] = math
            continue
        elif a == "4":
            eng = input("입력할 영어점수?(종료:0):")
            if eng == '0': return
            save_dict[area]["영어점"] = eng
            continue
        elif a == "5":
            student_edit()
            return
        elif a == "6":
            return
        else: continue




def student_delete():
    global save_dict
    student_edit_list1()
    while 1:
        sign = 0
        no = input("수정할 학생번호?(종료:0):")
        for i in save_dict.keys():
            if no == i:
                area = i
                sign = 1
        if sign == 1: break
        print("존재하지않는 번호입니다.")
        if no == '0': return
    del save_dict[area]

def exit_save():
    global save_dict
    try:
        f = open("student_list.txt", "w")
        for i in save_dict.keys():
            f.write(i+' ')
            for a,b in save_dict[i].items():
                f.write(' '+save_dict[i][a])

    except FileNotFoundError as e:
        print("해당파일이 존재하지않음", e, sep='\n')
    finally:
        f.close()



if __name__=="__main__":

    first_act()
    switch()


