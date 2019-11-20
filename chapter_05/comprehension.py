#square = [i**2 for i in range(1,6)]
#print(square)

#print([i**2 for i in range(1,6) if i >= 3])


def bsearch(list,search):
    start=0
    end=len(list)-1#4
    print(list)
    while(start <= end):
        mid = (start+end)//2
        print("[{}]".format(list[mid]))
        if list[mid] >search:
            end=mid
            print([list[i] for i in range(start,end)])

        elif list[mid] < search:
            start=mid
            print([list[i] for i in range(start, end)])

        else:
            return print("위치{},값{}".format(mid,list[mid]))


if __name__=="__main__":
    list1=[1,2,3,4,5,6,7,8,9,10,11]
    #print("{}||{}".format(list1,len(list1)))
    bsearch(list1,2)



