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

age_bins = ['5 and under', '9 to 13', '14 to 19', '20 to 24', '25-29', '30 to 39', '40-49', '50-59', '60-69','70 and above', 'NA']
age_map_base = {'5 and under':0, '9 to 13':0, '14 to 19':0, '20 to 24':0, '25-29':0, '30 to 39':0, '40-49':0, '50-59':0, '60-69':0,'70 and above':0, 'NA':0}
age= copy.deepcopy(course_dict_base)
for course_dict in age:
    course_dict['total']=copy.deepcopy(age_map_base)
    course_dict['certified']=copy.deepcopy(age_map_base)
    course_dict['uncertified']=copy.deepcopy(age_map_base)
    course_dict['sum_grades']=copy.deepcopy(age_map_base)
    course_dict['count_grades']=copy.deepcopy(age_map_base)
    course_dict['avg_grades']=copy.deepcopy(age_map_base)
    course_dict['sum_grades_overzero']=copy.deepcopy(age_map_base)
    course_dict['count_grades_overzero']=copy.deepcopy(age_map_base)
    course_dict['avg_grades_overzero']=copy.deepcopy(age_map_base)

with open('/Users/akasunic/Desktop/DataPipeline/DataPipelineProject1/Harvard-MITdatasets/data_updated.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)


    for row in reader:
        for item in age:
            if row['course_name'] == item['_course'] and row['Term']==item['_term']:
                item['total'][row['age_range']] += 1
                if int(row['certified'])==0:
                    item['uncertified'][row['age_range']]+=1
                if int(row['certified'])==1:
                    item['certified'][row['age_range']]+=1
                if row['grade'] != 'NA':
                    item['sum_grades'][row['age_range']] +=round(float(row['grade']),2)
                    item['count_grades'][row['age_range']]+=1
                if row['grade'] != 'NA' and row['grade'] >0:
                    item['sum_grades_overzero'][row['age_range']] +=round(float(row['grade']),2)
                    item['count_grades_overzero'][row['age_range']]+=1

    for course_dict in age:
        for key in course_dict['avg_grades']:
            try:
                course_dict['avg_grades'][key] = round((course_dict['sum_grades'][key])/(course_dict['count_grades'][key]),2)
            except ZeroDivisionError:
                course_dict['avg_grades'][key] = 'NA'
            try: 
                course_dict['avg_grades_overzero'][key] = round((course_dict['sum_grades_overzero'][key])/(course_dict['count_grades_overzero'][key]),2)
            except ZeroDivisionError:
                course_dict['avg_grades_overzero'][key] = 'NA'

    age_out = json.dumps(age, indent = 4, sort_keys = True)

    with open('/Users/akasunic/Desktop/DataPipeline/DataPipelineProject1/Harvard-MITdatasets/age_data.json', 'w') as data:
        data.write(age_out)

    
     