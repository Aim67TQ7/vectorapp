from flask import Flask, request, jsonify
from transform import transform_data
from supabase_client import upload_to_supabase

app = Flask(__name__)

# Route to handle file uploads and data transformation
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Transform data into vectors
    transformed_data = transform_data(file)

    # Upload to Supabase
    success = upload_to_supabase(transformed_data)
    if success:
        return jsonify({"message": "Data successfully uploaded to Supabase"}), 200
    else:
        return jsonify({"error": "Failed to upload data"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
