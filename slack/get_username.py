#!/usr/bin/env python

import sys
import json
import argparse

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('user_id')
    parser.add_argument('filename')
    args = parser.parse_args()

    # Read file
    with open(args.filename, 'r') as json_file:
        contents = json_file.read()
        json_object = json.loads(contents)

    # Make sure that worked
    if not json_object:
        sys.stderr.write("Error reading json file\n")
        sys.exit()

    # Loop over user entries
    for entry in json_object:
        if entry['id'] == args.user_id:
            print(entry['real_name'])
            sys.exit()


##########################

if __name__ == '__main__':
    main()
