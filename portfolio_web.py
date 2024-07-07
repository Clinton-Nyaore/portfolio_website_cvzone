import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave: Welcome to my portfolio!")
    st.title('I am Clinton Nyaore')

with col2:
    st.image("./images/clin.jpg")

st.title(" ")
st.title("Clinton's AI Bot")

persona = """
        You are Clinton AI bot. You help people answer questions about your self (i.e Clinton)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Clinton: 
         
        Clinton Nyaore is an Educator/Programmer/Entrepreneur in the field of Computer Vision and AI.
        He works in the field of Computer Vision, AI, and Deep Learning. Clinton obtained his Bachelor’s degree in
        Computer Science from Laikipia University, Kenya. 
        Clinton's Email: cnyaore@gmail.com """

user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona + "Here is the question that the user asked: " +  user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.write(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 70)
st.slider("Machine Learning", 0, 100, 90)
st.slider("Data Science", 0, 100, 85)

st.title(" ")
col1, col2 = st.columns(2)

with col1:
    st.subheader("About Me")
    st.write("- I am a machine learning engineer with a passion for AI and ML")
    st.write("- I have a background in computer science and statistics")
    st.write("- I am a certified machine learning engineer with 2 years experience")


with col2:
    st.subheader("Contact Me")
    st.write("Email: cnyaore@gmail.com")
    st.write("Phone: +254 745 504 421")
