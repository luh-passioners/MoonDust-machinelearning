from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax



def analyze(text):
    # Pipeline model from huggingface transformer pipeline
    #sentiment_classifier = pipeline('sentiment-analysis')
    #result = sentiment_classifier(text)
    #print(result)
    #text = "Apple Revolutionizes Mac Line with AI-Focused M4 Chips: 🍏💻 for NASDAQ:AAPL by DEXWireNews"
    

    #Roberta model from huggingface transformer pipeline
    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)

    #encoded_text = tokenizer(text, truncation=True, return_tensors='pt', max_length=45)
   # encoded_text = tokenizer(text, return_tensors='pt', padding=True, truncation=True)

    tokenizer = AutoTokenizer.from_pretrained(MODEL)  # Use the same MODEL variable
    encoded_text = tokenizer(text, truncation=True, return_tensors='pt', max_length=512)


    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    scores_dict = {
        'roberta_neg' : scores[0],
        'roberta_neu' : scores[1],
        'roberta_pos' : scores[2]
    }
    return -scores[0] + scores[2]
    print(scores_dict)



