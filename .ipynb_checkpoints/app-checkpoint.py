from flask import Flask, request, 
import joblib
import numpy as np
import re

try:
    model = joblib.load('lr_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    # Print a success message to the console to confirm that the models loaded correctly.
    print("Model and vectorizer loaded successfully.")
except FileNotFoundError:
    print("Error: Model or vectorizer file not found. Make sure 'lr_model.pkl' and 'tfidf_vectorizer.pkl' are in the same directory as app.py.")
    model = None
    vectorizer = None
except Exception as e:
    print(f"An error occurred while loading the model/vectorizer: {e}")
    model = None
    vectorizer = None