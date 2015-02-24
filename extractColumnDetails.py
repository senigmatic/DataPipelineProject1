"""Python code to extract individual column details from the csv"""

dataDict_uid = {} # dividing based on users
dataDict_cid = {} #dividing based on course
def createDictionary():
	with open('Harvard-MITdataset.csv') as fp:
		next(fp)
		counter = 0
		for line in fp:
			lineSplit = line.split(",")
			course = ()
			value = {'course':lineSplit[0],'registered':lineSplit[2],'viewed':lineSplit[3],'explored':lineSplit[4],'certified':lineSplit[5],'final_cc_cname_DI':lineSplit[6],'LoE_DI':lineSplit[7],'YoB':lineSplit[8],'gender':lineSplit[9],'grade':lineSplit[10],'start_time_DI':lineSplit[11],'last_event_DI':lineSplit[12],'nevents':lineSplit[13],'ndays_act':lineSplit[14],'nplay_video':lineSplit[15],'nchapters':lineSplit[16],'nforum_posts':lineSplit[17],'roles':lineSplit[18],'incomplete_flag':lineSplit[19]}
			value_cid = {'user':lineSplit[1],'registered':lineSplit[2],'viewed':lineSplit[3],'explored':lineSplit[4],'certified':lineSplit[5],'final_cc_cname_DI':lineSplit[6],'LoE_DI':lineSplit[7],'YoB':lineSplit[8],'gender':lineSplit[9],'grade':lineSplit[10],'start_time_DI':lineSplit[11],'last_event_DI':lineSplit[12],'nevents':lineSplit[13],'ndays_act':lineSplit[14],'nplay_video':lineSplit[15],'nchapters':lineSplit[16],'nforum_posts':lineSplit[17],'roles':lineSplit[18],'incomplete_flag':lineSplit[19]}
			
			if lineSplit[1] in dataDict_uid:
				(dataDict_uid[lineSplit[1]])[len(dataDict_uid[lineSplit[1]])] = value #= dataDict_uid[lineSplit[1]]+{len(dataDict_uid[lineSplit[1]]):value}
				#dataDict_uid[lineSplit[1]].update({len(dataDict_uid[lineSplit[1]]):value})
			else:
				dataDict_uid[lineSplit[1]] = {0:value}
			
			if lineSplit[0] in dataDict_cid:
				(dataDict_cid[lineSplit[0]])[len(dataDict_cid[lineSplit[0]])] = value_cid# = dataDict_cid[lineSplit[0]]+{len(dataDict_cid[lineSplit[0]]):value_cid}
				#dataDict_cid[lineSplit[0]].update({len(dataDict_cid[lineSplit[0]]):value_cid})
			else:
				dataDict_cid[lineSplit[0]] = {0:value_cid}

			counter=counter+1
			if counter%1000 is 0:
				print str(counter)+":"+str(len(dataDict_cid))
			#	if counter == 100000:
			#		break
				
			#print lineSplit[1]+"-->"+str(dataDict_uid[lineSplit[1]])
			#print lineSplit[0]+"-->"+str(dataDict_cid[lineSplit[0]])

def getUserAgeInDataset():
	for key, value in dataDict_cid.iteritems() :
		print key
		yob = 0;
		countYob = 0;
		for val in value:
			#print (value[val])['YoB'] 
			try:
				yob = yob + (2015 - int((value[val])['YoB']))
				countYob = countYob+1
			except:
				continue
		#		print str((value[val])['YoB'])+",",
		print "Average Age == "+str(yob/countYob)+" for "+str(countYob)+" users" 
				
createDictionary()
getUserAgeInDataset()