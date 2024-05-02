import streamlit as st
from twikit import Client
import pickle
import torch

conn = False

def make_connection():
    USERNAME = st.secrets['USERNAME']
    EMAIL = st.secrets['EMAIL']
    PASSWORD = st.secrets['PASSWORD']
    # Initialize client
    client = Client('en-US')

    # Login to the service with provided user credentials
    res = client.login(
        auth_info_1=USERNAME ,
        auth_info_2=EMAIL,
        password=PASSWORD
    )
    return res['status'] == 'success'


st.title("Sentiment Analysis")
def main():
    st.write("Sentiment analysis")

if __name__ == "__main__":
    if st.button("Proceed"):
        while not conn:
            conn = make_connection()
    main()