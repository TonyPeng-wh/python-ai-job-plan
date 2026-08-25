def check_retrieval_quality(retrieval_score):
    if retrieval_score >= 0.75:
        return "检索合格"
    else:
        return "检索不合格"
