import random
import json
import re
import os

adjectives = [
    "prettiest", "cutest", "sweetest", "most adorable", "most charming", 
    "most precious", "most angelic", "most beautiful", "most wonderful", 
    "most perfect", "softest", "brightest", "most radiant", "most dazzling", 
    "most lovely", "most magical", "most enchanting", "most darling", 
    "most delightful", "most gorgeous", "most breathtaking", "most stunning",
    "cutest little", "most elegant", "most flawless", "most mesmerizing"
]
nouns = [
    "girl", "princess", "angel", "fairy", "queen", "kitty", "sweetheart", 
    "darling", "baby", "sunshine", "star", "flower", "blossom", "treasure", 
    "gem", "cupcake", "marshmallow", "bunny", "dove", "butterfly", "diamond",
    "moonlight", "starlight", "dream", "miracle", "strawberry"
]
emojis = [
    "🎀", "🌸", "✨", "💕", "🍓", "💖", "💗", "💝", "🌷", "🧚‍♀️", "👑", "🥺", 
    "🥰", "😻", "🍯", "🍰", "🍭", "🍬", "🦋", "🦄", "🧸", "🤍", "🐰", "🐥", 
    "💫", "🌟", "🍒", "🍑", "🍄", "🫧"
]

templates = [
    "Who is the {adj} {noun}?",
    "Who has the {adj} smile?",
    "Who is the absolute {adj} {noun}?",
    "Whose eyes are the {adj}?",
    "Who is my favorite {noun}?",
    "Who is the {adj} person ever?",
    "Who is the definition of {adj}?",
    "Who is the world's {adj} {noun}?",
    "Who is as {adj} as a {noun}?",
    "Who shines brighter than a {noun}?",
    "Who is sweeter than a {noun}?",
    "Whose heart is the {adj}?",
    "Who is the universe's {adj} {noun}?",
    "Who makes every day {adj}?"
]

questions = set()
while len(questions) < 2000:
    t = random.choice(templates)
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    emoji = random.choice(emojis)
    
    # Simple formatting
    q = t.replace("{adj}", adj).replace("{noun}", noun) + f" {emoji}"
    questions.add(q)

q_list = list(questions)

js_path = r"c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (90)\script.js"
with open(js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Using ensure_ascii=False to keep raw emojis instead of \u escapes
array_str = json.dumps(q_list, indent=4, ensure_ascii=False)
new_content = re.sub(r'const questions = \[.*?\];', lambda _: f'const questions = {array_str};', content, flags=re.DOTALL)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Success! Generated {len(q_list)} unique questions and updated script.js.")
