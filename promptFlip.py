from close import close
from spacer import spacer

def promptFlip(flips):
    spacer()
    choice = 0

    while True:
        try:
            choice = int(input("[1] Flip it\n[2] Leave it alone\n"))

            break;
        except:
            spacer()
            print("The choice you have entered is invalid.")
            print("Enter either 1 or 2 for your choice.")
            choice = int(input("[1] Flip it\n[2] Leave it alone\n"))

    if choice == 1:
        flips += 1
        return flips
    elif choice == 2:
        close(flips)
    else:
        print("You've encountered an error that should not happen.")
        print("Good job, bud.")
        close(-1)
