#  Simple "99 bottles of beer on the wall" program using while loop and if statement.
x = 99   

while x > 1:

    print(x, "bottles of beer on the wall,", x,"bottles of beer,")
    x -= 1
    print("take one down, pass it around,", x, "bottles of beer on the wall.")
    
    print("")

if x == 1:
    print(x, "bottle of beer on the wall,", x, "bottle of beer,")
    print("take it down, pass it around, no more bottles of beer on the wall.")
    print(" ")
    print("No more bottles of beer on the wall, no more bottles of beer..")
