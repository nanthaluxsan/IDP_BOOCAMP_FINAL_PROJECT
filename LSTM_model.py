import numpy as np
import tensorflow as tf
import VGG16_model
import Toxigen_combine
import os


import os
import tensorflow as tf
import numpy as np


def predict_hateful_content_from_folder(folder_path):
    # Define a LSTM model with multiple LSTM layers, dropout, and renamed to model1
    model1 = tf.keras.Sequential(
        [
            tf.keras.layers.LSTM(64, return_sequences=True, input_shape=(2, 128)),
            tf.keras.layers.Dropout(0.2),  # Dropout layer with a 20% rate
            tf.keras.layers.LSTM(64, return_sequences=False),
            tf.keras.layers.Dropout(0.2),  # Dropout layer with a 20% rate
            tf.keras.layers.Dense(32, activation="relu"),
            tf.keras.layers.Dropout(0.2),  # Dropout layer with a 20% rate
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ]
    )

    # Compile the model with binary crossentropy loss for binary classification
    model1.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

    # Load the saved weights into the model
    model_path = (
        r"D:\study_further\Senzemate\Project\Weights\lstm_model1_weights.weights.h5"
    )
    model1.load_weights(model_path)

    # List all image files in the folder
    image_files = [
        f for f in os.listdir(folder_path) if f.endswith(("png", "jpg", "jpeg"))
    ]
    results = []

    # Loop over each image file in the folder
    for img_file in image_files:
        img_path = os.path.join(folder_path, img_file)

        # Extract text from the image and get normalized features
        extracted_text = Toxigen_combine.extract_output_from_image(img_path)
        arr_normalized = VGG16_model.load_model_and_extract_features(img_path)

        # Stack the outputs together
        img_out = np.stack((extracted_text, arr_normalized))

        # Add batch dimension using TensorFlow
        img_out_1 = tf.expand_dims(img_out, axis=0)

        # Make the prediction
        predictions = model1.predict(img_out_1)
        output_labels = ["non-hateful", "hateful"]

        # Convert predictions to class labels (0 or 1)
        class_labels = (predictions > 0.5).astype(int)[0][0]

        # Confidence calculation
        confident = predictions[0][0] * 100

        # image name
        image_name = os.path.basename(img_path)

        results.append((image_name, output_labels[class_labels], confident))

    return results
