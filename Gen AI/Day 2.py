"""
===========================================================
Day 2.py – LLMs and Transformers (ChatGPT Architecture)
===========================================================

Author: Vatsal Negi
Course: Generative AI Full Course

Topics Covered:

1. What is LLM (Large Language Model)
2. Examples of LLMs
3. How LLM works
4. Tokens and Tokenization
5. What is Transformer
6. Why Transformer is important
7. Transformer Architecture
8. Encoder vs Decoder
9. Attention Mechanism
10. Self Attention
11. How ChatGPT works
12. Training Process
13. Inference (Generation)
14. Python Demo (Tokenization + Attention Concept)
15. Interview Questions
16. Summary

===========================================================
"""


# ===========================================================
# 1. WHAT IS LLM (Large Language Model)
# ===========================================================

"""
LLM stands for Large Language Model.

It is a Deep Learning model trained on huge text data.

It can:
• Answer questions
• Write code
• Write essays
• Translate languages
• Chat like humans

Examples:
ChatGPT
Gemini
Claude
LLaMA

Large → billions of parameters
Language → works with text
Model → neural network
"""

print("LLM = Large Language Model")


# ===========================================================
# 2. EXAMPLES OF LLMs
# ===========================================================

llms = [
    "GPT-4 / GPT-5",
    "Google Gemini",
    "Meta LLaMA",
    "Claude",
    "Mistral"
]

print("\nExamples of LLMs:")
for model in llms:
    print(model)


# ===========================================================
# 3. HOW LLM WORKS (SIMPLIFIED)
# ===========================================================

"""
Steps:

1. Input text
2. Convert into tokens
3. Process using transformer
4. Predict next word
5. Generate response

Example:

Input: "AI is"
Output: "AI is transforming the world"
"""


# ===========================================================
# 4. TOKENS AND TOKENIZATION
# ===========================================================

"""
Token = small unit of text

Example:

Sentence:
"I love AI"

Tokens:
"I"
"love"
"AI"

Or:
"I", "lo", "ve", "AI"
"""

text = "I love Generative AI"

tokens = text.split()

print("\nTokens:")
print(tokens)


# ===========================================================
# 5. WHAT IS TRANSFORMER
# ===========================================================

"""
Transformer is a Neural Network architecture introduced in 2017.

Paper:
"Attention is All You Need"

It is used in:
ChatGPT
Gemini
Claude
All modern LLMs

Before Transformer:
RNN (slow)
LSTM (slow)

Transformer:
Fast
Parallel
Accurate
"""


# ===========================================================
# 6. WHY TRANSFORMER IS IMPORTANT
# ===========================================================

advantages = [
    "Parallel processing",
    "Understands context",
    "Handles long sentences",
    "Better accuracy",
    "Faster training"
]

print("\nTransformer Advantages:")
for adv in advantages:
    print(adv)


# ===========================================================
# 7. TRANSFORMER ARCHITECTURE
# ===========================================================

"""
Transformer has:

INPUT → TOKENIZATION → EMBEDDING → ATTENTION → OUTPUT

Structure:

            INPUT
              │
         Tokenization
              │
          Embedding
              │
        Self Attention
              │
        Feed Forward
              │
            OUTPUT

ChatGPT uses DECODER part of Transformer
"""


# ===========================================================
# 8. ENCODER vs DECODER
# ===========================================================

"""
Encoder:
Understands input

Decoder:
Generates output

Examples:

Encoder:
BERT

Decoder:
GPT
ChatGPT

Encoder-Decoder:
T5
"""


# ===========================================================
# 9. ATTENTION MECHANISM
# ===========================================================

"""
Attention helps model focus on important words.

Example:

Sentence:
"The animal didn't cross the street because it was tired"

What is tired?
animal

Attention helps understand this relationship.
"""


# ===========================================================
# 10. SELF ATTENTION (SIMPLIFIED DEMO)
# ===========================================================

words = ["I", "love", "AI"]

print("\nSelf Attention Demo:")

for word in words:
    print(f"{word} attends to all other words")


# ===========================================================
# 11. HOW CHATGPT WORKS
# ===========================================================

"""
Steps:

User Input
   ↓
Tokenization
   ↓
Transformer Decoder
   ↓
Predict next token
   ↓
Generate response
"""


# ===========================================================
# 12. TRAINING PROCESS
# ===========================================================

"""
Training steps:

1. Collect massive data (internet, books, code)
2. Train transformer model
3. Learn patterns
4. Adjust weights
5. Repeat billions of times

This is called Pretraining
"""


# ===========================================================
# 13. INFERENCE (TEXT GENERATION)
# ===========================================================

"""
Inference means using trained model.

Example:

Input:
"Python is"

Model predicts:
"Python is a programming language"
"""


# ===========================================================
# 14. PYTHON DEMO – SIMPLE NEXT WORD PREDICTION
# ===========================================================

import random

dataset = {
    "AI": ["is", "will", "can"],
    "is": ["powerful", "useful", "amazing"],
    "Python": ["is", "can", "will"],
    "ChatGPT": ["is", "can", "helps"]
}

def generate_text(start_word, length=5):
    word = start_word
    sentence = word

    for i in range(length):
        if word in dataset:
            next_word = random.choice(dataset[word])
        else:
            next_word = random.choice(["AI", "Python", "ChatGPT"])

        sentence += " " + next_word
        word = next_word

    return sentence

print("\nGenerated Text:")
print(generate_text("AI"))


# ===========================================================
# 15. INTERVIEW QUESTIONS
# ===========================================================

"""
Q1: What is LLM?

Answer:
LLM is Large Language Model trained on massive text data.

---

Q2: What architecture is used in ChatGPT?

Answer:
Transformer Decoder

---

Q3: Who invented Transformer?

Answer:
Google, 2017

Paper: Attention is All You Need

---

Q4: What is token?

Answer:
Small unit of text

---

Q5: What is attention?

Answer:
Mechanism to focus on important words

---

Q6: Difference between Encoder and Decoder?

Answer:
Encoder → understands input
Decoder → generates output
"""


# ===========================================================
# 16. SUMMARY
# ===========================================================

print("\nSummary:")
print("LLM = Large Language Model")
print("Transformer = Architecture used in LLM")
print("Attention = Focus mechanism")
print("ChatGPT uses Transformer Decoder")


# ===========================================================
# END OF DAY 2
# ===========================================================
