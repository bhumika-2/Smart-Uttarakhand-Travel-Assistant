import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# DESTINATIONS DATA (from your file)
destinations_data = [
     (1, "Mussoorie", "Hill Station", "Dehradun", "Uttarakhand",
     "Mar-Jun, Sep-Nov", "2000-4000", "Easy", "Low", 3,
     "Sightseeing, Cable Car, Waterfalls",
     "Queen of Hills known for scenic viewpoints and pleasant weather."),

     (2, "Nainital", "Hill Station", "Nainital", "Uttarakhand",
     "Mar-Jun, Oct-Dec", "2500-4500", "Easy", "Low", 3,
     "Boating, Shopping, Ropeway",
     "Famous lake city surrounded by mountains."),

     (3, "Auli", "Hill Station", "Chamoli", "Uttarakhand",
      "Dec-Mar", "3000-6000", "Medium", "Medium", 4,
      "Skiing, Snow Trekking",
      "Popular skiing destination with Himalayan views."),

     (4, "Ranikhet", "Hill Station", "Almora", "Uttarakhand",
      "Mar-Jun, Sep-Nov", "1500-3000", "Easy", "Low", 2,
      "Nature Walks, Golf Course",
      "Peaceful hill station with forest landscapes."),

     (5,"Dhanaulti", "Hill Station", "Tehri Garhwal", "Uttarakhand",
      "Mar-Jun", "1500-2500", "Easy", "Low", 2,
      "Eco Parks, Camping",
      "Quiet hill retreat known for snowfall."),

     (6, "Kedarnath", "Religious Site", "Rudraprayag", "Uttarakhand",
      "May-Oct", "2500-5000", "Hard", "High", 4,
      "Temple Visit, Trekking",
      "Sacred Shiva temple among Char Dham pilgrimage."),

     (7, "Badrinath", "Religious Site", "Chamoli", "Uttarakhand",
      "May-Oct", "2000-4000", "Medium", "Medium", 3,
      "Temple Visit, Spiritual Tourism",
      "Important Vishnu temple in Himalayas."),

     (8, "Haridwar", "Religious Site", "Haridwar", "Uttarakhand",
      "Oct-Mar", "1500-3000", "Easy", "Low", 2,
      "Ganga Aarti, Temples",
      "Holy city on the banks of River Ganga."),

     (9, "Rishikesh", "Religious Site", "Dehradun", "Uttarakhand",
      "Sep-Apr", "2000-3500", "Easy", "Low", 3,
      "Yoga, Ashrams, Rafting",
      "World capital of yoga and spirituality."),

     (10, "Tapkeshwar Temple", "Religious Site", "Dehradun", "Uttarakhand",
      "Year-round", "1000-2000", "Easy", "Low", 1,
      "Temple Visit",
      "Cave temple dedicated to Lord Shiva."),

     (11, "Jim Corbett National Park", "Wildlife Park", "Nainital/Pauri", "Uttarakhand",
      "Nov-Jun", "3000-7000", "Easy", "Medium", 3,
      "Safari, Wildlife Photography",
      "India's oldest national park famous for tigers."),

     (12, "Rajaji National Park", "Wildlife Park", "Haridwar", "Uttarakhand",
      "Nov-Jun", "2500-5000", "Easy", "Medium", 2,
      "Jungle Safari, Bird Watching",
      "Forest reserve with elephants and wildlife."),

     (13, "Binsar Wildlife Sanctuary", "Wildlife Park", "Almora", "Uttarakhand",
      "Oct-Apr", "2000-4000", "Easy", "Low", 2,
      "Nature Trails, Bird Watching",
      "Dense forest sanctuary with Himalayan views."),
      
     (14, "Valley of Flowers", "Wildlife Park", "Chamoli", "Uttarakhand",
      "Jul-Sep", "2500-4500", "Medium", "Medium", 4,
      "Trekking, Photography",
      "UNESCO site with alpine flowers."),

     (15, "Askot Wildlife Sanctuary", "Wildlife Park", "Pithoragarh", "Uttarakhand",
      "Oct-Apr", "2000-3500", "Medium", "Medium", 3,
      "Wildlife Exploration",
      "Himalayan wildlife reserve with rare species."),

     (16, "Rishikesh River Rafting", "Adventure Spot", "Dehradun", "Uttarakhand",
      "Sep-Jun", "1500-3500", "Medium", "Medium", 2,
      "River Rafting",
      "Popular white-water rafting destination."),

     (17, "Bedni Bugyal Trek", "Adventure Spot", "Chamoli", "Uttarakhand",
      "May-Oct", "2500-5000", "Hard", "Medium", 5,
      "High Altitude Trekking",
      "Alpine meadow trek with stunning views."),

     (18, "Chopta Trek", "Adventure Spot", "Rudraprayag", "Uttarakhand",
      "Mar-May, Sep-Nov", "2000-3500", "Medium", "Low", 3,
      "Trekking, Camping",
      "Mini Switzerland of India and Tungnath base."),

     (19, "Kempty Falls", "Adventure Spot", "Tehri Garhwal", "Uttarakhand",
      "Mar-Jun", "1500-3000", "Easy", "Low", 1,
      "Waterfall Visit",
      "Popular tourist waterfall near Mussoorie."),

     (20, "Robber's Cave (Guchhupani)", "Adventure Spot", "Dehradun", "Uttarakhand",
      "Mar-Jun", "1000-2000", "Easy", "Low", 1,
      "Cave Exploration",
      "Natural river cave with flowing water stream."),

     (21, "Naini Lake", "Lake", "Nainital", "Uttarakhand",
      "Mar-Jun", "2000-4000", "Easy", "Low", 2,
      "Boating",
      "Freshwater lake at the center of Nainital."),

     (22, "Bhimtal Lake", "Lake", "Nainital", "Uttarakhand",
      "Mar-Jun", "1500-3000", "Easy", "Low", 2,
      "Boating, Island Visit",
      "Serene lake with island aquarium."),
      
     (23, "Naukuchiatal Lake", "Lake", "Nainital", "Uttarakhand",
      "Mar-Jun", "1500-3000", "Easy", "Low", 2,
      "Kayaking, Boating",
      "Nine-cornered deep lake surrounded by hills."),

     (24, "Tehri Lake", "Lake", "Tehri Garhwal", "Uttarakhand",
      "Oct-Jun", "2000-4000", "Easy", "Medium", 2,
      "Water Sports, Boating",
      "Large reservoir famous for adventure sports."),

     (25, "Sat Tal Lake", "Lake", "Nainital", "Uttarakhand",
      "Mar-Jun", "1500-3000", "Easy", "Low", 2,
      "Camping, Bird Watching",
      "Cluster of seven interconnected lakes."),


]

