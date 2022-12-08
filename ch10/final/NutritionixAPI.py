import requests

Class NutritionixAPI():
  def __init__(self):
  self.api_url = http://www.nutritionix.com/api

  def get(self):
    self.output1 = requests.get(self.url).json()
    print(self.output1)