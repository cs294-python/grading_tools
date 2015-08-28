#!/usr/bin/env python

from sys import argv, stderr, exit

# Check command line args
if len(argv) != 4:
    stderr.write("usage: python calculate_final_grade.py <assignment points> <blog points> <project points>\n")
    exit()

# Attempt to parse command line args
assignment_points = float(argv[1])
blog_points = float(argv[2])
project_points = float(argv[3])

# Check that points are within range.
if assignment_points > 35:
    print("Please enter a value less than or equal to 35 for assignment points.")
if blog_points > 25:
        print("Please enter a value less than or equal to 25 for blog points.")
if project_points > 50:
        print("Please enter a value less than or equal to 50 for project points.")

# Calculate total points and determine letter grade
total_points = assignment_points + blog_points + project_points
if (assignment_points <= 35) and (blog_points <= 25) and (project_points <= 50):
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
