for i in range(2, 6):
    print(i, i * i)


print("new for: ")
for x in range(2,11,2):
    print(x,x*2)

numberOfRows = int(input("Enter a number from 1 through 20: "))
for i in range(numberOfRows):
    for j in range(i + 1):
        print("*", end="")
    print()



