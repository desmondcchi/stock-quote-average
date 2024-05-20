#!/bin/bash

symbol='GOOG' # Default is GOOG.
days=30 # Default is 30 days.

print_usage() {
  echo -e 'Incorrect usage.\n -s Ticker symbol.\n -d Number of days.'
}

while getopts ':s:d:' flag; do
  case "${flag}" in
    s) symbol=$OPTARG ;;
    d) days=$OPTARG ;;
    *) print_usage
      exit 1 ;;
  esac
done

python3.11 main.py $symbol $days
