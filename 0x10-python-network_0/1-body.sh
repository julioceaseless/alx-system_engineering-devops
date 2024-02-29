#!/usr/bin/env bash
# display the body of the response of a curl

if [ $# -ne 1 ]; then
	echo "Usage: $0 <argument"
	exit 1
fi

# get ip address from command line
ip=$1

# Send GET request to the URL and store status code in a variable
status_code=$(curl -s -o response.txt -w "%{http_code}" "$1")

if [ "$status_code" -ne 200 ]; then
	rm -f response.txt
	exit 1
fi

# store response in a variable
response_body=$(tail -n1 response.txt)

# display response
echo $response_body

# remove file
rm -f response.txt
