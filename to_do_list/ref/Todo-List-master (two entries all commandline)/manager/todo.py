class Item:
    # attribute

    #constructor
    def __init__(self, name, count):
        self.name = name
        self.count = count
    
    # properties
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            if value.isalpha():
                self.__name = value
            else:
                raise ValueError("value must be alphabet.")
        else:
            raise TypeError("value must be str data type.")

    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self, value):
        if isinstance(value, int):
            self.__count = value
        else:
            raise TypeError("value must be int data type.")

    # method
    # 
    # magic method    
    def __add__(self, other):
        total = self.__count + other
        self.__count = total
        return total
    
    def __iadd__(self, other):
        if isinstance(other, int):
            self.__count = self.__count + other
            return self
        else:
            raise TypeError("other must be int data type.")

    # casting
    def __str__(self):
        return '{} {}'.format(self.__name, self.__count)
    
    def __int__(self):
        return self.__count
    
    def __float__(self):
        return float(self.__count)

    # representation of an object
    def __repr__(self):
        return '({}, {})'.format(self.__name, self.__count)

class Items:
    def __init__(self):
        self.__items = list()
    
    def add(self, item):
        if isinstance(item, Item):
            self.__items.append(item)
        else:
            raise TypeError("value must be Item class.")

    def show(self):
        return self.__items

    def __iter__(self):
        yield from self.__items
    
    def __contains__(self, item):
        for i in self:
            if item.name == i.name and item.count == i.count:
                return True
        return False

    def __add__(self, other):
        self.add(other)
        return self
    
    def __len__(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)
    