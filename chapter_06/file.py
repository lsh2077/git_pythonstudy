try:
    f =open("/home/soso/PycharmProjects/git_pythonstudy_clone/chapter_06/print.py",'r')
    print(f)
    data =f.read()
    print(data)

except  FileNotFoundError as e:
    print("해당파일이 존재하지않음", e,sep='\n')
finally:
    f.close()



try:
    f = open("/home/soso/PycharmProjects/git_pythonstudy_clone/chapter_06/test.txt",'x')
    f.write(data)
except  FileNotFoundError as e:
    f = open("/home/soso/PycharmProjects/git_pythonstudy_clone/chapter_06/test.txt",'w')
    f.write(data)
    print("해당파일이 존재하지않음", e,sep='\n')
finally:
    f.close()

#f=open("/home/soso/PycharmProjects/git_pythonstudy_clone/chapter_06/test.txt",'w')
#f.write("해당파일이존재하지않음")
#f.write(data)
#f.close()

print("f")