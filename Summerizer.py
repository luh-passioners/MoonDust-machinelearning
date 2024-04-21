import anthropic
from keys import CLAUDE_API_KEY

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=CLAUDE_API_KEY,
) 

def summerizer(Article):
    if not Article.strip():
        return "There seems to be no text to summarize"
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
    #print(message.content)
    return str(message.content)