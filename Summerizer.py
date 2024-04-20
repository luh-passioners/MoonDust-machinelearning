import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="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",
) 

def summerizer(Article):
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        temperature=0,
        system="please summarize this text as much as possible using bullet points without introducing bias. Format into just the bulletpoints. \n\n",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": Article
                    }
                ]
            }
        ]
    )
    print(message.content)
    return str(message.content)