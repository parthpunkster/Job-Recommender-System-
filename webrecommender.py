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


class Environment:
	#Scrape ACM website and calculate jacquard for each job
	def webscrape(self,stream,area,field,location):
		ag = Agent()
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
			self.webscrape1(stream,area,field,location)
		count_total_acm = int(temp_acm.get_text())
		for bx_acm in box_acm:
			title_acm = str(bx_acm.find('div',attrs={'class':'aiResultTitle'}).get_text().strip().encode('utf-8'))
	
			url_acm = 'http://jobs.acm.org'+str(bx_acm.find('div',attrs={'class':'aiResultTitle'}).find('h3').find('a').get('href').encode('utf-8'))
		
			details_acm = bx_acm.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find_all('li')
		
			company_acm = str(details_acm[0].get_text().strip().encode('utf-8'))
		
			location_acm = str(details_acm[1].get_text().strip().encode('utf-8'))
		
			date_acm = str(details_acm[2].get_text().strip().encode('utf-8'))
		
			if bx_acm.find('li',attrs={'id':'searchResultsCategoryDisplay'}) != None:
				category_acm = str(details_acm[3].get_text().strip().encode('utf-8'))
			else :
				category_acm = 'None'
			if bx_acm.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}) == None:
				description_acm = str(bx_acm.find('div',attrs={'class':'aiResultsDescription'}).get_text().strip().encode('utf-8'))
			else :
				description_acm = str(bx_acm.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}).get_text().strip().encode('utf-8'))
		
		

			dictionary[dic_count] = [title_acm,company_acm,location_acm,date_acm,category_acm,description_acm,url_acm,0,'x']
			ag.jacard(field,location,dic_count)
			dic_count = dic_count+1

		
		if (page_count_acm < count_total_acm):
			page_count_acm = page_count_acm + 1
			self.webscrape(stream,area,field,location)
	
	


	#scrape Indeed website and calculate jacquard for each job
	def webscrape1(self,stream,area,field,location):
		ag = Agent()
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
		
		
		box_indeed = soup_indeed.find_all('div',attrs={'class':'row'})
		temmp_indeed = soup_indeed.find('div',attrs={'id':'searchCount'})
		if temmp_indeed == None:
			self.webscrape2(stream,area,field,location)
		if test_indeed == 0:
			count_total_indeed = int(temmp_indeed.get_text().split()[5].replace(',',''))
			while val_indeed <= count_total_indeed:
				cal_page_indeed = cal_page_indeed + 1
				val_indeed = 25 * cal_page_indeed
			test_indeed = 1
			cal_page_indeed = cal_page_indeed + 1
			if cal_page_indeed > 50:
				cal_page_indeed = 50
		
		for bx_indeed in box_indeed:
			title_indeed = str(bx_indeed.find('a',attrs={'data-tn-element':'jobTitle'}).get_text().strip().encode('utf-8'))
			
			company_indeed = str(bx_indeed.find('span',attrs={'class':'company'}).get_text().strip().encode('utf-8'))
			
			location_indeed = str(bx_indeed.find('span',attrs={'class':'location'}).get_text().strip().encode('utf-8'))
			
			description_indeed = str(bx_indeed.find('span',attrs={'class':'summary'}).get_text().strip().encode('utf-8'))
			
			date_indeed = 'None'
			category_indeed = 'None'
			url_indeed = str(bx_indeed.find('a',attrs={'data-tn-element':'jobTitle'}).get('href').encode('utf-8'))
		
			dictionary[dic_count] = [title_indeed,company_indeed,location_indeed,date_indeed,category_indeed,description_indeed,url_indeed,0,'x']
			ag.jacard(field,location,dic_count)
			dic_count = dic_count +1


		
		if (counter_indeed<cal_page_indeed):
			page_count_indeed = page_count_indeed + 20
			counter_indeed = counter_indeed+1
			self.webscrape1(stream,area,field,location)

		
	#scrape Ieee website and calculate jacquard for each job
	def webscrape2(self,stream,area,field,location):
		global page_count_ieee
		global dictionary
		global dic_count
		ag = Agent()
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
			
			url_ieee = 'http://jobs.ieee.org/jobs'+str(bx_ieee.find('div',attrs={'class':'aiResultTitle'}).find('h3').find('a').get('href').encode('utf-8'))
			
			details_ieee = bx_ieee.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find_all('li')
			company_ieee = str(details_ieee[0].get_text().strip().encode('utf-8'))
			
			location_ieee = (details_ieee[1].get_text().strip().encode('utf-8'))
			
			date_ieee = str(details_ieee[2].get_text().strip().encode('utf-8'))
			
			if bx_ieee.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find('li',attrs={'id':'searchResultsCategoryDisplay'}) != None:
				category_ieee =  str(bx_ieee.find('div',attrs={'class':'aiDescriptionPod'}).find('ul').find('li',attrs={'id':'searchResultsCategoryDisplay'}).get_text().strip().encode('utf-8'))
			else: category_ieee = 'None'
			if bx_ieee.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}) == None:
				description_ieee = str(bx_ieee.find('div',attrs={'class':'aiResultsDescription'}).get_text().strip().encode('utf-8'))
			else: 
				description_ieee = str(bx_ieee.find('div',attrs={'class':'aiResultsDescriptionNoAdvert'}).get_text().strip().encode('utf-8'))
			
			
			
			dictionary[dic_count] = [title_ieee,company_ieee,location_ieee,date_ieee,category_ieee,description_ieee,url_ieee,0,'x']
			ag.jacard(field,location,dic_count)
			dic_count = dic_count+1


		if (page_count_ieee < count_total_ieee):
			page_count_ieee = page_count_ieee + 1
			self.webscrape2(stream,area,field,location)

