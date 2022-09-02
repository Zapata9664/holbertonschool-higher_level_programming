#!/usr/bin/python3
#  takes in a URL and displays all HTTP methods the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f2
