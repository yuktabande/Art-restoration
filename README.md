# 🖼️ Art Restoration System
A deep learning-based application that restores distorted or damaged paintings, bringing them back to their original form using image inpainting techniques.

## ✨ Features
- Restores scratches, cracks, and missing parts in old or damaged artworks
- Supports high-resolution image input
- Uses CNN-based image inpainting models (e.g., Partial Convolutions or U-Net)
- Option to preview side-by-side comparison of original vs. restored image
- Simple UI for uploading and restoring artwork

## 📁 Project Structure
perl
Copy code
art-restoration-system/
├── model/
│   └── art_restorer.h5          # Pre-trained inpainting model
├── static/
│   └── sample_inputs/           # Example distorted paintings
├── app.py                       # Flask or Streamlit web app
├── requirements.txt             # Project dependencies
├── utils.py                     # Image preprocessing and postprocessing
└── README.md

## 🚀 Getting Started
1. Clone the repository
```
git clone https://github.com/yuktabande/Art-restoration.git
cd Art-restoration
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run the app
```
python app.py
```
Or if using Streamlit:
```
streamlit run app.py
```
4. Try It Out
Upload a distorted painting image.

Wait for the model to process and restore it.

View/download the restored version.

## 🧠 Model Details
The restoration model is trained on datasets of paintings with artificially applied distortions, using supervised learning to predict the undistorted output. You can swap in different models like:

Partial Convolutional Inpainting

DeepFill v2

U-Net + GAN combination

## 🖼️ Sample Results
Distorted Input	Restored Output

## 📦 Dependencies
- TensorFlow / PyTorch
- OpenCV
- NumPy
- Flask or Streamlit
- PIL

(See requirements.txt for full list)

## 🛠️ Future Improvements
Train on more diverse datasets (Baroque, Impressionist, etc.)
Add brush tool for manual mask editing
Batch restoration support

👩‍🎨 Made With Love For Art
By  Yukta Bande— preserving the past with the power of AI.
