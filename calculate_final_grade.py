#!/usr/bin/env python

import sys

# Check command line args
if len(sys.argv) != 4:
    sys.stderr.write("usage: python calculate_final_grade.py <assignment points> <blog points> <project points>\n")
    sys.exit()

# Attempt to parse command line args
assignment_points = int(sys.argv[1])
blog_points = int(sys.argv[2])
project_points = int(sys.argv[3])

# Calculate total points and determine letter grade
total_points = assignment_points + blog_points + project_points
if total_points >= 90:
    print("You get an 'A'")
elif total_points >= 80:
    print("You get an 'B'")
elif total_points >= 70:
    print("You get an 'C'")
elif total_points >= 60:
    print("You get an 'D'")
else:
    print("You get an 'F'")
