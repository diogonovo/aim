# AIM – LLM Personal Trainer

**AIM** (Adaptive Interactive Mentor) is an educational AI assistant that helps users learn about any topic through a conversation-based interface.

This project is also designed as a structured way to **learn Python** while building something real and useful, with clean architecture, persistence, and LLM integration — all without requiring paid APIs.

---

## 🔍 Features

- Learn any topic by simply typing it (uses a local language model).
- Automatically creates and updates a user profile.
- Stores your learning history locally in `.json` format.
- Interactive terminal menu: learn, view or clear your history.
- Fully offline and free (no OpenAI API required).
- Modular Python structure with good practices and documentation.

---

## 🚀 How It Works

1. At launch, the user chooses a profile name (saved locally).
2. The app prompts for a topic (e.g. `"daltonism"`).
3. A small local model (e.g. `flan-t5-small`) generates a short explanation.
4. The session is logged to the user's profile file.
5. User can review or clear their history at any time.

---

## 🧠 LLM Model Used (default)

| Model | Source | Type | Notes |
|-------|--------|------|-------|
| `google/flan-t5-small` | Hugging Face | text2text | Fast and free, good for short prompts |

> You can change the model in `llm_engine.py` to `flan-t5-base` or `tiiuae/falcon-rw-1b` for better results.

---

## 📁 Project Structure

