import unittest
from random import randint

from search_sort_library import * 


def generate_random_number_list(list_size):
    rand_list = []
    for count in range(list_size):
        rand_list.append(randint(0, list_size*2))
    return rand_list


class SearchSortTests(unittest.TestCase):

    def test_is_sorted(self):
        self.assertTrue(is_sorted([1, 2, 3, 4]))
        self.assertTrue(is_sorted([1, 5, 11, 22]))
        self.assertTrue(is_sorted([1, 5, 5, 11, 11,  22]))
        self.assertTrue(is_sorted([1, 4, 8, 10, 15, 29, 31, 34, 38, 72, 109]))
        self.assertTrue(is_sorted([-1000, 0, 1, 500, 1100, 22000]))
        self.assertTrue(is_sorted([1, 5]))
        self.assertTrue(is_sorted([5]))
        self.assertTrue(is_sorted([]))
        self.assertFalse(is_sorted([4, 3, 2, 1]))
        self.assertFalse(is_sorted([1, 5, 11, 0]))
        self.assertFalse(is_sorted([10, 5, 7, 9]))
        self.assertFalse(is_sorted([1, 7, 5, 9]))
        self.assertFalse(is_sorted([0, 1, 500, 1100, 22000, -23000]))
        self.assertFalse(is_sorted([10, 2]))
        self.assertFalse(is_sorted([1, 4, 8, 10, 15, 29, 34, 31, 38, 72, 109]))

    def test_my_linear_search(self):
        self.check_search_in_order_list(my_linear_search)
        self.check_search_out_of_order_list(my_linear_search)

    def test_system_linear_search(self):
        self.check_search_in_order_list(system_linear_search)
        self.check_search_out_of_order_list(system_linear_search)

    def test_my_sort(self):
        self.check_number_sorter_simple(my_sort)
        self.check_a_number_sorter_using_is_sorted(my_sort)

    def test_system_sort(self):
        self.check_number_sorter_simple(system_sort)
        self.check_a_number_sorter_using_is_sorted(system_sort)

    def test_my_binary_search(self):
        self.check_search_in_order_list(my_binary_search)

    def check_search_in_order_list(self, search_function):
        list_1 = [-8, 0, 1, 1, 2, 7, 12, 18, 22, 135, 7096, 7097]
        list_2 = [-7, -1, 9, 92, 114]
        self.check_search(search_function, list_1, list_2)
        self.check_search(search_function, list_2, list_1)

    def check_search_out_of_order_list(self, search_function):
        list_1 = [100, 7, -9, 113, 117, 4, 18, 3300, 62]
        list_2 = [11, 5, -100, 17, 9, 19, 1, 0]
        self.check_search(search_function, list_1, list_2)
        self.check_search(search_function, list_2, list_1)

    def check_search(self, search_function, test_data, data_not_in_test):
        for i in range(len(test_data)):
            answer = search_function(test_data, test_data[i])
            self.assertEqual(test_data[answer], test_data[i])
        for item in data_not_in_test:
            self.assertEqual(-1, search_function(test_data, item))

        self.assertEqual(-1, search_function([], 5))
        self.assertEqual(0, search_function([5], 5))

    def check_number_sorter_simple(self, number_sorter):
        example_list = [2, 7, 1, 3, 6, 5, 4]
        number_sorter(example_list)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], example_list)

        example_list = [1, 2, 3, 4, 5, 6, 7]
        number_sorter(example_list)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], example_list)

        example_list = [7, 2]
        number_sorter(example_list)
        self.assertEqual([2, 7], example_list)

        example_list = [2]
        number_sorter(example_list)
        self.assertEqual([2], example_list)

        example_list = []
        number_sorter(example_list)
        self.assertEqual([], example_list)

    def check_a_number_sorter_using_is_sorted(self, number_sorter):
        a_list = generate_random_number_list(20)
        number_sorter(a_list)
        self.assertTrue(is_sorted(a_list))

        a_list = generate_random_number_list(2000)
        number_sorter(a_list)
        self.assertTrue(is_sorted(a_list))


if __name__ == '__main__':
    unittest.main()
