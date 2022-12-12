import requests

class SpoonacularAPI():
  def __init__(self):
    self.api_url = 'https://spoonacular.com/food-api' 

  def get(self):
     response = requests.get(self.api_url).json()
     result = response['text']
     if response.get('text'):
       return result
     else:
       return None

  def __str__(self):
     resultStr = f"{self.get()}"
     return resultStr