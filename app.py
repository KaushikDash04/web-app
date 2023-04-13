import streamlit as st
from PIL import Image
import cv2
from streamlit_lottie import st_lottie
import requests



st.set_page_config(page_title="My Page", page_icon=":no_smoking::underage:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD LOCAL CSS ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_ZsoSL7RsIe.json")



# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Kaushik :snowflake:")
    st.title("About Me")
    st.write("I am a beginner in python.")
    st.write("[Hear My Favourite Song >](https://youtu.be/1j2YXCvTtTs)")


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
                I am from Cuttack. I have completed my matriculation and Intermediate from DAV Public School, CDA, Cuttack. 
                Currently am pursuing my Bachelors of Technology degree from Veer Surendra Sai University of Technology, Burla 
                (formerly known as University College of Engineering) in the Department of Computer Science & Engineering.
                """
        )
        st.write("[My Favourite Video >](https://youtu.be/jG7dSXcfVqE)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="cat")


# ---- sidebar ----
menu = ["Image", "Video"]
choice = st.sidebar.selectbox("Select an option", menu)

if choice == "Image":
    #make new page
    st.write("---")
    st.subheader("Image")
    file_option = st.radio("Select an option", ["Select local file", "Capture from camera"])
    st.subheader("Text Input")
    st.write("Please enter the caption first")
    text_input = st.text_input("Enter your caption")

    #new container
    with st.container():
        image_column, right_column = st.columns((1,2))
        if file_option == "Select local file":
            with st.expander("Click here to collapse", expanded=True):
                image_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
                if image_file is not None and text_input != "": 
                        with image_column:
                            image = Image.open(image_file)
                            st.image(image, caption = text_input, use_column_width=True)
                            st.snow()

        elif file_option == "Capture from camera":
            if text_input != "":
                picture = st.camera_input("Take a picture")
                if picture is not None:
                    st.markdown(f"<center>{text_input}</center>", unsafe_allow_html=True)

            
elif choice == "Video":
    #make new page
    st.write("---")
    st.subheader("Video")
    file_option = st.radio("Select an option", ["Select local file", "Capture from camera"])
    st.subheader("Text Input")
    st.write("Please enter the caption first")
    

    #new container
    with st.container():
        image_column, right_column = st.columns((1,2))
        if file_option == "Select local file":
            text_input = st.text_input("Enter your caption")
            with st.expander("Click here to collapse", expanded=True):
                video_file = st.file_uploader("Upload a video", type=["mp4", "mov"])
                if video_file is not None and text_input != "":
                        with image_column:
                            st.video(video_file, start_time=0)
                            st.markdown(f"<center>{text_input}</center>", unsafe_allow_html=True)
                            st.snow()

                
        elif file_option == "Capture from camera":
            st.subheader(':blue[_This feature is coming soon._:sunglasses:]')