fruits = ["apples","oranges","bananas"]
fruits.append("cherry")
print(fruits)
fruits.remove("cherry")
print(fruits)
my_fruits = fruits.pop(1)
print(fruits)
print(my_fruits)
fruits =["apples","oranges","bana"]#lists
fruits_2=["cherry","toms"]
fruits_3=fruits + fruits_2
print(fruits_3)
fruits.extend(fruits_2)
print(fruits)
fruits_2.clear()
print(fruits_2)
fruits_4 = ("apples","orange","something")#tupples
print(fruits_4)
print(fruits_4[1])
new_list= list(fruits_4)
new_list.append("tomatoes")
fruits_4=tuple(new_list)
ftuits_4 =("apple","orange","oranges","oranges")
fruits_5 ={"apples","oranges","oranges","oranges"}#sets
print(fruits_5)
