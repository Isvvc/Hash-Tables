# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def findPreviousLinkedPair(self, key, node):
        if isinstance(node.next, LinkedPair):
            if node.next.key == key:
                return node
            return self.findPreviousLinkedPair(key, node.next)
        else:
            return node


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]

        # Check to see if the key already exists
        if isinstance(node, LinkedPair):
            # If the head is the correct node, update its value
            if node.key == key:
                node.value = value
            else:
                # Find the node we need to update the child of
                prev = self.findPreviousLinkedPair(key, node)

                if isinstance(prev.next, LinkedPair):
                    # If the child is the correct node, update its value
                    prev.next.value = value
                else:
                    # If there is no node of this key, create one
                    prev.next = LinkedPair(key, value)
        else:
            # Save the key-value pair
            self.storage[index] = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]

        if isinstance(node, LinkedPair):
            if node.key == key:
                self.storage[index] = None
            else:
                prev = self.findPreviousLinkedPair(key, node)
                if isinstance(prev.next, LinkedPair):
                    prev.next = prev.next.next
                    return 

        print(f"Key {key} not found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]

        if isinstance(node, LinkedPair):
            if node.key == key:
                return node.value
            else:
                prev = self.findPreviousLinkedPair(key, node)
                if isinstance(prev.next, LinkedPair):
                    return prev.next.value

        return None


    def insertLinkedPairs(self, node):
        self.insert(node.key, node.value)
        if isinstance(node.next, LinkedPair):
            self.insertLinkedPairs(node.next)

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2

        old_storage = self.storage.copy()
        self.storage = [None] * self.capacity

        for item in old_storage:
            if isinstance(item, LinkedPair):
                self.insertLinkedPairs(item)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
