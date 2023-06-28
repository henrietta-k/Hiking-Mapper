"""
All hiking locations with neighbors and distances to neighbors
"""

braemar_hill = {"Name": "Braemar Hill Peak",
                "Neighbors": "Red Incense Burner Summit, Sir Cecil's Ride Stream, Jardine's Lookout",
                "Distances": "1.5, 1.1, 3.6"}
red_incense = {"Name": "Red Incense Burner Summit",
                "Neighbors": "Sir Cecil's Ride Stream, Braemar Hill Peak",
                "Distances": "1.1, 1.5"}
sir_cecil = {"Name": "Sir Cecil's Ride Stream",
                "Neighbors": "Red Incense Burner Summit, Braemar Hill Peak",
                "Distances": "1.1, 1.1"}
siu_ma = {"Name": "Siu Ma Shan Peak",
                "Neighbors": "Wilson Trail, Mount Cameron, Jardine's Lookout",
                "Distances": "2.7, 7, 1.4"}
mount_cameron = {"Name": "Mount Cameron",
                "Neighbors": "Aberdeen Country Park, Siu Ma Shan Peak",
                "Distances": "1.4, 7"}
lady_clementi = {"Name": "Lady Clementi's Ride",
                "Neighbors": "Aberdeen Country Park",
                "Distances": "2.6"}
aberdeen = {"Name": "Aberdeen Country Park",
                "Neighbors": "Mount Cameron, Lady Clementi's Ride, Bowen Road Lovers' Stone Garden",
                "Distances": "1.4, 2.6, 5.2"}
wilson = {"Name": "Wilson Trail",
                "Neighbors": "Siu Ma Shan Peak, Tai Tam Country Park",
                "Distances": "2.7, 1.3"}
tai_tam = {"Name": "Tai Tam Country Park",
                "Neighbors": "Tseng Kwan Shek, Wilson Trail, Tai Tam Mound Fall",
                "Distances": "6.4, 1.3, 2.3"}
mound_fall = {"Name": "Tai Tam Mound Fall",
                "Neighbors": "Tai Tam Country Park",
                "Distances": "2.3"}
tseng_kwan_shek = {"Name": "Tseng Kwan Shek",
                "Neighbors": "Tai Tam Country Park, Mount Parker Viewing Point, The Dinosaur Monolith",
                "Distances": "6.4, 3.0, 1.3"}
mount_parker = {"Name": "Mount Parker Viewing Point",
                "Neighbors": "Tseng Kwan Shek",
                "Distances": "3"}
dinosaur_monolith = {"Name": "The Dinosaur Monolith",
                "Neighbors": "Wartime Stoves, Hong Pak Country Trail, Tseng Kwan Shek",
                "Distances": "0.8, 1, 1.3"}
hong_pak = {"Name": "Hong Pak Country Trail",
                "Neighbors": "The Dinosaur Monolith",
                "Distances": "1"}
mount_parker_green = {"Name": "Mount Parker Road Green Trail",
                "Neighbors": "Tseng Kwan Shek",
                "Distances": "2.4"}
jardine_lookout = {"Name": "Jardine's Lookout",
                "Neighbors": "Siu Ma Shan Peak, Mount Butler Viewing Point, Braemar Hill Peak",
                "Distances": "1.4, 3.6, 3.6"}
wong_nai = {"Name": "Wong Nai Chung Reservoir",
                "Neighbors": "Wartime Stoves, Quarry Bay Reservoir Garden",
                "Distances": "5.8, 6.5"}
bowen_road = {"Name": "Bowen Road Lovers' Stone Garden",
                "Neighbors": "Aberdeen Country Park ",
                "Distances": "5.2"}
quarry_bay  = {"Name": "Quarry Bay Reservoir Garden",
                "Neighbors": "Wartime Stoves",
                "Distances": "0.65, 6.5"}
mount_butler = {"Name": "Mount Butler Viewing Point",
                "Neighbors": "Jardine's Lookout",
                "Distances": "3.6"}
wartime_stoves = {"Name": "Wartime Stoves",
                "Neighbors": "The Dinosaur Monolith, Wong Nai Chung Reservoir, Quarry Bay Reservoir Garden",
                "Distances": "0.80, 5.8, 0.65"}

locations = [braemar_hill, red_incense, sir_cecil, siu_ma, aberdeen, wilson,
            tai_tam, mound_fall, tseng_kwan_shek, mount_parker_green,
            dinosaur_monolith, hong_pak, mount_parker, jardine_lookout,
            wong_nai, bowen_road, quarry_bay, mount_butler, wartime_stoves,
            mount_cameron, lady_clementi]
