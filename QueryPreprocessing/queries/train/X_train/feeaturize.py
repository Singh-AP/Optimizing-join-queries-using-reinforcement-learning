import numpy as np
import os

tables=[0 for _ in range(21)]
#print(tables)
tables_num_cols={"aka_title" : 8,"cast_info" : 12,"char_name" : 7,"comp_cast_type" : 7,"company_name" : 2,"company_type" : 7,"complete_cast" : 2,"info_type" : 4,"keyword" : 2,"kind_type" : 3,"link_type" : 2,"movie_companies" : 2,"movie_info_idx" : 5,"movie_keyword" : 5,"movie_link" : 3,"name" : 4,"role_type" : 9,"title" : 2,"movie_info" : 12,"person_info" : 5}
#print(tables_num_cols)
cols_one_hot=[]
for i in tables_num_cols.values():
    temp=[0 for _ in range(i)]
    cols_one_hot=cols_one_hot+temp
print(cols_one_hot)
cols_names=["id","person_id","name","imdb_index","name_pcode_cf","name_pcode_nf","surname_pcode","md5sum","id","movie_id","title","imdb_index","kind_id","production_year","phonetic_code","episode_of_id","season_nr","episode_nr","note","md5sum","id","person_id","movie_id","person_role_id","note","nr_order","role_id","id","name","imdb_index","imdb_id","name_pcode_nf","surname_pcode","md5sum","id","kind","id","name","country_code","imdb_id","name_pcode_nf","name_pcode_sf","md5sum","id","kind","id","movie_id","subject_id","status_id","id","info","id","keyword","phonetic_code","id","kind","id","link","id","movie_id","company_id","company_type_id","note","id","movie_id","info_type_id","info","note","id","movie_id","keyword_id","id","movie_id","linked_movie_id","link_type_id","id","name","imdb_index","imdb_id","gender","name_pcode_cf","name_pcode_nf","surname_pcode","md5sum","id","role","id","title","imdb_index","kind_id","production_year","imdb_id","phonetic_code","episode_of_id","season_nr","episode_nr","series_years","md5sum","id","movie_id","info_type_id","info","note","id","person_id","info_type_id","info","note"]

cols_dict={}

for i in range(len(cols_names)):
    cols_dict[cols_names[i]]=i
print(cols_dict)
