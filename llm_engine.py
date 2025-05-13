from transformers import pipeline
import os

local_pipe = None

def set_model(model_name: str, task_type: str):
    global local_pipe
    print(f"Loading model: {model_name}")
    local_pipe = pipeline(
        task_type,
        model=model_name,
        max_new_tokens=100,
        do_sample=False
    )

def get_local_response(prompt: str) -> str:
    if local_pipe is None:
        return "[No model loaded.]"
    try:
        output = local_pipe(prompt)
        return output[0]["generated_text" if "generated_text" in output[0] else "generated_text"]
    except Exception as e:
        return f"[Error with local model: {e}]"
