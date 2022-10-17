from datetime import datetime, timedelta
from suncalc import get_position, get_times
import pandas as pd
import numpy as np

def datetime_range(start, stop, delta):
  curr = start
  while curr < stop:
    yield curr
    curr += delta

azirange = (np.radians(61.8), np.radians(24.2))

lat = 33.770284 
lon = -84.393383

# start = datetime(2022, 8, 14)
start = datetime.now()
# stop = datetime(2023, 8, 14)
stop = datetime(2022, 8, 15)
timestep = timedelta(minutes=30)

dates = [d for d in datetime_range(start, stop, timestep)]

timesDF = pd.DataFrame({
  'date': dates,
  'lon': [lon] * len(dates),
  'lat': [lat] * len(dates)
})

positions = pd.DataFrame(get_position(timesDF['date'], timesDF['lon'], timesDF['lat']))
AZI = positions['azimuth']
ALT = positions['altitude']

# X = np.cos(AZI)
# Y = np.sin(AZI)
# Z = np.sin(ALT)
X = np.degrees(AZI)
Y = np.degrees(ALT)
Z = np.arange(0, len(AZI), 1)

# print(positions)
for i in range(len(AZI)):
  print(dates[i], np.degrees(AZI[i]), np.degrees(ALT[i]))
print(f'azimuth ranges: {np.degrees(AZI.min()), np.degrees(AZI.max())}')
print(f'alt ranges: {np.degrees(ALT.min()), np.degrees(ALT.max())}')


print(len(X))
input('display graph?:')
import matplotlib.pyplot as plt
# plt.scatter(AZI, ALT, cmap='gray')

ax = plt.axes(projection='3d')
ax.scatter3D(X, Y, Z)
# ax.scatter3D(X, Y, Z+len(AZI)*2, color='green')

plt.show()
