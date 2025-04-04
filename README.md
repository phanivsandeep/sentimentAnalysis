# Real-time Twitter Sentiment Analysis using NLP

This project involves fine-tuning a BERT-based model for sentiment analysis of Twitter posts using real-time data streams. The model is trained using advanced techniques like Parameter-Efficient Fine-Tuning (PEFT) and Low-Rank Adaptation (LoRA).

## Introduction

In this project, we fine-tune a BERT model for the task of binary sentiment analysis. We utilize real-time Twitter data, which consists of tweets that are dynamically classified as positive or negative. We employ advanced techniques to efficiently adapt the model for this specific, fast-paced task.

Novel Techniques
----------------

### Parameter-Efficient Fine-Tuning (PEFT)

PEFT techniques aim to reduce the number of parameters that need to be fine-tuned by efficiently adapting only a subset of parameters. This approach is particularly beneficial in scenarios with limited computational resources or when deploying models that require quick updates.

### Low-Rank Adaptation (LoRA)

LoRA is a PEFT method that introduces trainable low-rank matrices to the model. These matrices are added to the original weights and are trained during the fine-tuning process. This method facilitates the efficient adaptation of the model without needing to retrain all the weights from scratch.

**LoRA Configuration:**

*   **r (rank):** 4
*   **lora_alpha:** 32
*   **lora_dropout:** 0.01
*   **target_modules:** \['q_lin'\]

The combination of PEFT and LoRA allows for effective fine-tuning of the BERT model with fewer resources and faster convergence, ideal for real-time processing.

Model Training
--------------

1.  **Data Preparation:**
    
    *   Twitter streaming API is used to collect real-time tweets.
    *   Tweets are tokenized using the BERT tokenizer.
        
2.  **Model Initialization:**
    
    *   We use the `bert-base-uncased` model for sequence classification.
    *   The model's output labels are mapped to "Positive" and "Negative".
        
3.  **Training Configuration:**
    
    *   **Learning Rate:** 1e-3
    *   **Batch Size:** 4
    *   **Number of Epochs:** 1
    *   **Evaluation Strategy:** Evaluate at the end of each epoch
    *   **Save Strategy:** Save model at the end of each epoch
        
4.  **Training:**
    
    *   The model is fine-tuned using the Trainer API from the transformers library, specifically suited for real-time updates.

## Setup

To run this project, you need to install the following Python packages:

```bash
pip install tweepy datasets evaluate transformers[sentencepiece]
pip install accelerate -U
pip install peft