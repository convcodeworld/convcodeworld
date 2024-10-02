import dspy

AZURE_OPENAI_MODEL_LIST = ["gpt-4o", "gpt-4-turbo-2024-04-09", "gpt-4-0613", "gpt-4o-mini", "gpt-35-turbo-0613", "gpt-35-turbo-instruct-0914"]

def load_api(path: str):
    api_keys = []
    with open(path, 'r') as f:
        for line in f:
            key = line.strip()
            api_keys.append(key)
    return api_keys

def get_azure_name(model_name):
    raise NotImplementedError

def get_azure_lm(_model_name):
    raise NotImplementedError

def get_openai_lm(model_name):
    keys = load_api(".api_key")
    lm = dspy.OpenAI(model=model_name, api_key=keys[0], max_tokens=2048, stop=["\n\n---\n\n"])

    return lm
