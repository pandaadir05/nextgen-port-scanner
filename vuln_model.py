import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_dummy_model():
    banners = [
        "Apache/2.4.41 (Ubuntu)",
        "nginx/1.18.0",
        "Microsoft-IIS/10.0",
        "OpenSSH_7.4",
    ]
    labels = [1, 0, 1, 0]  # 1 means "vulnerable", 0 means "not vulnerable"
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(banners)
    model = LogisticRegression()
    model.fit(X, labels)
    return vectorizer, model

if __name__ == "__main__":
    vectorizer, model = train_dummy_model()
    with open("model.pkl", "wb") as f:
        pickle.dump((vectorizer, model), f)
    print("Dummy model saved to model.pkl")
