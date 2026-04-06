from utils.ai_engine import generate_estimate

def master_estimate(text: str, prices: dict):
    return generate_estimate(text, prices)
