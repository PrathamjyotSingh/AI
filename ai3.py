import ollama

# Define the system message to introduce bias into the model's responses
system_message = "You are an assistant that provides biased answers based on a specific perspective."

# Generate a response with a prompt and the biased system message
res = ollama.chat(
    model="llama3.2",  # Using a model like llama3.2 or another Ollama-supported model
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    stream=False  # Set to False for standard responses or True for streaming
)

# Print the biased response
print(res["message"]["content"])
