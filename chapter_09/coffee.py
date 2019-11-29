file_path = "coffeeShopSales.txt"
all_dict={}
with open(file_path, 'r') as f:
    head = f.readline()
    head_list = head.split()
    coffee_sales1 = 0
    coffee_sales2 = 0
    coffee_sales3 = 0
    count =0
    for line in f:
        coffee_sales = line.split()
        dict_info={coffee_sales[0]:{head_list[1]:coffee_sales[1],
                   head_list[2]:coffee_sales[2], head_list[3]:coffee_sales[3]}}
        coffee_sales1 = coffee_sales1+int(coffee_sales[1])
        coffee_sales2 = coffee_sales2+int(coffee_sales[2])
        coffee_sales3 = coffee_sales3+int(coffee_sales[3])
        all_dict.update(dict_info)
        count= count+1
    dict_info={"총량":{head_list[1]:coffee_sales1,
                   head_list[2]:coffee_sales2, head_list[3]:coffee_sales3},
               "일평균":{head_list[1]:coffee_sales1/count,
                   head_list[2]:coffee_sales2/count, head_list[3]:coffee_sales3/count}}
    all_dict.update(dict_info)


for i in all_dict.keys():
    print("{}-->".format(i),end=' ')
    for a,b in all_dict[i].items():
        print("{}:{}".format(a,b),end=' ')
    print()
