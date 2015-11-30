#!/bin/bash

while true; do
	python runbot.py
	echo "Uh oh the snake died. Hatching new one in 5s..."
	# ./notify_james.sh
	sleep 5s;
done;
