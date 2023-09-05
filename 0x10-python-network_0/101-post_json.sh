#!/bin/bash
#script that takes in a URL and displays all HTTP methods
curl "$1" -sX POST -H "Content-Type: application/json" -d @"$2"
