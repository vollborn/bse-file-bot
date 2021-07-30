#!/bin/bash

directory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$directory/.." || exit

sudo docker build -t bse-file-bot .

