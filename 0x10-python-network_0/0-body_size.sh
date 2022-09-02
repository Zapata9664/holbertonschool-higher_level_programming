#!/bin/bash
# Takes in a URL, and displya lengt of body
curl -sI "$1" | grep "Content-Lengt" | cut -d " " -f 2
