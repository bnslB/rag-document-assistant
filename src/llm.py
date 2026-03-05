# src/llm.py
from transformers import pipeline

# Simple local text generation pipeline
llm = pipeline(
    "text-generation",
    model="tiiuae/falcon-7b-instruct",  # free HF model, smaller variant
    max_length=300
)

def query_llm(prompt):
    output = llm(prompt, do_sample=True, temperature=0.2)
    return output[0]["generated_text"]