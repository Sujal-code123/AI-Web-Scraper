# parse.py (final offline version)

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load FLAN-T5 Small (only ~300MB)
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Create text2text pipeline
nlp = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def parse_with_transformers(dom_chunks, parse_description):
    results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        prompt = f"Extract the following: {parse_description}\n\nFrom this content:\n{chunk}"
        output = nlp(prompt, max_new_tokens=256)[0]["generated_text"]
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        results.append(output)

    return "\n".join(results)
