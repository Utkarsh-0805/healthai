import os

try:
    from openai import OpenAI
except Exception:
    OpenAI = None

from django.conf import settings


def get_ai_advice(condition, result):
    prompt = f"""
    User health condition: {condition}
    Prediction: {result}

    Give:
    1. Simple explanation
    2. 3 tips
    3. 1 small habit
    4. 1 fun activity or game
    """

    api_key = os.getenv("NVIDIA_API_KEY") or getattr(settings, "NVIDIA_API_KEY", None)
    if not api_key or OpenAI is None:
        return "AI advice is unavailable. Please use the local recommendations."

    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=api_key,
    )

    completion = client.chat.completions.create(
        model="meta/llama3-70b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=500,
    )

    return completion.choices[0].message.content


def chat_with_ai(message):
    api_key = os.getenv("NVIDIA_API_KEY") or getattr(settings, "NVIDIA_API_KEY", None)
    if not api_key or OpenAI is None:
        return (
            "Hi! I’m your health assistant. I can help with general wellness questions, "
            "but I’m offline right now. Please try again later."
        )

    try:
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=api_key,
        )

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a friendly health chatbot that gives concise, caring wellness guidance. "
                    "Always encourage users to consult a doctor for medical advice. Add personalized touch to user and  give short bulet point messages keep it short and proessional"
                    "limit the response in 2-3 lines  "
                    
                ),
            },
            {"role": "user", "content": message},
        ]

        completion = client.chat.completions.create(
            model="meta/llama3-70b-instruct",
            messages=messages,
            temperature=0.6,
            max_tokens=300,
        )

        return completion.choices[0].message.content.strip() or "Sorry, I could not generate an answer."
    except Exception:
        return (
            "Sorry, I’m having trouble reaching the AI service right now. "
            "Please try again in a moment."
        )