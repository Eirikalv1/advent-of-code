#include <stdio.h>
#include <stdlib.h>


char**  grid;
int     nLines, lineLen;


void    fallAllRocks();
void    fallRock(int x, int y);
int     getScore();
void    memAllocForFile();
void    memDeAllocForFile();
int     rowLenInFile(FILE* file);
int     nRowsInFile(FILE* file);
void    readFile();


int main() {
    readFile();


    fallAllRocks();

    int score = getScore();
    printf("Answer: %i\n", score);


    memDeAllocForFile();
    return 0;
}


void fallAllRocks() {
    for (int y = 0; y < nLines; y++) {
        for (int x = 0; x < lineLen - 2; x++) {
            fallRock(x, y);
        }
    }
}


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


int getScore() {
    int score = 0;

    for (int y = 0; y < nLines; y++) {
        for (int x = 0; x < lineLen - 2; x++) {
            if (grid[y][x] == 'O') score += nLines - y;
        }
    }

    return score;
}


void memAllocForFile() {
    grid = (char**) malloc(nLines * sizeof(char*));
    if (!grid) exit(1);
    
    for (int i = 0; i < nLines; i++) {
        grid[i] = (char*) malloc(lineLen * sizeof(char));
        if (!grid[i]) exit(1);
    }
}


void memDeAllocForFile() {
    for (int i = 0; i < nLines; i++) {
        free(grid[i]);
    }

    free(grid);
}


int nRowsInFile(FILE* file) {
    int count = 1;

    while (!feof(file)) {
        if (fgetc(file) == '\n') count++;
    }

    fseek(file, 0, SEEK_SET);

    return count;
}


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


int rowLenInFile(FILE* file) {
    int count = 2;
    while (fgetc(file) != '\n') count++;

    fseek(file, 0, SEEK_SET);

    return count;
}