# Experiment 1: TF-IDF Evidence Retrieval Baseline

## Objective

Evaluate the initial TF-IDF-based evidence retrieval system using a manually submitted scientific claim.

## Test Claim

"Regular exercise improves cognitive performance and memory."

## Method

The system indexed 5,183 scientific documents using TF-IDF vectorization.

Cosine similarity was used to rank the scientific documents based on their relevance to the submitted claim.

The system returned the top five documents.

## Results

| Rank | Document ID | Similarity Score |
|---|---|---:|
| 1 | 3202143 | 0.3192 |
| 2 | 8604837 | 0.2729 |
| 3 | 32322418 | 0.2688 |
| 4 | 2424794 | 0.2357 |
| 5 | 21320417 | 0.2327 |

## Initial Observations

The retrieval system successfully returned documents containing related scientific terminology.

However, the results demonstrated limitations in lexical retrieval.

Some documents were related to the general topic of memory or exercise but were not directly relevant to the complete scientific claim.

For example, the document concerning T-cell memory was retrieved despite the claim referring to cognitive memory.

The results also showed that a document discussing exercise and the immune system may be retrieved even though it does not directly address cognitive performance.

## Limitations

- TF-IDF primarily relies on lexical similarity.
- It may not fully capture semantic relationships.
- Broad scientific terms may produce irrelevant results.
- Similarity scores do not establish whether evidence supports or refutes a claim.
- Retrieval relevance requires additional evaluation.

## Conclusion

The TF-IDF system provides a functional baseline for scientific evidence retrieval.

Further development will investigate semantic retrieval and evidence-level verification to improve relevance and reliability.