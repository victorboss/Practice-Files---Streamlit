import streamlit as st
import pandas as pd

st.subheader("Uploading CSV files")
df = st.file_uploader("Upload the CSV file:: ",type = ['csv','xlsx'])

st.subheader('Loading the csv files')
df = pd.read_csv('Products.csv')

if df is not None:
    st.table(df.head())

st.subheader('Working with Images')
img_file = st.file_uploader("Upload the Image file:: ",type = ['png','jpeg'])

if img_file is not None:
    st.image(img_file)

st.subheader('Working with Audio')
audio_file = st.file_uploader("Upload the audio file:: ",type = ['wav','mp3'])
if audio_file is not None:
    st.audio(audio_file.read())

st.subheader('Working with Video')
video_file = st.file_uploader("Upload the video files:: ",type = ['mp4','mkv'])
if video_file is not None:
    st.video(video_file,start_time = 10)
