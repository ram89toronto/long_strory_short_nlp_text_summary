# import libraries

from transformers import pipeline
import streamlit as st
from gtts import gTTS


#  Displaying the required information on site
st.write(' # Long Story Short -  A NLP based Text Summary for Day to Day Work')
st.write(''' Happy to build this "Long Story Short !!!" an NLP summarizing app for busy professionals, students, and entrepreneurs.

### Simplifies day-to-day tasks such as 
	"What was the meeting about ?" 
	"Can you summarize this lengthy email ?"
	"What is this article about ?"
	"Can tell shorten the executive summary ?"

### I think these are problems which take lot focus, energy and time, I built this app to solve this problem using NLP techniques. I think following are immediate benefits of using this app

1. Fast skimming of multiple emails, articles, information 
2. It saves time to skim not-so-important articles
3. Allows you to write shorter emails shorter 
4. Enables you to make informed decisions
5. Listen back and recollect the summary 

Lets do it in 3 Simple Steps !!!''')

# Creating the Profile  Summary on sidebar

st.sidebar.markdown("[![Ram Rallabandi](https://1.gravatar.com/avatar/10d166915c6715955ccdcf377a6544ba?s=400&d=mm)](https://ramrallabandi.link/)")
st.sidebar.markdown("## 👨 Ram Rallabandi - Data Science Professional")
column1, column2 , column3 =  st.sidebar.columns(3)
column1.markdown("[![,](https://img.icons8.com/color/48/null/wordpress.png)](https://ramrallabandi.link)")
column2.markdown("[![,](https://img.icons8.com/color/48/null/linkedin.png)](https://www.linkedin.com/in/ram-rallabandi/)")
column3.markdown("[![,](https://img.icons8.com/ios-filled/50/null/github.png)](https://github.com/ram89toronto)")

st.image("lsts.gif")
st.write("Image Credit: https://tinyurl.com/y6wdjsr7 ")

st.image("nlptextaudio.png")

st.write(" ## Step 1: Paste your text ")
data = st.text_area("Paste your text here...",value=" You can just delete this text and replace it with the text that you want to shorten", height=600)
st.snow()
# Apply transformers 
summarizer = pipeline("summarization")
#st.subheader("Min & Max of length for your Summary ...")

#slider_range =  st.slider(" Minimum and maximum words", value=[10,500])
#min_len = slider_range[0]
#max_len = slider_range[1]


# Display the text
st.write("## Step 2: Click to generate summary  ")
if st.button("Generate Summary"):
    summary =  summarizer(data, max_length=90, min_length=10, do_sample=False)
    output = summary[0]['summary_text']  
    aud = gTTS(text= output, lang = 'en', slow= False)
    aud.save("long_story_short.mp3") 	
    st.write(output)
    st.snow()
else:
    st.write("Waiting for input...")
# Play the audio 
st.write("## Step 3: Click and Connect to your headset and Listen to the Summary...")
if st.button("Listen to the Summary"):
    st.audio("long_story_short.mp3")
    st.snow()
else: 
    st.write("Happy Listening")

            
