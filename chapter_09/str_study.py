def string_split():
    coffee_menu="에소 아메 카라 카푸"
    print(type(coffee_menu.split()))
    coffee_list= coffee_menu.split()
    [print (coffee) for coffee in coffee_list]
    print()
    coffee_menu2="에소,아메,카라,카푸"
    [print(coffee) for coffee in coffee_menu2.split(',')]
    print()
    coffee_menu3="에소\n아메\n카라\n카푸"
    [print(coffee) for coffee in coffee_menu3.split()]
    print()
    [print(coffee) for coffee in coffee_menu2.split(',',2)]


def string_strip():
    test_str="aaabbbcccdddeeepython"
    print("{}\n{}\n{}\n{}".format(test_str.strip('a'),test_str.strip('ab'),test_str.strip('abc')
                                  ,test_str.strip('abcd'),test_str.strip('abcde')))

    # print(test_str.strip('a','b'))안됨







if __name__=="__main__":
    string_split()
    string_strip()