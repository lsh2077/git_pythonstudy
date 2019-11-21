#전역변수 선언
line_cut="-------------------------------------------------------------------------------"


#쓰기
def file_write(str):
    try:
        f=open(str,"w")
        for num in range(1,6):
            gugutwo="2 x {} = {}\n".format(num,num*2)
            f.write(gugutwo)
    except FileNotFoundError as e:
        print("파일없음",e,sep='\t')
    finally:
        f.close()

#readline
def file_readline(str):
    global line_cut
    try:
        print(line_cut)
        f = open(str, "r") #== 'f=open(str)'
        line=f.readline()
        num=1
        while line:
            print("{}번째라인 {}".format(num,line),end='')
            line = f.readline()
            num+=1
    except FileNotFoundError as e:
        print("파일없음", e, sep='\t')
    finally:
        print(line_cut,"\n")
        f.close()

#readlines
def file_readlines(str):
    global line_cut
    try:
        print(line_cut)
        f = open(str) #== 'f=open(str,"r")'
        lines=f.readlines()
        num = 1
        for line in lines:
            print("{}번째라인 {}".format(num,line),end='')
            num += 1
    except FileNotFoundError as e:
        print("파일없음", e, sep='\t')
    finally:
        print(line_cut,"\n")
        f.close()

#바로 f포문
def file_readprint(str):
    global line_cut
    try:
        print(line_cut)
        f = open(str) #== 'f=open(str,"r")'
        num=1
        for line in f.readlines():
            print("{}번째라인 {}".format(num,line),end='')
            num += 1
    except FileNotFoundError as e:
        print("파일없음", e, sep='\t')
    finally:
        print(line_cut,"\n")
        f.close()


if __name__=="__main__":
    str_file_name="two_times_table.txt"
    file_write(str_file_name)
    print("readline")
    file_readline(str_file_name)
    print("readlines")
    file_readlines(str_file_name)
    print("readlinesprint")
    file_readprint(str_file_name)