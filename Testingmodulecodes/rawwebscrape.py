import urllib2
from bs4 import BeautifulSoup
import sys
from operator import itemgetter
import random

#------------------------For webscrape 1
page_count_acm=1
#------------------------For webscrape 1

dictionary = {}
dkeys={}
dkeys1={}
searchvalue = []
concat_string =''

#------------------------For webscrape 2
page_count_indeed = 0
c_indeed = 1
test_indeed = 0
count_total_indeed = 0
counter_indeed = 1
cal_page_indeed = 0
val_indeed = 0
#------------------------For webscrape 2

#------------------------For webscrape 3
page_count_ieee = 1
#------------------------For webscrape 3

#------------------------Dictionary count
dic_count = 1
#------------------------Dictionary count



def webscrape(stream,area,field,location):
	global page_count_acm
	global dictionary
	global dic_count
	if area == "":
		quote_page_acm = 'http://jobs.acm.org/jobs/results/keyword/'+stream+'?page='+str(page_count_acm)
	elif stream == "": 
		quote_page_acm = 'http://jobs.acm.org/jobs/results/keyword/'+area+'?page='+str(page_count_acm)
	else: quote_page_acm = 'http://jobs.acm.org/jobs/results/keyword/'+stream+'/'+area+'?page='+str(page_count_acm)
	print quote_page_acm,'\n'
	page_acm = urllib2.urlopen(quote_page_acm)
	soup_acm = BeautifulSoup(page_acm, 'html.parser')
	box_acm = soup_acm.find_all('div',attrs={'class':'aiResultsMainDiv'})
	temp_acm = soup_acm.find('span',attrs={'class':'aiPageTotalTop'}) 
	if  temp_acm == None:
		print "No results found"
		sys.exit(1)
	count_total_acm = int(temp_acm.get_text())
	for bx_acm in box_acm:
		title_acm = str(bx_acm.find('div',attrs={'class':'aiResultTitle'}).get_text().strip().encode('utf-8'))
		#print 'Title:',bx.find('div',attrs={'class':'aiResultTitle'}).get_text().strip()
		url_acm = 'http://jobs.acm.org'+str(bx_acm.find('div',attrs={'class':'aiResultTitle'}).find('h3').find('a').get('href').encode('utf-8'))
		#print 'URL:',bx.find('div',attrs={'class':'aiResultTitle'}).find('h3').find('a').get('href')
		details_acm = bx_acm.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find_all('li')
		company_acm = str(details_acm[0].get_text().strip().encode('utf-8'))
		#print 'Company:',details[0].get_text().strip()
		location_acm = str(details_acm[1].get_text().strip().encode('utf-8'))
		#print 'Location:',details[1].get_text().strip()
		date_acm = str(details_acm[2].get_text().strip().encode('utf-8'))
		#print 'Date:',details[2].get_text().strip()+"\n"
		if bx_acm.find('li',attrs={'id':'searchResultsCategoryDisplay'}) != None:
			category_acm = str(details_acm[3].get_text().strip().encode('utf-8'))
		else :
			category_acm = 'None'
		if bx_acm.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}) == None:
			description_acm = str(bx_acm.find('div',attrs={'class':'aiResultsDescription'}).get_text().strip().encode('utf-8'))
		else :
			description_acm = str(bx_acm.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}).get_text().strip().encode('utf-8'))
		#print 'Description:', bx.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}).get_text().strip()
		
		

		dictionary[dic_count] = [title_acm,company_acm,location_acm,date_acm,category_acm,description_acm,url_acm,0,'x']
		jacard(field,location,dic_count)
		dic_count = dic_count+1

		#if (title_acm,location_acm) in dictionary:
		#	dictionary[title_acm,location_acm] = (dictionary[title_acm,location_acm],[title_acm,company_acm,location_acm,date_acm,category_acm,description_acm,0])
	
		#else:
		#	dictionary[title_acm,location_acm] = ([title_acm,company_acm,location_acm,date_acm,category_acm,description_acm,0])
  



    	#dont use as of now
    	#print 'Company:',bx.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find('li',attrs={'class':'aiResultsCompanyName'}).get_text().strip()
		#print 'Location:',bx.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find_all('li')[1].get_text() + "\n"
	
		#print bx.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}).get_text().strip()
		#print box.find('div',attrs={'class':'aiResultTitle'})
		#find('h3').get_text()

	if (page_count_acm < count_total_acm):
		page_count_acm = page_count_acm + 1
		webscrape(stream,area,field,location)
	#for element in dictionary:
	#	print x
	#	print y
	#	print dictionary[x,y][0]
	#	print dictionary[x,y][1]
	#	print dictionary[x,y][2]
	#	print dictionary[x,y][3]
	#	print "\n"
	#print dictionary  

	



