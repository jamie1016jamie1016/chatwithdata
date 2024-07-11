from pandasai.llm.openai import OpenAI
import streamlit as st

full_path = '/Users/jamie/Desktop/pandasai_image/'
myconfig = {
    "save_charts": True,
    "save_charts_path": full_path,
    "llm": OpenAI(api_token=st.secrets["openai"]["OPENAI_API_KEY"], model=st.secrets["openai"]["OPENAI_MODEL"])
}