cursor.executemany("""
INSERT OR IGNORE INTO destinations
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", destinations_data)


# TREK SAMPLE DATA
trek_data = [
("Kedarkantha Trek","Garhwal","Uttarkashi",
"Moderate","12500 ft","7 Days",
"Dec-March","6k-10k",
"Govind Pashu Vihar Permit",
"Ability to jog 5km in 35-40 mins",
"Micro-spikes, Gaiters, Headlamp",
"PHC Mori / CHC Purola",
"Risk of hypothermia and black ice in winter."),

("Kalindi Khal Trek","Garhwal","Uttarkashi-Chamoli",
"Extreme","19521 ft","14-15 Days",
"June-Sept","95k-1L",
"Inner Line Permit (Forest Dept)",
"Run 10km under 55 mins + previous 5000m trek experience",
"Crampons, Ice Axe, Harness, Carabiners, Rope, Helmet",
"Military Hospital Harsil / MH Joshimath",
"High crevasse risk and extreme altitude sickness danger."),

("Auden Col Trek","Garhwal","Uttarkashi",
"Extreme","18011 ft","15-16 Days",
"June or Sept-Oct","85k-1L",
"Forest Dept + IMF Permit",
"Pro athlete level fitness, run 10km under 55 mins",
"Harness, Helmet, Rope, Ice Axe, Crampons",
"Military Hospital Harsil / Kedarnath Hospital",
"Hidden crevasses and steep ice slopes near the pass."),

("Bali Pass Trek","Garhwal","Uttarkashi",
"Difficult","16240 ft","8-9 Days",
"May-June or Sept-Oct","15k-22k",
"Govind Pashu Vihar Permit",
"Run 10km under 60 mins, strong endurance",
"Micro-spikes, Helmet, Trekking Poles",
"CHC Purola / PHC Mori",
"Steep 60° descent and strong ridge winds."),

("Rudranath Trek","Garhwal","Chamoli",
"Moderate","11811 ft","5-6 Days",
"May-June or Sept-Oct","7k-10k",
"Forest Permit",
"Ability to climb 1200m in a day",
"Grip Boots, Knee Caps, Rain Poncho",
"District Hospital Gopeshwar",
"Slippery trails and lightning-prone ridges."),

("Bedni Bugyal Trek","Garhwal","Chamoli",
"Easy-Moderate","11000 ft","4-5 Days",
"May-June or Sept-Oct","10k-13k",
"Forest Dept Permit",
"Walk 7-8km carrying 7kg backpack",
"Trekking Shoes, Poles, Windcheater",
"CHC Dewal / District Hospital Gopeshwar",
"Whiteouts and steep descent to Wan village."),

("Kedartal Trek","Garhwal","Uttarkashi",
"Difficult","15584 ft","6-7 Days",
"May-June or Sept-Oct","15k-22k",
"Gangotri National Park Permit",
"Run 5km under 28 mins, strong balance",
"Micro-spikes, Gaiters, Trekking Poles",
"Military Hospital Harsil / CHC Uttarkashi",
"Rockfall near Spider Wall and high AMS risk."),

("Kalpeshwar Trek","Garhwal","Chamoli",
"Very Easy","7210 ft","2-3 Days",
"Year Round","4k-7k",
"No Permit Required",
"Suitable for beginners and families",
"Walking Shoes, Raincoat",
"CHC Joshimath / District Hospital Gopeshwar",
"Landslide risk near Helang road."),

("Gaumukh Tapovan Trek","Garhwal","Uttarkashi",
"Moderate-Difficult","14640 ft","7-8 Days",
"May-June or Sept-Oct","18k-25k",
"Gangotri National Park Permit",
"Ability to trek across glaciers",
"Micro-spikes, Poles, Gaiters",
"Military Hospital Harsil / CHC Uttarkashi",
"Crevasses and glacier crossings."),

("Satopanth Tal Trek","Garhwal","Chamoli",
"Difficult","15091 ft","6 Days",
"May-June or Sept-Oct","18k-25k",
"Forest Permit (Joshimath/Badrinath)",
"8-10 hours trekking stamina",
"High-traction Boots, Helmet, Poles",
"Military Hospital Joshimath / Badrinath Medical Center",
"Dangerous Suicide Wall scree slope."),

("Har Ki Dun Trek","Garhwal","Uttarkashi",
"Easy-Moderate","11700 ft","7 Days",
"Dec-Mar or Apr-June","10k-15k",
"Govind Pashu Vihar Permit",
"Ability to walk 10-12km daily",
"Waterproof Trek Shoes, Rain Poncho",
"PHC Mori / CHC Purola",
"Landslides and river crossing risks."),

("Madmaheshwar Trek","Garhwal","Rudraprayag",
"Moderate","12139 ft","4-5 Days",
"May-June or Sept-Oct","8k-12k",
"Forest Checkpost Registration",
"Ability to climb 3000+ stairs",
"Knee Brace, Trekking Poles, Headlamp",
"PHC Ukhimath / CHC Augustmuni",
"Slippery steps and narrow ridges."),

("Gartang Gali Trek","Garhwal","Uttarkashi",
"Easy-Moderate","11000 ft","2-3 Days",
"Apr-June or Sept-Nov","3k-9k",
"Gangotri National Park Permit",
"Basic fitness, walk 5km uphill",
"Hiking Shoes, Sunglasses, Windbreaker",
"Military Hospital Harsil / CHC Uttarkashi",
"Narrow wooden bridge with deep gorge."),

("Lord Curzon Trail","Garhwal","Chamoli",
"Easy-Moderate","12516 ft","6 Days",
"Dec-Mar or Oct-Nov","8k-12k",
"Nanda Devi Biosphere Permit",
"Jog 5km in 33-35 mins",
"Micro-spikes, Trekking Poles, Sunglasses",
"Military Hospital Joshimath / CHC Joshimath",
"High winds and icy ridge trails."),
]

cursor.executemany("""
INSERT OR IGNORE INTO treks
(trek_name, region, district, difficulty, max_altitude,
duration, best_season, budget, permits,
physical_requirement, essential_gear,
nearest_hospital, safety_note)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", trek_data)

connection.commit()
connection.close()

print("Data inserted successfully!")