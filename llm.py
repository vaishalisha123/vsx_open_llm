import os
import logging

from huggingface_hub import InferenceClient

from config import (
    MODEL_NAME,
    MAX_NEW_TOKENS,
    TEMPERATURE,
    TOP_P
)

from prompts import CHATBOT_PROMPT
from knowledge_retriever import get_relevant_knowledge


# -------------------- Logging --------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


# -------------------- HF Client --------------------

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)


# -------------------- Conversation History --------------------

conversation_history = []


# -------------------- Generate Response --------------------

def generate_response(
    user_message,
    system_prompt=CHATBOT_PROMPT,
    max_new_tokens=MAX_NEW_TOKENS,
    temperature=TEMPERATURE,
    top_p=TOP_P,
):

    global conversation_history

    try:

        logging.info(f"User Message: {user_message}")

        # Retrieve company knowledge
        knowledge = get_relevant_knowledge(user_message)

        logging.info(f"Retrieved Knowledge:\n{knowledge}")

        # Save user message
        conversation_history.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        # Build messages
        messages = [
            {
                "role": "system",
                "content": f"""
{system_prompt}

COMPANY_KNOWLEDGE:

{knowledge}
"""
            }
        ]

        messages.extend(conversation_history)

        # Call Hugging Face Inference API
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            max_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
        )

        response = completion.choices[0].message.content

        # Save assistant response
        conversation_history.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        # Keep only last 10 messages
        conversation_history = conversation_history[-10:]

        logging.info(f"Assistant Response: {response}")

        return response

    except Exception as e:

        logging.error(
            f"[LLM Error] {type(e).__name__}: {e}"
        )

        return "Sorry, I'm having trouble responding right now. Please try again."