import streamlit as st
import openai
from dotenv import load_dotenv
import os
from diffusers import StableDiffusionPipeline
import torch

# Directly set the OpenAI API key
openai.api_key = "sk-proj-jDOgCCsml1RciJyB8ZIOT3BlbkFJwEF28q4w011xd1ujv1W5"

# Function to generate AI-based images using OpenAI DALL-E
def generate_images_using_openai(text):
    response = openai.Image.create(
        prompt=text,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

# Function to generate AI-based images using Huggingface Diffusers
def generate_images_using_huggingface_diffusers(text):
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    prompt = text
    image = pipe(prompt).images[0]
    return image

# Streamlit Code
choice = st.sidebar.selectbox("Select your choice", ["Home", "DALL-E", "Huggingface Diffusers"])

if choice == "Home":
    st.title("AI Image Generation App")
    with st.expander("About the App"):
        st.write("This is a simple image generation app that uses AI to generate images from text prompts.")

elif choice == "DALL-E":
    st.subheader("Image generation using OpenAI's DALL-E")
    input_prompt = st.text_input("Enter your text prompt")
    if input_prompt:
        if st.button("Generate Image"):
            image_url = generate_images_using_openai(input_prompt)
            st.image(image_url, caption="Generated by DALL-E")

elif choice == "Huggingface Diffusers":
    st.subheader("Image generation using Huggingface Diffusers")
    input_prompt = st.text_input("Enter your text prompt")
    if input_prompt:
        if st.button("Generate Image"):
            image_output = generate_images_using_huggingface_diffusers(input_prompt)
            st.info("Generating image.....")
            st.success("Image Generated Successfully")
            st.image(image_output, caption="Generated by Huggingface Diffusers")