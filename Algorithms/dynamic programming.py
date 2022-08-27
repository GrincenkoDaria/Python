if word_a[i] == word_b[j]:
  cell[i][j]
else:
  cell[i][j] = 0
  
  
  
if word_a[i] == word_b[j]:
  cell[i][j] = cell[i-1][j-1] + 1
else: 
  cell[i][j] = max(cel[i - 1][j], cell[i][j-1])