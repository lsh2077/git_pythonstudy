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
save_dict = {}

# 파일에서 딕셔너리로 읽어오기
def first_act():
    global save_dict
    try:
        f = open("student_list.txt", "r")
        line = f.readline()
        while line:
            line_list = line.split()
            upload_dict = {
                line_list[0]: {"학생이름": line_list[1], "국어점수": line_list[2], "수학점수": line_list[3], "영어점수": line_list[4]}}
            save_dict.update(upload_dict)
            line = f.readline()
    except FileNotFoundError as e:
        print("해당파일이 존재하지않음", e, sep='\n')
    finally:
        f.close()

# IF문으로 스위치문 구현 메뉴 선택
def switch():
    while 1:
        a = input("--------menu--------\n 1.학생 목록\n 2.학생 추가\n 3.학생 수정\n 4.학생 삭제\n 5.종료\n*수행작업을 선택해주세요:")
        if a == "1":
            student_list()
            continue
        elif a == "2":
            student_add1()
            continue
        elif a == "3":
            student_edit1()
            continue
        elif a == "4":
            student_delete1()
            student_edit_list1()
            continue
        elif a == "5":
            exit_save()
            return
        else:
            continue

# 총점 평균을 포함한 출력
def student_list():
    global save_dict
    for i in save_dict.keys():
        print("{:>2}".format(i), end=' ')
        sumscore = int(save_dict[i]["국어점수"]) + int(save_dict[i]["수학점수"]) + int(save_dict[i]["영어점수"])
        averagescore = sumscore / 3
        for a, b in save_dict[i].items():
            print("  {}:{:6}".format(a, b), end=' ')
        print("총점:{}  평균:{:.1f}".format(sumscore, averagescore))

#총점 평균을 포함하지 않은 출력
def student_edit_list1():
    global save_dict
    for i in save_dict.keys():
        print("{:>2}".format(i), end=' ')
        for a, b in save_dict[i].items():
            print("  {}:{:6}".format(a, b), end=' ')
        print()

#선택 영역리스트 출력
def student_edit_list2(i):
    print("선택된학생: {}".format(i), end=' ')
    for a, b in save_dict[i].items():
        print("  {}:{:6}".format(a, b), end=' ')
    print()

#중복 검출
def duplication(value):
    global save_dict
    while 1:
        for i in save_dict.keys():
            if value == i:
                return i
        return -1

#ADD 검색
def student_add1():
    while 1:
        no = input("입력할 학생번호?(종료:z):")
        if no == 'z' or no == 'Z': return
        sign = int(duplication(no))
        if sign >= 0:
            print("중복하는사람이있습니다 다시 입력해주세요")
        else:
            student_add2(no)
            break

#ADD 실행
def student_add2(sign):
    global save_dict
    name = input("입력할 학생이름?(종료:z):")
    if name == 'z' or name == 'Z': return
    kor = input("입력할 국어점수?(종료:z):")
    if kor == 'z' or kor == 'Z': return
    math = input("입력할 수학점수?(종료:z):")
    if math == 'z' or math == 'Z': return
    eng = input("입력할 영어점수?(종료:z):")
    if eng == 'z' or eng == 'Z': return
    upload_dict = {sign: {"학생이름": name, "국어점수": kor, "수학점수": math, "영어점수": eng}}
    save_dict.update(upload_dict)
    student_edit_list1()

#EDIT 검색
def student_edit1():
    while 1:
        student_edit_list1()
        no = input("수정할 학생번호?(종료:z):")
        if no == 'z' or no=='Z': return
        sign = int(duplication(no))
        if sign < 0:
            print("존재하지않는 번호입니다.")
        else:
            student_edit2(no)
            break

#EDIT 실행
def student_edit2(sign):
    global save_dict
    while 1:
        student_edit_list2(sign)
        a = input("--------edit--------\n 1.이름\n 2.국어점수\n 3.수학점수\n 4.영어점수\n 5.다른학생선택\n 6.종료\n*수행작업을 선택해주세요:")
        if a == "1":
            name = input("수정할 학생이름?(종료:z):")
            if name == 'z' or name == 'Z' : return
            save_dict[sign]["학생이름"] = name
            continue
        elif a == "2":
            kor = input("입력할 국어점수?(종료:z):")
            if kor == 'z' or kor=='Z': return
            save_dict[sign]["국어점수"] = kor
            continue
        elif a == "3":
            math = input("입력할 수학점수?(종료:z):")
            if math == 'z' or math =='Z': return
            save_dict[sign]["수학점수"] = math
            continue
        elif a == "4":
            eng = input("입력할 영어점수?(종료:z):")
            if eng == 'z' or eng == 'Z': return
            save_dict[sign]["영어점"] = eng
            continue
        elif a == "5":
            student_edit1()
            return
        elif a == "6":
            return
        else:
            continue

#DELETE 검색
def student_delete1():
    while 1:
        student_edit_list1()
        no = input("삭제할 학생번호?(종료:0):")
        if no == '0': return
        sign = int(duplication(no))
        if sign < 0:
            print("존재하지않는 번호입니다.")
        else:
            student_delete2(no)
            break

#DELETE 실행
def student_delete2(sign):
    global save_dict
    del save_dict[sign]

#저장 후 종료
def exit_save():
    global save_dict
    try:
        f = open("student_list.txt", "w")
        for i in save_dict.keys():
            f.write(i + ' ')
            for a, b in save_dict[i].items():
                f.write(' ' + save_dict[i][a])
            f.write('\n')
    except FileNotFoundError as e:
        print("해당파일이 존재하지않음", e, sep='\n')
    finally:
        f.close()

#메인
if __name__ == "__main__":
    first_act()
    switch()
