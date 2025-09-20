import kaggle

# List datasets available on Kaggle
datasets = kaggle.api.datasets_list(page_size=5)
for dataset in datasets:
    print(dataset.title)
