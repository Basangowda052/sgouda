#Write a python program to get 3 subject marks out of that find average of two biggest marks
a=int(input("Enter 1st marks:"))
b=int(input("Enter 2nd marks:"))
c=int(input("Enter 3rd marks:"))
if(a>=b and a>=c):
    if(b>=c):
        print("M1 and M2 are greater")
        print("The average of this number is:",(a+b)/2)
    else:
        print("M1 and M3 are greater")
        print("The average of this number is:",(a+c)/2)
    
elif(b>=a and b>=c):
    if(a>=c):
        print("M1 and M2 are greater")
        print("The average of this number is:",(a+b)/2)
    else:
        print("M2 and M3 are greater")
        print("The average of this number is:",(b+c)/2)
else:        
    if(a>=b):
        print("M1 and M3 are greater")
        print("The average of this number is:",(a+c)/2)
    else:
        print("M2 and M3 are greater")
        print("The average of this number is:",(b+c)/2)
