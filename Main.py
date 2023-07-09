import streamlit as st
from PIL import Image
import os
import json
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import mysql.connector as sql


##This is to extract the data (from India -states-years-quarter files )to create a dataframe
# --------------------------------------------For df_aggregated_trans table----------------------------------------------------

path="data/aggregated/transaction/country/india/state/"
Agg_state_list=os.listdir(path)
#print(Agg_state_list)

clm={'State':[], 'Year':[],'Quater':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['Transacion_type'].append(Name)
              clm['Transacion_count'].append(count)
              clm['Transacion_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))

Agg_Trans=pd.DataFrame(clm)
#print(Agg_Trans)


# --------------------------------------------For df_aggregated_user ----------------------------------------------------
path2="data/aggregated/user/country/india/state/"
user_list = os.listdir(path2)
col2 = {'State': [], 'Year': [], 'Quater': [], 'brands': [], 'Count': [],'Percentage': []}
for i in user_list:
    p_i = path2 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            B = json.load(Data)
            try:
                for w in B["data"]["usersByDevice"]:
                    brand_name = w["brand"]
                    count_ = w["count"]
                    ALL_percentage = w["percentage"]
                    col2["brands"].append(brand_name)
                    col2["Count"].append(count_)
                    col2["Percentage"].append(ALL_percentage)
                    col2["State"].append(i)
                    col2["Year"].append(j)
                    col2["Quater"].append(int(k.strip('.json')))
            except:
                pass
df_aggregated_user = pd.DataFrame(col2)
#print(df_aggregated_user)


# ------------------------------------------------------- for map transaction table----------------------------------
path3="data/map/transaction/hover/country/india/state/"
hover_list = os.listdir(path3)

col3 = {'State': [], 'Year': [], 'Quater': [], 'District': [], 'count': [],
        'amount': []}
for i in hover_list:
    p_i = path3 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            C = json.load(Data)
            for x in C["data"]["hoverDataList"]:
                District = x["name"]
                count = x["metric"][0]["count"]
                amount = x["metric"][0]["amount"]
                col3["District"].append(District)
                col3["count"].append(count)
                col3["amount"].append(amount)
                col3['State'].append(i)
                col3['Year'].append(j)
                col3['Quater'].append(int(k.strip('.json')))
df_map_transaction = pd.DataFrame(col3)
#print(df_map_transaction)


# ------------------------------------------------------for map user table------------------------------------------------
path4="data/map/user/hover/country/india/state/"
map_list = os.listdir(path4)

col4 = {"State": [], "Year": [], "Quater": [], "District": [],
        "RegisteredUser": []}
for i in map_list:
    p_i = path4 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            D = json.load(Data)

            for u in D["data"]["hoverData"].items():
                district = u[0]
                registereduser = u[1]["registeredUsers"]
                col4["District"].append(district)
                col4["RegisteredUser"].append(registereduser)
                col4['State'].append(i)
                col4['Year'].append(j)
                col4['Quater'].append(int(k.strip('.json')))
df_map_user = pd.DataFrame(col4)


#------------------------------------------------for top transaction-------------------------------------------------------
path5="data/top/transaction/country/india/state/"

TOP_list = os.listdir(path5)

col5 = {'State': [], 'Year': [], 'Quater': [], 'District': [], 'Transaction_count': [],
        'Transaction_amount': []}
for i in TOP_list:
    p_i = path5 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            E = json.load(Data)
            for z in E['data']['pincodes']:
                Name = z['entityName']
                count = z['metric']['count']
                amount = z['metric']['amount']
                col5['District'].append(Name)
                col5['Transaction_count'].append(count)
                col5['Transaction_amount'].append(amount)
                col5['State'].append(i)
                col5['Year'].append(j)
                col5['Quater'].append(int(k.strip('.json')))
df_top_transaction = pd.DataFrame(col5)


# ------------------------------------------for top user-------------------------------------------------------------------
path6="data/top/user/country/india/state/"

USER_list = os.listdir(path6)

col6 = {'State': [], 'Year': [], 'Quater': [], 'District': [],
        'RegisteredUser': []}
for i in USER_list:
    p_i = path6 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            F = json.load(Data)
            for t in F['data']['pincodes']:
                Name = t['name']
                registeredUser = t['registeredUsers']
                col6['District'].append(Name)
                col6['RegisteredUser'].append(registeredUser)
                col6['State'].append(i)
                col6['Year'].append(j)
                col6['Quater'].append(int(k.strip('.json')))
df_top_user = pd.DataFrame(col6)



# CREATING CONNECTION WITH MYSQL

connection= sql.connect(host="localhost",user="root",password="1234", database="phonepe_db")
print(connection)
cursor=connection.cursor()
cursor.execute("use phonepe_db")

# create top_user sql table and insert DF values to table

cursor.execute("create table if not exists top_user(State varchar(255),Year int ,Quater int ,District varchar(255),RegisteredUser bigint)")
for row in df_top_user.itertuples(index=False):
    # Check if any value in the row is empty
    if any(value == '' or pd.isnull(value) for value in row):
        continue

    # Convert row values to a comma-separated string
    values = "', '".join(str(value) for value in row)

    insert_query = f"INSERT INTO top_user VALUES ('{values}')"
    cursor.execute(insert_query)

connection.commit()

# create top_transaction sql table and insert DF values to table

cursor.execute("create table if not exists top_transaction(State varchar(255),Year int ,Quater int,District int,Transaction_count bigint,Transaction_amount double)")
for row in df_top_transaction.itertuples(index=False):
    # Check if any value in the row is empty
    if any(value == '' or pd.isnull(value) for value in row):
        continue

    # Convert row values to a comma-separated string
    values = "', '".join(str(value) for value in row)

    insert_query = f"INSERT INTO top_transaction VALUES ('{values}')"
    cursor.execute(insert_query)

connection.commit()


# create aggregated_transaction sql table and insert DF values to table

cursor.execute("create table if not exists aggregated_transaction(State varchar(255),Year int ,Quater int ,Transacion_type varchar(255),Transacion_count bigint,Transacion_amount double)")
for row in Agg_Trans.itertuples(index=False):
    # Check if any value in the row is empty
    if any(value == '' or pd.isnull(value) for value in row):
        continue

    # Convert row values to a comma-separated string
    values = "', '".join(str(value) for value in row)

    insert_query = f"INSERT INTO aggregated_transaction VALUES ('{values}')"
    cursor.execute(insert_query)

connection.commit()


# create aggregated_user sql table and insert DF values to table

cursor.execute("create table if not exists aggregated_user(State varchar(255),Year int ,Quater int ,brands varchar(255),Count bigint ,Percentage double)")
for row in df_aggregated_user.itertuples(index=False):
    # Check if any value in the row is empty
    if any(value == '' or pd.isnull(value) for value in row):
        continue

    # Convert row values to a comma-separated string
    values = "', '".join(str(value) for value in row)

    insert_query = f"INSERT INTO aggregated_user VALUES ('{values}')"
    cursor.execute(insert_query)

connection.commit()


# create map_transaction sql table and insert DF values to table

cursor.execute("create table if not exists map_transaction(State varchar(255),Year int ,Quater int ,District varchar(255),count bigint,amount double)")
for row in df_map_transaction.itertuples(index=False):
    # Check if any value in the row is empty
    if any(value == '' or pd.isnull(value) for value in row):
        continue

    # Convert row values to a comma-separated string
    values = "', '".join(str(value) for value in row)

    insert_query = f"INSERT INTO map_transaction VALUES ('{values}')"
    cursor.execute(insert_query)

connection.commit()

# create map_user sql table and insert DF values to table

cursor.execute("create table if not exists map_user(State varchar(255),Year int ,Quater int ,District varchar(255),RegisteredUser bigint)")
for row in df_map_user.itertuples(index=False):
    # Check if any value in the row is empty
    if any(value == '' or pd.isnull(value) for value in row):
        continue

    # Convert row values to a comma-separated string
    values = "', '".join(str(value) for value in row)

    insert_query = f"INSERT INTO map_user VALUES ('{values}')"
    cursor.execute(insert_query)

connection.commit()


#

phn=Image.open('images/phonepe-logo-icon.png')
st.set_page_config(page_title='PhonePe Pulse',page_icon=phn,layout='wide')
st.title(':violet[ PhonePe Pulse Data Visualization ]')
st.title(':violet[                                  ]')


SELECT = option_menu(
            menu_title = None,
            options = ["Home","Search","Basic insights"],
            icons =["bar-chart","search","house","toggles","at"],
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "white","size":"cover"},
                "icon": {"color": "black", "font-size": "20px"},
                "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
                "nav-link-selected": {"background-color": "#6F36AD"}
            }
    )

