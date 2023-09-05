#!/bin/bash
#script that takes in a URL and displays all HTTP methods
curl -s -o /dev/null -w "%{http_code}" "$1"
