import time
import os
import logging
import traceback
from company_context import COMPANY_CONTEXT
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
load_dotenv()

from config import (
    MODEL_NAME,
    MAX_NEW_TOKENS,
    TEMPERATURE,
    TOP_P
)

from prompts import CHATBOT_PROMPT
from vsx_knowledge import get_static_response

# -------------------- Logging --------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


# -------------------- HF Client --------------------

client = InferenceClient(
    model=MODEL_NAME,
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
    user_message= user_message.strip().lower()
    static_response= get_static_response(user_message)
    if static_response:
        print("Static Knowledge Hit")
        logging.info("Static response found, skipping LLM.")
        return static_response
    
    global conversation_history


    try:

        logging.info(f"User Message:{user_message}")

        
        # Save user message
        conversation_history.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        #-------------------------------
        # Build messages
        #-------------------------------
        t1= time.perf_counter()
        messages = [
    {
        "role": "system",
        "content": f"""
{system_prompt}

========================
VISIONSCALEX KNOWLEDGE
========================

{COMPANY_CONTEXT}
"""
    }
]

        messages.extend(conversation_history)
        logging.info(f"Prompt Building: {(time.perf_counter()-t1)*1000:.2f}ms")

        # Call Hugging Face Inference API
        t2 = time.perf_counter()
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            max_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
        )
        logging.info(
            f"LLM Inference: {(time.perf_counter()-t2)*1000:.2f} ms"
        )

        response = completion.choices[0].message.content

        # Save assistant response

        t3 = time.perf_counter()
        conversation_history.append(
            {
                "role": "assistant",
                "content": response 
            }
        )

        # Keep only last 10 messages
        conversation_history = conversation_history[-10:]
        logging.info(
            f"Response Processing: {(time.perf_counter()-t3)*1000:.2f} ms"
        )

        logging.info(f"Assistant Response: {response}")

        return response

    except Exception as e:

        logging.error(
            f"[LLM Error] {type(e).__name__}: {e}"
        )
        logging.exception("LLM Error")

        traceback.print_exc()


        return "Sorry, I'm having trouble responding right now. Please try again later."
