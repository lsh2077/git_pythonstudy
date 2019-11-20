def dict_app():
    fruit_code={"사과":101,"배":102,"딸기":103,"포도":104,"바나나":105}
    print("fruit_code.keys-\n{}".format(fruit_code.keys()))
    print("fruit_code.values\n{}".format(fruit_code.values()))
    print("fruit_code.items\n{}".format(fruit_code.items()))
    print("list(fruit_code.keys)\n{}".format(list(fruit_code.keys())))
    print("lsit(fruit_code.values)\n{}".format(list(fruit_code.values())))
    print("lsit(fruit_code.items)\n{}".format(list(fruit_code.items())))
    fruit_code2 ={"오렌지":106,"수박":107}
    fruit_code.update(fruit_code2)
    print("fruit_code.update\n{}".format(fruit_code))
    #print("fruit_code.update\n{}".format(fruit_code.update(fruit_code2)))   안
    print("fruit_code.clear\n{}".format(fruit_code.clear()))




if __name__=="__main__":
    country_name={"영국":"런던","프랑스":"파리","스위스":"베른","호주":"멜버른","덴마트":"코펜하겐"}
    print((country_name))
    print(type(country_name))
    print(country_name["프랑스"])
    print(country_name['프랑스'])

    list1 = ['a','b','c']
    tuple1 =(1,2,3,4)
    set1 = {'가','나'}
    data_dict = {"lst":list1,"tpl":tuple1, "set":set1}

    for key, value in data_dict.items():
        print("key {} -> {}".format(key,value))

    for key in data_dict.keys():
        print("key {} -> {}".format(key, data_dict[key]))


    country_name["독일"] = "베를린"
    print(country_name)
    country_name["호주"] ="켄버라"
    print(country_name)
    del country_name["호주"]
    print(country_name)




    dict_app()