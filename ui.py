import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/predict"


st.title("Sentimental Analysis of Text Reviews")

user_input = st.text_area(
    label="Enter your review below",
    placeholder="This movie was fantastic and the acting was superb! I would highly recommend it to everyone.",
    height=200
)

analyze_button = st.button("Analyze Sentiment")

if analyze_button:
    if user_input.strip():

        payload = {
            "review": user_input
            }
        try:
            with st.spinner("Analyzing ..."):
                response = requests.post(API_URL, json=payload)
            # st.write(f"API Response Status Code: {response.status_code}")

            if response.status_code == 200:

                responce_data = response.json()

                sentiment = responce_data.get("sentiment")

                if sentiment == 'Positive':
                    # st.success() displays the message in a green box.
                    st.success(f"Prediction: Positive 👍")
                elif sentiment == 'Negative':
                    # st.error() displays the message in a red box.
                    st.error(f"Prediction: Negative 👎")
                else:
                    # A neutral message for any unexpected response.
                    st.warning("Could not determine the sentiment. Please try another review.")

                # if sentiment:
                #     st.write(f"Predicted Sentiment: **{sentiment.capitalize()}**")
                # else:
                #     st.error("The API response was valid, but did not contain a sentiment prediction. Please check the API.")


                # st.write("Data received from API:")
                # st.json(responce_data)

            else:

                try:
                    error_details = response.json()
                    st.error(f"API Error: {error_details.get('error', 'Unknown error')}")
                except requests.exceptions.JSONDecodeError:
                    st.error(f"API Error: Received non-JSON response with status code {response.status_code} - {response.text}")


        except requests.exceptions.ConnectionError as e:
            st.error(f"Connection Error: Could not connect to the API at {API_URL}. Please ensure the Flask server (app.py) is running.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

        # st.write("Button clicked!  The process to call the API will start now")
        # st.write("Constructed payload:")
        # st.json(payload)

    else:
        st.warning("Please enter a review before clicking the Analyze Sentiment button.")
