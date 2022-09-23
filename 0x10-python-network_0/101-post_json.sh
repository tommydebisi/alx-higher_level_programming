#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sL --data-binary -d @"$2" "$1"
