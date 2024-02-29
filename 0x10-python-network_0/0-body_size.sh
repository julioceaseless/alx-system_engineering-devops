#!/usr/bin/env bash
# curl command to display the size of the body of the response

ip=$1
curl -Is "$ip" | grep -i content-length | cut -d':' -f2 | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' 
