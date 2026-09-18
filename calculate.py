import csv

WEIGHTS = {
    "C1": 25,
    "C2": 20,
    "C3": 15,
    "C4": 15,
    "C5": 10,
    "C6": 10,
    "C7": 5,
}

TIEBREAK = ["C1", "C3", "C4", "C2", "C5", "C6", "C7"]

def weighted_score(row):
    return round(sum(float(row[c]) / 5 * w for c, w in WEIGHTS.items()))

with open("SCORE_MATRIX.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    calculated = weighted_score(row)
    published = int(row["final_score"])
    if calculated != published:
        raise SystemExit(
            f'{row["participant"]}: calculated={calculated}, published={published}'
        )

ordered = sorted(
    rows,
    key=lambda r: (
        -int(r["final_score"]),
        *[-int(r[c]) for c in TIEBREAK],
        r["participant"],
    ),
)

for i, row in enumerate(ordered, 1):
    expected = int(row["rank"])
    if i != expected:
        raise SystemExit(
            f'{row["participant"]}: calculated rank={i}, published rank={expected}'
        )

print("OK: SCORE_MATRIX.csv reproduces frozen scoring and tie-break")
