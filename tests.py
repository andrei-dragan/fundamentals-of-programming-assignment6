import unittest
from program import MyList, sort_function, filter_function


class TestMyList(unittest.TestCase):
    def setUp(self):
        self.my_list = MyList()
        self.my_list.append(5)
        self.my_list.append(7)

    def test_length(self):
        self.assertEqual(len(self.my_list), 2)

    def test_getItem(self):
        self.assertEqual(self.my_list[0], 5)
        self.assertEqual(self.my_list[1], 7)

    def test_setItem(self):
        self.my_list[0] = 9
        self.assertEqual(self.my_list[0], 9)

    def test_append(self):
        self.my_list.append(10)
        self.assertEqual(len(self.my_list), 3)
        self.assertEqual(self.my_list[0], 5)
        self.assertEqual(self.my_list[1], 7)
        self.assertEqual(self.my_list[2], 10)

    def test_delItem(self):
        del self.my_list[0]
        self.assertEqual(len(self.my_list), 1)
        self.assertEqual(self.my_list[0], 7)

    def test_remove(self):
        self.my_list.remove(5)
        self.assertEqual(len(self.my_list), 1)
        self.assertEqual(self.my_list[0], 7)

    def test_iter_next(self):
        i = 0
        for elem in self.my_list:
            self.assertEqual(elem, self.my_list[i])
            i += 1

    def test_str(self):
        self.assertEqual(str(self.my_list), '[5, 7]')

    def tearDown(self):
        pass


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.my_list = MyList()
        self.my_list.append(2)
        self.my_list.append(10)
        self.my_list.append(21)
        self.my_list.append(6)
        self.my_list.append(9)

    @staticmethod
    def comparison_f(a, b):
        return a <= b

    @staticmethod
    def acceptance_f(a):
        if '2' in str(a):
            return True

        return False

    def test_sort_function(self):
        sort_function(self.my_list, self.comparison_f)
        self.assertEqual(str(self.my_list), '[2, 6, 9, 10, 21]')

    def test_filter_function(self):
        self.assertEqual(str(filter_function(self.my_list, self.acceptance_f)), '[2, 21]')

    def tearDown(self):
        pass

