#dictionaries in python
mydict={
"Book" : "Dynamics",
"publisher" : "longhorn",
"year" : "2001"
}
#accesing item 
x=mydict["year"]
print(x)
#Accesing using get()
y=mydict["year"]
print(y)
#All keys
x=mydict.keys()
print()
#All values
x=mydict.values()
print(x)
#printing all items in a dictionary
x=mydict . items()
print(x)
#checking if keys Exist
if "publisher"in mydict :
    print("publisher is one of the keys")
print(len(mydict))
#dictionaries can hold different data types