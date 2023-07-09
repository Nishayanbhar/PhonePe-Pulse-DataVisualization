# PhonePe-Pulse-DataVisualization
Hello Friends , this is the app i created to analyse Phonepe pulse data which i get through Phonepe pulse github repo.Then I deployed this app in streamlit.

First lets extracts datas from the https://github.com/PhonePe/pulse#readme github repository .

After cloning files from github repo i created a for loop to loop through each folder and get datas from it and then append it to a dataframe to make it easy to covert to mySQL tables.

![image](https://github.com/Nishayanbhar/PhonePe-Pulse-DataVisualization/assets/84184284/40e78aea-5bdc-4bb1-a1be-f8217deb3b77)


In this above code we can see that in each step we go through the folders and we also setting the folder name as a value for dictionary.

Now we want to repeat this process for all respective folders then we can get all the data in our desired format .

After extracting the data we need to upload it into Mysql
To insert datas into Mysql i used mysql.connector .

In order to insert dataframes to Mysql we need to establish connection to Mysql server
sql_connection

![image](https://github.com/Nishayanbhar/PhonePe-Pulse-DataVisualization/assets/84184284/4e8400a1-6665-4193-9a40-27812230268b)

After connection we need to create table then we can insert dataframes to Mysql database
![image](https://github.com/Nishayanbhar/PhonePe-Pulse-DataVisualization/assets/84184284/bf555d7c-78d2-4e8d-b227-11ad41dc3a5b)

Then after inserting all dataframes to Mysql database. we Used the Streamlit and Plotly libraries in Python to create
an interactive and visually appealing dashboard.

My app preview
![image](https://github.com/Nishayanbhar/PhonePe-Pulse-DataVisualization/assets/84184284/a13bae08-373b-45b2-b910-3f987148c531)

Data anlysis by brand
![image](https://github.com/Nishayanbhar/PhonePe-Pulse-DataVisualization/assets/84184284/4b2cb143-a4f7-4298-9f91-03cb7c21066a)

Data anlysis registered users
![image](https://github.com/Nishayanbhar/PhonePe-Pulse-DataVisualization/assets/84184284/356765e8-b2fc-4d91-90a1-f8632925f985)

Data anlysis by top transcation
![image](https://github.com/Nishayanbhar/PhonePe-Pulse-DataVisualization/assets/84184284/7af66222-dc8f-43af-b679-2b6df89e3cb1)

