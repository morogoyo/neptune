import pandas
import json
import urllib.request
import hashlib
import os.path
import sys

from hashing import *

# scriptpath = "working_scripts/hashing.py"
# # Add the directory containing your module to the Python path (wants absolute paths)
# sys.path.append(os.path.abspath(scriptpath))
# import hashing

from pandas.io.json import json_normalize
result = json_normalize(obj['data'],)

conversion("csvFile",path,'csv',result)
#print(result)