#!/usr/bin/env python

## Grade module 8 "write code that breaks" experiences

import sys
import os
import subprocess 
from data.student_info import github_usernames

MODULE_NUMBER = 8
PROJECT = "errors"

folder_name = "module_" + str(MODULE_NUMBER) + "_repos"
results = {}

# Create a directory to hold all repositories
os.mkdir(folder_name)

# Navigate into that directory
os.chdir(folder_name)

# One by one, clone the repo, navigate inside, test the code
for username in github_usernames:
    results[username] = ""
    url = "https://github.com/" + username + "/" + PROJECT + ".git"
    clone_path = username + "." + PROJECT
    try:
        # Clone the repo
        subprocess.check_output(["git", "clone", url, clone_path])
    except:
        print("Couldn't clone it :(")
        results[username] += "couldn't clone repository at " + url
        continue
    # Navigate  inside
    os.chdir(clone_path)
    ## Test the code
    # First find out how many times 'raise' is used
    raise_count = 0
    script = open("throw_err.py", 'r')
    code = script.readlines()
    script.close()
    for line in code:
        if line.startswith("#"):
            continue
        if "raise" in line and "usage" not in line:
            raise_count += 1
    # Flag the repo if it looks like a custom class is implemented:
    for line in code:
        if line.startswith("class"):
            results[username] += "custom class! "
    # Also flag if it looks like extra errors are implemented
    elif_count = 0
    for line in code:
        if line.startswith("elif"):
            elif_count += 1
    if elif_count > 9:
        results[username] += "extra errors? "
    # Next confirm that appropriate errors are thrown
    error_count = 0
    expected_errors = {
            "assertion": "AssertionError",
            "io": "IOError",
            "import": "ImportError",
            "index": "IndexError",
            "key": "KeyError",
            "name": "NameError",
            "os": "OSError",
            "type": "TypeError",
            "value": "ValueError",
            "zerodivision": "ZeroDivisionError"
            }
    for arg, error_type in expected_errors.items():
        print("now on arg %s" % arg)
        p = subprocess.Popen(["python", "throw_err.py", arg], 
                stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        if error_type in stderr:
            error_count += 1
    results[username] += "raise_count: " + str(raise_count) + ", "
    results[username] += "error_count: " + str(error_count)
    # Navigate back
    os.chdir("..")

# Print results
for user in github_usernames:
    print(user + ": " + results[user])
