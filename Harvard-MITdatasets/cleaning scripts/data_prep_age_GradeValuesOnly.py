import csv
import json
import copy
import numpy

course_mapping_1 = {  'The Challenges of Global Poverty':'Spring',  
                    'Elements of structures':'Spring', 
                    'Intro to Solid State Chemistry':'Fall',
                    'Circuits & Electronics':'Fall', 
                    'Intro to CS & Programming':'Fall', 
                    'Intro to Biology':'Spring',  
                    'Electricity & Magnetism':'Spring', 
                    'Mechanics ReView':'Summer', 
                    'The Ancient Greek Hero':'Spring', 
                    'Introduction to CS 1':'Fall',  
                    'JusticeX':'Spring',  
                    'Health in Numbers':'Fall', 
                    'Human Health & Global Environmental  Change':'Spring'}
course_mapping_2 = {'Intro to Solid State Chemistry':'Spring',
                    'Circuits & Electronics':'Spring', 
                    'Intro to CS & Programming':'Spring',
                    }
                    
course_dict_base = []
for key in course_mapping_1:
    course_dict_base.append({'_course':key, '_term':course_mapping_1[key], 'grades':[]})
for key in course_mapping_2:
    course_dict_base.append({'_course':key, '_term':course_mapping_2[key], 'grades':[]})


with open('/Users/akasunic/Desktop/DataPipeline/DataPipelineProject1/Harvard-MITdatasets/data_updated.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)


    for row in reader:
        for item in course_dict_base:
            if row['course_name'] == item['_course'] and row['Term']==item['_term'] and row['grade']!='NA' and float(row['grade']) > 0.0:
                item['grades'].append({'age':row['age_range'], 'grade':100*float(row['grade']), 'country':row['final_cc_cname_DI'], 'edu':row['LoE_DI'], 'gender':row['gender'], 'id':row['userid_DI']})
               
    out = json.dumps(course_dict_base, indent = 4, sort_keys = True)

    with open('/Users/akasunic/Desktop/DataPipeline/DataPipelineProject1/Harvard-MITdatasets/alldata_grades.json', 'w') as data:
        data.write(out)

    
     