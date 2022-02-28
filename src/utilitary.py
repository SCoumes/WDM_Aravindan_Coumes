import os
from os import listdir
from os.path import isfile, join
import gzip
import shutil
import json

def decompress(inpath, outpath) :
    print(inpath, outpath)
    with gzip.open(inpath, 'rb') as f_in:
        with open(outpath, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def clean_folder(path) :
    for root, dirs, files in os.walk(path):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))

def listfiles(path) :
   return [join(path, f) for f in listdir(path) if isfile(join(path, f))]

def read_json_list(path) :
    dictList = []
    with open(path, 'r') as f :
        for jsonobj in f :
            dictList.append(json.loads(jsonobj))
    return dictList

def write_json(jsonList, filepath) : 
    with open(filepath,'x') as f :
            f.writelines([json.dumps(jsonObj) + "\n"  for jsonObj in jsonList])
