import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model" : "deepseek-r1:1.5b",
    "prompt" : "what is an apple"
}

response = requests.post(url,json=data,stream=True)

#check response
if response.status_code == 200:
    #get the response
    print("Generated Text:",end=" ", flush=True)
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode("utf-8")
            result = json.loads(decoded_line)
            generated_text = result.get("response","")
            print(generated_text,end=" ",flush=True)

else:
    print("Error:",response.status_code, response.text)