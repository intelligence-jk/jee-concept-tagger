import sys
from .core import tag, counts


def main(argv=None):
    a = sys.argv[1:] if argv is None else argv
    if len(a) != 1:
        print("usage: python -m jeetags questions.txt   (one question per line)")
        return 2
    with open(a[0]) as f:
        qs = [ln.strip() for ln in f if ln.strip()]
    for i, q in enumerate(qs, 1):
        r = tag(q)
        print(f"Q{i}: " + (", ".join(f"{t} ({s})" for t, s in r) or "no tag"))
    print("Totals:", ", ".join(f"{t} {n}" for t, n in sorted(counts(qs).items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
