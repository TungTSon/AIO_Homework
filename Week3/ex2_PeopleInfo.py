from abc import ABC, abstractmethod
import numpy as np


class People(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass


class Student(People):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f">> Student - Name: {self._name} - YoB: {self._yob}, Grade: {self.__grade}")


class Teacher(People):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f">> Teacher - Name: {self._name} - YoB: {self._yob}, Subject: {self.__subject}")


class Doctor(People):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f">> Doctor - Name: {self._name} - YoB: {self._yob}, Specialist: {self.__specialist}")


class Ward:
    def __init__(self, wardname):
        self.__wardname = wardname  # initialize the name of ward
        self.__people = []    # a list to store infor of added people

    def add_person(self, person):   # add new people to the Ward
        self.__people.append(person)

    def describe(self):
        print(f"Ward Name: {self.__wardname}")  # print out the Ward name
        for person in self.__people:
            person.describe()   # Calls the describe() method from the respective subclass

    def count_doctor(self):
        return sum(isinstance(person, Doctor) for person in self.__people)

    def sort_age(self):  # method to sort age of people
        print(f">> After sorting Age of {self.__wardname} people")
        print(f"Ward Name: {self.__wardname}")  # print out the Ward name first

        self.__people.sort(reverse=True, key=lambda person: person._yob)
        for person in self.__people:
            person.describe()

    def compute_average_age(self, class_name):
        return np.mean([person._yob for person in self.__people if isinstance(person, class_name)])


if __name__ == "__main__":
    # Test case: 2(a)
    print("\n---------------------------------- 2a --------------------------------------")
    student1 = Student(name="studentA", yob=2010, grade="7")
    student1.describe()
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher1.describe()
    doctor1 = Doctor(name="doctorA", yob=1945,
                     specialist="Endocrinologists")
    doctor1.describe()

    # Test case: 2(b)
    print("\n---------------------------------- 2b --------------------------------------")
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
    ward1 = Ward(wardname="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()

    # Test case: 2(c)
    print("\n---------------------------------- 2c --------------------------------------")
    print(f"Number of doctors: {ward1.count_doctor()}")

    # Test case: 2(d)
    print("\n---------------------------------- 2d --------------------------------------")
    ward1.sort_age()

    # Test case: 2(e)
    print("\n---------------------------------- 2e --------------------------------------")
    print(
        f"Average year of birth (teachers): {ward1.compute_average_age(Teacher)}")
