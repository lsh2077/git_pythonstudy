for i in [0,1,2,3,4,5]:
    print(i,end='  ')
print()
for i in range(1,10):
    print(i,end='  ')
print()
for i in range(0,10,2):
    print(i,end='  ')

print()
print("{}{}".format(range(0,10),list(range(0,10))))

x_list=['x1','x2']
y_list=['y1','y2']
print()
for x in x_list:
    for y in y_list:
        print(x,y)


print()
#gugudan
def gugu(dan):
    for i in range(1,10):
        print("{}x{}={:2}".format(dan,i,dan*i))


gugu(2)


def gugudan():
    for i in range(1,10):
        print()
        for j in range(2, 10):
            print("{}x{}={:2}".format(j,i,j*i),end='\t')


gugudan() #전체 구구단

#gugudan_land()