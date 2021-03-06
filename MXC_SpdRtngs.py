import psycopg2
import sys
import re
import numpy
 


def mean():

	for value in dict[time]:
		split(value)
		sumMins += mins
		sumSecs += float(secs)

	# Multiply mins by 60 to get seconds
	totalSum = float(sumSecs + (sumMins * 60))
	mean = float((totalSum / numRunners))

	return mean

def splitter(time):

	time_list = time.split(":", 2)
	mins = int(time_list[0])
	secs = float(time_list[1])
	time_in_secs = float(mins_to_secs(mins, secs))
	return time_in_secs

def mins_to_secs(mins, secs):

	temp_time = float(((mins * 60) + secs))
	return temp_time

def st_dev_michigan(myList1, myList2, myList3, myList4, 
myList5, myList6, myList7, myList8, myList9, myList10):

	mean1 = float(mean_of_list(myList1))
	mean2 = float(mean_of_list(myList2))
	mean3 = float(mean_of_list(myList3))
	mean4 = float(mean_of_list(myList4))
	mean5 = float(mean_of_list(myList5))
	mean6 = float(mean_of_list(myList6))
	mean7 = float(mean_of_list(myList7))
	mean8 = float(mean_of_list(myList8))
	mean9 = float(mean_of_list(myList9))
	mean10 = float(mean_of_list(myList10))

	mean_temp = float((mean1 + mean2 + mean3 + mean4 + mean5 + mean6 + mean7 + mean8 + mean9 + mean10)/10)
	
	sigma_value = (float(((mean1 - mean_temp)**2) + ((mean2 - mean_temp)**2) + ((mean3 - mean_temp)**2) + ((mean4 - mean_temp)**2) + ((mean5 - mean_temp)**2) + 
		((mean6 - mean_temp)**2) + ((mean7 - mean_temp)**2) + ((mean8 - mean_temp)**2) + ((mean9 - mean_temp)**2) + ((mean10 - mean_temp)**2)))
	
	st_dev_michigan = float((sigma_value/10)**0.5)
	return st_dev_michigan

def mean_michigan(myList1, myList2, myList3, myList4, 
myList5, myList6, myList7, myList8, myList9, myList10):

	mean1 = float(mean_of_list(myList1))
	mean2 = float(mean_of_list(myList2))
	mean3 = float(mean_of_list(myList3))
	mean4 = float(mean_of_list(myList4))
	mean5 = float(mean_of_list(myList5))
	mean6 = float(mean_of_list(myList6))
	mean7 = float(mean_of_list(myList7))
	mean8 = float(mean_of_list(myList8))
	mean9 = float(mean_of_list(myList9))
	mean10 = float(mean_of_list(myList10))

	meanMichigan = float((mean1 + mean2 + mean3 + mean4 + mean5 + mean6 + mean7 + mean8 + mean9 + mean10)/10)

	return meanMichigan

def mean_of_list(myList):

	sumList = 0

	for row in myList:
		sumList += row[6]
	mean_course = float((sumList / len(myList)))
	return mean_course

def std_dev_course(myList):

	std_dev_course = float(numpy.std(zip(*myList)[6]))
	return std_dev_course

def z_score_athlete(time_in_secs, mean_course, std_dev_course):

	z_score_athlete = float((time_in_secs - mean_course) / (std_dev_course))

	return z_score_athlete

def z_score_course(mean_course, mean_michigan, std_dev_michigan):

	z_score_course = float((mean_course - mean_michigan) / (std_dev_michigan))

	return z_score_course

def calc_speed_rating(z_score_michigan, z_score_course):

	speed_rating = float(100 + (z_score_michigan * z_score_course * 12))
	return speed_rating

'''
_________________________________________________
'''


#MIS
#Define our connection string
conn_string = "host='pellefant-01.db.elephantsql.com' dbname='uncrgpvf' user='uncrgpvf' password='rkWkfGnFqOJsniQbLNAFk07p-XOEIz31'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"

# reading in from file
cursor.execute("SELECT * FROM mis_states_2015")

mis = []
i = 0
for row in cursor.fetchall():
	mis.append(row)
	temp = splitter(row[3])
	mis[i] = list(mis[i])
	mis[i].append(temp)
	i = i + 1
	
conn.close()

'''
_________________________________________________
'''


#Huron Meadows

#Define our connection string
conn_string = "host='pellefant-01.db.elephantsql.com' dbname='uncrgpvf' user='uncrgpvf' password='rkWkfGnFqOJsniQbLNAFk07p-XOEIz31'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"

# reading in from file
cursor.execute("SELECT * FROM huron_meadows_metropark_2015")

huron_mp = []
i = 0
for row in cursor.fetchall():
	huron_mp.append(row)
	temp = splitter(row[3])
	huron_mp[i] = list(huron_mp[i])
	huron_mp[i].append(temp)
	i = i + 1
	
conn.close()

'''
_________________________________________________
'''

#Willow Metropark

#Define our connection string
conn_string = "host='pellefant-01.db.elephantsql.com' dbname='uncrgpvf' user='uncrgpvf' password='rkWkfGnFqOJsniQbLNAFk07p-XOEIz31'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"

# reading in from file
cursor.execute("SELECT * FROM willow_metropark_2015")

