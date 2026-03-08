import streamlit as st
import numpy as np
import pandas as pd
import cv2
from PIL import Image
import os
import time
import plotly.graph_objects as go

from utils.predict import load_model, preprocess_image, predict_image
from class_names import class_names


# PAGE CONFIG
st.set_page_config(
    page_title="Traffic Sign Classifier",
    page_icon="🚦",
    layout="wide"
)

# LOAD CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# LOAD MODEL
model = load_model("Models/CNN.h5")

# TITLE
st.markdown('<h1 class="title">🚦 Traffic Sign Classifier</h1>', unsafe_allow_html=True)

st.markdown("""
<p class="subtitle">
AI-powered Traffic Sign Recognition using Deep Learning (CNN) trained on the 
<b>German Traffic Sign Recognition Benchmark (GTSRB)</b> dataset.
</p>
""", unsafe_allow_html=True)

# APP DESCRIPTION
st.markdown("""
<div class="info-box">
<div class="class-text">

### 📌 About This Application
This application demonstrates a **Deep Learning-based Traffic Sign Recognition system** powered by a **Convolutional Neural Network (CNN)** trained on the **German Traffic Sign Recognition Benchmark (GTSRB)** dataset.
The system is designed to automatically identify and classify traffic signs from uploaded images.

### 🚗 Why Traffic Sign Recognition?
Traffic sign detection is an essential component of:
• Autonomous driving systems  
• Intelligent transportation systems  
• Driver assistance technologies  
By recognizing traffic signs in real-time, AI systems can help improve **road safety and navigation decisions**.

### ⚙️ How It Works
1️⃣ Upload an image containing a traffic sign  
2️⃣ The CNN model extracts visual features from the image  
3️⃣ The system predicts the most probable traffic sign class  
4️⃣ The predicted class and confidence score are displayed

</div>            
</div>
""", unsafe_allow_html=True)

# UPLOAD IMAGE
st.markdown('## 📤 Upload Traffic Sign Image')

uploaded_file = st.file_uploader(
    "Upload an image of a traffic sign to analyze",
    type=["png","jpg","jpeg"]
)

confidence_percent = 0

if uploaded_file is not None:
    
    uploaded_file.seek(0)
    col1, col2 = st.columns([1,1], gap="large")
    image = preprocess_image(uploaded_file)
    class_id, confidence, preds = predict_image(model, image)
    label = class_names[class_id]
    confidence_percent = confidence * 100

    # IMAGE COLUMN
    with col1:

        st.markdown(
            """
            <div class="kpi-card">
            <div class="kpi-title">🚦 Uploaded Traffic Sign</div>
            """,
            unsafe_allow_html=True
        )

        left, center, right = st.columns([1,2,1])

        with center:
            st.image(uploaded_file, width=250)

        st.markdown("</div>", unsafe_allow_html=True)


    # RESULT COLUMN
    with col2:

        st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-title">
            ⚡ AI Prediction Result
            </div>
        """,
        unsafe_allow_html=True
        )       

        icon_path = f"Meta/{class_id}.png"

        if os.path.exists(icon_path):

            left, center, right = st.columns([1,2,1])
            
            with center:
                st.image(icon_path, width=250)

        st.markdown(f'<div class="prediction-result">{label}</div>', unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()


# ANALYSIS SECTION
st.markdown("## 📊 AI Prediction Analysis")
col1, col2 = st.columns([1,1], gap="large")

# GAUGE CHART
with col1:

    gauge_placeholder = st.empty()

    for i in range(0, int(confidence_percent)+1, 2):

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=i,
            number={'suffix': "%"},
            title={'text': "Prediction Confidence"},
            gauge={
                'axis': {'range': [0,100]},
                'bar': {'color': "#00c4d6"},
                'borderwidth': 2,
                'bordercolor': "#00c4d6",
                'bgcolor': "rgba(0,0,0,0)",
                'steps': [
                    {'range': [0,50], 'color': "rgba(0,40,50,0.7)"},
                    {'range': [50,80], 'color': "rgba(0,70,80,0.7)"},
                    {'range': [80,100], 'color': "rgba(0,110,120,0.9)"}
                ]
            }
        ))

        fig_gauge.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font={'color': "#00c4d6", 'size': 18},
            height=350
        )

        gauge_placeholder.plotly_chart(fig_gauge, use_container_width=True)

        time.sleep(0.01)


# RADAR CHART
with col2:

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=[confidence_percent,
           confidence_percent*0.9,
           confidence_percent*0.95,
           confidence_percent*0.85],

        theta=["Prediction", "Confidence", "Accuracy", "Reliability"],

        fill='toself',
        fillcolor='rgba(0,200,220,0.35)',
        line=dict(color='#00c4d6', width=3)
    ))

    fig_radar.update_layout(

        polar=dict(
            bgcolor="rgba(0,0,0,0)",

            radialaxis=dict(
                visible=True,
                range=[0,100],
                gridcolor="rgba(0,200,220,0.2)",
                tickfont=dict(color="#00c4d6")
            ),

            angularaxis=dict(
                gridcolor="rgba(0,200,220,0.2)",
                tickfont=dict(color="#00c4d6")
            )
        ),

        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#00c4d6"),
        height=350
    )

    st.plotly_chart(fig_radar, use_container_width=True)

# FOOTER
st.markdown("""
<div class="footer">

Developed by <b>Atikah Dwi Rizky</b>  
Deep Learning Project • Traffic Sign Recognition • CNN Model

</div>

""", unsafe_allow_html=True)

