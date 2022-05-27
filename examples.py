fruits={"ORANGE","mangoes","apples"}
print(fruits)
print(fruits)
print(fruits)
#function to replace charsacteers in strings
def replace_in (phrase) :
  word =" "
  for letters in phrase :
      if letters . lower ()in "aeiou" :
          words = words + "g"
      else :
         word = word + letters
  return word
print(replace_in(input("Enter a phrase :")))