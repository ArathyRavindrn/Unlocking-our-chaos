"""
Edit all questions and written content here.
Change any text below to customize your love quiz website.
"""

# ============ INTRO SCREEN (first thing users see) ============
INTRO = {
    "greeting": "Hey Doodu 😘",           # e.g. "Hey [Name] 😘"
    "greeting_emoji": "💖",
    "question": "Will you be my Valentine?",
    "yes_button": "Yes 🥰",
    "no_button": "No 😔",
}

# ============ MAIN TITLE (shown above the image collage) ============
TITLE = "UNLOCKING OUR CHAOS"

# ============ QUIZ QUESTIONS ============
# For each question: "text" = question, "options" = list of 3 answers, "correct" = index of correct answer (0, 1, or 2)
QUESTIONS = [
    {
        "number": 1,
        "emoji": "❤️",
        "text": "Best part of our chats?",
        "options": ["Late Night", "Memes", "Random Talks"],
        "correct": 2,  # "Random Talks" is correct
    },
    {
        "number": 2,
        "emoji": "❤️",
        "text": "Date we went on our first trip?",
        "options": ["11th Jan 2026", "12th Jan 2026", "10th Jan 2026"],
        "correct": 0,  # change to 0, 1, or 2
    },
    {
        "number": 3,
        "emoji": "❤️",
        "text": "What is our favourite thing to do together?",
        "options": ["Netflix n Chill", "Drinking", "Bathing together"],
        "correct": 0,  # "OK Jaanu"
    },
    {
        "number": 4,
        "emoji": "✈️",
        "text": "My Dream Destination?",
        "options": ["Scotland", "Switzerland", "Maldives 🌴"],
        "correct": 1,  # "Maldives"
    },
]

# ============ WRONG ANSWER MESSAGES (shown in popup when user picks wrong answer) ============
# You can add more; one will be chosen randomly each time
WRONG_ANSWER_MESSAGES = [
    {
        "title": "Oops! 😉",
        "message": "Wrong answer... Think harder ❤️",
        "button": "Try Again 💖",
    },
    {
        "title": "ERRR! 😳💖",
        "message": "Aw.. aw..dont you remember? 🥺💔",
        "button": "Try Again 💖",
    },
]

# ============ SUCCESS SCREEN (after all answers are correct) ============
SUCCESS = {
    "heading": "Yayyy 🎉💖",
    "line1": "You unlocked every memory 🥺❤️",
    "line2": "Forever My Valentine 💍",
    "line3": "Love You Always 💖",
}

# ============ FOOTER (social-style section below quiz) ============
FOOTER = {
    "username": "",
    "follow_button": "",
    "music": "",
    "caption": "",
}

# ============ RIGHT SIDEBAR (like/comment/share counts - decorative) ============
SIDEBAR = {
    "likes": "",
    "comments": "",
    "shares": "",
    "saves": "",
    "more": "",
}

# ============ IMAGE PATHS (place your 4 images in static/images/) ============
# Use placeholder names; replace with your image filenames
IMAGE_PATHS = [
    "/static/images/photo1.jpeg",  # top-left
    "/static/images/photo2.jpeg",  # top-right
    "/static/images/photo3.jpeg",  # bottom-left
    "/static/images/photo4.jpeg",  # bottom-right
]
# Set to True to show a solid pink block instead of the 4th image
USE_PINK_BLOCK_FOR_LAST_IMAGE = False
