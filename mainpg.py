import mysql.connector
import streamlit as st
from crud import *
from streamlit_option_menu import option_menu



def main(mycursor,mydb):
    if(st.session_state['loggedIn']):
        st.title("Auto Spare Management System")
        # selected=option_menu(
        #         menu_title = None,
        #         options = ["Insert","Update","Delete","Query"],
        #         orientation="horizontal",
        #     )
        selected=st.sidebar.selectbox("Menu",["Insert","Update","Delete","Query","Read"])

        if selected=="Insert":
            st.subheader("Insert a record")
            insrt(mycursor,mydb)

        if selected=="Update":
            st.subheader("Update")
            updat(mycursor,mydb)

        if selected=="Delete":
            st.subheader("Delete")
            delet(mycursor,mydb)

        if selected=="Query":
            st.subheader("Query")
            quer(mycursor)
        
        if selected=="Read":
            st.subheader("Read")
            read(mycursor)
    else:
        st.error("Invalid Username/Password")
     

