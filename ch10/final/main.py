import NutritionixAPI
import SpoonacularAPI

def main():
  output1=NutritionixAPI.NutritionixAPI()
  output1=get()

  output2=SpoonacularAPI.SpoonacularAPI()
  output2=get()

main()
