from NutritionixAPI import NutritionixAPI
from SpoonacularAPI import SpoonacularAPI

def controller():
  userInput = input("Enter a food:")

  nutrition=NutritionixAPI(userInput)
  value=str(nutrition)
  food=SpoonacularAPI()

  if value>=50:
    print(f"Your food {userInput} is high in nutrition")
  if value<=50:
    print(f"Your food {userInput} is low in nutrition")

  if food=