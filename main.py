import numpy as np
import pandas as pd

from arch import ar
import ao_core as ao

from read import movies_array
from read import genre_map
from read import user_preference
from read import get_genre_binary

agent = ao.Agent(ar, notes="Default Agent")

for object in user_preference:
    genre = object['genre']
    INPUT = get_genre_binary(genre)['binary']
    LABEL = 1 if object['givenRating'] > 2 else 0

    agent.reset_state()

    

