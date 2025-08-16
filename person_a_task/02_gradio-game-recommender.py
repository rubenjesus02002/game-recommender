import gradio as gr
import random

games_db = {
    "happy": [
        {"title": "Stardew Valley", "year": 2016, "description": "A relaxing farming simulation where you build your dream farm."},
        {"title": "Animal Crossing: New Horizons", "year": 2020, "description": "Create your perfect island paradise with adorable animal friends."},
        {"title": "Minecraft", "year": 2011, "description": "Build and explore infinite worlds in this creative sandbox game."}
    ],
    "sad": [
        {"title": "Journey", "year": 2012, "description": "A beautiful, meditative adventure through mysterious landscapes."},
        {"title": "Gris", "year": 2018, "description": "An artistic platformer about dealing with loss and finding hope."},
        {"title": "Spiritfarer", "year": 2020, "description": "A cozy management game about caring for spirits before saying goodbye."}
    ],
    "excited": [
        {"title": "Doom Eternal", "year": 2020, "description": "Fast-paced demon-slaying action with incredible intensity."},
        {"title": "Rocket League", "year": 2015, "description": "High-octane soccer played with rocket-powered cars."},
        {"title": "Apex Legends", "year": 2019, "description": "Competitive battle royale with unique characters and abilities."}
    ],
    "relaxed": [
        {"title": "The Witness", "year": 2016, "description": "Solve beautiful puzzles on a mysterious island at your own pace."},
        {"title": "Firewatch", "year": 2016, "description": "A peaceful story about a fire lookout in the Wyoming wilderness."},
        {"title": "A Short Hike", "year": 2019, "description": "Explore a peaceful mountain park and help fellow hikers."}
    ]
}

def recommend_games(mood, genre_preference=None):
    if mood.lower() not in games_db:
        return "Sorry, I don't have recommendations for that mood. Try: happy, sad, excited, or relaxed."
    
    mood_games = games_db[mood.lower()]
    
    selected_games = random.sample(mood_games, min(2, len(mood_games)))
    
    recommendations = f"## Game Recommendations for {mood.capitalize()} Mood\n\n"
    
    for game in selected_games:
        recommendations += f"### {game['title']} ({game['year']})\n"
        recommendations += f"{game['description']}\n\n"
    
    return recommendations

# Create the interface
demo = gr.Interface(
    fn=recommend_games,
    inputs=[
        gr.Textbox(label="How are you feeling today?", placeholder="e.g., happy, sad, excited, relaxed"),
        gr.Dropdown(["Action", "Comedy", "Drama", "Sci-Fi", "Any"], label="Genre Preference (Optional)", value="Any")
    ],
    outputs=gr.Markdown(label="Game Recommendations"),
    title="Mood-Based Game Recommender",
    description="Get personalized game recommendations based on your current mood"
)

if __name__ == "__main__":
    demo.launch()