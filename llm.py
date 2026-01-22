from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "microsoft/phi-2"   # you can change to mistral or llama

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def analyze_resume(text):
    prompt = f"""
    Analyze this resume and give:
    1. Skills found
    2. Missing skills
    3. Resume improvement tips
    Resume:
    {text}
    """

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=300)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
