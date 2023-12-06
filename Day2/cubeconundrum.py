import os

file_name = 'games.txt'

max_vals = {
  'red': 12,
  'green': 13,
  'blue': 14
}

running_sum = 0

with open(file_name) as file:
  for line in file:
    print(line)
    line = line.strip()
    game, data = line.split(':')
    game = int(game[5:])
    # parse line by breaking it up by the semicolons
    # parse showings by breaking up , 
    # get the max of each 
    showings = data.split(';')
    # print(game)
    # print(showings)
    max_showings = {
      'red': [],
      'green': [],
      'blue': [],
    }


    for showing in showings:
      colors = showing.split(',')
      # print(colors)
      for color in colors:
        if color.endswith(' red'):
          max_showings['red'].append(int(color[:-4]))
        if color.endswith(' green'):
          max_showings['green'].append(int(color[:-6]))
        if color.endswith(' blue'):
          max_showings['blue'].append(int(color[:-5]))

    # is_possible = True

    product = 1
    
    for color in max_showings.keys():
      # print(f'{color}: {max(max_showings[color])}')
      # print(f'{color}_max: {max_vals[color]}')
      # print(max(max_showings[color]) > max_vals[color])
      # if max(max_showings[color]) > max_vals[color]:
      #   is_possible = False
      product *=max( max_showings[color])

    # if is_possible:
    #   running_sum += game
    running_sum += product
    
print(running_sum)
        

