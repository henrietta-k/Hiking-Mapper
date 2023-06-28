class Queue:
    """
    A priority queue to be used in Dijkstra's algorithm
    """

    def __init__(self):
        """
        A min heap that is a list of tuples of the form
        (priority, Location)
        """

        self.queue = []


    def is_empty(self):
        """
        Checks if self.queue is empty or not

        Input: none
        Returns (boolean): whether self.queue is empty or not
        """

        return len(self.queue) == 0


    def insert(self, item):
        """
        Inserts an item into the priority queue based on its priority.

        Inputs:
            item(tuple): a touple of the priority and Location name

        Returns: (does not return a value)
        """

        self.queue.insert(0, item)
        self.heapify(item)


    def heapify(self, item):
        """
        Checks the order of the items in the priority queue. If elements are not
        in order, it swaps the elements around.

        Inputs:
            item(tuple): tuple of the priority of the item and the item itself
        Returns: (does not return a value)
        """

        for i, item2 in enumerate(self.queue):
            if item[0] > item2[0]:
                item_idx = self.queue.index(item)
                self.queue[i], self.queue[item_idx] = self.queue[item_idx], self.queue[i]


    def pop_min(self):
        """
        Removes and returns the item with the highest priority in the Queue

        Inputs: None
        Returns (tuple): returns the item in the Queue of the highest priority
        """
        min_item = self.queue.pop(0)
        return min_item


