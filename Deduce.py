import geocoder
import math
import pandas as pd
import csv

g = geocoder.ip('me')
latitude, longitude = g.latlng
#print(latitude,longitude)


# Function to calculate the distance between two points using Haversine formula
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance



# Dataset containing location data (replace with your dataset)
# dataset = pd.read_csv('Station.csv',delimiter=",")
#print(dataset.columns)
threshold_distance = 10000 # Adjust as needed
dataset_file = 'Station.csv'
# Shortlist locations that are within the threshold distance
shortlisted_locations = []
with open(dataset_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header row if present
    for row in csv_reader:
        Location_Name,Latitude, Longitude = row[0], float(row[1]), float(row[2])
        distance = haversine_distance(latitude, longitude, Latitude, Longitude)
        if distance <= threshold_distance:
            shortlisted_locations.append((Location_Name, Latitude, Longitude))
#print(shortlisted_locations)
# # Print or process the shortlisted locations
# for location in shortlisted_locations:
#     Location_Name,Latitude, Longitude = location
#     print(f"Location '{Location_Name}' is within {threshold_distance} km from your live location.")
html_content = "<html><body><h1>Shortlisted Locations</h1><ul>"
for location_name in shortlisted_locations[:]:
    html_content += f"<li>{location_name}</li>"
html_content += "</ul></body></html>"

# Write the HTML content to a file
with open('shortlisted_locations.html', 'w') as html_file:
    html_file.write(html_content)

print("HTML file 'shortlisted_locations.html' has been created.")

