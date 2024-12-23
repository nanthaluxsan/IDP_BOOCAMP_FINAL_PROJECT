import numpy as np
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from sklearn.preprocessing import MinMaxScaler


def load_model_and_extract_features(img_path, target_size=(224, 224)):
    """
    This function loads a pre-trained VGG16 model, processes an image,
    runs inference through the model, and outputs the normalized feature vector.

    Parameters:
    - img_path: Path to the image to process.
    - target_size: Desired size to resize the image (default is (224, 224)).

    Returns:
    - arr_normalized: Normalized feature vector extracted from the intermediate layer of the model.
    """
    # Load VGG16 with pre-trained ImageNet weights (without top layers)
    base_model = VGG16(weights="imagenet", include_top=False, input_shape=(224, 224, 3))

    # Freeze the base model's layers before adding custom layers
    base_model.trainable = False

    # Add custom layers
    x = Flatten()(base_model.output)
    x = Dense(128, activation="relu", name="dense_4")(x)
    x = Dropout(0.5)(x)
    output = Dense(1, activation="sigmoid")(x)  # Binary classification output

    # Create the model with a single output
    model = Model(inputs=base_model.input, outputs=output)

    # Compile the model (before loading weights)
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

    # Load the model weights
    model.load_weights(
        r"D:\study_further\Senzemate\Project\Weights\best_model_weights.weights.h5"
    )

    # Load and preprocess the image
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Get the intermediate model (outputs layer 'dense_4')
    intermediate_model = Model(
        inputs=model.input, outputs=model.get_layer("dense_4").output
    )

    # Run inference using the intermediate model
    intermediate_output = intermediate_model.predict(img_array)

    # Normalize the feature vector using MinMaxScaler
    arr_normalized = MinMaxScaler().fit_transform(intermediate_output[0].reshape(-1, 1))
    arr_normalized = arr_normalized.flatten()

    return arr_normalized
