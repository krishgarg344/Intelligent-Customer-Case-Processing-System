import os
import pickle

from google import genai
from fastapi import FastAPI
from pydantic import BaseModel
from department_assignment import assign_department


# Gemini API key configuration
client = genai.Client()



# loading saved models
MODELS_DIR = 'models/saved_models'

with open(f'{MODELS_DIR}/ticket_classifier.pkl', 'rb') as f:
    ticket_clf = pickle.load(f)

with open(f'{MODELS_DIR}/tfidf_vectorizer.pkl', 'rb') as f:
    ticket_tfidf = pickle.load(f)

with open(f'{MODELS_DIR}/priority_classifier.pkl', 'rb') as f:
    priority_clf = pickle.load(f)

with open(f'{MODELS_DIR}/priority_tfidf_vectorizer.pkl', 'rb') as f:
    priority_tfidf = pickle.load(f)



# prompt generation function

def generate_draft_reply(ticket_text, category, priority):
    prompt = f"""You are a customer support agent. Write a short, polite draft
reply to the following customer ticket. Keep it under 4 sentences.

Ticket category: {category}
Priority: {priority}
Ticket: "{ticket_text}"

Draft reply:"""

    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=prompt.strip()
    )
    return response.text.strip()


#FastAPI app

app = FastAPI(title='Customer Case Processing API')


class TicketRequest(BaseModel):
    text: str


@app.post('/process-ticket')
def process_ticket(request: TicketRequest):
    text = request.text

    # category
    category_vec = ticket_tfidf.transform([text])
    category = ticket_clf.predict(category_vec)[0]

    # priority
    priority_vec = priority_tfidf.transform([text])
    priority = priority_clf.predict(priority_vec)[0]

    # department
    department = assign_department(category)

    # draft reply
    draft_reply = generate_draft_reply(text, category, priority)

    return {
        'ticket_text': text,
        'category': category,
        'priority': priority,
        'department': department,
        'draft_reply': draft_reply,
    }


# run with -> uvicorn main:app --reload


# # testing models

# if __name__ == '__main__':

#     import pandas as pd

#     # load your final dataset
#     df = pd.read_csv('dataset/labeled_tickets_with_priority.csv')
    
#     # testing on a small sample first
#     sample = df.sample(10, random_state=1)
    
#     for _, row in sample.iterrows():
#         text = row['text_clean']

#         cat_pred = ticket_clf.predict(ticket_tfidf.transform([text]))[0]
#         pri_pred = priority_clf.predict(priority_tfidf.transform([text]))[0]
#         dept = assign_department(cat_pred)

#         print('TEXT:', text[:100])
#         print('  stored category:', row['category'], '| predicted:', cat_pred)
#         print('  stored priority:', row['priority'], '| predicted:', pri_pred)
#         print('  department:', dept)
#         print()