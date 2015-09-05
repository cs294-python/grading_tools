#!/usr/bin/env python

import sys
import os
import subprocess 
from data.student_info import github_usernames

MODULE_NUMBER = 4
PROJECT = "vim_lessons"

folder_name = "module_" + str(MODULE_NUMBER) + "_repos"
results = {}

# Create a directory to hold all repositories
os.mkdir(folder_name)

# Navigate into that directory
os.chdir(folder_name)

# One by one, clone the repo, navigate inside, test the poem
for username in github_usernames:
    url = "https://github.com/" + username + "/" + PROJECT + ".git"
    clone_path = username + "." + PROJECT
    try:
        # Clone the repo
        subprocess.check_call(["git", "clone", url, clone_path])
    except:
        results[username] = "couldn't clone repository at " + url
        print("Couldn't find it :/\n")
        continue
    # Navigate  inside
    os.chdir(clone_path)
    # Test the poem
    with open("poetry/walt_whitman", 'r') as poem:
        poem_is_correct = True
        for line in poem:
            if "YOLO" in line:
                poem_is_correct = False
        if poem_is_correct:
            results[username] = "correct"
            print("Correct!\n")
        else:
            results[username] == "poem contains 'YOLO'"
            print("Not fixed :/\n")
    # Navigate back
    os.chdir("..")

# Print results
for user in github_usernames:
    print(user + "\t" + results[user])
