print('***Simple Calculater***')
print('For addition press 1\n')
print('For Subtraction press 2\n')
print('For Multiplication press 3\n')
print('For Division press 4\n')
print('For Module press 5\n')
print('For Exponential press 6\n')
a=int(input('Enter the operation Number\n'))
print('Please enter the number you want to do the operation with\n')
b=int(input())
c=int(input())
if(a==1):
    print('Addition of the',b,'and',c,'is',b+c)
elif(a==2):
    print('Subtraction of the',b,'and',c,'is',b-c)
elif(a==3):
    print('Multiplication of the',b,'and',c,'is',b*c)
elif(a==4):
    print('Division of the',b,'and',c,'is',b/c)
elif(a==5):
    print('Module of the',b,'and',c,'is',b%c)
elif(a==6):
    print('Exponential of the',b,'and',c,'is',b**c)
else:
    print('Please enter the correct option')
    exit()