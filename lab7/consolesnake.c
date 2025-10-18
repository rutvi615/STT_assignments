// console_snake.c
// A simple implementation of the classic Snake game in the terminal.
// This program uses loops for game state and rendering, and conditionals for logic.
// Note: This version is simplified and may not have perfect input handling on all systems.
// LOC: ~250

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// On Windows, use conio.h for non-blocking input.
// On Linux/macOS, a more complex setup (like ncurses) is needed for the same effect.
// This code uses a simple getchar() for portability.
#ifdef _WIN32
#include <conio.h>
#include <windows.h>
#else
#include <unistd.h>
#define Sleep(x) usleep((x)*1000)
#endif


#define WIDTH 40
#define HEIGHT 20

// Global variables for game state
int x, y, fruitX, fruitY, score, tailLength, gameOver;
int tailX[100], tailY[100]; // Snake's body coordinates

// Enum for direction
typedef enum { STOP = 0, LEFT, RIGHT, UP, DOWN } Direction;
Direction dir;

// Function Prototypes
void setup();
void draw();
void input();
void logic();

int main() {
    setup(); // Initialize game state

    // Main game loop
    while (!gameOver) {
        draw();
        input();
        logic();
        Sleep(100); // Slow down the game
    }

    printf("\n--- GAME OVER ---\n");
    printf("Final Score: %d\n", score);

    return 0;
}

// Initializes game variables and state
void setup() {
    gameOver = 0;
    dir = STOP;
    x = WIDTH / 2; // Start snake in the middle
    y = HEIGHT / 2;

    srand(time(NULL)); // Seed for random number generation
    fruitX = rand() % WIDTH; // Place fruit at a random position
    fruitY = rand() % HEIGHT;

    score = 0;
    tailLength = 0;
}

// Renders the game board to the console
void draw() {
    // Clear the screen (system-dependent)
    #ifdef _WIN32
    system("cls");
    #else
    system("clear");
    #endif

    // Top border
    int i = 0;
    for (i = 0; i < WIDTH + 2; i++) {
        printf("#");
    }
    printf("\n");

    // Game area
    int j = 0;
    for (i = 0; i < HEIGHT; i++) {
        for (j = 0; j < WIDTH; j++) {
            if (j == 0) {
                printf("#"); // Left border
            }

            // Check if current coordinate is the snake's head
            if (i == y && j == x) {
                printf("O");
            }
            // Check for fruit
            else if (i == fruitY && j == fruitX) {
                printf("F");
            }
            // Check for tail segments
            else {
                int isTailSegment = 0;
                int k = 0;
                for (k = 0; k < tailLength; k++) {
                    if (tailX[k] == j && tailY[k] == i) {
                        printf("o");
                        isTailSegment = 1;
                        break;
                    }
                }
                if (!isTailSegment) {
                    printf(" ");
                }
            }

            if (j == WIDTH - 1) {
                printf("#"); // Right border
            }
        }
        printf("\n");
    }

    // Bottom border
    for (i = 0; i < WIDTH + 2; i++) {
        printf("#");
    }
    printf("\n");
    printf("Score: %d\n", score);
    printf("Controls: W (Up), A (Left), S (Down), D (Right), X (Exit)\n");
}

// Handles user input to change snake's direction
void input() {
    char ch;
    // Non-blocking input check
    #ifdef _WIN32
    if (_kbhit()) {
        ch = _getch();
    #else
    // This is a simplified version for non-Windows.
    // A better implementation would use ncurses or select().
    // For this lab, we assume simple blocking input.
    printf("Enter move: ");
    ch = getchar();
    while(getchar() != '\n'); // Clear buffer
    {
    #endif
        switch (ch) {
            case 'a':
                if (dir != RIGHT) dir = LEFT;
                break;
            case 'd':
                if (dir != LEFT) dir = RIGHT;
                break;
            case 'w':
                if (dir != DOWN) dir = UP;
                break;
            case 's':
                if (dir != UP) dir = DOWN;
                break;
            case 'x':
                gameOver = 1;
                break;
        }
    }
}


// Updates the game state based on game rules
void logic() {
    // Logic for updating the tail position
    int prevX = tailX[0];
    int prevY = tailY[0];
    int prev2X, prev2Y;
    tailX[0] = x;
    tailY[0] = y;
    int i = 0;
    for (i = 1; i < tailLength; i++) {
        prev2X = tailX[i];
        prev2Y = tailY[i];
        tailX[i] = prevX;
        tailY[i] = prevY;
        prevX = prev2X;
        prevY = prev2Y;
    }

    // Update head position based on direction
    switch (dir) {
        case LEFT:
            x--;
            break;
        case RIGHT:
            x++;
            break;
        case UP:
            y--;
            break;
        case DOWN:
            y++;
            break;
        default:
            break;
    }

    // Check for collision with walls
    if (x >= WIDTH || x < 0 || y >= HEIGHT || y < 0) {
        gameOver = 1;
    }

    // Check for collision with tail
    for (i = 0; i < tailLength; i++) {
        if (tailX[i] == x && tailY[i] == y) {
            gameOver = 1;
        }
    }

    // Check for eating fruit
    if (x == fruitX && y == fruitY) {
        score += 10; // Increase score
        tailLength++; // Grow the snake
        // Generate new fruit position
        fruitX = rand() % WIDTH;
        fruitY = rand() % HEIGHT;
    }
}