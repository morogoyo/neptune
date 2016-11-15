

import pandas 
import urllib.request
import hashlib
import os.path
import sys

from hashing import *



# scriptpath = "working_scripts/hashing.py"
# # Add the directory containing your module to the Python path (wants absolute paths)
# sys.path.append(os.path.abspath(scriptpath))
# import hashing

# from pandas.io.json import json_normalize
# #for i in range(len(obj['data'])):
# 	# print (i)
# 	# result = json_normalize(obj['data'][i],)
# 	######################################################

# df = pandas.DataFrame(obj['data'])
# # result = read_json(obj['data'])

# conversion("csvFile",path,'csv',df)
# print(df)


import json

import csv

response = urllib.request.urlopen("http://localhost/data/file_test/encrypted_json.php")
#since it was a url it had to be decoded from bytes to strin
str_response = response.read().decode('utf-8').replace("'",'"')
#print(str_response)

################# testing variable with json##########################################

#raw_json='{"data":[{"profile_url": "http://www.google.com","username": "a85","password": "blah"},{"profile_url":"http://www.getpostman.com","username": "larry","password": "nocolors"}]}'

#######################################################################################

#loads response as a string since decoded
obj = json.loads(str_response).encode('utf-8')
#raw_json.encode('utf-8')
#obj = json.loads(raw_json)
#shows amount of objects in array for testing purposes only 
# print(len(obj['data']),'line 18 for testing purposes')


###########test print ###############################
# print(obj)
#####################################################
# employee_parsed = json.loads(raw_json)

# emp_data = employee_parsed['data']

# # # open a file for writing

# employ_data = open('EmployData.csv', 'w')

# # # create the csv writer object

# csvwriter = csv.writer(employ_data)

# count = 0

# for emp in emp_data:

#     if count == 0:

#         header = emp.keys()

#         csvwriter.writerow(header)

#         count += 1

# csvwriter.writerow(emp.values())
# employ_data.close()


###################### Working Code ###############################################
# employee_parsed = json.loads(raw_json)

# emp_data = employee_parsed['data']

# # # open a file for writing

# employ_data = open('EmployData.csv', 'w')

# # # create the csv writer object

# csvwriter = csv.writer(employ_data)

# count = 0

# for emp in emp_data:

#     if count == 0:

#         header = emp.keys()

#         csvwriter.writerow(header)

#         count += 1

# csvwriter.writerow(emp.values())
# employ_data.close()

#################### End of working Code ##########################################