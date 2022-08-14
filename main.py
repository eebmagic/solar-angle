from datetime import datetime, timedelta
from suncalc import get_position, get_times
import pandas as pd
import numpy as np

def datetime_range(start, stop, delta):
  curr = start
  while curr < stop:
    yield curr
    curr += delta

lat = 33.770284 
lon = -84.393383

start = datetime(2022, 8, 14)
stop = datetime(2023, 8, 14)
# timestep = timedelta(minutes=5)
timestep = timedelta(hours=3)

dates = [d for d in datetime_range(start, stop, timestep)]

timesDF = pd.DataFrame({
  'date': dates,
  'lon': [lon] * len(dates),
  'lat': [lat] * len(dates)
})

positions = pd.DataFrame(get_position(timesDF['date'], timesDF['lon'], timesDF['lat']))
azmin, azmax = positions['azimuth'].min(), positions['azimuth'].max()
almin, almax = positions['altitude'].min(), positions['altitude'].max()

print(positions)
print(f'azimuth ranges: {np.degrees(azmin), np.degrees(azmax)}')
print(f'alt ranges: {np.degrees(almin), np.degrees(almax)}')

