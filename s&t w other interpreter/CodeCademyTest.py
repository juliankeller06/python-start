# Define your functions
def coffe_bot():
  print("Welcome to the cafe!")
  size = get_size()

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'

# Call coffee_bot()!
coffe_bot()