# CSV null is not empty text: a small reproducible Python case

**A small, AI-assisted reference example, not a CSV repair product or a compatibility guarantee.** See NOTICE.md and LICENSES.md.

For developers exchanging nullable text through CSV, the question is not merely whether a file parses. It is whether the receiver still distinguishes a missing value from an empty string.

## Direct answer
For the provided fixture, an agreed Python 3.13.5 `csv.QUOTE_NOTNULL` writer/reader pair preserves that distinction. An unquoted empty field represents `None`; quoted empty text represents `""`. Ordinary CSV readers need not retain this convention.

A `QUOTE_NOTNULL` constant alone is not enough: Python's 3.12 documentation records a reader bug fixed in 3.13. That version statement is documentation evidence, not a 3.12 execution in this package. The stored observation is 3.13.5 only.

## Try the synthetic fixture locally
Run `python example.py` from this directory using your own permitted environment. It reads only the bundled example.csv and expected.json and prints the result. It installs nothing, opens no listener, uploads nothing and does not accept customer files. A successful run says only that this fixture behaved as described in that runtime.

The first two data-row values must be JSON `null` and `""` in the printed `standard_reader_rows`, rather than two empty strings. The ordinary-reader control deliberately shows the difference. The sample also retains literal `NA`, literal `__NULL__`, and a Korean string containing a comma and newline.

## Application boundary
Use this as a testable recipe only when you control or can verify both endpoints. If the receiving program cannot express this convention, first agree another representation and test that receiver. Do not silently change the receiving contract. If missing and empty were already written identically, this file alone does not identify the original values.

This is NOT a pandas `DataFrame.to_csv` / `read_csv` compatibility result. Preprocessing and reader policy matter; an option name carried through another library is not a product test. No n8n, Excel, database, pandas or remote service was tested in this sample. No timing, cost or market advantage is claimed.

## Existing alternatives
Python's built-in documentation is the primary baseline. Existing metadata systems such as TDDA Serial and Frictionless may already meet your workflow requirements. This sample is not a new format, parser, metadata standard or proof that those alternatives fail.

## Evidence for people and software
`evidence.json` gives the same question, conditions, observed runtime and nonclaims in structured form. The associated archived observations are same-author synthetic checks, not third-party validation. `sources.json` links to official documentation; webpage bodies and forum users' data are not redistributed.

Sharing feedback is optional and is not required to use the example. Report only a synthetic reproduction and minimum runtime/settings after deciding you have permission. Do not submit production files, private values, URLs, credentials or their hashes. No automatic collection is included.

## Reuse and support
See LICENSES.md for the separate code and authored-content terms. Upstream documents remain under their own terms. This example has no hosted service or promised response-time support. Feedback through this repository is optional; read FEEDBACK_GUIDE.md before posting and use only the bundled synthetic fixture.
