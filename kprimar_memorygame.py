import platform
import os

operatingSystem = platform.system()

print("Helloooo! Welcome to the game hakujin!")
input("Please remember these delicious japanese foods: mochi, ramen, sushi, takoyaki.\nPress Enter to continue.")

if operatingSystem == "Windows":
    os.system("cls")
else:
    os.system("clear")

answer = input("Which food started with M? \n")
if answer.lower() == 'mochi':
    input("That shit's delicous")
else:
    input("idiot...")
    
    