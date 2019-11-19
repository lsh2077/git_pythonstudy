def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

if __name__=="__main__":
    print("{}{}".format("hello python","hi pycharm"))

    x=10
    y=5
    res=add(x,y)
    print("add({},{})={} \n".format(x,y,add(x,y)))
    print("mul({},{})={} \n".format(x, y, mul(x, y)))
    print("div({},{})={} \n".format(x, y, div(x, y)))