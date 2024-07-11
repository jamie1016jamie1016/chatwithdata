from pandasai.llm.openai import OpenAI
import my_key

full_path = '/Users/jamie/Desktop/pandasai_image/'
myconfig = {
    "save_charts": True,
    "save_charts_path": full_path,
    "llm": OpenAI(api_token=my_key.OPENAI_API_KEY, model=my_key.OPENAI_MODEL)
}