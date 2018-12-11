def gameboard():
     size = int(input("Enter the size: "))
     design1 = ' ---'
     design2 = '|   '
     for i in range(1, size+1):
         print(design1 * size)
         print(design2 * (size+1))
     print(design1 * size)
     return gameboard

print(gameboard())


