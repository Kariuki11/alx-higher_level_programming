#!/bin/bash
# Sends request to a URL passed as an argument, and displays the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
