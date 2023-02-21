#Create Virtaul Environment
python -m venv myenv

#Activate Virtual Environment for Windows
myenv/Scripts/activate.bat

#Deavtivate
deactivate

#Getting installed package list for that particular environment
pip freeze > requirements.txt

#If I need to install all required package in My Environment I can get the list from it and install it in my Environment.
pip install -r requirements.txt
