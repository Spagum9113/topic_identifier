# 🧠 topic_identifier

An async Python function that uses OpenAI's GPT-4o (with optional web search) to identify the **core topic** of a Slack message in just **1–2 words**. Perfect for Slack bots, automated tagging, or routing messages to the right team.

---

## 🔧 Features

- Uses `AsyncOpenAI` for non-blocking performance
- Supports URLs in Slack messages with web search context
- Returns concise topic labels (e.g., `Dog Sitting`, `AI Scams`, `Imaginary Friends`)
- Easy to integrate into bots, pipelines, or internal tools

---

## 🚀 Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/topic_identifier.git
   cd topic_identifier
