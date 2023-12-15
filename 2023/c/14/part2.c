/**
 *  Advent Of Code 2023 Day 14 Part 2
 *
 *  @file       part1.c
    @author     Eirikalv1
 */


#include <stdio.h>
#include <stdlib.h>


#define     SCOPE           1000    //< Pattern range
const int   TOTAL_CYCLES =  1000000000;


char**  grid;
int     nLines, lineLen;
int     scores[SCOPE];     


void    cycle();
void    fallAllRocks();
void    fallRock(int x, int y);
int     getScore();
void    memAllocForFile();
void    memDeAllocForFile();
void    populateScores();
int     rowLenInFile(FILE* file);
int     nRowsInFile(FILE* file);
void    readFile();
void    rotateGrid();
int     scoreDiff(int index);


/**
 *  Main Program
 */
int main() {
    readFile();

    
    populateScores();
    
    for (int i = 0; i < SCOPE; i++) {
        int diff = scoreDiff(i);
        if (diff == 0) continue;

        if ((TOTAL_CYCLES - (i + 1)) % diff == 0) {
            printf("Answer: %i\n", scores[i]);
            break;
        } 
    }
    
    memDeAllocForFile();
    return 0;
}


/**
 *  Rotate grid and fall rocks x4
 *
 *  @see    fallAllRocks(...)
 *  @see    rotateGrid(...)
 */
void cycle() {
    for (int i = 0; i < 4; i++) {
        fallAllRocks();
        rotateGrid();
    }
}


/**
 *  Make all rocks fall
 * 
 *  @see    fallrock(...)
*/
void fallAllRocks() {
    for (int y = 0; y < nLines; y++) {
        for (int x = 0; x < lineLen - 2; x++) {
            fallRock(x, y);
        }
    }
}


/**
 *  Logic for falling rock
 *
 *  @param  x   - x coord in grid
 *  @param  y   - y coord in grid
*/
void fallRock(int x, int y) {
    if (grid[y][x] != 'O') return;

    grid[y][x] = '.';

    while (nLines > y - 1 && y - 1 >= 0 
        && lineLen - 2 > x && x >= 0) {
            
            if (grid[y - 1][x] == '.') y -= 1;
            else break;
    }

    grid[y][x] = 'O';
}


/**
 *  Calculate score for each rock
 *
 *  @return Calculated score
 */
int getScore() {
    int score = 0;

    for (int y = 0; y < nLines; y++) {
        for (int x = 0; x < lineLen - 2; x++) {
            if (grid[y][x] == 'O') score += nLines - y;
        }
    }

    return score;
}


/**
 *  Allocate memory for each row and column in grid
 */
void memAllocForFile() {
    grid = (char**) malloc(nLines * sizeof(char*));
    if (!grid) exit(1);
    
    for (int i = 0; i < nLines; i++) {
        grid[i] = (char*) malloc(lineLen * sizeof(char));
        if (!grid[i]) exit(1);
    }
}


/**
 *  Free grid
 */
void memDeAllocForFile() {
    for (int i = 0; i < nLines; i++) {
        free(grid[i]);
    }

    free(grid);
}


/**
 *  Get the score for cycles within SCOPE 
 *
 *  @see    cycle(...)
 *  @see    getScore(...)
*/
void populateScores() {
    for (int i = 0; i < SCOPE; i++) {
        cycle();

        scores[i] = getScore();
    }
}


/**
 *  Find amount of lines in file
 *
 *  @param  file    - input.txt
 *
 *  @return Amount of lines
 */
int nRowsInFile(FILE* file) {
    int count = 1;

    while (!feof(file)) {
        if (fgetc(file) == '\n') count++;
    }

    fseek(file, 0, SEEK_SET);

    return count;
}


/**
 *  Reads input.txt
 *
 *  @see    memAllocForFile(...)
 *  @see    nRowsInFile(...)
 *  @see    rowLenInFile(...)
 */
void readFile() {
    FILE* file = fopen("input.txt", "r");
    if (!file) exit(1);

    nLines  = nRowsInFile(file);
    lineLen = rowLenInFile(file);
    
    memAllocForFile();

    int i = 0;
    while (i < nLines) {
        fgets(grid[i], lineLen, file);
        i++;
    }

    fclose(file);
}


/**
 *  Find length of each line
 *
 *  @param  file    - input.txt
 *
 *  @return Amount of chars in line
 */
int rowLenInFile(FILE* file) {
    int count = 2;
    while (fgetc(file) != '\n') count++;

    fseek(file, 0, SEEK_SET);

    return count;
}


/**
 *  Rotate the grid clockwise (right)
 */
void rotateGrid() {
    for (int y = 0; y < nLines; y++) {
        for (int x = y + 1; x < lineLen - 2; x++) {
            char temp = grid[y][x];
            
            grid[y][x] = grid[x][y];
            grid[x][y] = temp;
        }
    }

    for (int y = 0; y < nLines; y++) {
        for (int x = 0; x < lineLen / 2 - 1; x++) {
            char temp = grid[y][x];
            grid[y][x] = grid[y][lineLen - x - 3];
            grid[y][lineLen - x - 3] = temp;
        }
    }
}


/**
 *  Find patterns
 *
 *  @param  index   - Index within SCOPE
 *
 *  @return The difference between two scores
 */
int scoreDiff(int index) {
    int diff = 0;

    for (int i = index + 1; i < SCOPE; i++) {
        if (scores[i] == scores[index]) {
            diff = i - index;
            break;
        }
    }

    if (diff == 0) return 0;
    
    for (int i = index; i + diff < SCOPE; i += diff) {
        if (scores[i] != scores[index]) return 0;
    }

    return diff;
}