import time
from itertools import cycle
luzes = [
  ('Verde', 2),
  ('Amarelo', 1),
  ('Vermelho', 2)
 ]
cores = cycle(luzes)

while True:
    cor,tempo = next(cores)
    print(cor)
    time.sleep(tempo)