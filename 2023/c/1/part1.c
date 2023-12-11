/**
 *  Advent Of Code 2023 Day 1 Part 1
 *
 *  @file       part1.c
 *  @author     Eirikalv1
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

const int STRLEN = 150;     ///< Max length of line
const int NLINES = 1001;    ///< Number of lines + \0

int left_number(char line[STRLEN]);
void read_from_file(char lines[NLINES][STRLEN]);

/**
 *  Main program.
*/
int main() {
    char lines[NLINES][STRLEN];
     for (int i = 0; i < NLINES; ++i) {
        lines[i][0] = '\0';
    }
    read_from_file(lines);

    int total = 0;
    int i = 0;
    while (lines[i][0]) {
        char number[3];
        number[0] = left_number(lines[i]);
        number[1] = left_number(strrev(lines[i++]));
        number[2] = '\0';
        total += atoi(number);
    }
    printf("%i", total);

    return 0;
}

/**
 *  Finds the left most number in string,
 *  crashes if none.
 *
 *  @param  line    - A line containing numbers
 *  
 *  @return The number it found
*/
int left_number(char line[STRLEN]) {
    for (int i = 0; i < strlen(line); i++) {
        if (isdigit(line[i])) return line[i];
    }
    exit(-1);
}

/**
 *  Reads from file input.txt.
 *
 *  @param  lines   - Pointer to an array of lines.
*/
void read_from_file(char lines[NLINES][STRLEN]) {
    FILE* file = fopen("input.txt", "r");
    if (!file) exit(-1); 
    
    int i = 0;
    while (!feof(file) && i < NLINES - 1) {
        fgets(lines[i++], STRLEN, file);
    }
    fclose(file);
}