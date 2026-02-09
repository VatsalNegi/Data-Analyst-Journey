"""
===========================================================
Day 1.py – Generative AI Introduction
===========================================================

Author: Vatsal Negi
Course: Generative AI Full Course
Level: Beginner to Advanced

This file covers:

1. What is AI
2. What is Machine Learning
3. What is Deep Learning
4. What is Generative AI
5. Difference between AI, ML, DL, GenAI
6. Real World Examples
7. How Generative AI Works
8. Types of Generative AI Models
9. Applications of Generative AI
10. Simple Python Demo
11. Interview Questions
12. Summary

===========================================================
"""

# ===========================================================
# 1. WHAT IS ARTIFICIAL INTELLIGENCE (AI)
# ===========================================================

"""
Artificial Intelligence is the ability of machines to think and act like humans.

It includes:
• Learning
• Reasoning
• Problem solving
• Understanding language
• Making decisions

Example:
Google Maps suggesting fastest route
Alexa answering questions
Netflix recommending movies
"""


# ===========================================================
# 2. WHAT IS MACHINE LEARNING (ML)
# ===========================================================

"""
Machine Learning is a subset of AI where machines learn from data.

Instead of programming rules, we provide data.

Example:
Spam detection
House price prediction
Recommendation systems
"""


# ===========================================================
# 3. WHAT IS DEEP LEARNING (DL)
# ===========================================================

"""
Deep Learning is a subset of Machine Learning.

It uses Neural Networks similar to human brain.

Example:
Face recognition
Voice recognition
Self-driving cars
ChatGPT
"""


# ===========================================================
# 4. WHAT IS GENERATIVE AI
# ===========================================================

"""
Generative AI creates NEW content.

It can generate:
• Text
• Images
• Code
• Music
• Videos

Example:
ChatGPT → generates text
DALL-E → generates images
GitHub Copilot → generates code

IMPORTANT:
Traditional AI → predicts
Generative AI → creates
"""


# ===========================================================
# 5. DIFFERENCE BETWEEN AI, ML, DL, GenAI
# ===========================================================

"""
AI → Broad field
ML → Learns from data
DL → Uses neural networks
GenAI → Creates new content

Hierarchy:

AI
 └── ML
      └── DL
           └── GenAI
"""


# ===========================================================
# 6. REAL WORLD EXAMPLES OF GENERATIVE AI
# ===========================================================

examples = [
    "ChatGPT → text generation",
    "Midjourney → image generation",
    "Copilot → code generation",
    "Google Gemini → assistant",
    "Sora → video generation"
]

print("\nReal World Examples:")
for example in examples:
    print(example)


# ===========================================================
# 7. HOW GENERATIVE AI WORKS (SIMPLE EXPLANATION)
# ===========================================================

"""
Steps:

1. Collect huge data
2. Train neural network
3. Learn patterns
4. Generate new output

Example:

Input: Write poem about AI
Output: AI generated poem
"""


# ===========================================================
# 8. TYPES OF GENERATIVE AI MODELS
# ===========================================================

models = [
    "LLM (Large Language Models) → ChatGPT",
    "GAN (Generative Adversarial Networks)",
    "Diffusion Models",
    "Transformers"
]

print("\nTypes of GenAI Models:")
for model in models:
    print(model)


# ===========================================================
# 9. APPLICATIONS OF GENERATIVE AI
# ===========================================================

applications = [
    "Content writing",
    "Code generation",
    "Chatbots",
    "Image generation",
    "Video creation",
    "Game development",
    "Medical research",
    "Education"
]

print("\nApplications of Generative AI:")
for app in applications:
    print(app)


# ===========================================================
# 10. SIMPLE PYTHON DEMO (TEXT GENERATION LOGIC)
# ===========================================================

import random

subjects = ["AI", "Machine Learning", "Deep Learning", "ChatGPT"]
verbs = ["is transforming", "is improving", "is changing", "is revolutionizing"]
objects = ["the world", "technology", "education", "healthcare"]

def generate_sentence():
    return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."

print("\nGenerated Sentences:")
for i in range(5):
    print(generate_sentence())


# ===========================================================
# 11. INTERVIEW QUESTIONS AND ANSWERS
# ===========================================================

"""
Q1: What is Generative AI?

Answer:
Generative AI is a type of artificial intelligence that creates new content
such as text, images, code, music, and videos.

---

Q2: Example of Generative AI?

Answer:
ChatGPT, Midjourney, DALL-E, GitHub Copilot

---

Q3: Difference between AI and Generative AI?

Answer:
AI → makes decisions
Generative AI → creates new content

---

Q4: What is LLM?

Answer:
LLM stands for Large Language Model.
Example: GPT, Gemini, Claude

---

Q5: Applications of Generative AI?

Answer:
Chatbots, coding, content writing, image generation
"""


# ===========================================================
# 12. SUMMARY
# ===========================================================

print("\nSummary:")
print("AI → Smart machines")
print("ML → Learning from data")
print("DL → Neural networks")
print("GenAI → Content generation")


# ===========================================================
# END OF DAY 1
# ===========================================================
