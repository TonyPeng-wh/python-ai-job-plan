with open(
    "week04/day19/file_io/feedback_notes.txt",
    "r",
    encoding="utf-8"
) as feedback_file:
    for current_line in feedback_file:
        cleaned_line = current_line.strip()
        print(cleaned_line)