import urllib2
from bs4 import BeautifulSoup
import sys

#------------------------For webscrape 1
page_count_acm=1
#------------------------For webscrape 1

dictionary = {}

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


def webscrape(stream,area):
	global page_count_acm
	global dictionary
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
		title_acm = bx_acm.find('div',attrs={'class':'aiResultTitle'}).get_text().strip()
		#print 'Title:',bx.find('div',attrs={'class':'aiResultTitle'}).get_text().strip()
		url_acm = bx_acm.find('div',attrs={'class':'aiResultTitle'}).find('h3').find('a').get('href')
		#print 'URL:',bx.find('div',attrs={'class':'aiResultTitle'}).find('h3').find('a').get('href')
		details_acm = bx_acm.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find_all('li')
		company_acm = details_acm[0].get_text().strip()
		#print 'Company:',details[0].get_text().strip()
		location_acm = details_acm[1].get_text().strip()
		#print 'Location:',details[1].get_text().strip()
		date_acm = details_acm[2].get_text().strip()
		#print 'Date:',details[2].get_text().strip()+"\n"
		if bx_acm.find('li',attrs={'id':'searchResultsCategoryDisplay'}) != None:
			category_acm = details_acm[3].get_text().strip()
		else :
			category_acm = 'None'
		description_acm = bx_acm.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}).get_text().strip()
		#print 'Description:', bx.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}).get_text().strip()
		
		

		if (title_acm,location_acm) in dictionary:
			dictionary[title_acm,location_acm] = (dictionary[title_acm,location_acm],[company_acm,date_acm,category_acm,description_acm,'acm'])
	
		else:
			dictionary[title_acm,location_acm] = ([company_acm,date_acm,category_acm,description_acm,'acm'])
  



    	#dont use as of now
    	#print 'Company:',bx.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find('li',attrs={'class':'aiResultsCompanyName'}).get_text().strip()
		#print 'Location:',bx.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find_all('li')[1].get_text() + "\n"
	
		#print bx.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}).get_text().strip()
		#print box.find('div',attrs={'class':'aiResultTitle'})
		#find('h3').get_text()

	if (page_count_acm < count_total_acm):
		page_count_acm = page_count_acm + 1
		webscrape(stream,area)
	#for (x,y) in dictionary:
	#	print x
	#	print y
	#	print dictionary[x,y][0]
	#	print dictionary[x,y][1]
	#	print dictionary[x,y][2]
	#	print dictionary[x,y][3]
	#	print "\n"
	#print dictionary  



def webscrape1(stream,area):
	global page_count_indeed
	global c_indeed
	global test_indeed
	global count_total_indeed 
	global counter_indeed
	global cal_page_indeed
	global val_indeed
	global dictionary
	
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
		title_indeed = bx_indeed.find('a',attrs={'data-tn-element':'jobTitle'}).get_text().strip()
		#print 'Company:', bx_indeed.find('span',attrs={'class':'company'}).get_text().strip()
		company_indeed = bx_indeed.find('span',attrs={'class':'company'}).get_text().strip()
		#print 'Location:', bx_indeed.find('span',attrs={'class':'location'}).get_text().strip()
		location_indeed = bx_indeed.find('span',attrs={'class':'location'}).get_text().strip()
		#print 'Description:', bx_indeed.find('span',attrs={'class':'summary'}).get_text().strip(),'\n'
		description_indeed = bx_indeed.find('span',attrs={'class':'summary'}).get_text().strip()
		#c_indeed = c_indeed+1
		date_indeed = 'None'
		category_indeed = 'None'
	
	if (title_indeed,location_indeed) in dictionary:
		dictionary[title_indeed,location_indeed] = (dictionary[title_indeed,location_indeed],[company_indeed,date_indeed,category_indeed,description_indeed,'indeed'])
	else:
		dictionary[title_indeed,location_indeed] = ([company_indeed,date_indeed,category_indeed,description_indeed,'indeed'])	

	
	if (counter_indeed<cal_page_indeed):
		page_count_indeed = page_count_indeed + 20
		counter_indeed = counter_indeed+1
		#print 'counter:',counter_indeed
		webscrape1(stream,area)

	#for (x,y) in dictionary:
	#	print x
	#	print y
	#	print dictionary[x,y][0]
	#	print dictionary[x,y][1]
	#	print "\n"  


