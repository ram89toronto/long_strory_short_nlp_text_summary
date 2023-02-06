# import libraries

from transformers import pipeline
import streamlit as st
from gtts import gTTS

# Setting page Configuration

st.set_page_config(page_title = "Cool looking Maps using Data",
    page_icon = "📑 📟 🎧 ",
    layout = "wide",
    initial_sidebar_state = "expanded",
    menu_items = { 'About': '# Load Text -> Read & Listen to Summary ',
        'Get Help' : 'https://ramrallabandi.link',
        'Report a bug': 'https://ramrallabandi.link/contact/'
        } )


#  Displaying the required information on site
st.write(' # Long Story Short Generator - An NLP Project')
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
data = st.text_area("Paste your text here...",value="Just replace this text with yours that is waiting to condense", height=600)

# Apply transformers 
summarizer = pipeline("summarization")
st.subheader("Min & Max of length for your Summary ...")

slider_range =  st.slider(" Minimum and maximum words", 0, 500,(35,95))
min_len = slider_range[0]
max_len = slider_range[1]

st.write("Loading step 2 in a min....")

summary =  summarizer(data, max_length=max_len, min_length=min_len)
output = summary[0]['summary_text'] 
aud = gTTS(text= output, lang = 'en', slow= False)
aud.save("long_story_short.mp3")

# Display the text
st.write("## Step 2: Click to generate summary  ")
if st.button("Generate Summary"):
    st.write(output)
    
else:
    st.write("Waiting for input...")
# Play the audio 
st.write("## Step 3: Click and Connect to your headset and Listen to the Summary...")
if st.button("Listen to the Summary"):
    st.audio("long_story_short.mp3")
    
else: 
    st.write("Happy Listening")

            
