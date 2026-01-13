# FairSplit
A lightweight Streamlit app for managing group expenses with fair settlements, a “Spin the Payer” feature, and a fun Gemini-powered summary that adds humor with AI-generated nicknames—built for demos, hackathons, and learning.

---

## 🚀 Features

### Core Features
- Add participants
- Add expenses with category and payer
- Automatic per-head calculation
- Minimal settlement calculation (who pays whom)
- Category-wise spending visualization
- Export expenses as CSV

### Fun & UX Features
- 🎡 **Spin the Payer**  
  Randomly suggests who should pay next (suggestion-only, no auto-assignment)

- 🤖 **Gemini Funny Summary**  
  Uses Gemini 2.5 Flash to:
  - Invent funny nicknames for participants
  - Generate a short, playful summary of expense distribution
  - Does **not** affect calculations

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** – UI
- **SQLite** – Local database
- **Pandas** – Data handling
- **Plotly** – Visualizations
- **Google Gemini 2.5 Flash** – Narrative AI (optional, fun-only)

---

## 📁 Project Structure

