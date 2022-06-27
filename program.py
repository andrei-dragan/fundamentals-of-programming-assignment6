class MyList:
    def __init__(self):
        self.__list = list()

    def __len__(self):
        return len(self.__list)

    def __setitem__(self, key, value):
        self.__list[key] = value

    def __getitem__(self, key):
        return self.__list[key]

    def __delitem__(self, key):
        del self.__list[key]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        self.__index += 1
        if self.__index <= self.__len__():
            return self.__list[self.__index - 1]
        else:
            raise StopIteration()

    def remove(self, elem):
        for e in self.__list:
            if e == elem:
                self.__list.remove(e)

    def append(self, value):
        self.__list.append(value)

    def __str__(self):
        return str(self.__list)


def sort_function(my_list, comparison_f):
    index = 0
    while index < len(my_list):
        if index == 0:
            index = index + 1
        if comparison_f(my_list[index - 1], my_list[index]):
            index = index + 1
        else:
            my_list[index], my_list[index - 1] = my_list[index - 1], my_list[index]
            index = index - 1
    return my_list


def filter_function(my_list, acceptance_f):
    new_filtered_list = list()
    for elem in my_list:
        if acceptance_f(elem):
            new_filtered_list.append(elem)

    return new_filtered_list
