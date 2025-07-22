import nltk
from transformers import AutoModelForCausalLM, AutoTokenizer

nltk.download("punkt")

events = [
    "Graduated from college today!",
    "Attended my first tech conference and even gave a short talk!",
    "Started my first job as a software engineer.",
    "🎓 Feeling proud and excited about the next chapter of my life.",
    "Overcoming my fear of public speaking."
]

model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = (
    "Write a short, first-person life story connecting ONLY these real events:\n"
    + "\n".join(events)
    + "\nMake it sound natural, personal, and reflective. Limit to ~5–6 sentences."
)

inputs = tokenizer(prompt, return_tensors="pt")
output = model.generate(
    **inputs,
    max_new_tokens=256,
    temperature=0.7,
    pad_token_id=tokenizer.eos_token_id
)

story = tokenizer.decode(output[0], skip_special_tokens=True)
print("\n=== Generated Life Story ===\n")
print(story)
