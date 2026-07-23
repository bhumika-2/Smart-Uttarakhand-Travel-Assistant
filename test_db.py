from database import fetch_all

places = fetch_all("SELECT * FROM destinations")

print("Total destinations:", len(places))

for place in places[:5]:
    print(place["name"])