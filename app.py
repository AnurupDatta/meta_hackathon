from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from ui.gradio_ui import create_ui
import gradio as gr

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)

# Mount UI
demo = create_ui()
app = gr.mount_gradio_app(app, demo, path="/ui")