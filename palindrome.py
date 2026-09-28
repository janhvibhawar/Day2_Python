num = int(input("Enter a number:"))

rev = 0

dup = num

while(dup>0):
    lastdigit = dup % 10
    rev = rev * 10 + lastdigit
    dup = dup //10

if(rev==num):
    print("Is Palindrome")
else:
    print("Is not palindrome")