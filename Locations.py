from Queue import*
import pandas as pd


def construct_path(start, end, all_locs):
    """
    Produces a list of Locations of the shortest path from the starting
    to the end point

    Input:
        start(str): name of the location to start at
        end(str): the name of the location to end at
        all_locs(Directory): Directory object with all the Locations

    Returns (List): a list of Location names
    """

    dijkstra(start, end, all_locs)

    result = []
    current = all_locs.directory[end]

    while start != current.name:
        result.append(current.name)
        current = current.previous

    result.append(start)
    result = result[::-1]
    result.append(end)

    return result


def dijkstra(start, end, all_locs):
    """
    Implementing Dijkstra's shortest path algorithm

    Input:
        start(str): name of the location to start at
        end(str): the name of the location to end at
        all_locs(Directory): Directory object with all the Locations

    Returns: (does not return a value)
    """

    #EDIT THIS CODE HERE

    visited = set()
    stack = Queue()

    visited.add(start)
    stack.insert((0, start))
    all_locs[start].distance = 0

    current = start
    while not stack.is_empty():
        current = stack.pop_min()[1].name
        visited.add(current)
        if current == end:
            return
        for neighbor in all_locs[current].neighbors:
            dist = all_locs[current].neighbor[0] + all_locs[current].distance
            if (neighbor[1] not in visited
                    and dist < all_locs[neighbor[1]].distance):
                current = neighbor[1]
                stack.insert((neighbor[0], neighbor[1]))


class Location:

    def __init__(self, name):
        """
        Constructor

        neighbors (list of tuples):
        """
        self.name = name
        self.previous = None
        self.distance = float("inf")
        self.neighbors = []


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

        for i, neighbor in enumerate(neighbors_lst):
            self.neighbors.append((neighbor, distances_lst[i]))


class Directory:
    """
    Class for keeping track of all Locations added
    """

    def __init__(self, filename):
        """
        Constructor for a directory of all hiking Location objects
        """

        self.file = filename
        self.directory = {}


    def add_locations(self):
        """
        Adds all of the locaitons into self.directory

        Input: none

        Returns: (does not return a value)
        """

        col_types = {"Name": str, "Neighbors": str, "Distances": str}
        all_locs = pd.read_csv(self.file, dtype=col_types)
        names_lst = all_locs["Name"].tolist()
        neighbors = all_locs["Neighbors"].tolist()
        distances = all_locs["Distances"].tolist()

        for i, name in enumerate(names_lst):
            self.directory[name] = Location(name)
            self.directory[name].add_neighbors(neighbors[i], distances[i])


#Driver Code
print("Here are all possible locations choose from: ")
all_locs = Directory("hiking_locations.csv")
counter = 0
for name in all_locs.directory:
    counter += 1
    print("{}. {}".format(counter, name))
start = input("What location would you like to start at? ")
end = input("What location would you like to end at?")
path = construct_path(start, end, all_locs)
print("Here is your constructed path: ")
for loc in path:
    print(loc)

