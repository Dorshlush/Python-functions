from transformers import pipeline
def summarize_text(text)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
return summarizer(text)


from transformers import pipeline, set_seed

def generate_text(text)
generator = pipeline('text-generation', model='facebook/bart-large-cnn')
set_seed(42)
return generator(text)

