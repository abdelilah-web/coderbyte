#Longest Word
def LongestWord(sen):
  word = ""
  for i in sen:
    if i.isalpha() or i.isnumeric():
      word += i
    else :
      word += " "

  return max(word.split(), key=len)

print(LongestWord(input()))


#First Factorial
def FirstFactorial(num):
  total = 1
  while num >1 :
    total = num * total
    num -= 1
  
  return total

print(FirstFactorial(input()))


#First Reverse
def FirstReverse(strParam):

  reverse = ""
  n = -1
  for letter in range(len(strParam)):
    reverse += strParam[n] 
    n -= 1

  return reverse

print(FirstReverse(input()))
