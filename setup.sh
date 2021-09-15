#!/bin/bash

# Create log/ folder in case it doens't exist
if [ ! -d "./log/" ]; then
	echo "Create log/ folder"
	mkdir log
fi

if [ ! -d "./results/" ]; then
	echo "Create results/ folder"
	mkdir results
fi

# Add working directory "QuestionAnsweringSystem/" to PYTHONPATH
echo $PYTHONPATH | grep $PWD

if [ $? -eq 1 ]; then
	echo "Add working directory to PYTHONPATH"
	export PYTHONPATH="$PWD":$PYTHONPATH
fi
