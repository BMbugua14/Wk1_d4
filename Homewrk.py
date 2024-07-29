#Task1
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#Answer1
for day in range(len(days_of_week)):
    if day % 2 == 0:
        print(days_of_week[day])
#Task2
#Answer1
while True:
    person = input("who made Chrome Heart?")
    if person == "Richard Stark":
        print("I forgot his name")
        break
#Answer2
shots = []
while len(shots) < 5:
    print("I'd like a shot of Patron")
    shots.append("Down the hatch")
    print("Im on drink #", len(shots), "im feeling good")
    

print(shots)
#Extra credit
import random
potion = ["HP", "XP", "AP", "Crit boost", "Def boost"]
selected_item = random.choice(potion)
print("You've made it to the boss lobby!")
print("Which potion will help defeat the floor boss?", potion)
while True:
    guess = input("Guess which potion is the best:")
    if guess == selected_item:
        print("Correct!! You may advance.")
        break
    else:
        print("Sorry, that's not correct. Try again.")
