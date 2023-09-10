import os
from dotenv import load_dotenv
import csv
import googlemaps

load_dotenv("secrets.env")
gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY"))

# Get latitude and longitude for the adress
def get_coords(adress):
    # Check if it's already in the csv
    try:
        with open("locations.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                fadress, location = row
                if fadress == adress:
                    return eval(location)
    except FileNotFoundError:
        pass

    # Otherwise check in Google's Geocode API
    try:
        location = gmaps.geocode({adress})[0]["geometry"]["location"]
    except IndexError:
        return False

    # If the location exist, add it to csv for later reuse
    with open("locations.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([adress, location])

    # Return latiutude and longitude as a dict
    return location
