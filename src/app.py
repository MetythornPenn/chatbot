import gradio as gr
from inference import get_response

import asyncio
from loguru import logger
from typing import Optional, List
from pydantic import BaseModel

# Define the Message class
class Message(BaseModel):
    role: str
    content: str

# Define the predict function
async def predict(input, history):
    """
    Predict the response of the chatbot and complete a running list of chat history.
    """
    # Append the user message to history
    history.append({"role": "user", "content": input})
    
    # Get the response using the inference function (adapted from your logic)
    response = get_response(input)
    
    # Append the bot response to history
    history.append({"role": "assistant", "content": response})
    
    # Format messages for display
    messages = [(history[i]["content"], history[i+1]["content"]) for i in range(0, len(history)-1, 2)]
    return messages, history

# Gradio Blocks low-level API that allows to create custom web applications (here our chat app)
with gr.Blocks() as demo:
    logger.info("Starting Demo...")
    chatbot = gr.Chatbot(label="Chatbot")
    state = gr.State([])
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter")
    txt.submit(predict, [txt, state], [chatbot, state])

# Launch the Gradio app
demo.launch(server_port=8080)
