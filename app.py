"""
Love Quiz - Valentine's style interactive quiz (replica of Netlify site from video).
"""
from flask import Flask, render_template, jsonify
import content_config as config
import os
import sys
import logging
from logging import StreamHandler

app = Flask(__name__)

# Configure logging to stdout so Railway captures logs
logger = logging.getLogger("love_quiz")
if not logger.handlers:
    logger.setLevel(logging.INFO)
    sh = StreamHandler(sys.stdout)
    sh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))
    logger.addHandler(sh)


@app.route("/")
def index():
    logger.info("Rendering index page")
    try:
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
    except Exception as e:
        logger.exception("Error rendering index")
        return "Internal Server Error", 500


@app.route('/health')
def health():
    # Simple health check for uptime monitoring
    return jsonify(status="ok"), 200


@app.errorhandler(Exception)
def handle_exception(e):
    logger.exception("Unhandled exception: %s", e)
    return "Internal Server Error", 500


if __name__ == "__main__":
    # Local dev runner (not used by Gunicorn in production)
    port = int(os.environ.get("PORT", 5000))
    logger.info(f"Starting local server on port {port}")
    app.run(host="0.0.0.0", port=port, debug=False)




