import ollama

# Provide the path to your image
image_path = "C:\\Users\\jyotp\\OneDrive\\Desktop\\AI\\WhatsApp Image 2025-01-30 at 4.48.00 PM.jpeg"


# Generate a response using the model for image description
res = ollama.generate(model="llava", prompt=f"Describe the image located at {image_path}")

# Print the response (assuming the API returns a response containing a description)
print(res["response"])
