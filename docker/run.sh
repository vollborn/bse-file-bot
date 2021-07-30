#!/bin/bash

cd ..

sudo docker run \
	--rm \
	-it \
	-v "$(pwd)/storage":/app/storage \
	--name bse-file-bot \
	--env-file .env \
	bse-file-bot
