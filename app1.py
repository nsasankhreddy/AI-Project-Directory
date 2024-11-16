#!/usr/bin/env python
# coding: utf-8

# In[13]:


# get_ipython().system('pip install transformers')
# get_ipython().system('pip install streamlit')


# In[14]:


import streamlit as st
from transformers import pipeline

# Initialize the text generation pipeline with GPT-2
generator = pipeline("text-generation", model="gpt2")

st.title("Story Generator")
st.write("Generate a fun story based on your prompt!")

# Input for user prompt
user_prompt = st.text_input("Enter a starting sentence for the story:", "Once upon a time, there was a curious turtle named Timmy.")

# Generate and display story
if st.button("Generate Story"):
    result = generator(user_prompt, max_length=100, num_return_sequences=1)
    st.write("### Your Story:")
    st.write(result[0]["generated_text"])

