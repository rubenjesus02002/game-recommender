import gradio as gr
import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("fae59a1407mshde9b98095612a09p14af8ajsne7a45c1b0292")

def get_mood_options():
    return ["happy", "sad", "excited", "relaxed", "competitive"]

# Function for getting games
def get_games(mood):
    url = "https://opencritic-api.p.rapidapi.com/game"
    
    querystring = {"platforms":"pc,ps4,ps5","sort":"score","order":"desc","skip":"0"}
    
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "opencritic-api.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    return f"Games for {mood} mood will appear here once API is working."

# Placeholder function for analyzing games
def analyze_game(game_name):
    return f"This will show an analysis of {game_name} once we integrate Ollama."

# Create the interface
with gr.Blocks(title="Game Mood Recommender") as demo:
    gr.Markdown("# 🎮 Game Mood Recommender")
    gr.Markdown("Get personalized game recommendations based on your current mood")
    
    with gr.Row():
        with gr.Column():
            mood = gr.Dropdown(
                choices=get_mood_options(),
                label="Current Mood",
                value="happy"
            )
            get_games_btn = gr.Button("Get Game Recommendations")
        
        with gr.Column():
            game_selector = gr.Textbox(
                label="Enter Game Name to Analyze",
                placeholder="Type game name here"
            )
            analyze_btn = gr.Button("Analyze Game")
    
    with gr.Row():
        with gr.Column():
            games_display = gr.Markdown(label="Game Recommendations")
        
        with gr.Column():
            analysis_display = gr.Markdown(label="Game Analysis")
    
    # Connect buttons to functions
    get_games_btn.click(
        get_games,
        inputs=mood,
        outputs=games_display
    )
    
    analyze_btn.click(
        analyze_game,
        inputs=game_selector,
        outputs=analysis_display
    )

if __name__ == "__main__":
    demo.launch()