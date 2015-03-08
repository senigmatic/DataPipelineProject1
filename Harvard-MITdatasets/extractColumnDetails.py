"""Python code to extract individual column details from the csv"""

dataDict_uid = {} # dividing based on users
dataDict_cid = {} #dividing based on course

def createDictionary():
	with open('Harvard-MITdataset.csv') as fp:
		next(fp) #ignore line 1 (header)
		counter = 0
		for line in fp:
			lineSplit = line.split(",")
			course = ()
			#based on userId
			value = {'course':lineSplit[0],'registered':lineSplit[2],'viewed':lineSplit[3],'explored':lineSplit[4],'certified':lineSplit[5],'final_cc_cname_DI':lineSplit[6],'LoE_DI':lineSplit[7],'YoB':lineSplit[8],'gender':lineSplit[9],'grade':lineSplit[10],'start_time_DI':lineSplit[11],'last_event_DI':lineSplit[12],'nevents':lineSplit[13],'ndays_act':lineSplit[14],'nplay_video':lineSplit[15],'nchapters':lineSplit[16],'nforum_posts':lineSplit[17],'roles':lineSplit[18],'incomplete_flag':lineSplit[19]}
			#based on courseId
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
		print "For course:"+str(key),
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
		print ", Average Age == "+str(yob/countYob)+" for "+str(countYob)+" users" 
				
def getGenderRatioInCourse(courseName):
	for key, value in dataDict_cid.iteritems():
		if key != courseName:
			continue
		else:
			print courseName,
			print len(value)
			
			male=0
			female=0
			unknown=0
			
			for val in value:
				if (value[val])['gender'] == "m":
					male=male+1
				elif (value[val])['gender'] == "f":
					female = female+1
				else:
					unknown = unknown+1
			
			print "males="+str(male)
			print "females="+str(female)
			print "unknown/missing="+str(unknown)

def getMeanAgeInCourse(courseName):
	for key, value in dataDict_cid.iteritems():
		if key != courseName:
			continue
		else:
			print courseName,
			print len(value)
			age = 0	
			countYob = 0
			for val in value:
				try:
					age = age + (2015 - int((value[val])['YoB']))
					countYob = countYob+1
				except:
					continue
			print " Average Age == "+str(age/countYob)+" for total age="+str(age)+" of "+str(countYob)+" users" 

ageGroups = ["<=20","21-30","31-40","41-50","50>"]

			
def getAgeGroupByCount(courseName):		
	for key, value in dataDict_cid.iteritems():
		if key != courseName:
			continue
		else:
			listingAll = {}
			for ii in ageGroups:
				listingAll[ii] = 0
				
			print courseName,
			print len(value)
			
			for val in value:
				try:
					age = (2015 - int((value[val])['YoB']))
					if age<=20:
						listingAll["<=20"] = listingAll["<=20"]+1
					elif age<=30:
						listingAll["21-30"] = listingAll["21-30"]+1
					elif age<=40:
						listingAll["31-40"] = listingAll["31-40"]+1
					elif age<=50:
						listingAll["41-50"] = listingAll["41-50"]+1
					else:
						listingAll["50>"] = listingAll["50>"]+1
				except:
					continue
			print 	listingAll
			

def getCertificationGradeCount(courseName):
	for key, value in dataDict_cid.iteritems():
		if key != courseName:
			continue
		else:
			print courseName,
			print len(value)
			certifiedCount = 0
			gradeAll=0
			gradeCertified = 0
			all = len(value)
			for val in value:
				try:
					
					certifiedCount = certifiedCount+int((value[val])['certified'])
					gradeAll = gradeAll+float((value[val])['grade'])		
					if int((value[val])['certified']) == 1:
						gradeCertified = gradeCertified+float((value[val])['grade'])
				except:
					continue
					
			print "certified Count = "+str(certifiedCount)+" Avg CertGrade = "+str(gradeCertified)+"/"+str(certifiedCount)
			print "total Count = "+str(all)+" Average courseGrade="+str(gradeAll)+"/"+str(all)

def getAgeGroupOfCertified(courseName):
	for key, value in dataDict_cid.iteritems():
		if key != courseName:
			continue
		else:
			print courseName,
			certified={}
			nonCertified={}
			for ii in ageGroups:
				certified[ii] = 0
				nonCertified[ii]=0
			for val in value:
				try:
					age = (2015 - int((value[val])['YoB']))
					if age<=20:
						if int((value[val])['certified']) == 1:
							certified["<=20"] = certified["<=20"]+1
						else:
							nonCertified["<=20"] = nonCertified["<=20"]+1
					elif age<=30:
						if int((value[val])['certified']) == 1:
							certified["21-30"] = certified["21-30"]+1
						else:
							nonCertified["21-30"] = nonCertified["21-30"]+1
						
					elif age<=40:
						if int((value[val])['certified']) == 1:
							certified["31-40"] = certified["31-40"]+1
						else:
							nonCertified["31-40"] = nonCertified["31-40"]+1

					elif age<=50:
						if int((value[val])['certified']) == 1:
							certified["41-50"] = certified["41-50"]+1
						else:
							nonCertified["41-50"] = nonCertified["41-50"]+1
					else:
						if int((value[val])['certified']) == 1:
							certified["50>"] = certified["50>"]+1
						else:
							nonCertified["50>"] = nonCertified["50>"]+1

				except:
					continue
			print 	"Certified:",	
			print 	certified
			print 	"Non-Certified:",	
			print 	nonCertified




createDictionary()
#getUserAgeInDataset()
#getGenderRatioInCourse("MITx/3.091x/2012_Fall")
#getGenderRatioInCourse("MITx/3.091x/2013_Spring")
#getMeanAgeInCourse("MITx/6.002x/2012_Fall")
#getMeanAgeInCourse("MITx/6.002x/2013_Spring")
#getMeanAgeInCourse("MITx/6.00x/2012_Fall")
#getMeanAgeInCourse("MITx/6.00x/2013_Spring")
#getMeanAgeInCourse("MITx/3.091x/2012_Fall")
#getMeanAgeInCourse("MITx/3.091x/2013_Spring")
#getAgeGroupByCount("MITx/6.002x/2012_Fall")
#getAgeGroupByCount("MITx/6.002x/2013_Spring")
#getAgeGroupByCount("MITx/3.091x/2012_Fall")
#getAgeGroupByCount("MITx/3.091x/2013_Spring")
#getAgeGroupByCount("MITx/6.00x/2012_Fall")
#getAgeGroupByCount("MITx/6.00x/2013_Spring")
#getCertificationGradeCount("MITx/6.00x/2012_Fall")
#getCertificationGradeCount("MITx/6.00x/2013_Spring")
#getCertificationGradeCount("MITx/6.002x/2012_Fall")
#getCertificationGradeCount("MITx/6.002x/2013_Spring")
#getCertificationGradeCount("MITx/3.091x/2012_Fall")
#getCertificationGradeCount("MITx/3.091x/2013_Spring")
getAgeGroupOfCertified("MITx/3.091x/2012_Fall")
getAgeGroupOfCertified("MITx/3.091x/2013_Spring")
getAgeGroupOfCertified("MITx/6.002x/2012_Fall")
getAgeGroupOfCertified("MITx/6.002x/2013_Spring")
getAgeGroupOfCertified("MITx/6.00x/2012_Fall")
getAgeGroupOfCertified("MITx/6.00x/2013_Spring")