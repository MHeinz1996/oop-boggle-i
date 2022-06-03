from random import randrange, shuffle, sample

class BoggleBoard:
  
  def __init__(self):
    self.board = f"""
    ____
    ____
    ____
    ____

    """
  
  def shake(self) -> str:
    alphabet = ('AAEEGN', 'ELRTTY', 'AOOTTW', 'ABBJOO', 'EHRTVW', 'CIMOTU', 'DISTTY', 'EIOSST', 'DELRVY', 'ACHOPS', 'HIMNQU', 'EEINSU', 'EEGHNW', 'AFFKPS', 'HLNNRZ', 'DEILRX')
    rolls = []
    grid = []
    for i in range(16):
      rolls.append(randrange(1,6))
    
    for i in range(0, len(rolls)):
      for j in range(0, len(alphabet)):
        if i == j:
          if(alphabet[j][rolls[i]] == 'Q'):
            grid.append('Qu')
          else:
            grid.append(alphabet[j][rolls[i]]+' ')

    grid = sample(grid, len(grid))

    self.board = f"""
    {grid[0]} {grid[1]} {grid[2]} {grid[3]}
    {grid[4]} {grid[5]} {grid[6]} {grid[7]}
    {grid[8]} {grid[9]} {grid[10]} {grid[11]}
    {grid[12]} {grid[13]} {grid[14]} {grid[15]}
    """

    return self.board

boggle = BoggleBoard()
print(boggle.shake())