from textblob import TextBlob
import random
import datetime

# ------------------------------
# Emotion Detection Function
# ------------------------------
def detect_emotion(text):
    text = text.lower()

    # Crisis keywords
    crisis_words = ["suicide", "kill myself", "end my life", "die"]
    if any(word in text for word in crisis_words):
        return "crisis"

    # Custom emotion keywords
    if any(word in text for word in ["sad", "depressed", "lonely", "unhappy"]):
        return "sad"

    if any(word in text for word in ["stress", "pressure", "overwhelmed", "tired"]):
        return "stress"

    if any(word in text for word in ["angry", "frustrated", "annoyed"]):
        return "anger"

    if any(word in text for word in ["happy", "good", "great", "excited"]):
        return "positive"

    # Fallback to sentiment analysis
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.3:
        return "positive"
    elif polarity < -0.3:
        return "negative"
    else:
        return "neutral"


# ------------------------------
# Chatbot Response Function
# ------------------------------
def chatbot_response(emotion):
    responses = {
        "positive": [
            "😊 That's wonderful to hear!",
            "✨ I'm really happy for you!",
            "🌟 Keep spreading positivity!"
        ],
        "sad": [
            "😔 I'm really sorry you're feeling this way. Do you want to talk about it?",
            "💙 It's okay to feel sad. I'm here for you.",
            "🤗 You are not alone. I'm listening."
        ],
        "stress": [
            "😓 That sounds stressful. Try taking a deep breath.",
            "🧘 Maybe take a short break. It might help.",
            "🌿 Relax for a moment. You deserve it."
        ],
        "anger": [
            "😠 I understand. Anger can be tough. Want to share what happened?",
            "💭 Let's talk it out. I'm here to listen."
        ],
        "negative": [
            "😔 I'm here for you. Do you want to explain more?",
            "💙 It’s okay to feel this way sometimes."
        ],
        "neutral": [
            "🙂 I see. Tell me more.",
            "💬 I'm listening..."
        ],
        "crisis": [
            "🚨 I'm really sorry you're feeling this way.",
            "🚨 Please talk to someone you trust immediately.",
            "🚨 You are not alone. Help is available."
        ]
    }

    return random.choice(responses.get(emotion, ["I'm here for you."]))


# ------------------------------
# Chat History Function
# ------------------------------
def show_chat_summary(history):
    print("\n📊 Chat Summary:")
    print("Total messages:", len(history))
    print("Conversation time:", datetime.datetime.now())
    print("💙 Thank you for sharing.\n")


# ------------------------------
# Main Chat Loop
# ------------------------------
def run_chatbot():
    print("🧠 Intelligent Mental Health Chatbot")
    print("Type 'exit' to stop\n")

    chat_history = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            show_chat_summary(chat_history)
            print("Bot: Take care! 💙")
            break

        # Store history
        chat_history.append(user_input)

        # Detect emotion
        emotion = detect_emotion(user_input)

        # Generate response
        response = chatbot_response(emotion)

        # Print response
        print("Bot:", response)


# ------------------------------
# Run Program
# ------------------------------
if __name__ == "__main__":
    run_chatbot()