if SELECT == "Home":
    #st.subheader("PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
    col1,col2, = st.columns(2)
    with col1:
        #st.video(video1)
        new_image = phn.resize((350, 350))
        st.image(new_image)
        st.download_button("     DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        st.subheader("PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")


if SELECT == "Basic insights":
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--","Top 10 states based on amount of transaction","Least 10 states based on amount of transaction",
               "Top 10 States based on Registered-users count","Least 10 States based on Registered-users count",
               "Top 10 mobile brands based on count of transaction","Least 10 mobile brands based on count of transaction"]

    select = st.selectbox("Select the option",options)

    if select=="Top 10 states based on amount of transaction":
        cursor.execute("SELECT State , SUM(transaction_amount) AS total_amount FROM top_transaction GROUP BY state ORDER BY total_amount DESC LIMIT 10 ");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 states based on amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount",color="State")
            st.plotly_chart(fig, theme=None, use_container_width=True)

    if select=="Least 10 states based on amount of transaction":
        cursor.execute("SELECT State , SUM(transaction_amount) AS total_amount FROM top_transaction GROUP BY state ORDER BY total_amount ASC LIMIT 10 ");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 states based on amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount",color="State")
            st.plotly_chart(fig, theme=None, use_container_width=True)



    elif select=="Top 10 mobile brands based on count of transaction":
        cursor.execute("SELECT brands, sum(count) as total_count FROM aggregated_user GROUP BY brands ORDER BY total_count DESC LIMIT 10")
        df = pd.DataFrame(cursor.fetchall(),columns=['brands','count'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 mobile brands based on count of transaction")
            fig=px.bar(df,x="brands",y="count",color="brands")
            st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Least 10 mobile brands based on count of transaction":
        cursor.execute("SELECT brands, sum(count) as total_count FROM aggregated_user GROUP BY brands ORDER BY total_count ASC LIMIT 10")
        df = pd.DataFrame(cursor.fetchall(),columns=['brands','count'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 mobile brands based on count of transaction")
            fig=px.bar(df,x="brands",y="count",color='brands')
            st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Top 10 States based on Registered-users count":
        cursor.execute("SELECT State, sum(RegisteredUser) as total_reg_user FROM top_user GROUP BY State ORDER BY total_reg_user DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','RegisteredUser'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 States based on Registered-users count")
            fig=px.bar(df,x="State",y="RegisteredUser",color='State')
            st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Least 10 States based on Registered-users count":
        cursor.execute("SELECT State, sum(RegisteredUser) as total_reg_user FROM top_user GROUP BY State ORDER BY total_reg_user ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','RegisteredUser'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 States based on Registered-users count")
            fig=px.bar(df,x="State",y="RegisteredUser",color='State')
            st.plotly_chart(fig, theme=None, use_container_width=True)




if SELECT =="Search":
    Topic = ["","Brand","Registered-users","Top-Transactions"]
    choice_topic = st.selectbox("Search by",Topic)

    def brand_state(state,brand_type,year):
        cursor.execute(f"SELECT State,Year,Quater,brands,sum(Percentage) as total_count FROM aggregated_user WHERE State = '{state}' AND brands='{brand_type}' AND Year = '{year}' group by Quater ORDER BY Quater ASC");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'brands', 'Percentage'])
        return df

    def transaction_state(state,year):
        cursor.execute(f"SELECT State,Year,Quater,sum(Transaction_count), sum(Transaction_amount) FROM top_transaction WHERE Year = '{year}' AND State = '{state}' GROUP BY Quater ORDER BY Quater ASC")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Transaction_count', 'Transaction_amount'])
        return df


    def registered_state(state, year):
        cursor.execute(f"SELECT State,Year,Quater,sum(RegisteredUser) FROM map_user WHERE Year = '{year}' AND State = '{state}' GROUP BY Quater ORDER BY Quater ASC ")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year','Quater','RegisteredUser'])
        return df

    if choice_topic == "Brand":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader(" SELECT BRAND ")
            mobiles = ['', 'Apple', 'Asus', 'COOLPAD', 'Gionee', 'HMD Global', 'Huawei', 'Infinix', 'Lava', 'Lenovo',
                       'Lyf', 'Micromax', 'Motorola', 'OnePlus', 'Oppo', 'Others', 'Realme', 'Samsung', 'Tecno', 'Vivo',
                       'Xiaomi']
            brand_type = st.selectbox("search by", mobiles, 0)
        with col2:
            st.subheader(" SELECT YEAR")
            choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
        with col3:
            st.subheader(" SELECT STATE ")
            menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar',
                          'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                          'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                          'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                          'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha',
                          'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura',
                          'uttar-pradesh', 'uttarakhand', 'west-bengal']
            choice_state = st.selectbox("State", menu_state, 0)

        if brand_type and choice_state and choice_year:
            col1, col2,col3 = st.columns(3)
            with col1:
                st.subheader(f' in {choice_state}')
                st.write(brand_state(choice_state, brand_type, choice_year))
            with col2:
                df = brand_state(choice_state, brand_type, choice_year)
                fig = px.bar(df, x="Quater", y="Percentage",title=f"{brand_type} Users in {choice_year} at {choice_state}",color='Quater')
                st.plotly_chart(fig, theme=None,use_container_width=True)

    if choice_topic == "Top-Transactions":
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader(" SELECT STATE ")
            menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar',
                          'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                          'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                          'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                          'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha',
                          'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura',
                          'uttar-pradesh', 'uttarakhand', 'west-bengal']
            choice_state = st.selectbox("State", menu_state, 0)

        with col2:
            st.subheader(" SELECT YEAR")
            choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)

        if choice_state and choice_year:
            col1, col2,col3 = st.columns(3)
            with col1:
                st.subheader(f'{choice_state}')
                st.write(transaction_state(choice_state, choice_year))
            with col2:
                df = transaction_state(choice_state, choice_year)
                fig = px.bar(df, x="Quater", y="Transaction_count",title=f"Transactions in {choice_year} at {choice_state}")
                st.plotly_chart(fig, theme=None, use_container_width=True)

            with col3:
                df = transaction_state(choice_state, choice_year)
                fig = px.bar(df, x="Quater", y="Transaction_amount",title=f"Transactions in {choice_year} at {choice_state}",color='Quater')
                st.plotly_chart(fig, theme=None, use_container_width=True)


    if choice_topic == "Registered-users":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader(" SELECT STATE ")
            menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar',
                          'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                          'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                          'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                          'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry',
                          'punjab',
                          'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand',
                          'west-bengal']
            choice_state = st.selectbox("State", menu_state, 0)
        with col2:
            st.subheader(" SELECT YEAR ")
            choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)


        if choice_state and choice_year:
            col1, col2,col3= st.columns(3)

            with col1:
                st.subheader(f'{choice_state}')
                st.write(registered_state(choice_state, choice_year))

            with col2:
                if choice_state and choice_year:
                    df = registered_state(choice_state, choice_year)
                    fig = px.bar(df, x="Quater", y="RegisteredUser",title=f"Registered users at {choice_state} in {choice_year} ",color='Quater')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
