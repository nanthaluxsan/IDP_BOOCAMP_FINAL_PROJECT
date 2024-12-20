# Use a pipeline as a high-level helper
from transformers import pipeline


text_input = {
    "01579": "mus om tiqure: ^we must haye pork-free menus or we will leave S'n Dacon america great again! ",
    "02538": "when my girl pissed me off but she. runs through the room in her draws me my dick ",
    "04583": "mom won't let me use the oven with my jewish friends ",
}

model_pipe = pipeline("text-classification", model="MilaNLProc/hate-ita-xlm-r-large")


def mila_model(text_input):

    result = []
    for key, value in text_input.items():
        result.append([key, model_pipe(value)])

    return result


print(mila_model(text_input))
