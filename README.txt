Hello User,
Please read this file before using the program

-----------------------------------------------------------------------------------------------------
-Install Beautifull Soup library for python 2.7

Instructions to run the program:
-Open terminal and go to the directory where the file 'parth_jain_assignment2.py' is located
-Type 'python parth_jain_assignment2.py'    (Do not pass any command line arguments while running)
-From the menu displayed select an option by tping the number coresponding to it.
    1: For KNN
    2: For KMeans
    3: For Exit 

-Enter the field: Enter thr field you want to search for, type the search string, if you want you can also type the location.(E.g -    Computer Science)(E.g-Computer Science san jose). 
-If the field is not a valid field it will show 'No Results'

-Enter the location: Enter the location where you want to search the jobs, if nothing entered, the program will take the default location as California.
-If the location is not a valid location it will show 'No Results'  

-Enter the value of K(Number of results you want to be printed)- For Kmeans k will be the max value for each cluster

After this you can see many url's getting loaded.(Those are the urls of the webpages from website being scraped) from all the pages.
If this error occurs during the loading of url and specifically for indeed:
-------------------------------------------------------------------------------------
Traceback (most recent call last):													
  File "parth_jain_assignement2.py", line 384, in <module>				
    main()																			
  File "parth_jain_assignement2.py", line 380, in main	
    menu()																			
  File "parth_jain_assignement2.py", line 370, in menu								
    webscrape1(a,b,field,location)													
  File "parth_jain_assignement2.py", line 115, in webscrape1						
    count_total_indeed = int(temmp_indeed.get_text().split()[5].replace(',',''))	
IndexError: list index out of range												
-------------------------------------------------------------------------------------
then """run the code again""", this happend due to the incosistency in the using tags accross multiple pages on website.

-If the code is kept running and if you enter the exact same search as any of the earlier searches then it ill directly extract the data from in memory and wont extract it over web

-The Url displayed in some jobs is not the exact url as many of the jobs are rediricting to different url.

-To exit press 3 


