import requests

class NutritionixAPI:
  def __init__(self,food):
    self.food=food
    self.api_url = 'http://www.nutritionix.com/api'

  def get(self):
    response = requests.get(self.api_url).json()
    result = response['main']
    if response.get('main'):
      return result
    else:
      return None
  def __str__(self):
    resultStr = f"{self.get()}"
    return resultStr