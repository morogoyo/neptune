import json
import urllib.request
import hashlib

#content in this variable must have quotation marks
location= 'http://localhost/data/json.php'
response = urllib.request.urlopen(location)

 #since it was a url it had to be decoded from bytes to strin
str_response = response.read().decode('utf-8')

#loads response as a string since decoded
obj = json.loads(str_response)
#obj.encode('utf-8') 



#shows amount of objects in array for testing purposes only 
print(len(obj['data']),'line 18 for testing purposes')

# instanshiation of class hash is the object for it // not being used at this time
# hash = hashlib.sha256()

#iterating thru json object using the main object as range to loop thru all objects in the array#
for i in range(len(obj['data'])):
	
#### accessing data from json array
	
	#printing consumer id's for testing purposes 
	# print(obj['data'][i]['consumer_id'],'testing purposes actual number') 

	#had to encode with utf-8 to be able to use the hash library 
	var = obj['data'][i]['consumer_id'].encode('utf-8')
	
#var_hash = print(hashlib.sha512(var).hexdigest(),'\t testing purposes encoded number')
  # this is in the correct format to be inserted in to the json array or list #####var_hash =  hashlib.sha512(var).hexdigest()
	# var_hash = '"unique_id" :''"'+ hashlib.sha512(var).hexdigest()+'"'

	var_hash =  hashlib.sha512(var).hexdigest()
   
## appending data back in to the json array

	obj['data'][i]['unique_id']=var_hash

	#second try
   # at this point data is only in memory still has not been written to a file for uploas
	# obj['data'][i] = var_hash

	
#test print on all data that was collected and appended
# print(obj)


# file = open('json.php','w')
# file.write(print(obj))
# file.close()

## writing file but it writes in same directory

# filename=
# file = open('/data/rene.php','w')
# file.write(repr(obj))
# file.close()



import os.path

save_path = 'C:\wamp64\www\data\\file_test'

name_of_file = "csv.php"

completeName = os.path.join(save_path, name_of_file+".csv")         
file1 = open(completeName, "w")
file1.write(repr(obj))
file1.close()












#############################################################################################################

#obj_standarization = obj['data'] #standarizing the object to have the initial calls data:[ "x": "y"]

#for email in obj_standarization:
	#if email == obj_standarization['email']
	#print(print email)

#print(obj['data'][0]) #printing objects from json file