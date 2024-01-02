from unittest import TestCase, main
from extended_list import IntegerList

class IntegerListTest(TestCase):
    def setUp(self) -> None:
        self.integers = IntegerList("1", 2, 3, True, False, "test", 4.5)

    def test_correct_initialization(self):
        self.assertEqual([2, 3], self.integers._IntegerList__data)

    def test_get_data(self):
        self.assertEqual([2, 3], self.integers.get_data())


    def test_add_data_with_integet_numeber(self):
        self.integers.add(4)
        self.assertEqual([2, 3, 4], self.integers.get_data())
        self.assertEqual([2, 3, 4], self.integers._IntegerList__data)


    def test_add_data_with_wrong_type(self):
        with self.assertRaises(ValueError) as ve:
            self.integers.add("test")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_wrong_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integers.remove_index(4)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_in_range(self):
        self.integers.remove_index(0)
        self.assertEqual([3], self.integers.get_data())
        self.assertEqual([3], self.integers._IntegerList__data)

    def test_get_wrong_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integers.get(4)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_index_in_range(self):
        self.assertEqual(2, self.integers.get(0))

    def test_insert_index_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.integers.insert(4, 6)
        self.assertEqual("Index is out of range", str(ie.exception))


    def test_insert_index_in_range_and_correct_type(self):
        self.integers.insert(1, 5)
        self.assertEqual([2,5,3], self.integers.get_data())
        self.assertEqual([2,5,3], self.integers._IntegerList__data)

    def test_insert_index_in_range_and_wrong_type(self):
        with self.assertRaises(ValueError) as ve:
            self.integers.insert(1, 6.5)
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_get_biggest(self):
        self.assertEqual(3, self.integers.get_biggest())

    def test_get_index(self):
        self.assertEqual(0, self.integers.get_data().index(2) )

    def test_get_index2(self):
        result = self.integers.get_index(2)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    main()