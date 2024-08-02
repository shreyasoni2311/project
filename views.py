from django.shortcuts import render

import pandas as pd

df = pd.read_csv("E:/suv_data.csv")

print(df)

import matplotlib.pyplot as plt
import seaborn as sns

def generate_histogram(df):
    plt.figure(figsize=(8, 6))
    sns.histplot(df['numeric_column'], bins=10, kde=True)
    plt.xlabel('Numeric Column')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.savefig('static/histogram.png')  # Save the plot


def home(request):
    context={}
    return render(request, "myApp/home.html",context)