from transformers import pipeline
def summarize_text(text)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
return summarizer(text)



