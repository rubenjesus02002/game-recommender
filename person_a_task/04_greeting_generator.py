import gradio as gr

def generate_greeting(name, greeting_type, include_emoji):
    """ 
    Generate a personalized greeting based on user inputs 
    """
    if not name:
        name = "there"
    
    if greeting_type == "Formal":
        greeting = f"Well good day, {name} my good sir."
    elif greeting_type == "Casual":
        greeting = f"Hey, what's up {name}!"
    elif greeting_type == "Enthusiastic":
        greeting = f"HELLO {name.upper()} HOW ARE YOU!!!"
    else:
        greeting = f"Hi {name}."
    
    if include_emoji:
        if greeting_type == "Formal":
            greeting += " 🎩"
        elif greeting_type == "Casual":
            greeting += " 👋"
        elif greeting_type == "Enthusiastic":
            greeting += " 🎉🎉🎉"
    
    return greeting

with gr.Blocks(title="Greeting Generator") as demo:
    gr.Markdown("# Personalized Greeting Generator")
    
    with gr.Row():
        with gr.Column():
            name_input = gr.Textbox(label="Your Name", placeholder="Enter your name here")
            greeting_type = gr.Radio(
                ["Formal", "Casual", "Enthusiastic"],
                label="Greeting Style",
                value="Casual"
            )
            emoji_checkbox = gr.Checkbox(label="Include Emoji", value=True)
            generate_btn = gr.Button("Generate Greeting")
        
        with gr.Column():
            # Output component
            output = gr.Textbox(label="Your Personalized Greeting")
    
    # Connect the button to the function
    generate_btn.click(
        generate_greeting,
        inputs=[name_input, greeting_type, emoji_checkbox],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch()