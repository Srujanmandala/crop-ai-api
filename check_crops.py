# check_crops.py
import pickle

try:
    with open('crop_label_encoder_v1.pkl', 'rb') as f:
        le = pickle.load(f)
    print("Available crops in model:")
    for i, crop in enumerate(le.classes_):
        print(f"{i}: {crop}")
except Exception as e:
    print(f"Error loading label encoder: {e}")

try:
    with open('crop_encoder.pkl', 'rb') as f:
        le2 = pickle.load(f)
    print("\nAvailable crops in backup encoder:")
    for i, crop in enumerate(le2.classes_):
        print(f"{i}: {crop}")
except Exception as e:
    print(f"Error loading backup encoder: {e}")