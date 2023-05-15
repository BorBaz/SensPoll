import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

pokedex = pd.read_csv(r'../data/Pokedex_Ver_SV2.csv')

# Peso de los pokemon

pokemon_weight = pokedex.filter(items=['Name', 'Weight'])
pokemon_weight_paginated = pokemon_weight[0:4]
x = pokemon_weight_paginated['Name']
y = pokemon_weight_paginated['Weight']

# ----- sin subplots
# plt.plot(pokemon_weight_paginated['Name'], pokemon_weight_paginated['Weight'])
# plt.title('Cuan gordo es segun que pokemon')
# plt.xlabel('Nombre del animal')
# plt.ylabel('Obesidad')
# plt.tight_layout()
# plt.show()

# ----- con subplots
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

# Numero de pokemon por cada tipo
pokemon_per_type = pokedex.filter(items=['Type1'])
fig, ax = plt.subplots(figsize=(20, 10))
ax.hist(pokemon_per_type, bins=2)
plt.show()
