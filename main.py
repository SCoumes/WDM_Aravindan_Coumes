import sys
import os

sys.path.append("src")

args = sys.argv

if len(args) <= 1 :
    print("Please specify a command")
elif args[1] == "sample" :
    from  preliminarySort import getfields
    datapath = args[2]
    temp_dir = args[3]
    nbr_samples = int(args[4])
    print(getfields(nbr_samples, datapath, temp_dir))
elif args[1] == "filter" :
    from preliminarySort import filter_data
    from utilitary import clean_folder
    datapath = args[2]
    temp_path = args[3]
    new_datapath = args[4]
    fieldname = args[5]
    clean_folder(new_datapath) 
    filter_data(fieldname, datapath, new_datapath, temp_path)
else : 
    print("Unknown command")

