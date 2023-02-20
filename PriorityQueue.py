class PriorityQueue:

    def __init__(self):
        """
        A priority queue that is a list of tuples of the form
        (priority, Locations)
        """

        self.queue = []

    def insert(self, item):
        """
        Inserts an item into the priority queue
        """

        self.sift