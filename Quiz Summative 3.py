#Introduction To Game
print("""Welcome to Meredith's Basketball Quiz. This quiz will decide if you are a true baller.
We will ask you 15 different questions about the game, it's culture, and famous players
Lets see if you are a true Big Baller.""")
name = str(input("What is your name?"))
startgame = input("Are you ready to see if you are a true baller?.(yes/no)")
if startgame == "yes":
    print("Okay",name,"let's start the quiz")
elif startgame == "no":
    print("I guess you're too afraid")


else:
    print("That is not an option")

print(name+", please answer the 15 questions to the best of your ability. Pick the letter that corresponds to the answer. No cheating")

score=0
def quiz1():
    global score
    print("1. What is outdoor basketball called?")
    answer1 = input ("""
    a. outdoorball
    b. roadball
    c. courtball
    d. streetball""")
    if answer1 == "d":
        print("Correct")
        score = score + 1
    elif answer1 == "a" or answer1 == "b" or answer1 == "c":
        print("Incorrect, the name for outdoor basketball is called streetball")
    else:
        print("That is not an option. Please try again. ")
        quiz1()

quiz1()

def quiz2():
    global score
    print("2.What do you call someone who does such a good move that they make their defender trip, fall, or freeze")
    answer2 = input("""
    a.crossover
    b.hoodie melo
    c.ankle breaker
    d.jelly fam""")
    if answer2 == "c":
        print("Correct")
        score = score + 1
    elif answer2 == "a" and "b" and "d":
        print("Incorrect, the name for that person is ankle breaker")
    else:
        print("That is not an option. Please try again.")
        quiz2()

quiz2()

def quiz3():
    global score
    print("3.Who is the youngest player to score 10,000 points in the NBA")
    answer3 = input("""
    a.Lebron James
    b.Michael Jordan
    c.Steph Curry
    d.Larry Bird""")
    if answer3 == "a":
        print("Correct")
        score = score + 1
    elif answer3 == "b" and "c" and "d":
        print("Incorrect, it is Lebron James")
    else:
        print("That is not an option. Please try again.")
        quiz3()

quiz3()

def quiz4():
    global score
    print("4.What does BBB stand for?")
    answer4 = input("""
    a.Best Basketball Brand
    b.Boston Basket Bruins
    c.Big Baller Brand
    d.Bradley B. Brown""")
    if answer4 == "c":
        print("Correct")
        score = score + 1
    elif answer4 == "a" and "b" and "d":
        print("Incorrect, it stands for Big Baller Brand")
    else:
        print("That is not an option. Please try again.")
        quiz4()

quiz4()

def quiz5():
    global score
    print("5.What does 'and one' mean?")
    answer5 = input("""
    a.Add one point to the score board
    b.You made a shot and got fouled
    c.You have to run another sprint
    d.Someone fouled you""")
    if answer5 == "b":
        print("Correct")
        score = score + 1
    elif answer5 == "a" and "c" and "d":
        print("Incorrect, it means you made a shot and got fouled in the process.")
    else:
        print("That is not an option. Please try again.")
        quiz5()

quiz5()

def quiz6():
    global score
    print("6.How many seconds do you get to pass half court on offense?")
    answer6 = input("""
    a.10
    b.6
    c.8
    d.12""")
    if answer6 == "a":
        print("Correct")
        score = score + 1
    elif answer6 == "b" and "c" and "d":
        print("Incorrect, a get 10 seconds to cross half court.")
    else:
        print("That is not an option. Please try again.")
        quiz6()

quiz6()

def quiz7():
    global score
    print("7.What is Michael Jordan's jersey number?")
    answer7 = input("""
    a.10
    b.0
    c.24
    d.23""")
    if answer7 == "d":
        print("Correct")
        score = score + 1
    elif answer7 == "a" and "b" and "c":
        print("Incorrect, his number was 23.")
    else:
        print("That is not an option. Please try again.")
        quiz7()

quiz7()

