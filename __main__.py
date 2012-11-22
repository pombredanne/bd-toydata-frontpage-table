import bitdeli
import random
from bitdeli.widgets import Bar, Table, set_theme
from bitdeli.textutil import COUNTRIES

set_theme('builder')

ITEMS = ['Memento Mori', 'Funky Stars', 'Knuckle Busters', 'Mosaic Days',
         'Sidology Episode 1', 'Desert Dream', 'Starshine', 'Marmelade',
         'Turrican Medley', 'Electric City']


random.seed(1)

def bar_data():
    for i, month in enumerate(['%.2d/11' % m for m in range(1, 13)] +
                              ['%.2d/12' % m for m in range(1, 7)]):
        yield month, 100 + abs(i - 6) * 25 + random.randint(1, 50)

def table_data():
    for i, item in enumerate(ITEMS):
        x= 1.0 - (i * 0.05 + random.random() * 0.1)
        yield {'Entry': item,
               'Score ': int(x * 1000),
               'Rank': i + 1,
               'Weight': x}
        
for profile in bitdeli.profiles():
    pass

Bar(label='Voting Activity',
    size=(12, 3),
    color=3,
    data=list(bar_data()))

Table(label='Top Entries',
      size=(12, 6),
      color=2,
      data=list(table_data()),
      chart={'Weight': 'bar'})
