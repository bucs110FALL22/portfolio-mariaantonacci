def multiply(num):
  result=0
  for i in range(num):
    result=result + num
  return result
def main():
  res=multiply(0)
  print(res)
  res=multiply(10)
  print(res)
main()

def exponent(num,exp):
  result=0
  for i in range(exp):
    result=result + num
  return result
def main():
  res=exponent(3,5)
  print(res)
main()