def webscrape1(stream,area,field,location):
	global page_count_indeed
	global c_indeed
	global test_indeed
	global count_total_indeed 
	global counter_indeed
	global cal_page_indeed
	global val_indeed
	global dictionary
	global dic_count
	
	quote_page_indeed = 'https://www.indeed.com/jobs?q='+stream+'&l='+area+'&start='+str(page_count_indeed)
	print quote_page_indeed,'\n'
	page_indeed = urllib2.urlopen(quote_page_indeed)
	soup_indeed = BeautifulSoup(page_indeed, 'html.parser')
	
	#a = str(soup_indeed)
	#f = open('1.html','w')
	#f.write(a)
	#f.close()
	
	#print soup_indeed

	
	box_indeed = soup_indeed.find_all('div',attrs={'class':'row'})
	temmp_indeed = soup_indeed.find('div',attrs={'id':'searchCount'})
	if temmp_indeed == None:
		print 'No results found'
		sys.exit(1)
	if test_indeed == 0:
		count_total_indeed = int(temmp_indeed.get_text().split()[5].replace(',',''))
		while val_indeed <= count_total_indeed:
			cal_page_indeed = cal_page_indeed + 1
			val_indeed = 25 * cal_page_indeed
		test_indeed = 1
		cal_page_indeed = cal_page_indeed + 1
		if cal_page_indeed > 50:
			cal_page_indeed = 50
		#print page_indeed
		#print val_indeed
	#print count_total_indeed
	
	for bx_indeed in box_indeed:
		#print c_indeed
		#print 'Title:',bx_indeed.find('a',attrs={'data-tn-element':'jobTitle'}).get_text().strip()
		title_indeed = str(bx_indeed.find('a',attrs={'data-tn-element':'jobTitle'}).get_text().strip().encode('utf-8'))
		#print 'Company:', bx_indeed.find('span',attrs={'class':'company'}).get_text().strip()
		company_indeed = str(bx_indeed.find('span',attrs={'class':'company'}).get_text().strip().encode('utf-8'))
		#print 'Location:', bx_indeed.find('span',attrs={'class':'location'}).get_text().strip()
		location_indeed = str(bx_indeed.find('span',attrs={'class':'location'}).get_text().strip().encode('utf-8'))
		#print 'Description:', bx_indeed.find('span',attrs={'class':'summary'}).get_text().strip(),'\n'
		description_indeed = str(bx_indeed.find('span',attrs={'class':'summary'}).get_text().strip().encode('utf-8'))
		#c_indeed = c_indeed+1
		date_indeed = 'None'
		category_indeed = 'None'
		url_indeed = str(bx_indeed.find('a',attrs={'data-tn-element':'jobTitle'}).get('href').encode('utf-8'))
	
		dictionary[dic_count] = [title_indeed,company_indeed,location_indeed,date_indeed,category_indeed,description_indeed,url_indeed,0,'x']
		jacard(field,location,dic_count)
		dic_count = dic_count +1

	#if (title_indeed,location_indeed) in dictionary:
	#	dictionary[title_indeed,location_indeed] = (dictionary[title_indeed,location_indeed],[title_indeed,company_indeed,location_indeed,date_indeed,category_indeed,description_indeed,0])
	#else:
	#	dictionary[title_indeed,location_indeed] = ([title_indeed,company_indeed,location_indeed,date_indeed,category_indeed,description_indeed,0])	

	
	if (counter_indeed<cal_page_indeed):
		page_count_indeed = page_count_indeed + 20
		counter_indeed = counter_indeed+1
		#print 'counter:',counter_indeed
		webscrape1(stream,area,field,location)

	#for (x,y) in dictionary:
	#	print x
	#	print y
	#	print dictionary[x,y][0]
	#	print dictionary[x,y][1]
	#	print "\n"  


