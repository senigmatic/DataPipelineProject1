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

country_map = { 'Australia':0,
            'Bangladesh':0,
            'Brazil':0,
            'Canada':0,
            'China':0,
            'Colombia':0,
            'Egypt':0,
            'France':0,
            'Germany':0,
            'Greece':0,
            'India':0,
            'Indonesia':0,
            'Japan':0,
            'Mexico':0,
            'Morocco':0,
            'Nigeria':0,
            'Other Africa':0,
            'Other East Asia':0,
            'Other Europe':0,
            'Other Middle East/Central Asia':0,
            'Other North & Central Amer., Caribbean':0,
            'Other Oceania':0,
            'Other South America':0,
            'Other South Asia':0,
            'Pakistan':0,
            'Philippines':0,
            'Poland':0,
            'Portugal':0,
            'Russian Federation':0,
            'Spain':0,
            'Ukraine':0,
            'United Kingdom':0,
            'United States':0,
            'Unknown/Other':0
            }

country= copy.deepcopy(course_dict_base)
for course_dict in country:
    course_dict['total']=copy.deepcopy(country_map)
    course_dict['certified']=copy.deepcopy(country_map)
    course_dict['uncertified']=copy.deepcopy(country_map)
    course_dict['sum_grades']=copy.deepcopy(country_map)
    course_dict['count_grades']=copy.deepcopy(country_map)
    course_dict['avg_grades']=copy.deepcopy(country_map)
    course_dict['sum_grades_overzero']=copy.deepcopy(country_map)
    course_dict['count_grades_overzero']=copy.deepcopy(country_map)
    course_dict['avg_grades_overzero']=copy.deepcopy(country_map)

with open('/Users/akasunic/Desktop/DataPipeline/DataPipelineProject1/Harvard-MITdatasets/data_updated.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile)


    for row in reader:
        for item in country:
            if row['course_name'] == item['_course'] and row['Term']==item['_term']:
                item['total'][row['final_cc_cname_DI']] += 1
                if int(row['certified'])==0:
                    item['uncertified'][row['final_cc_cname_DI']]+=1
                if int(row['certified'])==1:
                    item['certified'][row['final_cc_cname_DI']]+=1
                if row['grade'] != 'NA':
                    item['sum_grades'][row['final_cc_cname_DI']] +=round(float(row['grade']),2)
                    item['count_grades'][row['final_cc_cname_DI']]+=1
                if row['grade'] != 'NA' and row['grade'] >0:
                    item['sum_grades_overzero'][row['final_cc_cname_DI']] +=round(float(row['grade']),2)
                    item['count_grades_overzero'][row['final_cc_cname_DI']]+=1

    for course_dict in country:
        for key in course_dict['avg_grades']:
            try:
                course_dict['avg_grades'][key] = round((course_dict['sum_grades'][key])/(course_dict['count_grades'][key]),2)
            except ZeroDivisionError:
                course_dict['avg_grades'][key] = 'NA'
            try: 
                course_dict['avg_grades_overzero'][key] = round((course_dict['sum_grades_overzero'][key])/(course_dict['count_grades_overzero'][key]),2)
            except ZeroDivisionError:
                course_dict['avg_grades_overzero'][key] = 'NA'

    country_out = json.dumps(country, indent = 4, sort_keys = True)

    with open('/Users/akasunic/Desktop/DataPipeline/DataPipelineProject1/Harvard-MITdatasets/country_data.json', 'w') as data:
        data.write(country_out)

    
     