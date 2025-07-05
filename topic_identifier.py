from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio
import logging

# Set up basic logging to capture info-level messages with emojis for clarity.
logging.basicConfig(level=logging.INFO)

# Load environment variables from a .env file (e.g., your OpenAI API key).
load_dotenv()

# Retrieve the OpenAI API key from environment variables.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Create an async OpenAI client using the API key.
client = AsyncOpenAI(api_key=OPENAI_API_KEY)


async def topic_identifier(slack_message):
    """
    Identifies the core topic of a Slack message using OpenAI's GPT-4o with web search enabled.

    Args:
        slack_message (str): The content of the Slack message (may include a URL).

    Returns:
        str: The identified topic (1-2 words).
    """
    logging.info("🔍 Identifying topic for the Slack Message...")

    # Build the prompt to guide the AI:
    # - Use web search if a URL is present
    # - Output only a concise topic label (no extra explanation)
    prompt = (
        "You are an AI that can both interpret text and use the web search tool if a URL is provided.\n"
        "Given the following Slack message, identify the core topic in 1-2 words.\n"
        "If a URL is included, access the content of the link to inform your answer.\n"
        "Return ONLY the topic, with no extra explanation.\n\n"
        f"Slack message: {slack_message}"
    )

    # Call the OpenAI API asynchronously, requesting topic identification.
    completion = await client.chat.completions.create(
        model="gpt-4o-search-preview",
        web_search_options={},              # Default web search settings.
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    # Extract and clean up the model's response (should be just the topic).
    topic = completion.choices[0].message.content.strip()
    logging.info(f"✅ Identified topic: {topic}")

    return topic
