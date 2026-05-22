from flask import Flask, request, jsonify
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load model and vectorizer
try:
    model = joblib.load('lr_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')

    print("Model and vectorizer loaded successfully.")

except FileNotFoundError:
    print("Error: Model or vectorizer file not found.")
    model = None
    vectorizer = None

except Exception as e:
    print(f"An error occurred while loading the model/vectorizer: {e}")
    model = None
    vectorizer = None


# Home route
@app.route('/')
def home():
    return jsonify({
        'message': 'Sentiment Analysis API is running'
    })


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():

    # Check if model loaded properly
    if model is None or vectorizer is None:
        return jsonify({
            'error': 'Model or vectorizer not loaded properly.'
        }), 500

    # Get JSON data
    try:
        data = request.get_json()

        if data is None:
            return jsonify({
                'error': 'Invalid input: No JSON data received.'
            }), 400

    except Exception as e:
        return jsonify({
            'error': f'JSON parsing error: {str(e)}'
        }), 400

    # Get review text
    review_text = data.get('review')

    # Validate input
    if not review_text or not isinstance(review_text, str):
        return jsonify({
            'error': 'Review text is missing or invalid.'
        }), 400

    # Vectorize RAW review text
    try:
        text_vector = vectorizer.transform([review_text])

    except Exception as e:
        return jsonify({
            'error': f'Vectorization error: {str(e)}'
        }), 500

    # Make prediction
    try:
        prediction = model.predict(text_vector)

        print(prediction)

        # Model already returns strings like:
        # ['positive'] or ['negative']
        sentiment = prediction[0].capitalize()

    except Exception as e:
        return jsonify({
            'error': f'Prediction error: {str(e)}'
        }), 500

    # Return response
    return jsonify({
        'review': review_text,
        'sentiment': sentiment
    })


# Run Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)