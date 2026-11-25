"""Tag your own maths questions with concept tags by keyword rules.

Tags only: this tool never stores or supplies exam questions. You bring the
questions you wrote; it says which concepts they touch. The tag names and
keywords are our own and can be replaced by passing your own RULES.
"""
import re
from collections import Counter

# tag -> {keyword or phrase: weight}
RULES = {
    "quadratic-equations": {"quadratic": 3, "roots": 2, "discriminant": 3, "x^2": 1},
    "sequences-and-series": {"arithmetic progression": 3, "geometric progression": 3, "common difference": 2,
                             "common ratio": 2, "nth term": 2, "series": 1},
    "complex-numbers": {"complex": 3, "imaginary": 3, "modulus": 1, "conjugate": 2, "argument": 1},
    "permutations-and-combinations": {"arrangements": 3, "permutation": 3, "combination": 3, "choose": 2, "ways": 1},
    "probability": {"probability": 3, "random": 1, "dice": 2, "coin": 2, "independent events": 3},
    "limits-and-continuity": {"limit": 3, "continuous": 3, "tends to": 2, "approaches": 1},
    "differentiation": {"derivative": 3, "differentiate": 3, "tangent": 1, "maximum": 1, "minimum": 1, "rate of change": 2},
    "integration": {"integral": 3, "integrate": 3, "area under": 3, "antiderivative": 3},
    "straight-lines": {"slope": 2, "gradient": 2, "line passes": 2, "perpendicular": 1, "intercept": 1},
    "circles": {"circle": 3, "radius": 2, "chord": 2, "tangent": 1, "centre": 1},
    "vectors": {"vector": 3, "dot product": 3, "cross product": 3, "unit vector": 3},
    "matrices-and-determinants": {"matrix": 3, "determinant": 3, "inverse of": 1, "transpose": 2},
    "trigonometry": {"sin": 2, "cos": 2, "tan": 2, "identity": 1, "radian": 2},
    "binomial-theorem": {"binomial": 3, "coefficient of": 2, "expansion": 2},
}


def _score(text, kws):
    t = text.lower()
    s = 0
    for k, w in kws.items():
        pat = r"(?<![a-z])" + re.escape(k) + (r"(?![a-z])" if k[-1].isalpha() else "")
        if re.search(pat, t):
            s += w
    return s


def tag(question, rules=RULES, min_score=2):
    """Ranked list of (tag, score) with score at least min_score."""
    scored = [(t, _score(question, k)) for t, k in rules.items()]
    return sorted([x for x in scored if x[1] >= min_score], key=lambda x: (-x[1], x[0]))


def tag_many(questions, rules=RULES, min_score=2):
    return [tag(q, rules, min_score) for q in questions]


def counts(questions, rules=RULES, min_score=2):
    """How many questions carry each tag (top tag only counts as primary too)."""
    c = Counter()
    for r in tag_many(questions, rules, min_score):
        for t, _ in r:
            c[t] += 1
    return c
