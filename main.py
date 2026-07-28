import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
while True:
    question= input("You:")
    if question.lower()== "exit":
        break

    messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Reply briefly."
    },
    {
        "role": "user",
        "content": question
    }
    ]

    text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
    )

# Convert text to tensors
    inputs= tokenizer(text, return_tensors="pt")  

# Generate output tokens
    with torch.no_grad():
        outputs= model.generate(
    **inputs, 
    max_new_tokens=50,
    do_sample= True,
    repetition_penalty=1.2,
    temperature= 0.8,
    top_p=0.9,
    eos_token_id= tokenizer.eos_token_id,
    pad_token_id= tokenizer.eos_token_id
    )

    # Convert output tokens back to text
    response= tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    print(text)
    print("\nResponse:", response)
