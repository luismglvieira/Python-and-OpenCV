# -*- coding: utf-8 -*-

num = 1
sum = 0

while num != 0:
    num = float(input("Enter a number to sum. Press zero to finish. "))
    sum1 = sum + num;
    print(sum,"+",num,"=",sum1)
    sum = sum1

print("Finished sum.")

ii = int(input("Enter the number of times to loop: "))
i = 0
while i < ii:
    print("i =",i)
    i+=1 # i = i + 1
    
print("Finished the loop",i, "times.")
