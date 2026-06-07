print("Welcome to treassure island")
direction=input("left or right")
if direction == "right":
    print("game over")
elif direction == "left":
    boat=input("came across river swim or wait")
    if boat == "swim":
        print("game over")
    elif boat == "wait":
        colour=input("red, blue, yellow")
        if colour == "blue" or colour == "red":
            print("game over")
        elif colour == "yellow":
            print("you win")
