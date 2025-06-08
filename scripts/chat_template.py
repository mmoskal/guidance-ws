#!/usr/bin/env python3

import requests
import sys

def fetch_chat_template(model_id):
    url = f"https://huggingface.co/{model_id}/resolve/main/tokenizer_config.json"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    print(data.get("chat_template", "No chat_template found."))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <model_id>")
        sys.exit(1)
    fetch_chat_template(sys.argv[1])