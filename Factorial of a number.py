i=1
while i==1:
    a=int(input("ENTER THE NUMBER FOR WHICH YOU WANT FACTORIAL: "))
    if a<0:
        print("FACTORIAL NOT POSSIBLE")
    elif a==0:
        print("FACTORIAL IS: 1")
    else:
        f=1
        while a>1:
            f*=a
            a-=1
        print("FACTORIAL IS: {}".format(f))
    i = int(input("IF U WANT TO CONTINUE PRESS 1 ELSE PRESS ANY KEY: "))
