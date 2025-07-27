from tensorflow import keras

# Load the model
model = keras.models.load_model("best_weight.h5")

# Print a detailed summary of the model
model.summary()

# If you want even more detailed config
from pprint import pprint
pprint(model.get_config())
