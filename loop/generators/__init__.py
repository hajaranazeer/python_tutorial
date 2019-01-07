def returnsq(*n_list):
    for each in n_list:
        yield each*each#return returns just a no

for item in returnsq(2,5,4,3):
    print(item)