n = 20
for i in range(1,n + 1):
    string = " "
    for j in range(1,11):
        string = string + (str(i*j))+" "
    print(string)


n = 6
for i in range(0,n):
    for j in range(0,i):
        print("* ",end="")
    print("\r")


n = 6
for i in range(0,n):
    print(" "*(n-i),end=" ")
    print("* "*i)


n = 6
for i in range(0,n):
    print(" "*(n - i),end=" ")
    print("* "*i)



r = 6
for i in range(r+1,1,-1):
    for j in range(0,i-1):
        print("* ", end=" ")
    print("  ")


r = 5
k = 2 * r-2
for i in range(r,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k = k + 1
    for j in range(0,i + 1):
        print("*",end=" ")
    print(" ")


a = 1
end = 2
n = 10
for k in range(n):
    for i in range(1,end):
        print(a,end=" ")
        a+=1
    print(" ")
    end+=1
