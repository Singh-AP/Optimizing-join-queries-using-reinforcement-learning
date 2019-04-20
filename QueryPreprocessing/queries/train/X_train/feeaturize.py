import numpy as np
import os
'''
featurize all sql queries
'''
tables_one_hot=[0 for _ in range(21)]

tables_num_cols={"aka_title" : 8,"cast_info" : 12,"char_name" : 7,"comp_cast_type" : 7,"company_name" : 2,"company_type" : 7,"complete_cast" : 2,"info_type" : 4,"keyword" : 2,"kind_type" : 3,"link_type" : 2,"movie_companies" : 2,"movie_info_idx" : 5,"movie_keyword" : 5,"movie_link" : 3,"name" : 4,"role_type" : 9,"title" : 2,"movie_info" : 12,"person_info" : 5}

tables_dict={'aka_title': 0, 'cast_info': 1, 'char_name': 2, 'comp_cast_type': 3, 'company_name': 4, 'company_type': 5, 'complete_cast': 6, 'info_type': 7, 'keyword': 8, 'kind_type': 9, 'link_type': 10, 'movie_companies': 11, 'movie_info_idx': 12, 'movie_keyword': 13, 'movie_link': 14, 'name': 15, 'role_type': 16, 'title': 17, 'movie_info': 18, 'person_info': 19}

cols_one_hot= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

cols_names=["id","person_id","name","imdb_index","name_pcode_cf","name_pcode_nf","surname_pcode","md5sum","id","movie_id","title","imdb_index","kind_id","production_year","phonetic_code","episode_of_id","season_nr","episode_nr","note","md5sum","id","person_id","movie_id","person_role_id","note","nr_order","role_id","id","name","imdb_index","imdb_id","name_pcode_nf","surname_pcode","md5sum","id","kind","id","name","country_code","imdb_id","name_pcode_nf","name_pcode_sf","md5sum","id","kind","id","movie_id","subject_id","status_id","id","info","id","keyword","phonetic_code","id","kind","id","link","id","movie_id","company_id","company_type_id","note","id","movie_id","info_type_id","info","note","id","movie_id","keyword_id","id","movie_id","linked_movie_id","link_type_id","id","name","imdb_index","imdb_id","gender","name_pcode_cf","name_pcode_nf","surname_pcode","md5sum","id","role","id","title","imdb_index","kind_id","production_year","imdb_id","phonetic_code","episode_of_id","season_nr","episode_nr","series_years","md5sum","id","movie_id","info_type_id","info","note","id","person_id","info_type_id","info","note"]


cols_dict={'aka_title': {'id': 0, 'person_id': 1, 'name': 2, 'imdb_index': 3, 'name_pcode_cf': 4, 'name_pcode_nf': 5, 'surname_pcode': 6, 'md5sum': 7}, 'cast_info': {'id': 8, 'movie_id': 9, 'title': 10, 'imdb_index': 11, 'kind_id': 12, 'production_year': 13, 'phonetic_code': 14, 'episode_of_id': 15, 'season_nr': 16, 'episode_nr': 17, 'note': 18, 'md5sum': 19}, 'char_name': {'id': 20, 'person_id': 21, 'movie_id': 22, 'person_role_id': 23, 'note': 24, 'nr_order': 25, 'role_id': 26}, 'comp_cast_type': {'id': 27, 'name': 28, 'imdb_index': 29, 'imdb_id': 30, 'name_pcode_nf': 31, 'surname_pcode': 32, 'md5sum': 33}, 'company_name': {'id': 34, 'kind': 35}, 'company_type': {'id': 36, 'name': 37, 'country_code': 38, 'imdb_id': 39, 'name_pcode_nf': 40, 'name_pcode_sf': 41, 'md5sum': 42}, 'complete_cast': {'id': 43, 'kind': 44}, 'info_type': {'id': 45, 'movie_id': 46, 'subject_id': 47, 'status_id': 48}, 'keyword': {'id': 49, 'info': 50}, 'kind_type': {'id': 51, 'keyword': 52, 'phonetic_code': 53}, 'link_type': {'id': 54, 'kind': 55}, 'movie_companies': {'id': 56, 'link': 57}, 'movie_info_idx': {'id': 58, 'movie_id': 59, 'company_id': 60, 'company_type_id': 61, 'note': 62}, 'movie_keyword': {'id': 63, 'movie_id': 64, 'info_type_id': 65, 'info': 66, 'note': 67}, 'movie_link': {'id': 68, 'movie_id': 69, 'keyword_id': 70}, 'name': {'id': 71, 'movie_id': 72, 'linked_movie_id': 73, 'link_type_id': 74}, 'role_type': {'id': 75, 'name': 76, 'imdb_index': 77, 'imdb_id': 78, 'gender': 79, 'name_pcode_cf': 80, 'name_pcode_nf': 81, 'surname_pcode': 82, 'md5sum': 83}, 'title': {'id': 84, 'role': 85}, 'movie_info': {'id': 86, 'title': 87, 'imdb_index': 88, 'kind_id': 89, 'production_year': 90, 'imdb_id': 91, 'phonetic_code': 92, 'episode_of_id': 93, 'season_nr': 94, 'episode_nr': 95, 'series_years': 96, 'md5sum': 97}, 'person_info': {'id': 98, 'movie_id': 99, 'info_type_id': 100, 'info': 101, 'note': 102}}

base_dir="/media/cerialkiller/New Volume/github/Optimizing-join-queries-using-reinforcement-learning/QueryPreprocessing/queries/train/X_train_sql/"

files=["10b.sql","12b.sql","14b.sql","16b.sql","17e.sql","19c.sql","20b.sql","22c.sql","25b.sql","27c.sql","2b.sql","31b.sql","3b.sql","5c.sql","6f.sql","8d.sql","10c.sql","12c.sql","14c.sql","16d.sql","17f.sql","19d.sql","20c.sql","22d.sql","25c.sql","28b.sql","2c.sql","31c.sql","3c.sql","6b.sql","7b.sql","9b.sql","11b.sql","13b.sql","15b.sql","17b.sql","18b.sql","1b.sql","21b.sql","23b.sql","26b.sql","28c.sql","2d.sql","32b.sql","4b.sql","6c.sql","7c.sql","9c.sql","11c.sql","13c.sql","15c.sql","17c.sql","18c.sql","1c.sql","21c.sql","23c.sql","26c.sql","29b.sql","30b.sql","33b.sql","4c.sql","6d.sql","8b.sql","9d.sql","11d.sql","13d.sql","15d.sql","17d.sql","19b.sql","1d.sql","22b.sql","24b.sql","27b.sql","29c.sql","30c.sql","33c.sql","5b.sql","6e.sql","8c.sql"]
print(files.sort())


# for file in files:
#     with open(base_dir+file,"r") as f:
#         from_line=""
#         select_line=""
#         where_line=""
#         for line in f:
#             if line[:4]=="FROM":
#                 from_line=line
#             elif line[:6]=="SELECT":
#                 select_line=line
#             elif line[:5]=="WHERE":
#                 where_line=line
#             else:
#                 print(f"SQL File {file} not formatted")
#                 continue
#         from_splitted=[str(x) for x in from_line.split()]
#         #print("fromline=",from_line,"\nselect line=",select_line,"\nwhere line=",where_line)
#         break
