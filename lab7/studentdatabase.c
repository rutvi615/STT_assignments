// student_database.c
// A simple command-line student database management system.
// This program allows adding, displaying, searching, and deleting student records.
// LOC: ~230

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_STUDENTS 100
#define MAX_NAME_LENGTH 50

// Structure to define a student record
typedef struct {
    int rollNumber;
    char name[MAX_NAME_LENGTH];
    float marks;
    int isActive; // Use 1 for active, 0 for deleted
} Student;

// Global database array and student count
Student database[MAX_STUDENTS];
int studentCount = 0;

// Function Prototypes
void addStudent();
void displayAllStudents();
void findStudentByRollNumber();
void deleteStudent();
void updateStudent();
void printMenu();
int findStudentIndex(int rollNumber);

int main() {
    int choice = 0;
    int running = 1; // Loop control variable

    printf("--- Student Database Management System ---\n");

    while (running) {
        printMenu();
        printf("Enter your choice: ");
        scanf("%d", &choice);

        // Clear the input buffer
        while(getchar() != '\n');

        switch (choice) {
            case 1:
                addStudent();
                break;
            case 2:
                displayAllStudents();
                break;
            case 3:
                findStudentByRollNumber();
                break;
            case 4:
                deleteStudent();
                break;
            case 5:
                updateStudent();
                break;
            case 6:
                printf("Exiting program. Goodbye!\n");
                running = 0; // Terminate the loop
                break;
            default:
                printf("Invalid choice. Please try again.\n");
                break;
        }
        printf("\n");
    }

    return 0;
}

// Displays the main menu options
void printMenu() {
    printf("\n--- Main Menu ---\n");
    printf("1. Add a new student\n");
    printf("2. Display all students\n");
    printf("3. Find a student by Roll Number\n");
    printf("4. Delete a student\n");
    printf("5. Update a student's marks\n");
    printf("6. Exit\n");
}

// Adds a new student to the database
void addStudent() {
    if (studentCount >= MAX_STUDENTS) {
        printf("Error: Database is full. Cannot add more students.\n");
        return;
    }

    int newRollNumber;
    printf("Enter Roll Number: ");
    scanf("%d", &newRollNumber);

    // Check if roll number already exists
    if (findStudentIndex(newRollNumber) != -1) {
        printf("Error: A student with Roll Number %d already exists.\n", newRollNumber);
        while(getchar() != '\n'); // Clear buffer
        return;
    }

    database[studentCount].rollNumber = newRollNumber;

    printf("Enter Name: ");
    // Clear buffer before reading string
    while(getchar() != '\n');
    fgets(database[studentCount].name, MAX_NAME_LENGTH, stdin);
    // Remove trailing newline character from fgets
    database[studentCount].name[strcspn(database[studentCount].name, "\n")] = 0;

    printf("Enter Marks: ");
    scanf("%f", &database[studentCount].marks);

    database[studentCount].isActive = 1; // Mark as active
    studentCount++;

    printf("Student added successfully!\n");
}

// Displays all active student records
void displayAllStudents() {
    printf("\n--- List of All Students ---\n");
    if (studentCount == 0) {
        printf("No students in the database.\n");
        return;
    }

    int i = 0;
    int foundActiveStudents = 0;
    for (i = 0; i < studentCount; i++) {
        if (database[i].isActive == 1) {
            printf("------------------------------------\n");
            printf("Roll Number: %d\n", database[i].rollNumber);
            printf("Name: %s\n", database[i].name);
            printf("Marks: %.2f\n", database[i].marks);
            foundActiveStudents++;
        }
    }

    if (foundActiveStudents == 0) {
        printf("No active student records found.\n");
    } else {
        printf("------------------------------------\n");
        printf("Total active students: %d\n", foundActiveStudents);
    }
}

// Finds and returns the array index of a student by roll number
int findStudentIndex(int rollNumber) {
    int i = 0;
    for (i = 0; i < studentCount; i++) {
        // Search only active records
        if (database[i].rollNumber == rollNumber && database[i].isActive == 1) {
            return i; // Return the index if found
        }
    }
    return -1; // Return -1 if not found
}

// Wrapper function to find and display a student
void findStudentByRollNumber() {
    int rollNumber;
    printf("Enter Roll Number to find: ");
    scanf("%d", &rollNumber);

    int index = findStudentIndex(rollNumber);

    if (index != -1) {
        printf("\n--- Student Found ---\n");
        printf("Roll Number: %d\n", database[index].rollNumber);
        printf("Name: %s\n", database[index].name);
        printf("Marks: %.2f\n", database[index].marks);
    } else {
        printf("Student with Roll Number %d not found.\n", rollNumber);
    }
}

// Logically deletes a student by setting their isActive flag to 0
void deleteStudent() {
    int rollNumber;
    printf("Enter Roll Number to delete: ");
    scanf("%d", &rollNumber);

    int index = findStudentIndex(rollNumber);

    if (index != -1) {
        database[index].isActive = 0; // "Delete" the student
        printf("Student with Roll Number %d has been deleted.\n", rollNumber);
    } else {
        printf("Error: Student with Roll Number %d not found.\n", rollNumber);
    }
}

// Updates the marks of an existing student
void updateStudent() {
    int rollNumber;
    printf("Enter Roll Number to update marks: ");
    scanf("%d", &rollNumber);

    int index = findStudentIndex(rollNumber);

    if (index != -1) {
        float newMarks;
        printf("Current Marks: %.2f\n", database[index].marks);
        printf("Enter new Marks: ");
        scanf("%f", &newMarks);

        database[index].marks = newMarks; // Reassignment of marks
        printf("Marks updated successfully for Roll Number %d.\n", rollNumber);
    } else {
        printf("Error: Student with Roll Number %d not found.\n", rollNumber);
    }
}