import json, datetime

d = json.load(open("raw.json"))["fear_and_greed"]
out = {
    "score": round(d["score"]),
    "rating": d["rating"],
    "previous_close": round(d["previous_close"], 1),
    "cnn_timestamp": d["timestamp"],
    "fetched_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
}
json.dump(out, open("fng.json", "w"), indent=2)
print(out)
