from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

csv_files = {
    "description": "./data/description.csv",
    "diets": "./data/diets.csv",
    "medications": "./data/medications.csv",
    "precautions": "./data/precautions_df.csv",
    "symptom_severity": "./data/Symptom-severity.csv",
    "symptoms_df": "./data/symptoms_df.csv",  
    "training": "./data/Training.csv",
    "workout_df": "./data/workout_df.csv",
    "quotes": "./data/motivational_quotes_dataset.csv",
    "emotions": "./data/emotions.csv"
}

@app.route('/')
def index():
    return render_template('index.html')

def create_csv_name(route_name, file_name):
    # Define the function inside create_csv_name
    def get_data():
        try:
            df = pd.read_csv(file_name)
            data = df.to_dict(orient='records')  # Convert DataFrame to a list of records
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Register the route after defining the function
    app.route(f'/{route_name}', methods=['GET'], endpoint=route_name)(get_data)

# Loop through the csv_files dictionary and create routes
for route_name, file_name in csv_files.items():
    create_csv_name(route_name, file_name)

if __name__ == "__main__":
    app.run(debug=True)
