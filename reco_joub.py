import pandas as pd
import sys

sim = pd.read_csv('sim.csv')
data = pd.read_csv('data_final.csv')

ind = list(data.titles).index(str(sys.argv[1]))
res = list(sim.loc[ind].sort_values(ascending=True).index[1:10])

print(' ')
print(30*'-','Incoming',30*'-')
print(' ')
print('Our recommendation for Bibou for',str(sys.argv[1]))
print(' ')
for r in res:
    print('                 ',list(data.titles)[int(r)],' (',list(data.Director)[int(r)],list(data.Year)[int(r)],')')
