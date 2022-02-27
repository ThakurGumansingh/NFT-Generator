import streamlit as st
import time
from generator import NFTGenerator
from pathlib import Path

st.set_page_config(
    page_title="NFT Generator",
    page_icon="chart_with_upwards_trend",
    layout="wide", #centered
)
st.title("NFT Generator")
st.markdown("To let you generate thousands of NFTs with few clicks..")

if 'generate' not in st.session_state:
    print('Lets generate')
    st.session_state.generate = False

with st.sidebar:
    input_dir = st.text_input('Input Folder')
    
   
    test = st.button('Test')
    st.session_state['test'] = True
    age = st.slider('How many NFTs do you want to generate?', 0, 5000, 1)
    with st.form(key="generate?"):
        amount = st.number_input('Amount', age)
        output_dir = st.text_input('Output Folder', 'Output')
        submit_button = st.form_submit_button(label='Generate')

if submit_button:
    p = Path(output_dir)
    p.mkdir(parents=True, exist_ok=True)
    the_bar = st.progress(0)
    with st.spinner('Wait, NFTs are getting generated...'):
        time.sleep(5)
    st.success("NFTs are generated")

    nft_generator = NFTGenerator(input_dir=input_dir)
    for i in range(amount):
        the_bar.progress((i + 1) / amount)
        nft_generator.generate(save_path=output_dir, file_name=i)
    st.subheader(f"Please check out the Output Folder \n{p.absolute()}")
    st.markdown("## Its Party time!")
    st.write("Yay! You've successfully generated " + str(amount) + " NFTs.")
    st.balloons()

if test:
    nft_generator = NFTGenerator(input_dir=input_dir)
    sample = nft_generator.generate()
    st.image(sample, caption="Sample NFT")

st.header("Creator")
st.markdown("> It is created by Thakur Gumansingh")

st.header("Some Famous NFT Collections")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("CrytoPunks")
    st.image("https://www.larvalabs.com/cryptopunks/cryptopunk3100.png")
with col2:
    st.subheader("CryptoKitties")
    st.image("https://helios-i.mashable.com/imagery/articles/07ucJyzszHZJ2HYS08KC1Gm/hero-image.fill.size_1200x1200.v1623367744.png")
with col3:
    st.subheader("BoredApes")
    st.image("https://news.artnet.com/app/news-upload/2021/08/Yuga-Labs-Bored-Ape-Yacht-Club-7940.jpg")
