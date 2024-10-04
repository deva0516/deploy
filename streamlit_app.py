import streamlit as st
import mysql.connector

# Create a connection to the database
cnx = mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    database='node_crud'
)

# Create a cursor object to execute queries
cursor = cnx.cursor()

# Create a Streamlit app
st.title("Node CRUD App")

# Create input fields for ID, name, and email
id_input = st.text_input("Enter ID:")
name_input = st.text_input("Enter Name:")
email_input = st.text_input("Enter Email:")

# Create a button to read data from database
read_button = st.button("Read Data")

# Create a button to store data in database
store_button = st.button("Store Data")

# Read data from database when button is clicked
if read_button:
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (id_input,))
    result = cursor.fetchone()
    if result:
        st.write("User  found:")
        st.write(f"ID: {result[0]}")
        st.write(f"Name: {result[1]}")
        st.write(f"Email: {result[2]}")
    else:
        st.write("User  not found")

# Store data in database when button is clicked
if store_button:
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(query, (name_input, email_input))
    cnx.commit()
    st.write("Data stored successfully")

# Close the cursor and connection
cursor.close()
cnx.close()
