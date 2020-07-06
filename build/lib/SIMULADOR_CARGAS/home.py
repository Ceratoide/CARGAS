from pathlib import Path
import os 
from os.path import join
home = str(Path.home())
try:
    os.mkdir(join(home,'SIMULADOR_CARGAS'))
except FileExistsError:
    pass
print(join(home,'SIMULADOR_CARGAS','electron.png'))
