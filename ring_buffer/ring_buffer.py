class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        #I want to create an empty list for the items to be stored in
        #if the len(storage) is < than capacity, the length should be
        #as long as the number of items added to it. Otheriwse,
        #len(self.storage) should always be the capacity size
        self.storage = [][:capacity]
        # store the index (starts at 0) this helps us
        #keep track of where I'm putting these items
        self.index = 0

    def append(self, item):
        #if the length of our storage is already the max, change the item 
        #at the oldest index to that new item
        if len(self.storage) == self.capacity:
            self.storage[self.index] = item
        #otherwise, just append the item to the storage list
        else:
            self.storage.append(item)

        #I want to update the index item so the RingBuffer knows where to add
        #the new item if the capacity is full
        #something like this
        #if capacity is 2. first index was 0 and length < 2, I need to append
        #to the empty list. Next, I will update the index. The new index is 1.
        #The length < 3 is still next so the item will be appended. Next, I'll 
        # to update the index again. (0 + 1) / 2 = 1
        self.index = (self.index + 1) % self.capacity

    def get(self):
        #return the list of items
        return self.storage