def webscrape2(stream,area):
	global page_count_ieee
	global dictionary
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
		title_ieee = bx_ieee.find('div',attrs={'class':'aiResultTitle'}).get_text().strip() 
		#print bx_ieee.find('div',attrs={'class':'aiResultTitle'}).get_text().strip()
		url_ieee = bx_ieee.find('div',attrs={'class':'aiResultTitle'}).find('h3').find('a').get('href')
		#print 'URL:',bx_ieee.find('div',attrs={'class':'aiResultTitle'}).find('h3').find('a').get('href')
		details_ieee = bx_ieee.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find_all('li')
		company_ieee = details_ieee[0].get_text().strip()
		#print 'Company:',details_ieee[0].get_text().strip()
		location_ieee = details_ieee[1].get_text().strip()
		#print 'Location:',details_ieee[1].get_text().strip()
		date_ieee = details_ieee[2].get_text().strip()
		#print 'Date:',details_ieee[2].get_text().strip()+"\n"
		if bx_ieee.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find('li',attrs={'id':'searchResultsCategoryDisplay'}) != None:
			category_ieee =  bx_ieee.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find('li',attrs={'id':'searchResultsCategoryDisplay'}).get_text().strip()
		else: category_ieee = 'None'
		if bx_ieee.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}) == None:
			description_ieee = bx_ieee.find('div',attrs={'class':'aiResultsDescription'}).get_text().strip()
		else: 
			description_ieee = bx_ieee.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}).get_text().strip()
		#print 'Description:', bx_ieee.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}).get_text().strip()
		
		if (title_ieee,location_ieee) in dictionary :
			dictionary[title_ieee,location_ieee] = (dictionary[title_ieee,location_ieee],[company_ieee,date_ieee,category_ieee,description_ieee,'ieee'])

		else:
			dictionary[title_ieee,location_ieee] = ([company_ieee,date_ieee,category_ieee,description_ieee,'ieee'])	
	


	if (page_count_ieee < count_total_ieee):
		page_count_ieee = page_count_ieee + 1
		webscrape2(stream,area)

	#for (x,y) in dictionary:
	#	print x
	#	print y
	#	print dictionary[x,y][0]
	#	print dictionary[x,y][1]
	#	print dictionary[x,y][2]
	#	print dictionary[x,y][3]
	#	print dictionary[x,y][4]
	#	print "\n"  




def printDictionary():
	#print dictionary
	for (x,y) in dictionary:
		ptr = 0
		if len(dictionary[x,y][ptr][0]) == 1:
			print x
			print y
			print dictionary[x,y][0]
			print dictionary[x,y][1]
			print dictionary[x,y][2]
			print dictionary[x,y][3]
			print dictionary[x,y][4]
			print "\n"
		else:
			while ptr<len(dictionary[x,y]):
				print x
				print y
				print dictionary[x,y][ptr][0]
				print dictionary[x,y][ptr][1]
				print dictionary[x,y][ptr][2]
				print dictionary[x,y][ptr][3]
				print dictionary[x,y][ptr][4]
				print "\n"
				ptr = ptr +1

		



def main():
	field = raw_input('Enter the field: ')
	a = field.replace(' ','+')
	#print a
	location = raw_input('Enter the location: ')
	b = location.replace(' ','+')
	b = b.replace(',','%2C')
	#print b
	if a == "" and b == "": 
		print "Enter atleast one of the above."
		sys.exit(1)
	webscrape(a,b)
	webscrape1(a,b)
	webscrape2(a,b)
	printDictionary()

if __name__ == '__main__':
	main()
