# SUTRA: Smart Universal Tagging of Revision Attempts

Formerly `jee-concept-tagger`.

Tags your own maths questions with concept tags, using keyword rules you can read and change.

## What it solves
When you write practice questions, you want to know which concepts each one touches and whether a set is balanced. This tool gives each question ranked tags and counts per tag across a file. It is tags only: it contains no exam questions and supplies none, and the example file has invented questions. The tag names and keywords are our own. Pure Python 3.10+, standard library only.

## Example
```bash
python -m jeetags examples/invented-questions.txt
```
```
Q1: quadratic-equations (8)
Q2: sequences-and-series (7)
Q3: complex-numbers (9)
Q4: permutations-and-combinations (4)
Q5: probability (5)
Q6: integration (6)
Q7: differentiation (4)
Q8: binomial-theorem (7)
Totals: binomial-theorem 1, complex-numbers 1, differentiation 1, integration 1, permutations-and-combinations 1, probability 1, quadratic-equations 1, sequences-and-series 1
```
(Output pasted from a real run.)

## The maths behind it
Each tag has keywords with integer weights. A question's score for a tag is the sum of the weights of the keywords it contains, each counted once, matched as whole words so that "sin" does not fire inside "single". Tags scoring at least 2 are kept and ranked by score. For "The discriminant of a quadratic equation is zero" the keywords quadratic (3) and discriminant (3) give 6. Replace the rules with your own dictionary to fit another syllabus.

## Install and run
```bash
python -m pip install -e .
python -m pytest
```

## Licence
MIT. Made by Math & Myth (mathandmyth.ae): one to one maths mentoring, online, across the UAE.
