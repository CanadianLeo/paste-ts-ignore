#!/usr/bin/python
# -*- coding: latin-1 -*-

import os
import sys

# Write tsc output in file 
os.system('tsc > tscErrors.txt')
print('tsc was finish')

file = open('tscErrors.txt', 'r')

# Current open file
curr_file = ''

# Count of errors
count = 0

for line in file:
    # Parse the line
    line = line.replace('(', ' ')
    line = line.replace(')', ' ')
    arr = line.split(' ')

    # Check first element (if our tsc write long line)
    if arr[0] != '':
        # If current file is not equals arr[0] then we reset all counters
        if curr_file != arr[0]:
            # Current line
            curr_line = -1
            # Current offset
            offset = -1
            # Change current file
            curr_file = arr[0]
        if len(arr[0]) - arr[0].rfind('.ts') == 3:
            count += 1

            editing_file = open(arr[0], 'r', encoding='utf-8')

            # Get line where we need use ts-igonre
            point = arr[1].split(',')[0]

            # To not comment on the same line twice
            if curr_line != point:

                offset += 1
                curr_line = point

                # Parse opening file
                lines_in_file = editing_file.read().split('\n')
                editing_file.close()

                i = 0
                final_text = ''
                for line_in_file in lines_in_file:
                    i += 1

                    # If true then our current position is necessary
                    if i - offset == int(point) :
                        # Count of spaces
                        count_of_spaces = len(line_in_file) - len(line_in_file.lstrip())

                        final_text += count_of_spaces * ' ' + '// @ts-ignore\n'
                    final_text += line_in_file + '\n'   

                # Open file for writing
                editing_file = open(arr[0], 'w', encoding='utf-8')
                # Delete all \n from the end of file and add one
                editing_file.write(final_text.rstrip('\n') + '\n')
                editing_file.close()
file.close()

print('Was comment ' + str(count) + ' errors!\n')

# tsc for show output
os.system('tsc');

os.remove('tscErrors.txt')
print('Success!!!')