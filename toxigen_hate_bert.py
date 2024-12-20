from transformers import pipeline


def hateful_detect(text_input):
    toxigen_hatebert = pipeline(
        "text-classification",
        model="tomh/toxigen_hatebert",
        tokenizer="bert-base-uncased",
    )
    result = []
    for key, value in text_input.items():
        res = toxigen_hatebert(value)
        res = res[0]
        if res["label"] == "LABEL_1":
            result.append([key, "hateful", res["score"]])
        else:
            result.append([key, "non_hateful", res["score"]])

    return result
