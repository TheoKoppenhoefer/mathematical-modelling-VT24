#!/usr/bin/env bash

sed -i 's/->/\\textrightarrow /g' *.csv
sed -i 's/"//g' *.csv
