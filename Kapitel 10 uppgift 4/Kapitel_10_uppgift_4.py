
def maximum(a,b,c):
    if a>b and a>c:
        print("Storsta tal: ",a)
    if b>a and b>c:
        print("Storsta tal: ",b)
    if c>a and c>b:
        print("Storsta tal: ",c)


tal1=int(input("Tal 1: "))
tal2=int(input("Tal 2: "))
tal3=int(input("Tal 3: "))
maximum(tal1,tal2,tal3)

