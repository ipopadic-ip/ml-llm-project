# 🔒 Password Strength & Breach Checker – Full Stack Project

This is a **full stack application** that combines:

- **React frontend** for user interaction
- **Flask API backend** for ML prediction, breach checking, and AI advice
- **Machine Learning (scikit-learn)** for password strength prediction
- **HaveIBeenPwned (HIBP)** for breach checks
- **AI LLM (OpenRouter)** for generating actionable password improvement advice

---

## 📺 Watch Demo Video

[![Watch the demo video](https://img.youtube.com/vi/--2VfEpgXP4/0.jpg)](https://youtu.be/--2VfEpgXP4?si=l0fK2u9iiQSHUVTU)

▶️ **Click the image above to watch the demo video on YouTube.**

 ---

## 🚀 Features

- ✅ **Checks** if a password has been breached using [HaveIBeenPwned](https://haveibeenpwned.com/)
- ✅ **Predicts** password strength using a trained ML model
- ✅ **Generates** AI advice to strengthen passwords
- ✅ Built as a **full stack project** with React frontend and Flask backend

---

## 🛠️ Tech Stack

### 🔧 Backend

- **Flask** – Python API framework
- **scikit-learn** – for ML password strength prediction
- **pandas** – for data processing during model training
- **HaveIBeenPwned API** – to check if a password has been leaked and how many times
- **OpenRouter LLM API** – to generate password improvement advice

### 💻 Frontend

- **React** – for building interactive UI
- **Axios** – for API requests to the Flask backend

---

## 🤖 Machine Learning Details

The ML model is built with:

- **Random Forest Classifier** – for classifying password strength (0, 1, 2)
- **TfidfVectorizer** – with **char-level analysis** to vectorize password strings effectively
