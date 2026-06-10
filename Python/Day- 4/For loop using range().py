for game in range(1,101):
    if game % 3==0:
        print("Fizz")
    elif game % 5==0:
        print("Buzz")
    elif game % 3==0 and game % 5==0:
        print("FizzBuzz")
    else:
        print(game)
