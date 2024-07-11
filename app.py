import my_key
import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
from pandasai import SmartDataframe
from pandasai.responses.response_parser import ResponseParser
import some_stuff

matplotlib.use('Agg')

full_path = some_stuff.full_path
config = some_stuff.myconfig

if not os.path.exists(full_path):
    os.makedirs(full_path)

class StreamlitResponse(ResponseParser):
    def __init__(self, context) -> None:
        super().__init__(context)

    def parse_response(self, result):
        if isinstance(result, pd.DataFrame):
            self.format_dataframe(result)
        elif isinstance(result, str):
            self.format_string(result)
        elif isinstance(result, (int, float)):
            self.format_number(result)

    def format_dataframe(self, result):
        st.dataframe(result)

    def format_string(self, result):
        if result.endswith('.png'):
            st.image(result)
        else:
            st.write(f"<div style='font-size: 20px;'>{result}</div>", unsafe_allow_html=True)

    def format_number(self, result):
        st.write(f"<div style='font-size: 20px;'>{result}</div>", unsafe_allow_html=True)





st.title("🐼 Show me your DATA!!!")
st.write("With just a few clicks, a chatbot could totally do your job. No pressure!")

with st.sidebar:
    st.write("*About to lose your job*")
    st.caption('''**Use with caution!!!**''')
    st.caption('''**Do not overly rely on chatbot!!!**''')
    st.divider()
    st.caption("Made by Jamie")

uploaded_file = st.file_uploader("Click to uplaod CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    with st.expander("🔍 Take a peek"):
          st.write(df.head(5))

    sdf = SmartDataframe(df, config=config)
   

    def overview_data():
        st.markdown("<div style='font-size: 20px;'>Data Overview:</div>", unsafe_allow_html=True)  

        missing_data = sdf.chat("how many missing values are there and in which column? return in a sentence.")
        st.write(missing_data)

        duplicates = sdf.chat("how many duplicates are there?return in a sentence.")
        st.write(duplicates)

        question = 'what is this data mainly about?'
        st.write("<div style='font-size: 20px;'>About the data:</div>", unsafe_allow_html=True)

        result = sdf.chat(question)
        st.write(f"{result}")
    
    with st.spinner('Analyzing data...'):
        overview_data()

    st.divider()

    st.write("<div style='font-size: 20px;'>Ask me anything about the data:</div>", unsafe_allow_html=True)
    
    with st.spinner('Generating sample questions...'):
        promt_question = "Provide a special question sentence about the data"
        default_question = sdf.chat(promt_question)

    user_input = st.text_area(label="", value=default_question)

    if st.button("Submit"):
        with st.spinner('Let me think...'):
            if user_input:
                input_result = sdf.chat(user_input)
                st.write("## Answer")
                response_parser = StreamlitResponse(context=None)
                response_parser.parse_response(input_result)