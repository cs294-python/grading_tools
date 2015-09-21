#!/usr/bin/env python

import sys
import os
import subprocess 
from data.student_info import github_usernames

MODULE_NUMBER = 6
PROJECT = "debug_me"

folder_name = "module_" + str(MODULE_NUMBER) + "_repos"
results = {}

# Create a directory to hold all repositories
os.mkdir(folder_name)

# Navigate into that directory
os.chdir(folder_name)

# One by one, clone the repo, navigate inside, test the code
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
    # Test the code
    try:
        subprocess.check_call(["python", "add_five.py", "4"])
    except:
        # This means the script threw an error; it's not supposed to
        results[username] = "code threw an error"
        print("Error in code...")
        os.chdir("..")
        continue
    results[username] = "correct"
    print("Correct!\n")
    # Navigate back
    os.chdir("..")

# Print results
for user in github_usernames:
    print(user + ": " + results[user])
