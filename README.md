# Intelligent Customer Case Processing System

Started this project as part of my ML internship at Stetig Consulting.

The goal is to build an AI service that can understand customer support tickets, classify them, predict their priority and later generate a draft response using Gemini. The idea is to expose everything through a FastAPI backend so it can be integrated with CRM systems.

Currently working on the ticket classification module.

## Dataset

Using the Twitter Customer Support dataset. 
Link: https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter

Right now only customer (inbound) messages are being used. Company replies and conversation thread information are ignored since they are not needed for the classification model.

## Current Progress

- Loaded and explored the dataset
- Cleaned and preprocessed customer tickets
- Removed unnecessary metadata columns
- Built TF-IDF feature extraction pipeline
- Trained Logistic Regression model for ticket classification
- Saved trained ticket classification model and TF-IDF vectorizer
- Generated ticket category labels
- Built priority prediction pipeline
- Generated priority labels for all tickets
- Saved processed dataset containing both category and priority labels for the next modules

## Project Structure

```
dataset/
models/
saved_models/
README.md
```

## Next

- Department routing
- Gemini response generation
- FastAPI backend
- API testing with Postman
- CRM integration