def webscrape2(stream,area,field,location):
	global page_count_ieee
	global dictionary
	global dic_count
	if area == "":
		quote_page_ieee = 'http://jobs.ieee.org/jobs/results/keyword/'+stream+'?page='+str(page_count_ieee)
	elif stream == "": 
		quote_page_ieee = 'http://jobs.ieee.org/jobs/results/keyword/'+area+'?page='+str(page_count_ieee)
	else: quote_page_ieee = 'http://jobs.ieee.org/jobs/results/keyword/'+stream+'/'+area+'?page='+str(page_count_ieee)
	print quote_page_ieee,'\n'
	page_ieee = urllib2.urlopen(quote_page_ieee)
	soup_ieee = BeautifulSoup(page_ieee, 'html.parser')
	box_ieee = soup_ieee.find_all('div',attrs={'class':'aiDevFeaturedSection'})
	temp_ieee = soup_ieee.find('span',attrs={'class':'aiPageTotalTop'})
	if  temp_ieee == None:
		print "No results found"
		sys.exit(1)
	count_total_ieee = int(temp_ieee.get_text())
	for bx_ieee in box_ieee:
		title_ieee = str(bx_ieee.find('div',attrs={'class':'aiResultTitle'}).get_text().strip().encode('utf-8')) 
		#print bx_ieee.find('div',attrs={'class':'aiResultTitle'}).get_text().strip()
		url_ieee = 'http://jobs.ieee.org/jobs'+str(bx_ieee.find('div',attrs={'class':'aiResultTitle'}).find('h3').find('a').get('href').encode('utf-8'))
		#print 'URL:',bx_ieee.find('div',attrs={'class':'aiResultTitle'}).find('h3').find('a').get('href')
		details_ieee = bx_ieee.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find_all('li')
		company_ieee = str(details_ieee[0].get_text().strip().encode('utf-8'))
		#print 'Company:',details_ieee[0].get_text().strip()
		location_ieee = (details_ieee[1].get_text().strip().encode('utf-8'))
		#print 'Location:',details_ieee[1].get_text().strip()
		date_ieee = str(details_ieee[2].get_text().strip().encode('utf-8'))
		#print 'Date:',details_ieee[2].get_text().strip()+"\n"
		if bx_ieee.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find('li',attrs={'id':'searchResultsCategoryDisplay'}) != None:
			category_ieee =  str(bx_ieee.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find('li',attrs={'id':'searchResultsCategoryDisplay'}).get_text().strip().encode('utf-8'))
		else: category_ieee = 'None'
		if bx_ieee.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}) == None:
			description_ieee = str(bx_ieee.find('div',attrs={'class':'aiResultsDescription'}).get_text().strip().encode('utf-8'))
		else: 
			description_ieee = str(bx_ieee.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}).get_text().strip().encode('utf-8'))
		#print 'Description:', bx_ieee.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}).get_text().strip()
		
		
		dictionary[dic_count] = [title_ieee,company_ieee,location_ieee,date_ieee,category_ieee,description_ieee,url_ieee,0,'x']
		jacard(field,location,dic_count)
		dic_count = dic_count+1

		
		#if (title_ieee,location_ieee) in dictionary :
		#	dictionary[title_ieee,location_ieee] = (dictionary[title_ieee,location_ieee],[title_ieee,company_ieee,location_ieee,date_ieee,category_ieee,description_ieee,0])

		#else:
		#	dictionary[title_ieee,location_ieee] = ([title_ieee,company_ieee,location_ieee,date_ieee,category_ieee,description_ieee,0])	
	


	if (page_count_ieee < count_total_ieee):
		page_count_ieee = page_count_ieee + 1
		webscrape2(stream,area,field,location)

	#for (x,y) in dictionary:
	#	print x
	#	print y
	#	print dictionary[x,y][0]
	#	print dictionary[x,y][1]
	#	print dictionary[x,y][2]
	#	print dictionary[x,y][3]
	#	print dictionary[x,y][4]
	#	print "\n"  




def jacard(field,location,key):
	global dkeys
	global dictionary
	#print stream
	#print area
	if field == '_': field = ''
	if location == '_':location = ''
	field_split = field.replace(',',' ').lower().split()
	location_split = location.replace(',',' ').lower().split()
	#print dkeys

	for elem in field_split:
		dkeys[elem] = 0
	for elem in location_split:
		dkeys[elem] = 0
	elem_cntr = 0
	binto_total_cntr = 0
	total_words = 0
	while elem_cntr<len(dictionary[key]):
		temp = str(dictionary[key][elem_cntr]).replace(',',' ').lower()
		array = temp.split()
		total_words = total_words + len(array)
		for elem in field_split:
			if temp.find(elem) != -1 and dkeys[elem] == 0:
				dkeys[elem] = 1
				binto_total_cntr = binto_total_cntr + 1
				#print elem

		for elem in location_split:
			if temp.find(elem) != -1 and dkeys[elem] == 0:
				dkeys[elem] = 1
				binto_total_cntr = binto_total_cntr + 1
				#print elem

		elem_cntr = elem_cntr + 1
	#print dkeys
	#print binto_total_cntr
	#print total_words
	total_words = total_words + len(dkeys)
	jacard_distance = round(1 - (float(binto_total_cntr) / total_words),4)
	#print binto_total_cntr
	#print total_words
	#dictionary[key][-1] = jacard_distance
	#print jacard_distance
	dictionary[key][7] = jacard_distance


