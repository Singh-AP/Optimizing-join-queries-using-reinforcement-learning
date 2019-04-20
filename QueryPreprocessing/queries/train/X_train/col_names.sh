#!/bin/bash
var=0
awk '{if ( $1 != "CREATE" && $1 != "" && $1 != ");" ) printf "\"%s\",",$1;}' schematext.sql > new_file
