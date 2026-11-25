import json
from pathlib import Path

DATA_DIR = Path("Dataset/data")


def load_jsonl(filename):
    records = []

    with open(DATA_DIR / filename, "r", encoding="utf-8") as file:
        for line in file:
            records.append(json.loads(line))

    return records


# Load datasets
train_claims = load_jsonl("claims_train.jsonl")
dev_claims = load_jsonl("claims_dev.jsonl")
test_claims = load_jsonl("claims_test.jsonl")
corpus = load_jsonl("corpus.jsonl")


# Dataset statistics
print("=" * 60)
print("SCIFACT DATASET OVERVIEW")
print("=" * 60)

print("Training claims:", len(train_claims))
print("Development claims:", len(dev_claims))
print("Test claims:", len(test_claims))
print("Scientific documents:", len(corpus))


# Inspect a claim
print("\n" + "=" * 60)
print("EXAMPLE CLAIM")
print("=" * 60)

print(json.dumps(train_claims[0], indent=2, ensure_ascii=False))


# Inspect a scientific document
print("\n" + "=" * 60)
print("EXAMPLE SCIENTIFIC DOCUMENT")
print("=" * 60)

document = corpus[0]

print("Document ID:", document.get("doc_id"))
print("Title:", document.get("title"))

abstract = document.get("abstract", [])

print("\nAbstract:")

if isinstance(abstract, list):
    for sentence in abstract[:5]:
        print("-", sentence)
else:
    print(abstract)


# Inspect available fields
print("\n" + "=" * 60)
print("DATA STRUCTURE")
print("=" * 60)

print("Claim fields:", list(train_claims[0].keys()))
print("Document fields:", list(corpus[0].keys()))