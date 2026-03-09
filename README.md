🚦 Traffic Sign Recognition
---
🧠 Deep Learning | Computer vision (CNN) | MobileNet
---
⚡ Industry Level + Bonus Completed ✅

https://elevvoml-gtsrb-cnn-model.streamlit.app/

 ---

 🎯 Task Description
---

The main objective of this project is to build a deep learning model that can classify traffic signs based on image inputs.

The workflow includes:
- Preprocess traffic sign images (resizing and normalization)
- Apply data augmentation to improve model generalization
- Train a custom CNN model
- Train a transfer learning model (MobileNetV2)
- Evaluate models using accuracy, classification report, and confusion matrix
- Compare model performance
- Deploy the trained model using Streamlit for real-time predictions

---

📊 Dataset Information
---

Dataset used in this project:

German Traffic Sign Recognition Benchmark (GTSRB)

Dataset characteristics:
- 43 traffic sign classes
- More than 50,000 images
- Images captured under various conditions:
  
      - lighting variations
      - different viewing angles
      - motion blur
      - partial occlusions

Each image contains a cropped traffic sign belonging to one of the predefined classes.

Typical traffic sign categories include:

     - Speed limit signs
     - Stop signs
     - Priority road signs
     - Warning signs
     - Prohibition signs
     
This dataset is widely used as a benchmark for traffic sign recognition systems.


<img width="1988" height="490" alt="image" src="https://github.com/user-attachments/assets/f1ad4f3b-31cc-472e-ab9c-6f77616429d7" />
<img width="695" height="547" alt="image" src="https://github.com/user-attachments/assets/b65d3df3-1073-445c-95b6-d30a5091b85e" />

 ---

🧰 Tools & Technologies
---

This project uses the following tools and frameworks:

| Category	| Tool|
|-----------|-----|
| Programming Language	| Python|
| Deep Learning Framework	| TensorFlow / Keras|
| Data Processing	| NumPy, Pandas| 
| Image Processing	| OpenCV|
| Visualization	| Matplotlib, Seaborn|
| Model Evaluation	| Scikit-learn|
| Deployment	| Streamlit|

 ---

🔬 Project Workflow
---

The project follows a standard Machine Learning pipeline:

1️⃣ Data Loading
---

- Load traffic sign images from the dataset
- Extract labels for each class

2️⃣ Data Preprocessing
---

- Resize images to a fixed resolution (64 × 64)
- Normalize pixel values
- Split dataset into:
    
      - Training set
      - Validation set
      -  Test set

3️⃣ Data Augmentation
---

To improve generalization and reduce overfitting:

- Random rotation
- Random zoom
- Random horizontal shifts
- Random brightness changes

4️⃣ Model Development
---

Two models are trained and compared:

**Custom CNN**

A convolutional neural network built from scratch using layers such as:
- Convolution layers
- MaxPooling layers
- Dropout layers
- Dense layers

**Transfer Learning (MobileNetV2)**

A pre-trained MobileNetV2 architecture is used with transfer learning to leverage features learned from large image datasets.

5️⃣ Model Training
---

Models are trained using:
- Adam optimizer
- Early stopping
- Learning rate reduction

6️⃣ Model Evaluation
---

Performance is evaluated using:

- Accuracy
- Classification report
- Confusion matrix

7️⃣ Model Results
---

After evaluating both models, the following results were obtained:

| Model	| Test Loss	| Test Accuracy|
|-------|-----------|--------------|
| Custom CNN	| 0.0295	| 99.37%|
| MobileNetV2	| 1.5475	| 56.09%|

The custom CNN model significantly outperformed MobileNetV2, achieving very high accuracy on the test dataset. This suggests that a well-designed architecture trained directly on the dataset can sometimes perform better than transfer learning for specialized image classification tasks.

<img width="536" height="374" alt="image" src="https://github.com/user-attachments/assets/3ccfe9a9-a233-4467-ad36-50c88fd742e4" />

8️⃣ Model Deployment
---

The best-performing model is deployed using Streamlit to create a simple web interface where users can upload a traffic sign image and receive a prediction.
 
 ---
 
📈 Model Performance
---

Evaluation metrics used:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Comparing CNN vs MobileNetV2 helps determine whether a lightweight transfer learning model performs better than a custom architecture.

<img width="846" height="547" alt="image" src="https://github.com/user-attachments/assets/e6374c50-31be-4a6f-8897-b3e2364132fa" />

 ---
 
💼 Business Insight
---

Traffic sign classification systems have real-world applications in:


🚗 Autonomous Vehicles

Self-driving cars must accurately detect and interpret traffic signs to ensure safe navigation.


🚦 Driver Assistance Systems (ADAS)

Advanced Driver Assistance Systems rely on traffic sign recognition to alert drivers about:

- Speed limits
- Stop signs
- Road warnings


🛣 Smart Transportation Infrastructure

Automated monitoring systems can analyze traffic signs to ensure proper placement and detect damaged or missing signs.

A reliable traffic sign recognition system helps improve road safety, automation, and intelligent transportation systems.

 ---
 
🧠 Concepts Covered
---

This project demonstrates several key machine learning and deep learning concepts:

- Computer Vision
- Image Classification
- Convolutional Neural Networks (CNN)
- Transfer Learning
- Data Augmentation
- Model Evaluation
- Hyperparameter tuning
- Deep Learning Deployment with Streamlit

 ---
 
🚀 Future Improvements
---

Possible improvements for this project include:

- Hyperparameter optimization
- Using more advanced architectures (EfficientNet, ResNet)
- Model quantization for edge deployment
- Real-time video traffic sign detection
- Integration with autonomous driving systems

 ---

 👨‍💻 Author
---

Deep Learning Project — Traffic Sign Classification
Built using TensorFlow, CNN, and Transfer Learning.




