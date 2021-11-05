import plotly.express as px
import csv

rows = []

with open("final.csv", 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]

star_masses = []
star_radii = []
star_gravity = []
star_names = []

for star_data in star_data_rows:
    if star_data[3] == '?' or star_data[4] == '?' or star_data[5] == '?':
        star_data_rows.remove(star_data)
    else:
        star_names.append(star_data[1])
        star_masses.append(float(star_data[3]))
        star_radii.append(float(star_data[4]))
        star_gravity.append(float(star_data[5]))

fig = px.scatter(x = star_masses, y = star_radii, size = star_gravity, range_y=(-2e+8,3e+9), range_x=(-1e+31,2.1e+32), labels=dict(x='Mass of Star', y='Radius of Star'))
fig.show()