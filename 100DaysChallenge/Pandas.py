import pandas as pd
import datetime
import matplotlib as plt
import seaborn as sns
import plotly as px

#####Ananlysis on our First Dataset covid_df#############
covid_df = pd.read_csv("Path") # Reading CSV Data using Pandas LIB and stroin it in Dataframe
vaccine_df = pd.read_csv("Path") # Reading CSV Data using Pandas LIB and stroin it in Dataframe
covid_df.head(10) #Gives Top 10 rows data to preview for analysis
covid_df.info() #Gives Table description for our created Dataframe
covid_df.drop(["Column1"],["Column2"],["Column3"],inplace = True,axis = 1) #Drop Unwanted Columns from Dataframe
covid_df(['Date']) = pd.to_datetime(covid_df(['Date']), format = '%Y-%m-%d') #Convert Date column Datatype from Object to Datetime
covid_df['Active_Cases']  = covid_df['Confirmed'] - (covid_df['Cured'] + covid_df['Deaths']) #Creating New Column in our Dataframe
covid_df.tail() #Gives you Data from Bottom for analysis
statewise = pd.pivot_table(covid_df,values = ["Confirmed","Deaths","Cured"], index = "State" , aggfunc = max) #Create Pivot Table for our Dataframe
statewise['RecoveryRate'] = statewise['Cured']*100/statewise['Confirmed']
statewise['MortalityRate'] = statewise['Deaths']*100/statewise['Confirmed'] #Creating Calulated Columns from our Pivot Table
statewise = statewise.sort_values(by = "Confirmed", ascending = False) #Will sort the Pivot Table by Confirmed Column in descending order
statewise.style.background_gradient(cmap = 'cubehelix') #This is a function from Matplotlib which gives the columns a color

#Top 10 Active cases. Using Groupby function of Pandas
top_10_active_cases = covid_df.groupby(by = "State").max()[['Active_Cases','Date']].sort_values(by = ['Active_Cases'], ascending = False).reset_index()
fig = plt.figure(figsize = (16,9)) #This variable creates a Graph of given size
plt.title("Top 10 States with most active cases in India",size = 25) #Gives Title to the Graph
ax = sns.barplot(data = top_10_active_cases.iloc[:10], y = "Active_Cases" ,x = "State", linewidth = 2, edgecolor = 'red') #This will create Bar Graph for Top 10 Active States for Covid
plt.xlabel("States")
plt.ylabel("Total Active Cases")
plt.show() #The above 3 lines will give proper display for our Bar Graph with Labels

#Top States with Highest Deaths
top_10_death_cases = covid_df.groupby(by = "State").max()[['Deaths','Date']].sort_values(by = ['Death'], ascending = False).reset_index()
fig = plt.figure(figsize = (16,9)) #This variable creates a Graph of given size
plt.title("Top 10 States with most Death cases in India",size = 25) #Gives Title to the Graph
ax = sns.barplot(data = top_10_death_cases.iloc[:12], y = "Deaths" ,x = "State", linewidth = 2, edgecolor = 'black') #This will create Bar Graph for Top 10 Active States for Covid Deaths
plt.xlabel("States")
plt.ylabel("Total Death Cases")
plt.show() #The above 3 lines will give proper display for our Bar Graph with Labels

#Growth Trend
fig = plt.figure(figsize = (12,6))
ax = linePlot(data = covid_df[covid_df["State"].isin(['Maharashtra','Karnataka','Kerala','Tamil Nadu','Uttar Pradesh']), x= 'Date', y= 'Active_Cases', hue = 'State'])
ax.set_title("Top 5 Affected States in India" , size = 16) #Also defines Title in Line Graph


#####Analysis on our Second Dataframe########
vaccine_df.rename(columns = {'Update_on':'Vaccine_Date'},inplace = True) # Renaming column of the Date Column
vaccine_df.info()
vaccine_df.isnull().sum() #Gives all Columns Count with missing Values
vaccination = vaccine_df.drop(["Column1"],["Column2"],["Column3"],inplace = True,axis = 1) #Drop Unwanted Columns from Dataframe
vaccination.head()

#Male vs Female Vaccination
male = vaccination["Male_Vaccinated"].sum()
female = vaccination["Female_Vaccinated"].sum()
px.pie(names = ["Males","Females"], values = [male,female], title = "Male and Female Vaccination") #Using Pie Graph from Plotly LIB with its functions

#Remove rows where State is India
vaccine = vaccine_df[vaccine_df.State != "India"]
vaccine #Dataframe where State is not equal to India
vaccine.rename(columns = {Total Individual Vaccinated}: "Total",inplace=True)
vaccine.head()

#Most Vaccinated State
#Creating Variable which will create Table for Most number of Vaccinated States
max_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
max_vac = max_vac.sort_values(by = 'Total', ascending = False)[:5]
max_vac

#Making Barplot
fig = plt.figure(figsize = (10,5)) #This variable creates a Graph of given size
plt.title("Top 5 Most Vaccinated States in India",size = 20) #Gives Title to the Graph
ax = sns.barplot(data = max_vac.iloc[:10], y = max_vac.Total ,x = max_vac.index, linewidth = 2, edgecolor = 'black')
plt.xlabel("States")
plt.ylabel("Vaccination")
plt.show()

#Least Vaccinated State
#Creating Variable which will create Table for Most number of Vaccinated States
max_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
max_vac = max_vac.sort_values(by = 'Total', ascending = True)[:5]
max_vac

#Making Barplot
fig = plt.figure(figsize = (10,5)) #This variable creates a Graph of given size
plt.title("Top 5 Least Vaccinated States in India",size = 20) #Gives Title to the Graph
ax = sns.barplot(data = max_vac.iloc[:10], y = max_vac.Total ,x = max_vac.index, linewidth = 2, edgecolor = 'black')
plt.xlabel("States")
plt.ylabel("Vaccination")
plt.show()