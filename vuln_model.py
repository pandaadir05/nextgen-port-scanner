# vuln_model.py
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_dummy_model():
    # Sample banners and labels (1 = vulnerable, 0 = not vulnerable)
    banners = [
        "Apache/2.4.41 (Ubuntu)",
        "nginx/1.18.0",
        "Microsoft-IIS/10.0",
        "OpenSSH_7.4"
    ]
    labels = [1, 0, 1, 0]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(banners)
    model = LogisticRegression()
    model.fit(X, labels)
    return vectorizer, model

if __name__ == "__main__":
    vec, clf = train_dummy_model()
    with open("model.pkl", "wb") as f:
        pickle.dump((vec, clf), f)
    print("Dummy model trained and saved as model.pkl")
