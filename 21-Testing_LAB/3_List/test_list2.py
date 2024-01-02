from unittest import TestCase, main


class TestIntegerList(TestCase):
    def setUp(self):
        self.some_list = IntegerList("test", 1.2, 10, "20", 30)

    def test_initialization(self):
        self.assertEqual(self.some_list._IntegerList__data, [10, 30])

    def test_correct_get_data(self):
        self.assertEqual(self.some_list.get_data(), [10, 30])

    def test_add_method_with_correct_data(self):
        result = self.some_list.add(5)
        self.assertEqual(result, [10, 30, 5])
        self.assertEqual(self.some_list._IntegerList__data, [10, 30, 5])

    def test_add_method_with_wrong_data(self):
        with self.assertRaises(ValueError) as vl:
            self.some_list.add("5")
        self.assertEqual("Element is not Integer", str(vl.exception))

    def test_remove_wrong_index(self):
        with self.assertRaises(IndexError) as ie:
            self.some_list.remove_index(7)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_in_range(self):
        result = self.some_list.remove_index(0)
        self.assertNotIn(10, self.some_list._IntegerList__data)
        self.assertEqual(10, result)

    def test_get_method_with_wrong_data(self):
        with self.assertRaises(IndexError) as ie:
            self.some_list.get(7)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_method_with_correct_data(self):
        self.assertEqual(self.some_list.get(0), 10)

    def test_insert_method_with_wrong_index(self):
        with self.assertRaises(IndexError) as ie:
            self.some_list.insert(7, 20)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_method_with_non_integer_element_raise_value_error(self):
        with self.assertRaises(ValueError) as ie:
            self.some_list.insert(1, "20")
        self.assertEqual("Element is not Integer", str(ie.exception))

    def test_insert_method_with_valid_Data(self):
        self.some_list.insert(1, 20)
        self.assertEqual(self.some_list._IntegerList__data, [10, 20, 30])
        self.assertEqual(self.some_list.get_data(), [10, 20, 30])

    def test_get_biggest(self):
        self.assertEqual(self.some_list.get_biggest(), 30)

    def test_get_index(self):
        result = self.some_list.get_index(10)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    main()
