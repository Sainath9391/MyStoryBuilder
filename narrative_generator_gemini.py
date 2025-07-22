import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-pro")

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

response = model.generate_content(prompt)
print("\n=== Generated Life Story ===\n")
print(response.text)
