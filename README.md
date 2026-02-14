# Love Quiz – Valentine’s style website

Replica of the “Unlocking Our Love” quiz from the video: intro screen, image collage, multiple-choice questions, wrong-answer popup, and success screen.

## Run the site

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Start the app:
   ```
   python app.py
   ```
3. Open in browser: **http://127.0.0.1:5000**

## Change questions and all text

Edit **`content_config.py`** in this folder. Everything is in one place:

- **INTRO** – Greeting (e.g. “Hey Smit”), “Will you be my Valentine?”, Yes/No button text
- **TITLE** – Main title above the collage (e.g. “UNLOCKING OUR LOVE”)
- **QUESTIONS** – Each question has:
  - `number` – Display number (e.g. Q3, Q4)
  - `emoji` – Icon before the question
  - `text` – The question
  - `options` – List of 3 answer strings
  - `correct` – Index of the right answer (0, 1, or 2)
- **WRONG_ANSWER_MESSAGES** – Popup when the user picks a wrong answer (title, message, “Try Again” button text)
- **SUCCESS** – Text on the final screen (“Yayyy”, “You unlocked every memory”, etc.)
- **FOOTER** – Username, “Follow”, music line, caption
- **SIDEBAR** – Like/comment/share/save counts (decorative)
- **IMAGE_PATHS** – Paths to your 4 collage images (see `static/images/README.txt`)

After editing `content_config.py`, save and refresh the browser (restart `python app.py` only if you add or remove questions).

## Adding your photos

Put your images in **`static/images/`** and set their names in **`content_config.py`** in `IMAGE_PATHS`. You can use a pink block for the 4th slot by setting `USE_PINK_BLOCK_FOR_LAST_IMAGE = True`.