willow_mp = []
i = 0
for row in cursor.fetchall():
	willow_mp.append(row)
	temp = splitter(row[3])
	willow_mp[i] = list(willow_mp[i])
	willow_mp[i].append(temp)
	i = i + 1
	
conn.close()

'''
_________________________________________________
'''

#Portage

#Define our connection string
conn_string = "host='pellefant-01.db.elephantsql.com' dbname='uncrgpvf' user='uncrgpvf' password='rkWkfGnFqOJsniQbLNAFk07p-XOEIz31'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"

# reading in from file
cursor.execute("SELECT * FROM portage_2k15")

portage_ms = []
i = 0
for row in cursor.fetchall():
	portage_ms.append(row)
	temp = splitter(row[3])
	portage_ms[i] = list(portage_ms[i])
	portage_ms[i].append(temp)
	i = i + 1
	
conn.close()

'''
_________________________________________________
'''

#Forest Akers

#Define our connection string
conn_string = "host='pellefant-01.db.elephantsql.com' dbname='uncrgpvf' user='uncrgpvf' password='rkWkfGnFqOJsniQbLNAFk07p-XOEIz31'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"

# reading in from file
cursor.execute("SELECT * FROM spartanfixed2_2015")

forest_ak = []
i = 0
for row in cursor.fetchall():
	forest_ak.append(row)
	temp = splitter(row[3])
	forest_ak[i] = list(forest_ak[i])
	forest_ak[i].append(temp)
	i = i + 1
	
conn.close()


'''
_________________________________________________
'''


#Springfield Oaks

#Define our connection string
conn_string = "host='pellefant-01.db.elephantsql.com' dbname='uncrgpvf' user='uncrgpvf' password='rkWkfGnFqOJsniQbLNAFk07p-XOEIz31'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"

# reading in from file
cursor.execute("SELECT * FROM nholly_2015")

spring_ok = []
i = 0
for row in cursor.fetchall():
	spring_ok.append(row)
	temp = splitter(row[3])
	spring_ok[i] = list(spring_ok[i])
	spring_ok[i].append(temp)
	i = i + 1
	
conn.close()

'''
_________________________________________________
'''

#Ella Sharp

#Define our connection string
conn_string = "host='pellefant-01.db.elephantsql.com' dbname='uncrgpvf' user='uncrgpvf' password='rkWkfGnFqOJsniQbLNAFk07p-XOEIz31'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"

# reading in from file
cursor.execute("SELECT * FROM ella_sharp_park_15")

ella_sp = []
i = 0
for row in cursor.fetchall():
	ella_sp.append(row)
	temp = splitter(row[3])
	ella_sp[i] = list(ella_sp[i])
	ella_sp[i].append(temp)
	i = i + 1
	
conn.close()


'''
_________________________________________________
'''

#Bloomer Park

#Define our connection string
conn_string = "host='pellefant-01.db.elephantsql.com' dbname='uncrgpvf' user='uncrgpvf' password='rkWkfGnFqOJsniQbLNAFk07p-XOEIz31'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"

# reading in from file
cursor.execute("SELECT * FROM bloomer_park_2015")

bloom_pk = []
i = 0
for row in cursor.fetchall():
	bloom_pk.append(row)
	temp = splitter(row[3])
	bloom_pk[i] = list(bloom_pk[i])
	bloom_pk[i].append(temp)
	i = i + 1
	
conn.close()

'''
_________________________________________________
'''

#Uncle John's Cider Mill

#Define our connection string
conn_string = "host='pellefant-01.db.elephantsql.com' dbname='uncrgpvf' user='uncrgpvf' password='rkWkfGnFqOJsniQbLNAFk07p-XOEIz31'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"

# reading in from file
cursor.execute("SELECT * FROM uncle_johns_cider_mill_2015")

uncle_cm = []
i = 0
for row in cursor.fetchall():
	uncle_cm.append(row)
	temp = splitter(row[3])
	uncle_cm[i] = list(uncle_cm[i])
	uncle_cm[i].append(temp)
	i = i + 1
	
conn.close()

'''
_________________________________________________
'''

#Lake Erie Metropark

#Define our connection string
conn_string = "host='pellefant-01.db.elephantsql.com' dbname='uncrgpvf' user='uncrgpvf' password='rkWkfGnFqOJsniQbLNAFk07p-XOEIz31'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"

# reading in from file
cursor.execute("SELECT * FROM lake_erie_metropark_2015")

lake_mp = []
i = 0
for row in cursor.fetchall():
	lake_mp.append(row)
	temp = splitter(row[3])
	lake_mp[i] = list(lake_mp[i])
	lake_mp[i].append(temp)
	i = i + 1
	
conn.close()

'''
_________________________________________________
'''





	


 
if __name__ == "__main__":
	#main()

	#meanMichigan = mean_michigan(mis, huron_mp, willow_mp, portage_ms, forest_ak, spring_ok, ella_sp, bloom_pk, uncle_cm, lake_mp)
	#print meanMichigan
	#print st_dev_michigan(mis, huron_mp, willow_mp, portage_ms, forest_ak, spring_ok, ella_sp, bloom_pk, uncle_cm, lake_mp)
	count = 0
	i = 0
	for index in mis:
		j = 0
		if i < len(mis):
			for index in mis[i]:
				print mis[i][j]
				count = count + 1
				j = j+1



		i = i + 1

	print count
