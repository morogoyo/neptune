import json
import urllib.request
import hashlib
import os.path

#### working variables
location= 'http://localhost/data/test/json.php'# this variable is to fetch the information from php script #content in this variable must have quotation marks
path = 'C:/wamp64/www/data/test/file_test' #changing this variable will change the location of the file produced by this script
file_name = "encrypted_json" # this is the name of the file that will be outputed by this script no file extention


 #this will be put in to the file being created 

response = urllib.request.urlopen(location)
#since it was a url it had to be decoded from bytes to strin
str_response = response.read().decode('utf-8')
#loads response as a string since decoded
obj = json.loads(str_response)
#shows amount of objects in array for testing purposes only 
print(len(obj['data']),'line 18 for testing purposes')
# print(obj['data'])
#iterating thru json object using the main object as range to loop thru all objects in the array#
#rang(len()) counts the amout of items with in the array 
for i in range(len(obj['data'])):
#had to encode with utf-8 to be able to use the hash library####################################################
		

		### start of if statement
	if obj['data'][i]['first_name'] != None:  #conditional is set to catch any None vaules that might be in the json and will convert accordingly 
		f_name = obj['data'][i]['first_name'].encode('utf-8')
	else:
		f_name = obj['data'][i]['first_name'] ="test"
		f_name = obj['data'][i]['first_name'].encode('utf-8')
		#### end of if 
		### start of if statement
	if obj['data'][i]['last_name'] != None:  #conditional is set to catch any None vaules that might be in the json and will convert accordingly 
		l_name = obj['data'][i]['last_name'].encode('utf-8')
	else:
		l_name = obj['data'][i]['last_name'] ="test"
		l_name = obj['data'][i]['last_name'].encode('utf-8')
		#### end of if 
		### start of if statement
	if obj['data'][i]['address_1'] != None:  #conditional is set to catch any None vaules that might be in the json and will convert accordingly 
		address_1 = obj['data'][i]['address_1'].encode('utf-8')
	else:
		f_name = obj['data'][i]['last_name'] ="test"
		address_1 = obj['data'][i]['address_1'].encode('utf-8')
		#### end of if 
	 ### start of if statement
	if obj['data'][i]['address_2'] != None:  #conditional is set to catch any None vaules that might be in the json and will convert accordingly 
		address_2 = obj['data'][i]['address_2'].encode('utf-8')
	else:
		obj['data'][i]['address_2']="test"
		address_2 = obj['data'][i]['address_2'].encode('utf-8')
		#### end of if 
		### start of if statement
	if obj['data'][i]['email'] != None:
		email = obj['data'][i]['email'].encode('utf-8')
	else:
		obj['data'][i]['email']="test"
		email = obj['data'][i]['email'].encode('utf-8')
		#### end of if
		### start of if statement
	if obj['data'][i]['city'] != None :
		city = obj['data'][i]['city'].encode('utf-8')
	else:
		obj['data'][i]['city']="test"
		city = obj['data'][i]['city'].encode('utf-8')
		#### end of if
		### start of if statement
	if obj['data'][i]['state'] != None:
		state = obj['data'][i]['state'].encode('utf-8')
	else:
		obj['data'][i]['state']="test"
		state = obj['data'][i]['state'].encode('utf-8')
		#### end of if
		### start of if statement
	if obj['data'][i]['PAX_EMAIL'] != None:
	 	Email = obj['data'][i]['PAX_EMAIL'].encode('utf-8')
	else:
		obj['data'][i]['PAX_EMAIL']="test"
		Email = obj['data'][i]['PAX_EMAIL'].encode('utf-8')

############# Hahsing acciton ##################################################################################
	hash_f_name =  hashlib.sha512(f_name).hexdigest()
	hash_l_name =  hashlib.sha512(l_name).hexdigest()
	hash_address_1 =  hashlib.sha512(address_1).hexdigest()
	hash_address_2 =  hashlib.sha512(address_2).hexdigest()
	hash_email =  hashlib.sha512(email).hexdigest()
	hash_Email =  hashlib.sha512(Email).hexdigest() 

############# inserting data back in to the json array #########################################################

	obj['data'][i]['first_name']=hash_f_name
	obj['data'][i]['last_name']=hash_l_name
	obj['data'][i]['address_1']=hash_address_1
	obj['data'][i]['address_2']=hash_address_2
	obj['data'][i]['email']=hash_email
	obj['data'][i]['PAX_EMAIL']=hash_Email
	# obj['data'][i]['first_name']=var_hash
	# obj['data'][i]['first_name']=var_hash
	# obj['data'][i]['first_name']=var_hash
	# obj['data'][i]['first_name']=var_hash


data_object = obj['data']
# print(obj['data'][0]['first_name'])
## Creation of file containing code that is hashed 

def conversion(name_of_file,save_path,format,data):
	completeName = os.path.join(save_path, name_of_file+'.'+format)         
	file1 = open(completeName, "w")
	file1.write(repr(data))
	file1.close()



def ret_object(test):
    print(test)
    return obj

conversion(file_name,path,'php',data_object)
#test = ret_object(obj['data'])
