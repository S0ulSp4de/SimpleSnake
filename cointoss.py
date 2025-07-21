from random import randint

guess = ""
randomnumber = 0

def cointoss():
    global randomnumber
    randomnumber = randint(0, 1)
    if randomnumber == 0:
        return "H"
    else:
        return "N"

while guess != "quit":
    guess = input("Bitte geben sie Head (H,h) oder Number (N,n) ein: ")
    if guess.lower() in ["h", "n"]:
        if cointoss() == guess.upper():
            print("Sie haben korrekt geraten!")
        else:
            print("Ihr Versuch war falsch.")
    elif guess == "quit":
        print("Spiel beendet.")
    else:
        print("Ungültige Eingabe. Bitte geben Sie H, N oder quit ein.")