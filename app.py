from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('student_performance_model.pkl')

grade_labels = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'F'}
grade_colors = {
    'A': '#00ff88',
    'B': '#00bfff',
    'C': '#ffaa00',
    'D': '#ff6600',
    'F': '#ff3333'
}
grade_messages = {
    'A': 'Outstanding! Keep it up! 🌟',
    'B': 'Great Performance! 👏',
    'C': 'Average. You can do better! 💪',
    'D': 'Needs Improvement. Study harder! 📚',
    'F': 'Critical! Please seek help immediately! 🚨'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    features = np.array([[
        int(data['age']),
        float(data['studyTime']),
        int(data['absences']),
        int(data['tutoring']),
        int(data['parentalSupport']),
        int(data['extracurricular']),
        int(data['sports']),
        int(data['music']),
        int(data['volunteering'])
    ]])
    
    prediction = model.predict(features)[0]
    grade = grade_labels[int(prediction)]
    
    return jsonify({
        'grade': grade,
        'color': grade_colors[grade],
        'message': grade_messages[grade]
    })

if __name__ == '__main__':
    app.run(debug=True)