#!/bin/bash
awk '{printf "\"%s\" : %d,",$1,$2}' tables_numfields > new_file
