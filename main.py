from promptFlip import promptFlip
from close import close
from spacer import spacer

def flip(flips):
    print("There is a box with a switch in front of you.")
    print("The switch is toggled to the OFF position.")
    spacer()
    
    print("Do you flip it?")
    flips = promptFlip(flips)
    spacer()
    
    if flips == 1:
        print("You flip the switch.")
        print("The box lid lifts up to reveal a mechanical arm.")
        print("The arm seems... irritated.")
        print("It flips the switch back to the OFF position before retracting.")        
    elif flips == 2:
        print("Indignantly, you flip the switch again.")
        print("The arm flings out, faster, and more jittery this time.")
        print("It flips the switch back to the OFF position and retracts again.")
    elif 3 <= flips <= 5:
        print("You decide to flip the switch with a little more speed.")
        print("The arm flings out, even faster than before, and flips the switch off.")
        print("It then contorts into an obscenity before recessing back into the box.")
    elif flips == 6:
        print("You flip the switch again, with a little more speed.")
        print("The arm flings out at light speed.")
        print("You didn't notice when the switch turned off... But now, it's off.")
    elif flips == 7:
        print("You flip the switch again, a little harder.")
        print("This box has nothing on you.")
        print("The arm stalls. It doesn't flip the switch back.")
        print("No, the arm didn't flip the switch back.")
        print("YOU flipped the switch back. Without realizing.")
    elif flips == 8:
        print("You decide to flip the switch properly this time.")
        print("Verifying that the switch was flipped forwards, you poise yourself.")
        print("Without missing a beat, the arm extends from the box.")
        print("You push the arm down, pinning it to the box.")
        print("The arm looks longingly at the switch.")
        print("The arm then jiggles free, and makes a break for the switch. It flips it off.")
    elif flips == 9:
        print("You flip the switch again.")
        print("The arm, now slowed down to normal speed, flips it back, before retracting.")
    elif 10 <= flips <= 15:
        print("You flip the switch.")
        print("The arm flips it back.")
    elif flips == 16:
        print("Enraged, you take a hammer and smash the switch.")
        print("The switch is now permanently in the ON position.")
        print("The arm brings out a screwdriver and detaches the old switch.")
        print("It then replaces the old switch with a new switch, in the OFF position.")
        print("The new switch looks more mechanized than others, almost military-grade.")
    elif 17 <= flips <= 21:
        print("You flip the switch. Alarms around the room sound.")
        print("The arm comes out and flips the switch again. The alarms turn off.")
    elif flips == 22:
        print("That's enough. These alarms are annoying.")
        print("You flip the switch, and ready your hammer one last time.")
        print("When the arm comes out, you hit the arm with all your might.")
        print("In its dying attempts, it flicks the switch back one last time.")
    elif flips == 23:
        print("You flip the switch once more.")
        print("... Silence.")
        print("No alarms, no arm.")
        close(flips)
    else:
        pass

    flip(flips)

# Initial amount of flips
flips = 0

# Start game
flip(flips)
