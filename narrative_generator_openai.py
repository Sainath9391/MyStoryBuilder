import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

events = [
    "Graduated from college today!",
    "Attended my first tech conference and even gave a short talk!",
    "Started my first job as a software engineer.",
    "🎓 Feeling proud and excited about the next chapter of my life.",
    "Overcoming my fear of public speaking."
]

prompt = (
    "Write a short, first-person life story connecting ONLY these real events:\n"
    + "\n".join(events)
    + "\nMake it sound natural, personal, and reflective. Limit to ~5–6 sentences."
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7
)

print("\n=== Generated Life Story ===\n")
print(response.choices[0].message.content)
