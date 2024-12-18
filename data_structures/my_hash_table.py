import math
from .time_logger import time_logger


class HashTable:

    def __init__(self, size) -> None:
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]
    
    def __eq__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.hash_table[0][0] == self.hash_table[0][0]
        else:
            return NotImplemented
    
    def __ne__(self, other) -> bool:
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result
    
    def __gt__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.hash_table[0][0] > self.hash_table[0][0]
        else:
            return NotImplemented
    
    def __ge__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.hash_table[0][0] >= self.hash_table[0][0]
        else:
            return NotImplemented

    def __lt__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.hash_table[0][0] < self.hash_table[0][0]
        else:
            return NotImplemented

    def __le__(self, other) -> bool:
        if other.__class__ == self.__class__:
            return self.hash_table[0][0] <= self.hash_table[0][0]
        else:
            return NotImplemented
    
    def __repr__(self) -> str:
        return "".join(str(item) for item in self.hash_table)

    def _hash_function(self, key) -> int:
        A = (math.sqrt(5) - 1) / 2

        return math.floor(self.size * ((key * A) % 1))

    @time_logger
    def insert(self, key, value) -> None:
        hashed_key = self._hash_function(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    @time_logger
    def search(self, key) -> None:
        hashed_key = self._hash_function(key) % self.size
        
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            return record_val
        else:
            return "No record found"

    @time_logger
    def delete(self, key) -> None:
        hashed_key = self._hash_function(key) % self.size
        
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
