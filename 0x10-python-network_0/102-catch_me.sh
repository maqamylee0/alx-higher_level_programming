#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me
curl -s 0.0.0.0:5000/catch_me tee /dev/null | grep -o 'You got me!'