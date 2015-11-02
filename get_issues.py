#!/usr/bin/env python

import requests
import json
from data.project_urls import urls

def parse_request_url(url):
    """Take a github project url, return username and issues API request url"""
    # urls look like "https://github.com/nynhle/competitive_scraper"
    split_url = url.split('/')
    username = split_url[-2]
    project_name = split_url[-1]
    request_url = "https://api.github.com/repos/{0}/{1}/issues".format(
                    username, project_name)
    return username, request_url

for url in urls:
    # Fetch data from API
    username, request_url = parse_request_url(url)
    response = requests.get(request_url)
    if response.status_code != 200:
        print("Error fetching data for {0} -- skipping.".format(url))
        continue
    # Parse JSON and print output
    got_issues = False
    j = json.loads(response.content)
    for entry in j:
        if 'title' in entry:
            got_issues = True
            print('\t'.join([username, entry['title']]))
    if not got_issues:
        print('\t'.join([username, "NO ISSUES", url]))
