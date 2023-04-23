from transformers import pipeline

def summarize_text(event, context):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    text = event['body']
    summary = summarizer(text)
    return {
        'statusCode': 200,
        'body': summary[0]['summary_text']
    }
