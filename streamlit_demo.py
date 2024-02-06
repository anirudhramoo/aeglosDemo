import streamlit as st
import requests

# Title of the app
st.title('Aeglos API Demo')

# Input text box
user_input = st.text_input("Enter your input")

# Button to make the API call
if st.button('Call API'):
   
    url = "https://api.aeglos.ai/api/v1"
    headers = {
        "x-api-key": "fvs0kViMdL4I2J0ocvs8Sa010QzoA6eN4Q1FKj4R",
        "Content-Type": "application/json"
    }
    
    
    payload={"inputs": user_input}
    response = requests.post(url, headers=headers, json=payload)
    

    if response.status_code == 200:
       
        data = response.json()
        st.write(data[0])
    else:
        st.write("Failed to retrieve data, status code:", response.status_code)
