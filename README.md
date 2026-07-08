# Intelligent Customer Case Processing System

Started this project as part of my ML internship at Stetig Consulting.

The goal is to build an AI service that can understand customer support tickets, classify them, predict their priority and later generate a draft response using Gemini. The idea is to expose everything through a FastAPI backend so it can be integrated with CRM systems.

Currently working on the ticket classification module.

## Dataset

Using the Twitter Customer Support dataset. 
Link: https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter

Right now only customer (inbound) messages are being used. Company replies and conversation thread information are ignored since they are not needed for the classification model.
