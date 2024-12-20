from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from PIL import Image
import ocr_extraction
import toxigen_hate_bert

app = Flask(__name__)
CORS(app)


app.config["UPLOAD_FOLDER"] = "uploads"
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])


@app.route("/upload_image", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return jsonify({"error": "No file part"}), 400

    image = request.files["image"]
    if image.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if image:
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
        image.save(image_path)

        result = process_image(app.config["UPLOAD_FOLDER"])

        return jsonify(result)


def process_image(folder_path):
    texts = ocr_extraction.extract_text_from_images(folder_path)

    try:
        total_outputs = toxigen_hate_bert.hateful_detect(texts)
    except Exception as e:
        return jsonify({"error": f"Hate speech detection failed: {str(e)}"}), 500

    # Convert total_outputs to a dictionary with labels for easier interpretation
    results = []
    for output in total_outputs:
        result = {
            "id": output[0],  # Text or image identifier (01579, 02538, etc.)
            "label": output[1],  # 'hateful' or 'non_hateful'
            "confidence": output[2],  # Confidence score
        }
        results.append(result)
    return results


@app.route("/results/<filename>")
def results(filename):
    # Add code to display results
    return f"Processed {filename}"


if __name__ == "__main__":
    app.run(debug=True)
