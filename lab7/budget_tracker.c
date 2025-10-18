// budget_tracker.c
// A simple command-line personal budget tracker.
// Users can add income and expenses, view all transactions, and see a summary.
// This program is designed for control-flow and data-flow analysis.
// LOC: ~250

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_TRANSACTIONS 100
#define MAX_DESC_LENGTH 100

// Structure to define a single financial transaction
typedef struct {
    char type; // 'I' for Income, 'E' for Expense
    char description[MAX_DESC_LENGTH];
    double amount;
} Transaction;

// Global array to store all transactions and a counter
Transaction transactions[MAX_TRANSACTIONS];
int transactionCount = 0;

// Function Prototypes
void printMenu();
void addTransaction(char type);
void viewAllTransactions();
void viewSummary();
void clearInputBuffer();

int main() {
    int choice = 0;
    int running = 1; // Main loop control variable

    printf("--- Personal Budget Tracker ---\n");

    // Main application loop
    while (running) {
        printMenu();
        printf("Enter your choice: ");

        // Read user choice and handle non-integer input
        if (scanf("%d", &choice) != 1) {
            printf("\nError: Invalid input. Please enter a number between 1 and 5.\n");
            clearInputBuffer(); // Clear the faulty input
            continue; // Skip the rest of the loop
        }
        clearInputBuffer(); // Clear the newline character

        // Switch statement to direct control flow based on user choice
        switch (choice) {
            case 1:
                addTransaction('I'); // Income
                break;
            case 2:
                addTransaction('E'); // Expense
                break;
            case 3:
                viewSummary();
                break;
            case 4:
                viewAllTransactions();
                break;
            case 5:
                printf("Exiting the budget tracker. Goodbye!\n");
                running = 0; // Set flag to terminate the while loop
                break;
            default:
                printf("\nError: Invalid choice. Please select an option from 1 to 5.\n");
                break;
        }
        printf("\n"); // Add a newline for better formatting
    }

    return 0;
}

/**
 * @brief Clears any remaining characters from the standard input buffer.
 * Useful after scanf to prevent issues with subsequent fgets calls.
 */
void clearInputBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

/**
 * @brief Displays the main menu options to the user.
 */
void printMenu() {
    printf("\n--- Main Menu ---\n");
    printf("1. Add Income\n");
    printf("2. Add Expense\n");
    printf("3. View Financial Summary\n");
    printf("4. View All Transactions\n");
    printf("5. Exit\n");
}

/**
 * @brief Adds a new transaction (either income or expense) to the records.
 * @param type A character indicating the transaction type ('I' or 'E').
 */
void addTransaction(char type) {
    // Conditional check to prevent buffer overflow
    if (transactionCount >= MAX_TRANSACTIONS) {
        printf("Error: Maximum number of transactions reached.\n");
        return;
    }

    // Set the transaction type
    transactions[transactionCount].type = type;

    // Get description from the user
    if (type == 'I') {
        printf("Enter income description: ");
    } else {
        printf("Enter expense description: ");
    }
    fgets(transactions[transactionCount].description, MAX_DESC_LENGTH, stdin);
    // Remove the trailing newline character from fgets
    transactions[transactionCount].description[strcspn(transactions[transactionCount].description, "\n")] = 0;

    // Get amount from the user
    double amount = 0.0;
    printf("Enter amount: ");
    if (scanf("%lf", &amount) != 1 || amount <= 0) {
        printf("Error: Invalid amount. Please enter a positive number.\n");
        clearInputBuffer();
        return;
    }
    clearInputBuffer();

    transactions[transactionCount].amount = amount; // Assignment

    // Increment the global transaction counter
    transactionCount++; // Reassignment

    printf("Transaction added successfully!\n");
}

/**
 * @brief Displays a detailed list of all recorded transactions.
 */
void viewAllTransactions() {
    printf("\n--- All Transactions ---\n");

    // Conditional check for empty records
    if (transactionCount == 0) {
        printf("No transactions recorded yet.\n");
        return;
    }

    printf("--------------------------------------------------\n");
    printf("%-10s | %-30s | %-10s\n", "Type", "Description", "Amount");
    printf("--------------------------------------------------\n");

    // Loop through the array to print each transaction
    int i = 0; // Loop counter initialization
    for (i = 0; i < transactionCount; i++) { // Reassignment of 'i' in each iteration
        char typeStr[8];
        if (transactions[i].type == 'I') {
            strcpy(typeStr, "Income");
        } else {
            strcpy(typeStr, "Expense");
        }
        printf("%-10s | %-30s | $%-9.2f\n",
               typeStr,
               transactions[i].description,
               transactions[i].amount);
    }
    printf("--------------------------------------------------\n");
}

/**
 * @brief Calculates and displays a summary of total income, expenses, and net balance.
 */
void viewSummary() {
    printf("\n--- Financial Summary ---\n");

    if (transactionCount == 0) {
        printf("No transactions to summarize.\n");
        return;
    }

    // Initialize accumulator variables
    double totalIncome = 0.0;
    double totalExpense = 0.0;
    double balance = 0.0;

    // Loop through all transactions to aggregate data
    int i = 0;
    for (i = 0; i < transactionCount; i++) {
        // Conditional logic inside the loop
        if (transactions[i].type == 'I') {
            totalIncome += transactions[i].amount; // Reassignment
        } else {
            totalExpense += transactions[i].amount; // Reassignment
        }
    }

    // Final calculation and assignment
    balance = totalIncome - totalExpense;

    // Print the final summary
    printf("Total Income:   $%.2f\n", totalIncome);
    printf("Total Expenses: $%.2f\n", totalExpense);
    printf("---------------------------\n");
    printf("Net Balance:    $%.2f\n", balance);
    printf("---------------------------\n");
}