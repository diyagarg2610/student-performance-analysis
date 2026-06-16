# 🎓 Student Performance Analysis System

A machine learning project that analyzes student academic data to identify performance trends and predict grades.

## 📊 Overview
- Analyzed **2,392 students** academic records
- Identified key factors affecting student performance
- Built ML model with **70% accuracy** to predict grades
- Generated **5 insightful visualizations**

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Latest-green)
![Scikit--Learn](https://img.shields.io/badge/ScikitLearn-Latest-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Latest-red)

## 📈 Visualizations
| Graph | Insight |
|-------|---------|
| GPA Distribution | Overall student performance spread |
| Study Time vs GPA | Impact of study hours on grades |
| Absences vs GPA | Effect of attendance on performance |
| Correlation Heatmap | Relationships between all features |
| Feature Importance | Key factors affecting grades |

## 🔍 Key Findings
- **Study Time** is the strongest predictor of grades
- Students with **5+ absences** show significant GPA drop
- **Parental support** plays major role in performance
- **Tutoring** positively impacts grade outcomes

## 🤖 ML Model
- Algorithm: **Random Forest Classifier**
- Accuracy: **70%**
- Features: Age, Study Time, Absences, Tutoring, Parental Support

## 📁 Project Structure
student-performance/

├── Student_Performance_Analysis.ipynb  # Main notebook

├── student_performance_model.pkl       # Saved ML model

├── gpa_distribution.png               # Visualization

├── studytime_vs_gpa.png               # Visualization

├── absences_vs_gpa.png                # Visualization

├── correlation_heatmap.png            # Visualization

├── feature_importance.png             # Visualization

└── data/

└── student_performance.csv        # Dataset

## 🚀 How to Run
1. Clone the repository
```bash
git clone https://github.com/diyagarg2610/student-performance-analysis.git
```
2. Install dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```
3. Open Jupyter Notebook
```bash
jupyter notebook Student_Performance_Analysis.ipynb
```

## 👩‍💻 Author
**Diya** — B.Tech CS (Robotics & AI)