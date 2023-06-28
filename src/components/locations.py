"""
Using Djikstra's Algorithm to calculate the shortest hiking trail
"""

from loc_queue import*
from utils import*


def construct_path(start, end, all_locs):
    """
    Produces a list of Locations of the shortest path from the starting
    to the end point

    Input:
        start(str): name of the location to start at
        end(str): the name of the location to end at
        all_locs(Directory): Directory object with all the Locations

    Returns (lst of lsts): a list of an float for the total path distance
        and a list of Location names
    """

    dijkstra(start, end, all_locs)

    path = []
    current = all_locs.directory[end]

    while start != current.name:
        path.append(current.name)
        current = current.previous

    path.append(start)
    path = path[::-1]

    result = [all_locs.directory[end].distance, path]

    return result


def dijkstra(start, end, locs):
    """
    Implementing Dijkstra's shortest path algorithm

    Input:
        start(str): name of the location to start at
        end(str): the name of the location to end at
        locs(Directory): Directory object with all the Locations

    Returns: (does not return a value)
    """

    visited = set()
    stack = Queue()

    start_loc = locs.directory[start]

    visited.add(start)
    stack.insert((0, start))
    start_loc.distance = 0

    while not stack.is_empty():
        current_name = stack.pop_min()[1]
        visited.add(current_name)
        if current_name == end:
            return
        current_loc = locs.directory[current_name]
        for neighbor, neigh_dist in current_loc.neighbors.items():
            dist = neigh_dist + current_loc.distance
            if (neighbor not in visited
                    and dist < locs.directory[neighbor].distance):
                locs.directory[neighbor].previous = current_loc
                current_name = neighbor
                locs.directory[neighbor].distance = dist
                stack.insert((dist, neighbor))


class Location:

    def __init__(self, name):
        """
        Constructor

        neighbors (list of tuples):
        """
        self.name = name
        self.previous = None
        self.distance = float("inf")
        self.neighbors = {}


    def change_distance(self, dist):
        """
        Changes the self.distance attribute

        Input:
            distr(int): distance to change to

        Return: (does not return a value)
        """

        self.distance = dist


    def add_neighbors(self, neighbors, distances):
        """
        Adds neighbor tuples to the self.neighbors attribute

        Inputs:
            neighbors(str): str of all neighbor names
            distances(str): str of all distances to the neighbors

        Returns: (does not return a value)
        """

        neighbors_lst = neighbors.split(", ")
        distances_lst = distances.split(", ")

        for distance in distances_lst:
            distance = float(distance)

        for i, neighbor in enumerate(neighbors_lst):
            self.neighbors[neighbor] = float(distances_lst[i])


class Directory:
    """
    Class for keeping track of all Locations added
    """

    def __init__(self):
        """
        Constructor for a directory of all hiking Location objects
        """

        self.directory = {}
        self.add_locations()


    def add_locations(self):
        """
        Adds all of the locations into self.directory

        Input: none

        Returns: (does not return a value)
        """

        for loc in locations:
            name = loc["Name"]
            neighbors = loc["Neighbors"]
            distances = loc["Distances"]
            self.directory[name] = Location(name)
            self.directory[name].add_neighbors(neighbors, distances)

#Driver Code
print("Welcome to the hiking trail planner!")
print("Here are all possible locations choose from: \n")
locs = Directory()
counter = 0
for name in locs.directory:
    counter += 1
    print("{}. {}".format(counter, name))
start = input("\nWhat location would you like to start at? ")
end = input("What location would you like to end at? ")
path = construct_path(start, end, locs)
print("\nHere is your constructed path: ")
for loc in path[1]:
    print("- ", loc)
print("\nHere is the total distance: {}km\n".format(path[0]))