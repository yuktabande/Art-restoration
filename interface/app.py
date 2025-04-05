import streamlit as st
from PIL import Image
from model import restore_art
import io

# Page config
st.set_page_config(page_title="🖼️ Art Restoration Studio", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM CSS THEME (ADD YOUR COLORS BELOW) ---
st.markdown("""
    <style>
    /* 🔵 PAGE BACKGROUND */
    body, .main {
        background-color: #483248;
        color: 	#CBC3E3;
    }

    /* 🟣 HEADINGS */
    h1, h2, h3 {
        color: #CF9FFF ;
    }

    /* 🔘 PRIMARY BUTTONS */
    .stButton>button {
        background-color: 	#E6E6FA;
        color: 	#5D3FD3;
        border-radius: 10px;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #E6E6FA;
    }

    /* 🟢 DOWNLOAD BUTTON */
    .stDownloadButton>button {
        background-color: #E6E6FA;
        color: #5D3FD3;
        font-weight: bold;
        border-radius: 10px;
    }
    .stDownloadButton>button:hover {
        background-color: #E6E6FA;
    }

    /* Optional: Customize File Uploader Label */
    .stFileUploader label {
        color: #CCCCFF;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("🖼️ Art Restoration Studio")
st.markdown("#### Revive the beauty of historic art with one click!")

st.markdown("""
Upload a **distorted or damaged image** of an artwork, and let our AI model **restore it to its original state**.
Perfect for artists, curators, and restoration enthusiasts ✨
""")

# --- Upload Image ---
uploaded_file = st.file_uploader("📤 Upload your distorted artwork", type=["jpg", "jpeg", "png"])

if uploaded_file:
    original_img = Image.open(uploaded_file)

    # Columns layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔻 Distorted Input")
        st.image(original_img, caption="Uploaded Image", use_column_width=True)

    with col2:
        st.subheader("🎨 Restored Output")
        with st.spinner("Restoring the artwork..."):
            restored_img = restore_art(original_img)
        st.image(restored_img, caption="Restored Image", use_column_width=True)

        # Download button
        img_bytes = io.BytesIO()
        restored_img.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        st.download_button(
            label="📥 Download Restored Image",
            data=img_bytes,
            file_name="restored_image.png",
            mime="image/png"
        )
else:
    st.info("Upload a distorted image above to get started ✨")
