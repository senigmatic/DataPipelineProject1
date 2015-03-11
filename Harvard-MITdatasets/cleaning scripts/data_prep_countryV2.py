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
    course_dict_base.append({'_course':key, '_term':course_mapping_1[key]})
for key in course_mapping_2:
    course_dict_base.append({'_course':key, '_term':course_mapping_2[key]})

country_map_base = { 'Australia':0,
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
box_plot_base = {'all_grades':[], 
                'median':0,
                'q1start':0,
                'q3start':0,
                'lineStart':0,
                'lineEnd':0,
                'outliers': [],
                'count_nograde':0,
                'count_totalStudents':0,
                'percent_nograde':0.00
                }
country= copy.deepcopy(course_dict_base)
for course_dict in country:
    course_dict['total']=copy.deepcopy(country_map_base)
    course_dict['certified']=copy.deepcopy(country_map_base)
    course_dict['uncertified']=copy.deepcopy(country_map_base)
    course_dict['sum_grades']=copy.deepcopy(country_map_base)
    course_dict['count_grades']=copy.deepcopy(country_map_base)
    course_dict['avg_grades']=copy.deepcopy(country_map_base)
    course_dict['box_plot'] = copy.deepcopy(country_map_base)
    for country_range in course_dict['box_plot']:
        course_dict['box_plot'][country_range] =  copy.deepcopy(box_plot_base)

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
                if row['grade'] != 'NA' and float(row['grade']) > 0.0:
                    item['sum_grades'][row['final_cc_cname_DI']] +=round(float(row['grade']),2)
                    item['count_grades'][row['final_cc_cname_DI']]+=1
                    item['box_plot'][row['final_cc_cname_DI']]['all_grades'].append(float(row['grade']),)
                if row['grade'] == 'NA' or float(row['grade']) <= 0.0:
                    item['box_plot'][row['final_cc_cname_DI']]['count_nograde']+=1
                
    for course_dict in country:
        for country_range in course_dict['box_plot']:
            count = course_dict['box_plot'][country_range]['count_nograde']
            total = course_dict['total'][country_range]
            course_dict['box_plot'][country_range]['count_totalStudents']=total
            try:
                course_dict['box_plot'][country_range]['percent_nograde']= round(float(count)/float(total),2)
            except ZeroDivisionError:
                course_dict['box_plot'][country_range]['percent_nograde'] = 'NA'
            base = course_dict['box_plot'][country_range]['all_grades']
            if len(base)>0:
                grade_array = numpy.array(base)
                course_dict['box_plot'][country_range]['median']=numpy.median(grade_array)
                q1start = numpy.percentile(grade_array, 25)
                q3start = numpy.percentile(grade_array, 75)
                course_dict['box_plot'][country_range]['q1start']=q1start
                course_dict['box_plot'][country_range]['q3start']=q3start
                iqr = q3start-q1start
                lineStart = q1start-1.5*iqr
                lineEnd = q3start + 1.5*iqr
                course_dict['box_plot'][country_range]['lineStart']=lineStart
                course_dict['box_plot'][country_range]['lineEnd'] = lineEnd
                for item in grade_array:
                    if item <lineStart or item>lineEnd:
                        course_dict['box_plot'][country_range]['outliers'].append(item)
            del course_dict['box_plot'][country_range]['all_grades']

    for course_dict in country:
        for key in course_dict['avg_grades']:
            try:
                course_dict['avg_grades'][key] = round((course_dict['sum_grades'][key])/(course_dict['count_grades'][key]),2)
            except ZeroDivisionError:
                course_dict['avg_grades'][key] = 'NA'
           

    country_out = json.dumps(country, indent = 4, sort_keys = True)

    with open('/Users/akasunic/Desktop/DataPipeline/DataPipelineProject1/Harvard-MITdatasets/country_data_BoxPlot.json', 'w') as data:
        data.write(country_out)

    
     