#!/bin/bash

directory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$directory/.." || exit

sudo docker run \
	--rm \
	-it \
	-v "$(pwd)/storage":/app/storage \
	--name bse-file-bot \
	--env-file .env \
	bse-file-bot
