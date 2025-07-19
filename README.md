# Smart Tweet Generator and Like Predictor

This is a small project that can do two things:
1. Generate a tweet using a simple template.
2. Predict how many likes that tweet might get.

## Files in the Project

- `comboapp.py` – This is the main Flask app.
- `tweet_generator.py` – This creates sample tweets using a template.
- `like_predictor.pkl` – This is a trained model that predicts the number of likes.
- `test_generate.py` – This is a script that sends a request to the API and prints the result.

## How to Run the Project

1. Install the required packages:
pip install -r requirements.txt

2. Start the Flask app:
python comboapp.py

This will run the app at `http://localhost:5002`

3. Test the app using:

## API Endpoint

### POST `/generate_smart_tweet`

You need to send a JSON with this data:

```json
{
"company": "Nike",
"industry": "sportswear",
"word_count_target": 12,
"sentiment_target": 0.5,
"has_media": 1
}
```
You will get a response like this:

```json
{
  "tweet": "Sample tweet for Nike",
  "predicted_likes": 123
}
```
## Bonus: Smart Tweet Feature

This project includes a smart tweet feature that not only generates a sample tweet, but also predicts the number of likes it might get using a trained model.

You can control the following when sending the request:
- `company` – the brand name in the tweet
- `industry` – the type of industry
- `sentiment_target` – the expected tone (positive or neutral)
- `has_media` – whether the tweet has an image or not
- `word_count_target` – how long the tweet should be

This makes the tweet generation more flexible and useful.