#Used for prinitng KNN list
	def printList(self,sortedarray,k):
		g = 0
		while g<k:
			e = 0
			while e<(len(sortedarray[g][1])-2):
				print sortedarray[g][1][e]
				e = e+1
			g=g+1
			print "\n"

	#Used by KMeans to print clusters
	def printList1(self,sortedarray1,k):
		acounter = 1
		bcounter = 1
		ccounter = 1

		for item in sortedarray1:
			if (item[1][8] == 'A' and acounter<=k):
				print 'Cluster :',item[1][8]
				e = 0
				while e<(len(item[1])-2):
					print item[1][e]
					e=e+1
				print "\n"
				acounter = acounter + 1
			if (item[1][8] == 'B' and bcounter<=k):
				print 'Cluster :',item[1][8]
				e = 0
				while e<(len(item[1])-2):
					print item[1][e]
					e=e+1
				print "\n"
				bcounter = bcounter + 1
			if (item[1][8] == 'C' and ccounter<=k):
				print 'Cluster :',item[1][8]
				e = 0
				while e<(len(item[1])-2):
					print item[1][e]
					e=e+1
				print "\n"
				ccounter =ccounter +1

	#Displays the menu until user opts for exit
	def menu(self):
		ag=Agent()
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
		
			sv = (field+' '+location).lower().replace(',',' ')
			if sv in searchvalue:
				if choice == 1:
					ag.knn(k)
				if choice == 2 :
					ag.kmeans(k)
			else :
				searchvalue.append(sv) 
				self.webscrape(a,b,field,location)
				self.webscrape1(a,b,field,location)
				self.webscrape2(a,b,field,location)
				if choice == 1:
					ag.knn(k)
				if choice == 2 :
					ag.kmeans(k)
			self.menu()


class Agent:
	#Used for KNN to calculate jacquard value
	def jacard(self,field,location,key):
		global dkeys
		global dictionary
		
		if field == '_': field = ''
		if location == '_':location = ''
		field_split = field.replace(',',' ').lower().split()
		location_split = location.replace(',',' ').lower().split()
		
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
					
			for elem in location_split:
				if temp.find(elem) != -1 and dkeys[elem] == 0:
					dkeys[elem] = 1
					binto_total_cntr = binto_total_cntr + 1
					
			elem_cntr = elem_cntr + 1
		total_words = total_words + len(dkeys)
		jacard_distance = round(1 - (float(binto_total_cntr) / total_words),4)
		dictionary[key][7] = jacard_distance


	#KNN function
	def knn(self,k):
		env = Environment()
		global dictionary
		sortedarray = sorted(dictionary.items(), key = lambda dictionary: dictionary[1][7])
		if k <= len(dictionary):
			env.printList(sortedarray,k)
		else : print "Total results available are %i, you asked for %i results"%(len(dictionary),k)	

	#Used by KMeans to generate random centroid 
	def randomnumber(self):
		global dictionary
		r1=0
		r2=0
		r3=0
		while r1==r2 or r1 == r3 or r2 == r3:
			r1 = random.randint(1,len(dictionary))
			r2 = random.randint(1,len(dictionary))
			r3 = random.randint(1,len(dictionary))
		return r1,r2,r3




	#KMeans
	def kmeans(self,k):
		env = Environment()
		global dictionary
		r1,r2,r3 = self.randomnumber()
		r1_list = self.concat(r1).lower().replace(',', ' ').split()
		r2_list = self.concat(r2).lower().replace(',',' ').split()
		r3_list = self.concat(r3).lower().replace(',',' ').split()
		for key in dictionary:
			test_list = self.concat(key).lower().replace(',',' ').split()
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
		env.printList1(sortedarray1,k)

	#Used by KMeans to convert a list of strings to single string
	def concat(self,key):
		global dictionary
		concat_string=''
		key1 = 0
		while key1<(len(dictionary[key])-1):
			concat_string = concat_string + str(dictionary[key][key1])
			key1 = key1+1
		return concat_string




def main():
	env = Environment()
	env.menu()
				

if __name__ == '__main__':
	main()
