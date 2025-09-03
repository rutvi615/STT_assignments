"""
lab1.py - Demonstrates Python basics for Lab Assignment 1.
Includes variables, functions, loops, and classes for Pylint testing.
"""

# Global variables
STUDENT = "Rutvi"
ROLL_NO = 22110227


def introduce(student_name: str, roll: int) -> str:
    """
    Return an introduction message.

    Args:
        student_name (str): The student's name.
        roll (int): The student's roll number.

    Returns:
        str: Introduction string.
    """
    return f"My name is {student_name} and my roll number is {roll}."


def square_numbers(numbers: list[int]) -> None:
    """
    Print squares of numbers in a list.

    Args:
        numbers (list[int]): List of integers.
    """
    print("\nSquares of numbers:")
    for num in numbers:
        print(f"{num}^2 = {num * num}")


def list_subjects(subject_list: list[str]) -> None:
    """
    Display the subjects taken by the student.

    Args:
        subject_list (list[str]): List of subject names.
    """
    print("\nSubjects enrolled:")
    for subject in subject_list:
        print(f"- {subject}")


class Vehicle:
    """Represent a simple vehicle."""

    def __init__(self, name: str, wheels: int) -> None:
        """
        Initialize the vehicle.

        Args:
            name (str): The vehicle name.
            wheels (int): Number of wheels.
        """
        self.name = name
        self.wheels = wheels

    def description(self) -> None:
        """Print the vehicle description."""
        print(f"{self.name} has {self.wheels} wheels.")

    def change_wheels(self, new_wheels: int) -> None:
        """Update the number of wheels."""
        self.wheels = new_wheels
        print(f"{self.name} now has {self.wheels} wheels.")


if __name__ == "__main__":
    print(introduce(STUDENT, ROLL_NO))

    nums = [2, 4, 6, 8]
    square_numbers(nums)

    subjects = ["Math", "Physics", "Computer Science"]
    list_subjects(subjects)

    bike = Vehicle("Bike", 2)
    bike.description()
    bike.change_wheels(3)
    bike.description()
