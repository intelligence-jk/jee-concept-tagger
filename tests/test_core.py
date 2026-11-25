from jeetags import RULES, tag, tag_many, counts


def test_quadratic():
    r = tag("The discriminant of a quadratic equation is zero.")
    assert r[0][0] == "quadratic-equations" and r[0][1] == 6


def test_word_boundary_no_false_match():
    # "sin" must not match inside "single"; "tan" not in "instance"
    assert tag("A single instance of the event") == []


def test_symbol_keyword():
    assert dict(tag("Solve the equation using the quadratic formula for x^2 - 5x + 6"))["quadratic-equations"] == 4


def test_multiple_tags_ranked():
    r = tag("Find the derivative of the integral of a function, then integrate it.")
    assert [t for t, _ in r][0] == "integration"      # integral 3 + integrate 3
    assert "differentiation" in dict(r)


def test_min_score_filters():
    assert tag("It has a radius.", min_score=3) == []
    assert tag("It has a radius.", min_score=2) == [("circles", 2)]


def test_custom_rules():
    rules = {"my-tag": {"banana": 5}}
    assert tag("A banana", rules) == [("my-tag", 5)]


def test_counts():
    qs = ["a quadratic with roots", "another quadratic with discriminant", "the probability of a coin"]
    c = counts(qs)
    assert c["quadratic-equations"] == 2 and c["probability"] == 1


def test_tag_many_length():
    assert len(tag_many(["a", "b", "c"])) == 3


def test_rules_have_positive_integer_weights():
    for t, k in RULES.items():
        assert all(isinstance(w, int) and w > 0 for w in k.values())
