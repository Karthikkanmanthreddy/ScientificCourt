import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DATA_DIR = Path("Dataset/data")


def load_jsonl(filename):
    records = []

    with open(DATA_DIR / filename, "r", encoding="utf-8") as file:
        for line in file:
            records.append(json.loads(line))

    return records


print("Loading scientific corpus...")

corpus = load_jsonl("corpus.jsonl")

print(f"Loaded {len(corpus)} scientific documents.")


# Extract document information
documents = []

for document in corpus:

    abstract = document.get("abstract", [])

    if isinstance(abstract, list):
        abstract_text = " ".join(abstract)
    else:
        abstract_text = str(abstract)

    title = document.get("title", "")

    text = title + " " + abstract_text

    documents.append({
        "doc_id": document.get("doc_id"),
        "title": title,
        "text": text
    })


# Build TF-IDF index
print("Building TF-IDF index...")

texts = [document["text"] for document in documents]

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=100000
)

document_vectors = vectorizer.fit_transform(texts)

print("Index built successfully!")


def search_evidence(query, top_k=5):

    query_vector = vectorizer.transform([query])

    scores = cosine_similarity(
        query_vector,
        document_vectors
    ).flatten()

    top_indices = scores.argsort()[::-1][:top_k]

    results = []

    for index in top_indices:

        document = documents[index]

        results.append({
            "doc_id": document["doc_id"],
            "title": document["title"],
            "score": float(scores[index]),
            "text": document["text"]
        })

    return results


if __name__ == "__main__":

    query = input("\nEnter a scientific claim: ")

    results = search_evidence(query)

    print("\n" + "=" * 60)
    print("TOP RETRIEVED EVIDENCE")
    print("=" * 60)

    for rank, result in enumerate(results, start=1):

        print(f"\nRank: {rank}")
        print(f"Document ID: {result['doc_id']}")
        print(f"Title: {result['title']}")
        print(f"Similarity Score: {result['score']:.4f}")
        print("\nAbstract/Text:")
        print(result["text"][:1000])
        print("-" * 60)