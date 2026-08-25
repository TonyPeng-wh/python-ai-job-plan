import json
with open(
    "week05/day21/json_io/feedback_data1.json",
    "r",
    encoding="utf-8"
)as feedback_file:
    feedback_data = json.load(feedback_file)

print(feedback_data)
print(type(feedback_data))
print(type(feedback_data["feedback_id"]))
print(type(feedback_data["processed"]))
print(type(feedback_data["retrieval_score"]))
print(type(feedback_data["retry_count"]))
print(type(feedback_data["error_message"]))