class LinkedListItem:
    def __init__(self, value):
        self.value = value
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next_item):
        self.__next = next_item

    def has_next(self):
        return self.__next is not None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def __getitem__(self, index):
        current = self.__head
        for _ in range(index):
            if current is None or not current.has_next():
                raise IndexError
            current = current.get_next()
        return current.value

    def __len__(self):
        return self.__len

    def print_list(self):
        current = self.__head
        for _ in range(len(self)):
            print(current.value, end=' ')
            current = current.get_next()
        print()
    
    def add(self, value, index=None):
        if index is not None and index > self.__len:
            raise IndexError
            
        new_item = LinkedListItem(value)
        self.__len += 1
        
        if self.__head == None:
            self.__head = new_item
            self.__tail = new_item
            return
        
        if index is None or index == (self.__len):
            self.__tail.set_next(new_item)
            self.__tail = new_item         
            return
            
        if index == 0:
            new_item.set_next(self.__head)
            self.__head = new_item
            return

        if index < 0:
            index = self.__len + index
            
        current = self.__head

        for _ in range(index-1):
            if current is None or not current.has_next():
                raise IndexError
            current = current.get_next()

        saved_next = current.get_next()
        current.set_next(new_item)
        current = current.get_next()
        current.set_next(saved_next)

        
    def pop(self, index=None):
        if index == None:
            index = self.__len - 1
        self.__len -= 1
        if index == 0:
            pop_el = self.__head
            self.__head = pop_el.get_next()
            return pop_el.value
        
        current = self.__head 
        for _ in range(index - 1):
            if current is None or not current.has_next():
                raise IndexError
            current = current.get_next()
        pop_el = current.get_next()
        current.set_next(pop_el.get_next())
        
        return pop_el.value
    
    def remove_last_occurence(self, el):
        index = None
        current = self.__head
        
        for i in range(len(self) - 1):
            if current.value == el:
                index = i
            current = current.get_next()
        if index is not None:
            self.pop(index)
        
        
    def add_all(self, items_list, index=None):
        if index is not None and index < 0:
            index = self.__len + index
        for item in items_list:
            self.add(item, index)
            if index is not None:
                index += 1
            
    def __contains__(self, value):
        current = self.__head
        for _ in range(len(self)):
            if current.value == value:
                return True
            current = current.get_next()
        return False

    def first(self):
        if len(self) == 0:
            raise AttributeError
        return self.__head.value

    def last(self):
        if len(self) == 0:
            raise AttributeError
        return self.__tail.value
