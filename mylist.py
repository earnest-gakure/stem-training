my_list=[1,2,3,5,6,7,8,9,11]
for elem in my_list:
     print(elem)
other_list = []
my_list = [2,4,1,7,8,10,12]
for elem in my_list:
    other_list.append(elem)
print(other_list)
#comments
my_lists=[2,4,1,7,8,10,12]
other_list=[elem for elem in my_list]
print(other_list)
for elem in my_list:
    if elem %2 ==0:
        other_list.append(elem)
print(other_list)
my_list =[2,4,1,7,8,10,12]
other_list = [elem for elem in my_list if elem %2 == 0]
print(other_list)
#creating a function
def add(a,b):
     return a+b
result = add(4,6)
print(result)
result_2 = add(8,6)
print(result_2) 