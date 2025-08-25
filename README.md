# 🩺 Kidney Disease Predictior

A **Machine Learning** based web application that analyzes medical parameters to predict **Chronic Kidney Disease (CKD)**.  It combines a **Random Forest model** with a **Flask-powered web interface** for real-time predictions.  

---

## 🚀 Features  
-  Predicts the likelihood of Chronic Kidney Disease (CKD).  
-  Uses **Random Forest Classifier** for reliable predictions.  
-  Flask-based backend for handling model inference.  
-  Simple and interactive web interface for input and results.  

---

## 🛠️ Tech Stack  

### 🔙 Backend (Python)  
- **Flask** → Lightweight web framework to handle requests and serve pages.  
- **Scikit-learn** → For training the Random Forest Classifier model.  
- **Pandas** → For data cleaning and preparation of the CSV dataset.  
- **Joblib** → For saving and loading the trained ML model without retraining.  

### 🌐 Frontend (Web)  
- **HTML** → Structures the web page with input forms and result display.  
- **CSS** → Styles the interface with modern effects .  
- **JavaScript** → Handles interaction, sends input data to Flask, and updates the result dynamically.  

---

## 📊 Dataset  
- Based on patient medical records (`Kidney_disease_data.csv`).  
- Features include blood pressure, blood glucose, hemoglobin, etc.  
- Target: Presence or absence of **Chronic Kidney Disease**.  

---

## ⚙️ How to Run  

1. **Train the Model**  
   Run the training script to generate the `model.pkl` file:  
   ```bash
   python train_model.py
   ```
2. **Start the Flask App**
   After the model is created, run the Flask application:
   ```bash
   python app.py
   ```
3. **Open in Browser Go to** :
http://127.0.0.1:5000
Enter patient details and get the CKD prediction.

---

## 📜 License  
This project is licensed under the **MIT License**.  
