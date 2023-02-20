class Queue:

    def __init__(self):
        """
        A min heap that is a list of tuples of the form
        (priority, Locations)
        """

        self.queue = []


    def insert(self, item):
        """
        Inserts an item into the priority queue

        Inputs:
            item(tuple): the item to be insereted into the queue

        Returns: (does not return a value)
        """

        self.queue.append(item)
        self.sift_up(item)


    def sift_up(self, item):
        """
        Sifts the value up the priority queue if possible

        Parameters: none
        Returns: (does not return a value)
        """

        for i, item2 in enumerate(self.queue):
            if item2[0] > item[0]:
                temp_idx = self.queue.index(item)
                self.queue[i] = item
                self.queue[temp_idx] = item2



