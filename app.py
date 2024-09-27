from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load the data from the CSV file
data_file = 'instagram_data.csv'  # Path to your CSV file
df = pd.read_csv(data_file)

# Ensure columns are of appropriate types
df['post_id'] = df['post_id'].astype(str)
df['likes_count'] = df['likes_count'].astype(int)
df['comments_count'] = df['comments_count'].astype(int)
df['shares_count'] = df['shares_count'].astype(int)
df['saves_count'] = df['saves_count'].astype(int)
df['engagement_rate'] = df['engagement_rate'].astype(float)

@app.route('/')
def home():
    return "Welcome to the Instagram Insights API!"

# Route 1: Get insights for a specific post by post_id
@app.route('/post/<post_id>', methods=['GET'])
def get_post_by_id(post_id):
    # Filter the DataFrame by post_id
    post = df[df['post_id'] == post_id]

    # Check if the post exists
    if post.empty:
        return jsonify({'error': 'Post not found'}), 404
    
    # Convert the specific post to a JSON-friendly format
    post_data = post.astype(object).to_dict(orient='records')[0]
    return jsonify(post_data)

# Route 2: Get insights for all posts (cumulative)


if __name__ == '__main__':
    app.run(debug=True)