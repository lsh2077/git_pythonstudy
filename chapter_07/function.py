#(1,리스트 전달 2 투플 3dictionary)
line_cut="************************************"
def my_student_info_list(list):
    global line_cut
    for i in range(len(list)):
        print(line_cut)
        print("* 학생이름: {}\n* 학급번호: {}\n* 전화번호: {}".format(list[i][0],list[i][1],list[i][2]))
    print(line_cut)

def my_student_info_tuple(tuple):
    global line_cut
    for i in range(len(tuple)):
        print(line_cut)
        print("* 학생이름: {}\n* 학급번호: {}\n* 전화번호: {}".format(tuple[i][0], tuple[i][1], tuple[i][2]))
    print(line_cut)



def my_student_info_dictionary(dictionary):
    global  line_cut
    for i in dictionary.keys():
        print(line_cut)
        print("* 번호: {}".format(i))
        for a,b in dictionary[i].items():
            print("* {} : {}".format(a,b))
    print(line_cut)





if __name__=="__main__":
    std_list =[["현아","01","01-235-6789"],["진수","02","01-987-6543"]]
    my_student_info_list(std_list)
    std_tuple=(("현아","01","01-235-6789"),("진수","02","01-987-6543"))
    my_student_info_tuple(std_tuple)
    std_dictionary={"01":{"학생이름":"현아","학급번호":"01","전화번호":"01-235-6789"},
                    "02":{"학생이름":"진수","학급번호":"02","전화번호":"01-987-6543"}}
    my_student_info_dictionary(std_dictionary)






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


"""
