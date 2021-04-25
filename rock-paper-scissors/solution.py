matrix = {
  'R':{
    'R':'tie',
    'P':'lose',
    'S':'win'
  },
  'P':{
    'R':'win',
    'P':'tie',
    'S':'lose'
  },
  'S':{
    'R':'lose',
    'P':'win',
    'S':'tie'
  }
}

def play(p1, p2):
  print("PLAYER 1 " + matrix[p1][p2])

play('R', 'P')