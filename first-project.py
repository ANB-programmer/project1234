import random 

n = random.randint(1,99)

hads = int(input("enter your number: "))


while n != "hads":
    if hads > n:
        print("kamtare")
        hads = int(input("enter your number: "))
    elif hads < n:
        print("bishtare")
        hads = int(input("enter your number: "))
    else:
        print("doroste")
        break

print("wwwwwwwwwwiiiiiiiiiiiinnnnnnnnn")