"""Replay one synthetic CSV fixture. No uploads, network, or customer-file inputs.
This is an illustrative use of Python's csv module, not a general CSV repair tool.
"""
from __future__ import annotations
import csv
import hashlib
import io
import json
from pathlib import Path
import platform
import sys


def main() -> int:
    if sys.version_info < (3, 13):
        print(json.dumps({"status": "NOT_RUN_UNSUPPORTED_VERSION",
                          "reason": "This example requires Python 3.13 or later; see version caveats."}))
        return 2
    base = Path(__file__).resolve().parent
    wire = (base / "example.csv").read_bytes()
    expected = json.loads((base / "expected.json").read_text(encoding="utf-8"))
    if len(wire) > 65536:
        raise ValueError("Bundled fixture exceeds declared sample size")
    text = wire.decode("utf-8")
    rows = list(csv.reader(io.StringIO(text, newline=""),
                           quoting=csv.QUOTE_NOTNULL, strict=True))
    # This is a normal-reader negative control, not another customer's failure.
    ordinary = list(csv.reader(io.StringIO(text, newline=""), strict=True))
    generated = io.StringIO(newline="")
    csv.writer(generated, quoting=csv.QUOTE_NOTNULL,
               lineterminator="\n").writerows(expected)
    result = {
        "status": "MATCHED_FROZEN_FIXTURE" if rows == expected else "FIXTURE_MISMATCH",
        "python": platform.python_version(),
        "csv_sha256": hashlib.sha256(wire).hexdigest(),
        "standard_reader_rows": rows,
        "matches_expected": rows == expected,
        "generated_bytes_match": generated.getvalue().encode("utf-8") == wire,
        "ordinary_reader_preserves_null_empty": ordinary[1][1] is None and ordinary[2][1] == "",
        "scope": "bundled synthetic fixture only",
        "external_customer_use": False,
        "n8n_tested": False,
        "pandas_tested": False,
        "network_used": False,
        "note": "stdout only; redirect locally if needed. Nothing is sent anywhere."
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["matches_expected"] and result["generated_bytes_match"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
