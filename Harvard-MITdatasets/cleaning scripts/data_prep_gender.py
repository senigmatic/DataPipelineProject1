import csv
import json
import copy

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
    course_dict_base.append({'_course':key, '_term':course_mapping_1[key]})
for key in course_mapping_2:
    course_dict_base.append({'_course':key, '_term':course_mapping_2[key]})

gender_map = {  'male':0,
                'female':0,
                'Other':0,
                'NA':0
                }

gender= copy.deepcopy(course_dict_base)
for course_dict in gender:
    course_dict['total']=copy.deepcopy(gender_map)
    course_dict['certified']=copy.deepcopy(gender_map)
    course_dict['uncertified']=copy.deepcopy(gender_map)
    course_dict['sum_grades']=copy.deepcopy(gender_map)
    course_dict['count_grades']=copy.deepcopy(gender_map)
    course_dict['avg_grades']=copy.deepcopy(gender_map)
    course_dict['sum_grades_overzero']=copy.deepcopy(gender_map)
    course_dict['count_grades_overzero']=copy.deepcopy(gender_map)
    course_dict['avg_grades_overzero']=copy.deepcopy(gender_map)

with open('/Users/akasunic/Desktop/DataPipeline/DataPipelineProject1/Harvard-MITdatasets/data_updated.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)


    for row in reader:
        for item in gender:
            if row['course_name'] == item['_course'] and row['Term']==item['_term']:
                item['total'][row['gender']] += 1
                if int(row['certified'])==0:
                    item['uncertified'][row['gender']]+=1
                if int(row['certified'])==1:
                    item['certified'][row['gender']]+=1
                if row['grade'] != 'NA':
                    item['sum_grades'][row['gender']] +=round(float(row['grade']),2)
                    item['count_grades'][row['gender']]+=1
                if row['grade'] != 'NA' and row['grade'] >0:
                    item['sum_grades_overzero'][row['gender']] +=round(float(row['grade']),2)
                    item['count_grades_overzero'][row['gender']]+=1

    for course_dict in gender:
        for key in course_dict['avg_grades']:
            try:
                course_dict['avg_grades'][key] = round((course_dict['sum_grades'][key])/(course_dict['count_grades'][key]),2)
            except ZeroDivisionError:
                course_dict['avg_grades'][key] = 'NA'
            try: 
                course_dict['avg_grades_overzero'][key] = round((course_dict['sum_grades_overzero'][key])/(course_dict['count_grades_overzero'][key]),2)
            except ZeroDivisionError:
                course_dict['avg_grades_overzero'][key] = 'NA'

    gender_out = json.dumps(gender, indent = 4, sort_keys = True)

    with open('/Users/akasunic/Desktop/DataPipeline/DataPipelineProject1/Harvard-MITdatasets/gender_data.json', 'w') as data:
        data.write(gender_out)

    
     