def printList(sortedarray,k):
	g = 0
	while g<k:
		#print sortedarray[g][0]
		e = 0
		while e<(len(sortedarray[g][1])-2):
			print sortedarray[g][1][e]
			e = e+1
		g=g+1
		print "\n"

def knn(k):
	global dictionary
	sortedarray = sorted(dictionary.items(), key = lambda dictionary: dictionary[1][7])
	#print sortedarray
	if k <= len(dictionary):
		printList(sortedarray,k)
	else : print "Total results available are %i, you asked for %i results"%(len(dictionary),k)	


def randomnumber():
	global dictionary
	r1=0
	r2=0
	r3=0
	while r1==r2 or r1 == r3 or r2 == r3:
		r1 = random.randint(1,len(dictionary))
		r2 = random.randint(1,len(dictionary))
		r3 = random.randint(1,len(dictionary))
	return r1,r2,r3

def printList1(sortedarray1):
	acounter = 1
	bcounter = 1
	ccounter = 1

	for item in sortedarray1:
		if (item[1][8] == 'A' and acounter<=15):
			print 'Cluster :',item[1][8]
			e = 0
			while e<(len(item[1])-2):
				print item[1][e]
				e=e+1
			print "\n"
			acounter = acounter + 1
		if (item[1][8] == 'B' and bcounter<=15):
			print 'Cluster :',item[1][8]
			e = 0
			while e<(len(item[1])-2):
				print item[1][e]
				e=e+1
			print "\n"
			bcounter = bcounter + 1
		if (item[1][8] == 'C' and ccounter<=15):
			print 'Cluster :',item[1][8]
			e = 0
			while e<(len(item[1])-2):
				print item[1][e]
				e=e+1
			print "\n"
			ccounter =ccounter +1



def kmeans():
	global dictionary
	r1,r2,r3 = randomnumber()
	r1_list = concat(r1).lower().replace(',', ' ').split()
	r2_list = concat(r2).lower().replace(',',' ').split()
	r3_list = concat(r3).lower().replace(',',' ').split()
	for key in dictionary:
		test_list = concat(key).lower().replace(',',' ').split()
		intersection1 = len(list(set(r1_list) & set(test_list)))
		union1 = len(list(set(r1_list) | set(test_list)))
		jacardval1 = 1 - float(intersection1)/union1
		intersection2 = len(list(set(r2_list) & set(test_list)))
		union2 = len(list(set(r2_list) | set(test_list)))
		jacardval2 = 1 - float(intersection2)/union2
		intersection3 = len(list(set(r3_list) & set(test_list)))
		union3 = len(list(set(r3_list) | set(test_list)))
		jacardval3 = 1 - float(intersection3)/union3
		minjacard = min(jacardval1,jacardval2,jacardval3)
		if minjacard == jacardval1: dictionary[key][8] = 'A'
		elif minjacard == jacardval2: dictionary[key][8] = 'B'
		elif minjacard == jacardval3: dictionary[key][8] = 'C' 

	sortedarray1 = sorted(dictionary.items(), key = lambda dictionary: dictionary[1][8])
	printList1(sortedarray1)










def concat(key):
	global dictionary
	concat_string=''
	key1 = 0
	while key1<(len(dictionary[key])-1):
		concat_string = concat_string + str(dictionary[key][key1])
		key1 = key1+1
	return concat_string



def menu():
	global searchvalue
	print 'Menu'
	print ' 1:To run KNN \n 2: To run K-Means \n 3: To exit'
	choice = input('Enter your choice: ')
	if choice == 3:
		print 'Thank You for your valuable time'
		sys.exit()
	else:
		field = raw_input('Enter the field: ')
		if field == "":
			field = '_'

		a = field.replace(' ','+')
		#print a
		location = raw_input('Enter the location: ')
		if location == "":
			location = 'California'
		b = location.replace(' ','+')
		b = b.replace(',','%2C')
		while a == "" and b == "": 
			print "Enter atleast one of the above." 		
		k = input('Enter an integer value for k(number of results you wish to be shown): ')
		while type(k) != int:
			print 'The "k" value you entered is not an integer\n'
		#print b

		sv = (field+' '+location).lower().replace(',',' ')
		if sv in searchvalue:
			if choice == 1:
				knn(k)
			if choice == 2 :
				kmeans()
		else :
			searchvalue.append(sv) 
			webscrape(a,b,field,location)
			webscrape1(a,b,field,location)
			webscrape2(a,b,field,location)
			if choice == 1:
				knn(k)
			if choice == 2 :
				kmeans()
		menu()


def main():
	menu()
			

if __name__ == '__main__':
	main()
