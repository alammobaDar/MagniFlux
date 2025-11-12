# 🧲 Magnetic Flux Calculator

## See the app 
[https://magni-flux.vercel.app/](https://magni-flux.vercel.app/)

## 🌐 Overview
**Magnetic Flux Calculator** is an interactive web application that allows users to calculate magnetic flux based on input parameters or solve word problems through AI assistance. Built with **React**, **Tailwind CSS**, **FastAPI**, and integrated with **Google's Gemini AI API**, the app also features rich 3D visualizations using **Plotly**.

It is designed to support both learning and real-world problem solving by offering detailed explanations, visual representations, and an intuitive user interface.

---

## ✨ Key Features

### 📌 Dual Calculation Modes
- **Manual Input Mode**
  - Enter Magnetic Field (Tesla), Area, and Angle (Degrees or Radians)
  - Instant calculation of magnetic flux
  - Explanations provided with AI support
  - Visualization using Plotly 3D

- **Word Problem Mode**
  - Input word problems in plain English
  - Uses **Gemini AI API** to extract and compute relevant data
  - Generates step-by-step explanation and result
  - Visualizes the scenario in 3D

### 📊 Visualization
- 3D magnetic flux representation powered by **Plotly.js**
- Dynamic and interactive vector-based visualization

### 🤖 AI Integration
- Uses **Gemini AI API** for:
  - Understanding natural language word problems
  - Providing context-aware, step-by-step explanations
  - Accurate computation of magnetic flux from problem statements

---

## 🛠️ Tech Stack

| Layer       | Technology                        |
|-------------|------------------------------------|
| Frontend    | React, JavaScript, Tailwind CSS    |
| Backend     | FastAPI (Python)                   |
| AI Service  | Gemini API (via Google Generative AI) |
| Visualization | Plotly.js (3D representation)    |

---

## 🚀 Getting Started

### 🖥️ Frontend

```bash
cd frontend
npm install
npm run dev  # or npm start