def quiz8():
    global score
    print("8.Which team is know best for its team offense?")
    answer8 = input("""
    a.Golden State Warriors
    b.San Antonio Spurs
    c.Chicago Bulls
    d.Las Angeles Lakers""")
    if answer8 == "b":
        print("Correct")
        score = score + 1
    elif answer8 == "a" and "c" and "d":
        print("Incorrect, San Antonio Spurs are know for amazing team offense.")
    else:
        print("That is not an option. Please try again.")
        quiz8()

quiz8()

def quiz9():
    global score
    print("8.How high is the rim of the basketball basket")
    answer9 = input("""
    a.12 feet
    b.9 feet
    c.10 feet
    d.11 feet""")
    if answer9 == "c":
        print("Correct")
        score = score + 1
    elif answer9 == "a" and "b" and "c":
        print("Incorrect, San Antonio Spurs are know for amazing team offense.")
    else:
        print("That is not an option. Please try again.")
        quiz9()

quiz9()

def quiz10():
    global score
    print("10.Which slogan do ballers use most?")
    answer10 = input("""
    a.Spash Bro
    b.Bounce Back
    c.We're All The Way Up
    d.Ball Is Life""")
    if answer10 == "d":
        print("Correct")
        score = score + 1
    elif answer10 == "a" and "b" and "c":
        print("Incorrect, a true baller slogan is #BALLISLIFE.")
    else:
        print("That is not an option. Please try again.")
        quiz10()

quiz10()

def quiz11():
    global score
    print("11.What is the name for the NBA video game?")
    answer11 = input("""
    a.Madden NBA
    b.NBA2K
    c.NBA3K
    d.NBA 18""")
    if answer11 == "b":
        print("Correct")
        score = score + 1
    elif answer11 == "a" and "c" and "d":
        print("Incorrect, the NBA games are called NBA2K.")
    else:
        print("That is not an option. Please try again.")
        quiz11()

quiz11()

def quiz12():
    global score
    print("12.Who is Uncle Drew?")
    answer12 = input("""
    a.Kyrie Irving
    b.Issaiah Thomas
    c.Drew Gooden
    d.James Harden""")
    if answer12 == "a":
        print("Correct")
        score = score + 1
    elif answer12 == "b" and "c" and "d":
        print("Incorrect, Uncle Drew is Kyrie Irving.")
    else:
        print("That is not an option. Please try again.")
        quiz12()

quiz12()

def quiz13():
    global score
    print("13.What size ball do girls play with?")
    answer13 = input("""
    a.10
    b.7
    c.6
    d.12""")
    if answer13 == "c":
        print("Correct")
        score = score + 1
    elif answer13 == "b" and "a" and "d":
        print("Incorrect, girls play with a size 6 ball.")
    else:
        print("That is not an option. Please try again.")
        quiz13()

quiz13()


def quiz14():
    global score
    print("13.What does J's mean?")
    answer14 = input("""
    a.Jayhawks
    b.Name of NBA player
    c.Jordans
    d.Jaylen Hands""")
    if answer14 == "c":
        print("Correct")
        score = score + 1
    elif answer14 == "a" and "b" and "d":
        print("Incorrect, J's are a nickname for Jordan shoes.")
    else:
        print("That is not an option. Please try again.")
        quiz14()

quiz14()

def quiz15():
    global score
    print("15.What does G.O.A.T stand for and who is the G.O.A.T of the NBA?")
    answer15 = input("""
    a.Greatest Offense Of All Time; Michael Jordan
    b.Greats Of All Time; Magic Johnson
    c.A Type Of Sheep; Shawn the Sheep
    d.Greatest Of All Time; Lebron James""")
    if answer15 == "d":
        print("Correct")
        score = score + 1
    elif answer15 == "a" and "b" and "c":
        print("Incorrect, it stands for Greatest Of All Time and it is a tie between Lebron James and Michael Jordan.")
    else:
        print("That is not an option. Please try again.")
        quiz15()

quiz15()


def scoretotal():
    print("Yay, you have completed the quiz.")
    print("Your score is",score)
    if score >= 11:
        print("YOU ARE A BALLER")
    elif score <= 11:
        print("You are not a baller at all")

scoretotal()
