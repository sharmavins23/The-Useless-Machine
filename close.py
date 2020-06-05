import sys
from spacer import spacer

def close(flips):
    spacer()
    print("You have decided to leave the box alone for now.")
    spacer()

    if flips == 0:
        print("It's not a good idea to press random things, anyways.")
        print("You keep your head down and move on your way.")
    elif flips == 1:
        print("Who even creates a switch that turns itself off?")
        print("You figure either someone masochistic or crazy would.")
        print("What a waste of time.")
    elif flips == 2:
        print("If the box wants the switch closed THAT much, then fine.")
        print("What a waste of time.")
    elif 3 <= flips <= 5:
        print("The box has insulted you personally now.")
        print("You feel an emptiness. Today, the box has won.")
    elif flips == 6:
        print("You've had enough.")
        print("The box is now moving at inhuman speeds.")
        print("The arm has won... But it was never much of a competition.")
    elif flips == 7:
        print("It's all too much to handle. You don't even remember turning it off.")
        print("Defeated, you leave.")
        print("The arm hasn't just won... You have completely lost.")
    elif flips == 8:
        print("You've taught the arm a lesson.")
        print("That's the last time it messes with you.")
        print("Have you won? No. But the arm hasn't either.")
    elif 9 <= flips <= 15:
        print("You give up. This arm won't learn.")
        print("You hope that the arm at least has some respect for you.")
    elif flips == 16:
        print("You realize you've wasted your time. Nothing you can do will win.")
        print("You've lost not only your time but your dignity as well. The arm won.")
    elif 17 <= flips <= 21:
        print("The alarms are too annoying for you to handle.")
        print("Your ears are still ringing.")
        print("The box has won.")
    elif flips == 22:
        print("You feel you've been a bit too harsh to the arm.")
        print("Out of pity, you leave it alone.")
        print("It can have its switch off for today.")
    elif flips == 23:
        print("You have won.")
    else:
        print("The box disappears, as if fleeing in fear.")
        print("You sit there, looking at your computer, having broken several laws of physics.")
        print("Disappointed, you close the game and go to bed.")
    
    sys.exit(0)
