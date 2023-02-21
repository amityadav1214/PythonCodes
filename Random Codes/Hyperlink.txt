import csv
import requests
from datetime import datetime
import os

today = datetime.now()
newdr = r"C:/Users/HP/Desktop/AllExcelData/PythonFiles/" + today.strftime('%Y%m%d')
os.makedirs(newdr,exist_ok=True)    #Creating Date wise folder in Local Path
hpl_file = open('C:/Users/HP/Desktop/AllExcelData/PythonFiles/Main_File.csv')   #Opening Main File to extract URLs from CSV File
hplReader = csv.reader(hpl_file)
next(hplReader)    #Skip First Row as Header of CSV File
hplData = list(hplReader)
count = 0
for row in hplData:
    if row[13] != '':  #If Column contains Blank then pass otherwise extract the Filename
        res = requests.get(row[13])
        filename = res.url[row[13].rfind('/')+1:]
        with open(os.path.join(newdr,filename),'wb') as f:   #Open the file and write in the path
            for chunk in res.iter_content(chunk_size = 8192):
                if chunk:
                    f.write(chunk)
        f.close()
        count += 1
string = str(count)+" No of files downloaded successfully"   #Creating Logfile for count of successfull downloaded sounds
with open(os.path.join(newdr,"LogFile.txt"),'w') as s:
    s.write(string)
s.close()
