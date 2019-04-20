#!/bin/bash
#Add line spaces in sql files
for i in X_train_sql/*;do
  #echo $i
  file_name=$(echo $i | cut -d "/" -f 2)
  echo $file_name
  sed  's/FROM/\nFROM/g
  s/WHERE/\nWHERE/g' $i > $file_name
done
