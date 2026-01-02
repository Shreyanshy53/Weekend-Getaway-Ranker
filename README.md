# 🧳 Weekend Getaway Ranker

## 📌 Project Overview
Weekend Getaway Ranker is a beginner-friendly **Data Engineering project** built using **Python and Pandas**.  
The project takes a **source city** as input and recommends the **top weekend travel destinations** based on **Google ratings and popularity**.

Dataset used: **Top Indian Places to Visit**

---

## 🎯 Problem Statement
Build a recommendation engine that:
- Accepts a **source city** from the user
- Filters destinations belonging to that city
- Ranks destinations using:
  - Google Review Rating
  - Number of Google Reviews (Popularity)

---

## 🛠️ Technologies Used
- Python
- Pandas
- CSV Dataset

---

## 📂 Project Structure
```
weekend-getaway-ranker/
│
├── data/
│   └── Top Indian Places to Visit.csv
│
├── weekend_getaway_ranker.py
├── requirements.txt
├── sample_output.txt
└── README.md
```

---

## 📊 Dataset Description
The dataset contains information about popular tourist places in India.

Key columns used:
- `City` – Source city
- `Name` – Destination name
- `Google review rating` – Rating of the place
- `Number of google review in lakhs` – Popularity indicator

---

## 🧠 Ranking Logic
A simple weighted scoring formula is applied:

```
Score = (Rating × 0.7) + (Popularity × 0.3)
```

- Higher ratings improve rank
- Higher number of reviews increases popularity score
- Top 5 destinations are displayed for each city

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```
pip install pandas
```

### 2️⃣ Run the script
```
python weekend_getaway_ranker.py
```

### 3️⃣ Enter source city
Example:
```
Enter source city: Delhi
```

---

## 📄 Sample Output
```
Source City: Delhi

Top Weekend Destinations:
India Gate - Rating: 4.6, Popularity: 2.60
Red Fort - Rating: 4.5, Popularity: 1.50
Qutub Minar - Rating: 4.5, Popularity: 1.37
Akshardham Temple - Rating: 4.6, Popularity: 0.40
Lotus Temple - Rating: 4.5, Popularity: 0.59
```

---

## 🚀 Key Learnings
- Reading and processing CSV files using Pandas
- Handling real-world datasets with inconsistent column names
- Filtering data based on user input
- Ranking data using a custom scoring logic
- Building a basic recommendation system

---
