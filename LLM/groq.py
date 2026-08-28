from groq import Groq
from Helpers.config import GROQ_API_KEY  # Add your Groq API Key here

client = Groq(api_key=GROQ_API_KEY)

def ask_groq(prompt: str, model="openai/gpt-oss-120b", temperature=0.7):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert in Amazon products."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )
    return response.choices[0].message.content
