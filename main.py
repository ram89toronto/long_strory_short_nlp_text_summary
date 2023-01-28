# import libraries

from transformers import pipeline
import streamlit as st
from gtts import gTTS


#  Displaying the required information on site
st.sidebar.markdown("[![Ram Rallabandi]('https://pybank.files.wordpress.com/2022/11/profile-2170006031-e1669772800488.png?w=343')]('https://ramrallabandi.link/')")
st.write(' # Long Story Short -  A NLP based text summary application')
st.write('  Assuming your text is in English, this app helps you solve the common problems in day to day business, students, and enterprenuers life. \
            We here these prompts every other day \
                - Long Story Short \
                - Come to the point \
                - What is the meeting summary ? \
                - What have you learned today ? \
                - What was the new movie about ? \
            and in many more context, we here that very often. \
             So, I build a basic app, that can help you assit not only summarizing but also listen the summary ')

st.image("https://tenor.com/en-CA/view/long-story-short-ed-punk-duck-please-stop-talking-final-result-gif-17187495", width=400)
data = st.text_area("Paste your text here...")




st.subheader("Minimum and maximum word length of the summary")

slider_range =  st.slider(" Minimum and maximum words", value[10,500])
min_len = slider_range[0]
max_len = slider_range[1]
#summarizer = pipeline("summarization")
#summary =  summarizer(data, max_length=max_len, min_length=min_len)

#st.write(summary[0]['summary_text'])

st.snow()
            