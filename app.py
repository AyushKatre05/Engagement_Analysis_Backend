from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import pandas as pd

app = Flask(__name__)
CORS(app) 

data_file = 'instagram_data.csv'  
df = pd.read_csv(data_file)

df['post_id'] = df['post_id'].astype(str)
df['likes_count'] = df['likes_count'].astype(int)
df['comments_count'] = df['comments_count'].astype(int)
df['shares_count'] = df['shares_count'].astype(int)
df['saves_count'] = df['saves_count'].astype(int)
df['engagement_rate'] = df['engagement_rate'].astype(float)

@app.route('/')
def home():
    return "Welcome to the Social Media Insights API!"

@app.route('/post/<post_id>', methods=['GET'])
def get_post_by_id(post_id):
    post = df[df['post_id'] == post_id]

    if post.empty:
        return jsonify({'error': 'Post not found'}), 404
    
    post_data = post.astype(object).to_dict(orient='records')[0]
    return jsonify(post_data)


if __name__ == '__main__':
    app.run(debug=True)
