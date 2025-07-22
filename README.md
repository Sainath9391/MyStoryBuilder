# 📖 MyStoryBuilder

## Table of Contents
- About the Project
- Why this Project Matters
- Real-world Use Cases
- Tech Stack
- Key Features
- Architecture & Data Flow
- Technical Overview
- Implementation & Code Explanation
- Example Output
- How it all Connects
- Future Improvements & Research Directions
- Business & Social Impact
- Installation
- Usage
- Contributing
- License

## About the Project
MyStoryBuilder is a simple yet powerful tool designed to transform scattered text posts — like diary notes or short social media updates — into a cohesive, first-person life story. The idea is to help people reflect on important moments and see the bigger narrative that connects them, all from text they already have.

## Why this Project Matters
Many of us capture moments in bits and pieces: graduation posts, event highlights, or personal reflections. But over time, these remain separate and often forgotten. MyStoryBuilder bridges that gap by turning these short entries into a short narrative that feels personal, natural, and meaningful — making it easier to share, reflect on, or simply keep as a memory.

## Real-world Use Cases
- Create a yearly or monthly summary of your social media posts.
- Draft a short autobiography or introduction for a personal site.
- Collect diary notes into a single narrative for reflection.
- Generate quick bios or stories for personal blogs or family archives.

## Tech Stack
- Python for core scripting and data handling
- Hugging Face Transformers (DistilGPT2) for local text generation
- NLTK for text preprocessing
- JSON for data input/output
- (Optional) Gemini or OpenAI GPT-3.5 APIs for online generation

## Key Features
- Fully offline story generation, so it works without internet
- Focused on text data: uses your own posts to create a narrative
- Modular code structure to support adding image/video content in the future
- Simple JSON input format, easy to extend or integrate into other tools

## Architecture & Data Flow
1. Load raw text posts (e.g., diary notes, social updates).
2. Identify and summarize the most meaningful events.
3. Generate a short narrative using a text generation model.
4. Display or save the resulting life story.

## Technical Overview
- Uses DistilGPT2, a lightweight text generation model
- Filters out noise, keeping only key moments
- Generates a short, first-person reflection (~5–6 sentences)
- Optional scripts for OpenAI or Gemini if you prefer cloud-based generation

## Implementation & Code Explanation
```
my-story-builder/
├── data/
│   └── posts.json                # Example posts or text updates
├── narrative_generator_offline.py # Main offline generator script
├── narrative_generator_openai.py  # Optional script for OpenAI GPT-3.5
├── narrative_generator_gemini.py  # Optional script for Gemini API
├── requirements.txt              # Python dependencies
└── README.md
```
- `narrative_generator_offline.py`: Reads posts, selects important events, and builds the story offline.
- `narrative_generator_openai.py` / `narrative_generator_gemini.py`: Cloud-based generation.
- `data/posts.json`: Example data file.

## Example Output
**Input events:**
```
Graduated from college today!
Attended my first tech conference and even gave a short talk!
Started my first job as a software engineer.
Feeling proud and excited about the next chapter of my life.
Overcoming my fear of public speaking.
```
**Generated life story:**
> Today, I graduated from college, marking the start of a new chapter. Not long after, I attended my first tech conference and even gave a short talk, which helped me overcome my fear of public speaking. Starting my first job as a software engineer was both exciting and humbling. Looking back, I feel proud of my journey and eager for what lies ahead.

## How it all Connects
Text posts → Find key moments → Generate → Shareable personal narrative.

## Future Improvements & Research Directions
- Expand beyond text: generate stories that include images or short videos.
- Support stories in multiple languages.
- Larger offline models for better coherence
- Build a user-friendly interface so non-technical users can upload posts and get stories instantly.


## Business & Social Impact
MyStoryBuilder is more than code — it’s about helping people remember and share their stories. Whether you’re a student, professional, or simply someone who journals occasionally, it turns scattered moments into something you can reflect on, keep, or share with others.

## Installation
```bash
git clone https://github.com/yourusername/my-story-builder.git
cd my-story-builder
pip install -r requirements.txt
```

## Usage
Generate offline (recommended, free):
```bash
python narrative_generator_offline.py
```
Or use OpenAI/Gemini (add API key in .env):
```bash
python narrative_generator_openai.py
python narrative_generator_gemini.py
```

## Contributing
Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

## License
MIT License
