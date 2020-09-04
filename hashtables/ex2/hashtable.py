class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_tail(self, key, value):
        new_entry = HashTableEntry(key, value)
        if self.head is None and self.tail is None:
            self.head = new_entry
            self.tail = new_entry

        else:
            self.tail.next = new_entry
            self.tail = new_entry
        self.length += 1

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None

        if self.head == self.tail:
            removed_entry = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return val

        else:
            removed_entry = self.tail
            current = self.head
            while current.next != self.tail:
                current = current.next
            
            self.tail = current
            self.tail.next = None
            self.length -= 1
            return removed_entry

    def remove_head(self):
        if self.head is None and self.tail is None:
            return None

        if self.head == self.tail:
            removed_entry = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_entry
        
        else:
            removed_entry = self.head
            self.head = self.head.next
            self.length -= 1
            return removed_entry

    def contains(self, key):
        if not self.head:
            return False

        current = self.head
        while current:
            if current.key == key:
                return True
            
            current = current.next

        return False
        
    def remove_key(self, key):
        if self.head is None and self.tail is None:
            return None

        current = self.head
        while current.key != key:
            removed_entry = self.remove_head()
            self.add_to_tail(removed_entry.key, removed_entry.value)
            current = self.head
        return self.remove_head()

    def find_key_value(self, key):
        if self.head is None and self.tail is None:
            return None

        current = self.head
        while current:
            if current.key == key:
                return current.value
            else:
                current = current.next

        return None


       



# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity
        self.table = [None] * self.capacity
        self.size = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.table)
        


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.get_num_slots()


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        FNV_PRIME = 1099511628211  # prime number for 64-bit
        FNV_OFFSET_BASIS = 14695981039346656037  # for 64-bit

        hash = FNV_OFFSET_BASIS
        for k in key:
            hash = hash * FNV_PRIME + ord(k)
        
        return hash

        """
        Pseudo:
        hash = offset_basis
        for each octet_of_data to be hashed
        hash = hash * FNV_prime
        hash = hash xor octet_of_data
        return hash
        """

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381  # Prime number found to be great for application purposes

        for k in key:  # iterate through character in key
            hash = hash * 33 + ord(k)  # 33 used because it works well, apparently
        
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.table[index] is not None:
            if self.table[index].contains(key):
                self.table[index].remove_key(key)
            self.table[index].add_to_tail(key, value)

        else:
            self.table[index] = LinkedList()
            self.table[index].add_to_tail(key, value)

        self.size += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.table[index] is None:
            print("Key was not found within the table")
        else:
            self.table[index].remove_key(key)
        self.size -= 1


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        return self.table[index].find_key_value(key)
        


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        temp_list = []
        [temp_list.append(entry) for entry in self.table if entry is not None]
        self.capacity = new_capacity
        self.table = [None] * self.capacity
        for entry in temp_list:
            while entry.length > 0:
                head = entry.remove_head()
                self.put(head.key, head.value)




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
