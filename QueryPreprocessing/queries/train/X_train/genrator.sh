#!/bin/bash

awk 'NR>1{printf "%s %d\n",$1,$2-var-3} {var=$2}' number_fields > num_fields
