import streamlit as st
import pathlib
import textwrap


from IPython.display import display
from IPython.display import Markdown
#from altair.vegalite.v4.api import Chart

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

import os
os.environ['GEMINI_API_KEY']='your_api_key_here'


import google.generativeai as genai
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Insights Assistant ", page_icon=":robot_face:", layout="centered")

st.markdown(
    """
    <style>
    /* Include your custom CSS styles here */
    body {
        background-color: #1a1a1a; /* Dark background color */
        color: #ffffff; /* Light text color */
        font-family: Arial, sans-serif; /* Optional: Choose a suitable font */
    }

    .stTextInput, .stTextArea, .stSelectbox, .stMultiSelect, .stNumberInput {
        background-color: #333333; /* Darker input fields */
        color: #ffffff; /* Light text color */
    }

   
    .stButton > button {
            background-color: #4CAF50;
            color: white;
        }

    .stMarkdown {
        color: #ffffff; /* Light text color for Markdown components */
    }

    /* Customize other Streamlit components as needed */

    </style>
    """,
    unsafe_allow_html=True
)


st.header("Data Buddy Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Click me to get response")

## If ask button is clicked

if submit:
    
   if input.strip() == "":
        st.warning("Please enter a question.")
   else:
        try:
            response = get_gemini_response(input)
            st.subheader("The Response is")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
