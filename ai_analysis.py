# ai_analysis.py
import pickle
import os
from vuln_model import train_dummy_model

MODEL_PATH = "model.pkl"

def load_model():
    if not os.path.exists(MODEL_PATH):
        vec, clf = train_dummy_model()
        with open(MODEL_PATH, "wb") as f:
            pickle.dump((vec, clf), f)
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

vectorizer, model = load_model()

def analyze_banner(banner: str) -> dict:
    """
    Analyzes the service banner using the ML model.
    Returns a dictionary with the banner and vulnerability prediction.
    """
    X = vectorizer.transform([banner])
    prediction = model.predict(X)[0]
    vulnerability = "Vulnerable" if prediction == 1 else "Not Vulnerable"
    return {
        "banner": banner,
        "vulnerability": vulnerability
    }

if __name__ == "__main__":
    print(analyze_banner("Apache/2.4.41 (Ubuntu)"))
