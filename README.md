# PhonePe-Pulse-DataVisualization
Hello Friends , this is the app i created to analyse Phonepe pulse data which i get through Phonepe pulse github repo.Then I deployed this app in streamlit.

First lets extracts datas from the https://github.com/PhonePe/pulse#readme github repository .

After cloning files from github repo i created a for loop to loop through each folder and get datas from it and then append it to a dataframe to make it easy to covert to mySQL tables.

![image](https://github.com/Nishayanbhar/PhonePe-Pulse-DataVisualization/assets/84184284/40e78aea-5bdc-4bb1-a1be-f8217deb3b77)


data_extraction

In this above code we can see that in each step we go through the folders and we also setting the folder name as a value for dictionary.

Now we want to repeat this process for all respective folders then we can get all the data in our desired format of csv.

After extracting the data we need to upload it into Mysql
To insert datas into Mysql i used sqlalchemy(in order to establish connection you want pymysql also)

In order to insert csv to Mysql we need to establish connection to Mysql server
sql_connection

After connection we need to create table then we can insert csv files to Mysql database
sql_insert

To see full code see in mysqlinsert.ipynb file Repeat the above process for all csv files to insert into your Mysql database

Then after inserting all my files to Mysql database. I created a new file named main.py to create a app using streamlit.

My app preview
appimage

Geo-visualization of Transaction datas
To see detailed code to use plotly for Geo visualization see main.py (Geo-visualization of transacion data section) geo visualization

User device analysis od Phonepe data
TREEMAP ANALYSIS
userdevice

BAR CHART ANALYSIS
user

Payment type analysis
PIE CHART ANALYSIS
paymentpie

BAR CHART ANALYSIS
paymentbar

In side bar you can see overall India's data visualization for all datas.
