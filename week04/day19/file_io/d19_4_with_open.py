# with open(...)。
with open(
    "week04/day19/file_io/feedback_notes.txt",
    "r",
    encoding="utf-8"
) as feedback_file:     # 把 open(...) 打开的这个文件对象，临时命名为 feedback_file。“这个刚刚打开的文件，后面我就叫它 feedback_file。”
    feedback_text = feedback_file.read()
    print(feedback_text)


"""
feedback_notes.txt
↓
open()
↓
feedback_file：文件对象
↓
.read()
↓
feedback_text：str
↓
离开 with
↓
feedback_file 自动关闭
↓
feedback_text 仍然存在
"""