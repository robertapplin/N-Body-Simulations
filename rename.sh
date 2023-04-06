#!/usr/bin/env bash

mkdir uploads

FILE=./uploads/dependencies.txt
if test -f "$FILE"; then
    echo "$FILE exists."
    mv $FILE previous.txt
fi

conda list > ./uploads/dependencies.txt

#echo "date=$(/bin/date -u "+%Y%m%d")" >> $GITHUB_OUTPUT
