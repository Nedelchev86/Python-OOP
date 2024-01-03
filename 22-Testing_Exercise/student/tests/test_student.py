from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = Student("Tihomir")
        self.student2 = Student("Ivan", {"A": ["test"]})

    def test_initialization_with_no_courses(self):
        self.assertEqual(self.student.name, "Tihomir")
        self.assertEqual(self.student.courses, {})

    def test_initialization_with_courses(self):
        self.assertEqual(self.student2.name, "Ivan")
        self.assertEqual(self.student2.courses, {"A": ["test"]})

    def test_enroll_with_course_name_already_added_and(self):
        result = self.student2.enroll("A", ["test2", "test3"],)
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(self.student2.courses, {"A": ["test", "test2", "test3"]})
        self.assertEqual(self.student2.courses["A"], ["test", "test2", "test3"])

    def test_enroll_with_course_name_already_added_and_yes(self):
        result = self.student.enroll("A", ["test2", "test3"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(self.student.courses, {"A": ["test2", "test3"]})

    def test_enroll_with_course_name_already_added_and_empty_string(self):
        result = self.student.enroll("A", ["test2", "test3"])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(self.student.courses, {"A": ["test2", "test3"]})

    def test_enroll_with_course_name_already_added_and_now(self):
        result = self.student.enroll("A", ["test2", "test3"], "N")
        self.assertEqual("Course has been added.", result)
        self.assertEqual(self.student.courses, {"A": []})

    def test_add_notes_with_Existing_course(self):
        result = self.student2.add_notes("A", "test2")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(self.student2.courses["A"], ["test", "test2"])

    def test_add_notes_with_wrong_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("A", "test2")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_existing_course(self):
        result = self.student2.leave_course("A")
        self.assertEqual("Course has been removed", result)
        self.assertEqual(self.student2.courses, {})

    def test_leave_course_with_wrong_course_name(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("A")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()