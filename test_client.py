import requests, time
import pandas as pd

df = pd.read_csv('dataset/labeled_tickets_with_priority.csv')

for _, row in df.sample(20).iterrows():
    resp = requests.post('http://127.0.0.1:8000/process-ticket', json={'text': row['text_clean']})
    print(resp.json())
    time.sleep(5)