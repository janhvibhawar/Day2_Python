n = int(input("Enter a number:"))

reverseNum = 0 

while n!=0:
   lastdigit = n%10
   reverseNum = reverseNum * 10 + lastdigit
   n = n//10

print(reverseNum)
