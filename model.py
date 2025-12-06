# Use a pipeline as a high-level helper

import torch
from transformers import pipeline
categories = ["Fiction","Nonfiction"]

pipe = pipeline("zero-shot-classification", model="facebook/bart-large-mnli",device=0)