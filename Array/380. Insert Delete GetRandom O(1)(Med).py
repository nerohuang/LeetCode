import random;

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.set = [], set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.set:
            self.nums.append(val);
            self.set.add(val);
            return True;
        return False;
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.set:
            self.set.remove(val);
            self.nums.remove(val);
            return True;
        return False;
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


#sample 80 ms submission
#class RandomizedSet:
#
#    def __init__(self):
#        """
#        Initialize your data structure here.
#        """
#        self.list = []
#        
#        self.dict = dict()
#        
#        self.size = 0
#
#    def insert(self, val: int) -> bool:
#        """
#        Inserts a value to the set. Returns true if the set did not already contain the specified element.
#        """
#        if val in self.dict:
#            return False
#        else:            
#            
#            self.dict[ val ] = self.size
#            
#            # append new element into list
#            self.list.append( val )
#            
#            # update size of collection
#            self.size += 1
#            
#            return True
#        
#
#    def remove(self, val: int) -> bool:
#        """
#        Removes a value from the set. Returns true if the set contained the specified element.
#        """
#        if val not in self.dict:
#            return False
#        
#        else:
#
#            # To reach O(1) performance, use technique of element swap, and pop on tail
#            
#            # get the index of element with value
#            index_of_val = self.dict[val]
#            
#            
#            # update index of last_element
#            self.dict[ self.list[-1] ] = index_of_val
#            
#            
#            # swap val with last element of number_list
#            self.list[-1], self.list[index_of_val] = self.list[index_of_val], self.list[-1]
#            
#            
#            # remove val from list by popping last
#            self.list.pop()
#            
#            # remove val from dictionary by deleting key
#            del self.dict[val]
#        
#            # update size of collection
#            self.size -= 1
#        
#            return True
#
#    def getRandom(self) -> int:
#        """
#        Get a random element from the set.
#        """
#        return random.choice( self.list )
#
#
## Your RandomizedSet object will be instantiated and called as such:
## obj = RandomizedSet()
## param_1 = obj.insert(val)
## param_2 = obj.remove(val)
## param_3 = obj.getRandom()