"""
Love Quiz - Valentine's style interactive quiz (replica of Netlify site from video).
"""
from flask import Flask, render_template
import content_config as config
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        intro=config.INTRO,
        title=config.TITLE,
        questions=config.QUESTIONS,
        wrong_messages=config.WRONG_ANSWER_MESSAGES,
        success=config.SUCCESS,
        footer=config.FOOTER,
        sidebar=config.SIDEBAR,
        image_paths=config.IMAGE_PATHS,
        use_pink_block=config.USE_PINK_BLOCK_FOR_LAST_IMAGE,
    )



