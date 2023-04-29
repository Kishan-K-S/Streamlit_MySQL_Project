import streamlit as st
import pandas as pd
import mysql.connector
from streamlit_option_menu import option_menu



def insrt(mycursor,mydb):
    selected=option_menu(
        menu_title = "Choose the table",
        options = ["Category","Customer"],      #job,location,type
        orientation="vertical",
    )
    if(selected=="Category"):
        with st.form(key="form1"):
            categorId=st.number_input('Enter the category id')
            catName =st.text_input(label='Enter the category name')
            submit=st.form_submit_button("Insert")

    if(selected=="Customer"):
        with st.form(key="form2"):      
            cust_id=st.number_input('Enter the customer id')
            first_name= st.text_input('Enter the first name')
            last_name= st.text_input('Enter the last name')
            phone_number=st.text_input('Enter the Phone number(10 digits)')
            submit=st.form_submit_button("Insert")
    if(submit):
        if(selected=="Category"):
            str1=f"insert into category values ({categorId},'{catName}')"
        if(selected=="Customer"):
            str1=f"insert into customer values ({cust_id},'{first_name}','{last_name}','{phone_number}')"
        try:
            mycursor.execute(str1)
            st.info("Insertion successful!!")
            mydb.commit()
        except mysql.connector.Error as e:
            st.warning(e)

def quer(mycursor):
    with st.form(key="form1"):
        str1=st.text_area("Enter the query here:")
        submit=st.form_submit_button("Submit")
        if(submit):
            try:
                mycursor.execute(str1)
                df=pd.DataFrame(mycursor.fetchall())
                st.table(df)
            except mysql.connector.Error as e:
                st.warning(e)


def updat(mycursor,mydb):
    selected=option_menu(
        menu_title = "Choose the table",
        options = ["Job","Location"],      
        orientation="horizontal",
    )
    if(selected=="Job"):
        st.subheader("Update operation for Job table")
        mycursor.execute("Select * from job")
        st.write("Before updation")
        df=pd.DataFrame(mycursor.fetchall())
        st.table(df)
        with st.form("form1"):
            str2="SELECT EXISTS (SELECT 1 FROM job)"
            mycursor.execute(str2)
            if(mycursor.fetchone()['EXISTS (SELECT 1 FROM job)']):
                job_id=st.selectbox("Select the Job to be updated[JOB_IDs]",df['JOB_ID'])
                job_title=st.text_input("Select the Job Title to be updated")
                submit=st.form_submit_button("Update")
                if(submit):
                    str1=f"update job set job_title='{job_title}' where job_id={job_id}"
                    try:
                        mycursor.execute(str1)
                        mydb.commit()
                        st.info("Updation successful")
                        st.write("After updation")
                        mycursor.execute("Select * from job")
                        df=pd.DataFrame(mycursor.fetchall())
                        st.table(df)
                    except mysql.connector.Error as e:
                        st.warning(e)
                        st.experimental_rerun()
    if(selected=="Location"):
        st.subheader("Update operation for Location table")
        mycursor.execute("Select * from location")
        st.write("Before updation")
        df=pd.DataFrame(mycursor.fetchall())
        st.table(df)
        with st.form("form1"):
            str2="SELECT EXISTS (SELECT 1 FROM location)"
            mycursor.execute(str2)
            if(mycursor.fetchone()['EXISTS (SELECT 1 FROM location)']):
                location_id=st.selectbox("Select the location to be updated[LOCATION_IDs]",df['LOCATION_ID'])
                province=st.selectbox("Select the province to be updated",df['PROVINCE'])
                city= st.text_input('Enter the city name')
                submit=st.form_submit_button("Update")
                if(submit):
                    str1=f"update location set province='{province}',city='{city}' where location_id={location_id}"
                    try:
                        mycursor.execute(str1)
                        mydb.commit()
                        st.info("Updation successful")
                        st.write("After updation")
                        mycursor.execute("Select * from location")
                        df=pd.DataFrame(mycursor.fetchall())
                        st.table(df)
                    except mysql.connector.Error as e:
                        st.warning(e)
                        st.experimental_rerun()


def delet(mycursor,mydb):
    selected=option_menu(
        menu_title = "Choose the table",
        options = ["Category","Customer"],      
        orientation="horizontal",
    )
    if(selected=="Category"):
        st.subheader("Delete operation available for Category table")
        mycursor.execute("Select * from category")
        st.write("Before deletion")
        df=pd.DataFrame(mycursor.fetchall())
        st.table(df)
        with st.form("form1"):
            str2="SELECT EXISTS (SELECT 1 FROM category)"
            mycursor.execute(str2)
            if(mycursor.fetchone()['EXISTS (SELECT 1 FROM category)']):
                select=st.selectbox("Select the Category to be deleted (CAT_ID)",df['CATEGORY_ID'])
                submit=st.form_submit_button("Delete")
                if(submit):
                    try:
                        str1=f"delete from category where category_id= {select}"
                        mycursor.execute(str1)
                        mydb.commit()
                        st.info("Deletion successful")
                        st.write("After deletion")
                        mycursor.execute("Select * from category")
                        df=pd.DataFrame(mycursor.fetchall())
                        st.table(df)
                    except mysql.connector.Error as e:
                        st.warning(e)
                        st.experimental_rerun()
    if(selected=="Customer"):
        st.subheader("Delete operation available for Customer Table")
        mycursor.execute("Select * from customer")
        st.write("Before deletion")
        df=pd.DataFrame(mycursor.fetchall())
        st.table(df)
        with st.form("form2"):
            str2="SELECT EXISTS (SELECT 1 FROM customer)"
            mycursor.execute(str2)
            if(mycursor.fetchone()['EXISTS (SELECT 1 FROM customer)']):
                select=st.selectbox("Select the Customer Details to be deleted (CUST_ID)",df['CUST_ID'])
                submit=st.form_submit_button("Delete")
                if(submit):
                    try:
                        str1=f"delete from customer where cust_id= {select}"
                        mycursor.execute(str1)
                        mydb.commit()
                        st.info("Deletion successful")
                        st.write("After deletion")
                        mycursor.execute("Select * from customer")
                        df=pd.DataFrame(mycursor.fetchall())
                        st.table(df)
                    except mysql.connector.Error as e:
                        st.warning(e)
                        st.experimental_rerun()
                        
def read(mycursor):
    with st.form(key="form1"):
        mycursor.execute("show tables")
        df=pd.DataFrame(mycursor.fetchall())
        str1=st.selectbox('Select the table to view',df["Tables_in_spare_parts_project"])
        str2=f"select * from {str1}"
        submit=st.form_submit_button("Submit")
        if(submit):
            try:
                mycursor.execute(str2)
                df=pd.DataFrame(mycursor.fetchall())
                st.table(df)
            except mysql.connector.Error as e:
                st.warning(e)
        
        

