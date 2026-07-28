import torch
import logging
from transformers import AutoTokenizer, AutoModelForCausalLM

from config import (
    MODEL_NAME,
    MAX_NEW_TOKENS,
    TEMPERATURE,
    TOP_P,
    REPETITION_PENALTY
)

from prompts import CHATBOT_PROMPT
from knowledge_retriever import get_relevant_knowledge


# -------------------- Logging --------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


# -------------------- Load Model --------------------

logging.info("Loading Tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

logging.info("Loading Model...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    dtype=torch.float32
)

logging.info(f"Model '{MODEL_NAME}' loaded successfully.")


# -------------------- Conversation History --------------------

conversation_history = []


# -------------------- Generate Response --------------------

def generate_response(
    user_message,
    system_prompt=CHATBOT_PROMPT,
    max_new_tokens=MAX_NEW_TOKENS,
    temperature=TEMPERATURE,
    top_p=TOP_P,
    repetition_penalty=REPETITION_PENALTY
):
    global conversation_history

    try:

        logging.info(f"User Message: {user_message}")

        # Retrieve only relevant company knowledge
        knowledge = get_relevant_knowledge(user_message)

        logging.info(f"Retrieved Knowledge:\n{knowledge}")

        # Save current user message
        conversation_history.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        # Build conversation
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

        # Convert into chat template
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = tokenizer(
            text,
            return_tensors="pt"
        )

        # Generate response
        with torch.inference_mode():

            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                do_sample=True,
                repetition_penalty=repetition_penalty,
                eos_token_id=tokenizer.eos_token_id,
                pad_token_id=tokenizer.eos_token_id
            )

        # Decode response
        response = tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[1]:],
            skip_special_tokens=True
        )

        # Save assistant response
        conversation_history.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        # Keep only last 10 messages
        conversation_history = conversation_history[-10:]

        logging.info(f"Conversation History:\n{conversation_history}")
        logging.info(f"Assistant Response: {response}")

        return response

    except Exception as e:

        logging.error(
            f"[LLM Error] {type(e).__name__}: {e}"
        )

        return "Sorry, I'm having trouble responding right now. Please try again."