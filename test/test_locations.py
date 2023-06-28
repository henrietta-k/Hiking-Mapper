"""
Tests for Locations.py and Queue.py
"""

from queue import*
from locations import*
from utils import*

import sys
sys.path = ['src/components/locations.py']

#Testing to see if the priority Queue works
def test_create_queue():
    new = Queue()
    new.insert((1, ""))
    new.insert((3, ""))
    new.insert((4, ""))
    new.insert((2, ""))

    assert new.queue == [(1, ''), (2, ''), (3, ''), (4, '')]


#Testing to see if the Directory works
def test_make_directory():
    dir = Directory()
    assert len(dir.directory) == len(locations)



#Testing to see if the paths are built correctly
def test_construct_path_1():
    all_locs = Directory()
    result = construct_path("Tai Tam Country Park", "Aberdeen Country Park",
                            all_locs)

    assert result == [12.4, ["Tai Tam Country Park", "Wilson Trail",
                             "Siu Ma Shan Peak", "Mount Cameron",
                             "Aberdeen Country Park"]]

def test_construct_path_2():
    all_locs = Directory()
    result = construct_path("Mount Butler Viewing Point",
                            "Red Incense Burner Summit", all_locs)

    assert result == [8.7, ["Mount Butler Viewing Point", "Jardine's Lookout",
                           "Braemar Hill Peak", "Red Incense Burner Summit"]]

def test_construct_path_3():
    all_locs = Directory()
    result = construct_path("Mount Parker Viewing Point",
                            "Hong Pak Country Trail", all_locs)

    assert result == [5.3, ["Mount Parker Viewing Point", "Tseng Kwan Shek",
                            "The Dinosaur Monolith", "Hong Pak Country Trail"]]

def test_construct_path_4():
    all_locs = Directory()
    result = construct_path("Wong Nai Chung Reservoir",
                            "Bowen Road Lovers' Stone Garden", all_locs)
    assert result == [31.9, ["Wong Nai Chung Reservoir", "Wartime Stoves",
                         "The Dinosaur Monolith", "Tseng Kwan Shek",
                         "Tai Tam Country Park", "Wilson Trail",
                         "Siu Ma Shan Peak", "Mount Cameron",
                         "Aberdeen Country Park",
                         "Bowen Road Lovers' Stone Garden"]]

