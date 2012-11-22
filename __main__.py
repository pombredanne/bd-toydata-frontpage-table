import bitdeli
from bitdeli.widgets import Map, set_theme

set_theme('eighties')

for profile in bitdeli.profiles():
    pass

Map(size=(12, 7), data={'IN': 30})
