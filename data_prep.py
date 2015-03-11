import csv
import json
import copy

course_mapping = {'14.73x':'The Challenges of Global Poverty',  '2.01x': 'Elements of structures', '3.091x':'Intro to Solid State Chemistry', '6.002x': 'Circuits & Electronics',  '6.00x': 'Intro to CS & Programming',  '7.00x':'Intro to Biology',  '8.02x':'Electricity & Magnetism', '8.MReV':'Mechanics ReView', 'CB22x':'The Ancient Greek Hero', 'CS50x':'Introduction to CS 1',  'ER22x': 'JusticeX',   'PH207x': 'Health in Numbers', 'PH278x':'Human Health & Global Environmental  Change'}
course_dict_base = []
for key in course_mapping:
    course_dict_base.append({'course':course_mapping[key]})

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

csvfile = open('/Users/akasunic/Desktop/Data Pipeline/DataPipelineProject1/Harvard-MITdatasets/data_updated.csv', 'rU')

reader = csv.DictReader(csvfile)

for row in reader:
    course = row
    for item in age:
        if row['course_name'] == item['course']:
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

age_out = json.dumps( [ row for row in age ] )

data = open('/Users/akasunic/Desktop/Data Pipeline/DataPipelineProject1/Harvard-MITdatasets/age_data.json', 'w')
data.write(age_out)


'''Files needed:
    
   
    
    Ages_certified
    Ages_grades
    [course:rr 
    
    Edu level_certified
    Edu_grades
    Gender_certified
    Gender_grades
   
    Country_certified
    Country_grades
    
    
    
    
    Courses
    Terms (Fall 2012, Spring 2013, Summer 2013)
    
    course: '''
    
     