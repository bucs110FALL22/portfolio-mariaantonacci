import requests

Class SpoonacularAPI():
  def __init__(self):
  self.api_url = https://spoonacular.com/food-api 

  def get(self):
    self.output1 = requests.get(self.url).json()
    print(self.output1)