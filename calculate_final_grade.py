#!/usr/bin/env python

from sys import argv, stderr, exit

# Check command line args
if len(argv) != 4:
    stderr.write("usage: python calculate_final_grade.py <assignment points> <blog points> <project points>\n")
    exit()

# Attempt to parse command line args
assignment_points = int(argv[1])
blog_points = int(argv[2])
project_points = int(argv[3])

# Calculate total points and determine letter grade
total_points = assignment_points + blog_points + project_points
if total_points >= 90:
    print("You get an 'A'")
elif total_points >= 80:
    print("You get a 'B'")
elif total_points >= 70:
    print("You get a 'C'")
elif total_points >= 60:
    print("You get a 'D'")
else:
    print("You get an 'F'")
