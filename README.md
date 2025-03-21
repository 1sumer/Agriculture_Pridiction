# 🌱 Crop and Fertilizer Recommendation System  

This is a **Flask-based web application** that predicts the best **crop** to grow and the **fertilizer** to use based on soil and environmental conditions.

---

## 📌 Features  
- ✅ **Crop Recommendation** based on **NPK, temperature, humidity, pH, and rainfall**.  
- ✅ **Fertilizer Recommendation** based on **soil type, crop type, and environmental factors**.  
- ✅ User-friendly **web interface** with **HTML & CSS**.  
- ✅ **Machine Learning Models** trained using **Random Forest Classifier**.  
- ✅ **Flask API** for predictions.  

---

## ⚙️ Tech Stack  
- **Backend**: Flask, Scikit-learn, Pandas, NumPy  
- **Frontend**: HTML, CSS  
- **ML Model**: Random Forest Classifier  
- **Deployment**: Render Cloud (Can be hosted on **Heroku, AWS, or any Flask-compatible server**)  

---

## 📂 Project Structure  
```plaintext
📁 Crop-Fertilizer-Prediction  
│── 📁 assets/Data/               # Datasets (CSV files)  
│── 📁 models/                    # Saved ML Models (crop_model.pkl, fertilizer_model.pkl, etc.)  
│── 📁 static/                    # CSS and images  
│── 📁 templates/                 # HTML Files  
│   │── index.html                # Homepage  
│   │── crop.html                 # Crop Recommendation Form  
│   │── fertilizer.html            # Fertilizer Recommendation Form  
│   │── result.html                # Prediction Result Page  
│── app.py                         # Flask Backend  
│── requirements.txt                # Required Dependencies  
│── README.md                       # Project Documentation  
```
---

##  🚀 Installation & Usage 
- **🔹 Step 1: Clone the Repository**: 
```
git clone https://github.com/your-repo/crop-fertilizer-prediction.git
cd Crop-Fertilizer-Prediction
``` 
- **🔹 Step 2: Install Dependencies**:

`pip install -r requirements.txt`

- **Step 3: Run Flask Application**:
  
`python app.py`

- **Step 4: Access the Web UI**: 
    - Open http://127.0.0.1:5000/ in a browser.
    - Select Crop Recommendation or Fertilizer Prediction.
    - Enter values and get predictions instantly! 🎯

---

## 🌍 Deployment on Render Cloud

The project is live on Render Cloud. Check it out:

- 🔗 **Live App**: https://agriculture-pridiction.onrender.com/
- 📂 **GitHub Repo**: https://github.com/1sumer/Agriculture_Pridiction

---

## 📜 License  
- This project is open-source and available under the MIT License.

---

## 💡 Future Enhancements 
- 🔹 Add real-time weather API for better predictions.
- 🔹 Implement Deep Learning models for improved accuracy.
- 🔹 Develop a mobile app version for Android/iOS.
- 🔹 Deploy on AWS SageMaker for scalable AI solutions.

---

⭐ If you found this project helpful, don't forget to star the repo! ⭐
