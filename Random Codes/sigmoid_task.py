import pandas as pd
import numpy as np
import datetime
import time
import warnings
import sys
warnings.filterwarnings("ignore")

from_date=sys.argv[1]
file_name=sys.argv[2]
from_date=((time.mktime(datetime.datetime.strptime(from_date,"%Y%m%d").timetuple()))*1000.0)
from_date=from_date + 19800000 #to gmt
to_date=from_date+86340000 # add 23:59 hrs
sections = ['bids\n','impression\n', 'wins\n', 'click\n'] #number of sections

#fetch all in list
with open(file_name) as raw_data: 
    ldata=[x for x in raw_data] 
    
section_index=[ldata.index(s) for s in sections] #index location of section names in csv
section_index.append(len(ldata)) #add index of last element section (end of file) 

#split the main list into section wise lists
splits=[[] for x in range(len(sections))] #split the main list into section wise lists
i,j=0,1
for s in range(len(section_index)-1):
    splits[s].append(ldata[section_index[i]:section_index[j]])
    i+=1
    j+=1

def pull_section_data(sec):
    ind = sections.index(sec+'\n')
    lsecdata=[e.split(',')[1] for E in splits[ind] for e in E if not e.startswith(sec)]
    lsecdata=[e[:len(e)-1] for e in lsecdata]#remove trailing \n
    return lsecdata
    
lhour=[ e.split(',')[0] for E in splits[0] for e in E if not e.startswith('bids') ]#get the timestamp out 

#segregate the sections
lbids=pull_section_data('bids')
limpression=pull_section_data('impression')
lwins=pull_section_data('wins')
lclick=pull_section_data('click')

#all lists need to be same size before put in Data Frame
lwins.append(0)
lclick.append(0)
lclick.append(0)

#push all list to Dataframe
raw_data_df= pd.DataFrame({'Hour':lhour,'Bids':lbids,'Impression':limpression,'Wins':lwins,'Click':lclick})

#finding The value column that might be empty for some rows
np.where(raw_data_df.applymap(lambda x: x == '')) 
#(array([ 977,  977,  978, 1028, 1028, 1029], dtype=int64),
# array([3, 4, 1, 3, 4, 1], dtype=int64))
raw_data_df.iloc[[977,  977,  978, 1028, 1028, 1029],[3, 4, 1, 3, 4, 1]] = 0 #update all blanks

#convert all columns from object to respective data types as per the problem
raw_data_df['Hour'] = raw_data_df['Hour'].astype('float')#column was too long for int
raw_data_df['Bids'] = raw_data_df['Bids'].astype('int64')
raw_data_df['Impression'] = raw_data_df['Impression'].astype('int64')
raw_data_df['Wins'] = raw_data_df['Wins'].astype('int64')
raw_data_df['Click'] = raw_data_df['Click'].astype('int64')

#sort timestamp ASC
raw_data_df.sort_values(by='Hour',inplace=True, ascending=False)

#filter the DataFrame based on input date and then group by 1hr each sum all other columns
working_set_df=raw_data_df.loc[(raw_data_df['Hour'] >= from_date) & (raw_data_df['Hour'] <= to_date)]

#using Groupby to group sum based on 1hour each
working_set_df['Hour'] = pd.to_datetime(working_set_df['Hour'],unit='ms')
working_set_df=working_set_df.groupby([pd.Grouper(key='Hour', freq='H')])['Bids','Impression','Wins','Click'].sum()
working_set_df=working_set_df.reset_index()
working_set_df['Hour']=(working_set_df['Hour'] - datetime.datetime(1970,1,1)).dt.total_seconds()* 1000.0
working_set_df.to_csv(file_name.split('.')[0]+'_out'+'.csv')
