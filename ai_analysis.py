import pickle
import os
from vuln_model import train_dummy_model

MODEL_PATH = "model.pkl"

def load_model():
    if not os.path.exists(MODEL_PATH):
        # Train and save a dummy model if it doesn't exist
        vec, clf = train_dummy_model()
        with open(MODEL_PATH, "wb") as f:
            pickle.dump((vec, clf), f)
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

vectorizer, model = load_model()

def analyze_banner(banner: str) -> dict:
    X = vectorizer.transform([banner])
    pred = model.predict(X)[0]
    vulnerability = "Vulnerable" if pred == 1 else "Not Vulnerable"
    return {
        "banner": banner,
        "vulnerability": vulnerability
    }

if __name__ == "__main__":
    print(analyze_banner("Apache/2.4.41 (Ubuntu)"))
