print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""" )
door = input("> ")
if door == "1":
    print("there's is a giant bear here eating a cheese cake.")
    print("what do you do?")
    print("1.take the cake.")
    print("2.scream at the bear.")
    bear = input("> ")
    if bear == "1":
        print("the bear eats your face off. good job!")
    elif bear == "2":
        print("the bear eats your legs off. good job!")
    else:
        print(f"well, doing {bear} is probably better.")
        print("bear runs away.")
elif door == "2":
    print("you stare into the endless abyss at cthulhu's retina.")
    print("1. blueberries \n 2. yellow jacket clothespins \n 3. understanding revolvers yelling melodies.")
    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("your body survives powered by a mind of jello.")
        print("good job!")
    else:
        print("the insanity rots your eyes into a pool of muck")
        print("good job!")
else:
    print("you stumble around and fall on a knife and die . good job!")
    