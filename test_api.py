import requests

# Correct API endpoint
API_URL = 'https://sentiment-analysis-app-x1uy.onrender.com/predict'

positive_review = {
    "review": "This movie was absolutely brilliant! The acting was superb and the plot was engaging from start to finish."
}

negative_review = {
    "review": "What a complete waste of time. The plot was predictable and the characters were incredibly boring."
}

def test_sentiment(review_data, expected_sentiment):

    print(f"--- Testing review: '{review_data['review'][:30]}...' ---")

    try:
        response = requests.post(API_URL, json=review_data)

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:

            response_data = response.json()

            print(f"Received Data: {response_data}")

            if response_data.get('sentiment') == expected_sentiment:

                print("Prediction matches expected result. Test PASSED! ✅")

            else:

                print("Prediction does NOT match expected result. Test FAILED! ❌")

        else:
            print(f"Error: {response.text}")

    except requests.exceptions.RequestException as e:

        print(f"An error occurred while making the request: {e}")

    print("-" * 40 + "\n")


if __name__ == '__main__':

    test_sentiment(positive_review, "Positive")
    test_sentiment(negative_review, "Negative")