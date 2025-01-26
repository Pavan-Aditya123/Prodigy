from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

def generate_response(prompt, max_length=600, temperature=0.7, top_k=50, top_p=0.9, repetition_penalty=1.2):
    """
    Generates a more focused and coherent response based on the user's prompt using GPT-2 Large model.

    Args:
        prompt (str): The input text prompt.
        max_length (int): Maximum length of the generated text (default 350 tokens).
        temperature (float): Sampling temperature; lower values make the output more deterministic.
        top_k (int): Top-K sampling; restricts sampling to the top k tokens.
        top_p (float): Top-p (nucleus) sampling; restricts sampling to the smallest set of tokens with a cumulative probability > top_p.
        repetition_penalty (float): Penalty for repeated tokens (to discourage repetitive output).

    Returns:
        str: The generated response.
    """
    # Load the tokenizer and the GPT-2 large model
    model_name = 'gpt2-large'
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    
    # Tokenize the input prompt
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Create attention mask (1 for real tokens, 0 for padding tokens)
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
    
    # Generate text using the model
    output = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_length=max_length,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        eos_token_id=tokenizer.eos_token_id
    )
    
    # Decode and return the generated text
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Main function to interact with the user
if __name__ == "__main__":
    print("Welcome to the GPT-2 Large Response Generator!")
    
    # User input for the prompt
    prompt = input("Enter your prompt: ")

    # Generate the response using gpt2-large model
    response = generate_response(prompt, max_length=350)
    print("\nGenerated Response:")
    print(response)
