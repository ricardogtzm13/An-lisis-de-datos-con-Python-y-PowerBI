import pandas as pd

diccionario = {1: 'A', 9: 'B', 7: 'D', 2: 'C', 4: 'G', 8: 'I',
6: 'E', 7: 'H', 3: 'F', 10: 'J', 12: 'X'}
series = pd.Series(diccionario)
series[14] = 'W'
series[18] = 'Y'
series[10] = 'N'
print ("Diccionario: \n%s" % series)