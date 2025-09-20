import os

from kaggle.api.kaggle_api_extended import KaggleApi

# STEP 1: Define the custom folder path

custom_kaggle_dir = r"C:\Personal Project\DogBreedPrediction"

kaggle_json_path = os.path.join(custom_kaggle_dir, "kaggle.json")

# STEP 2: Create the folder if it doesn't exist

if not os.path.exists(custom_kaggle_dir):

    os.makedirs(custom_kaggle_dir)

    print(f"📁 Created folder: {custom_kaggle_dir}")

else:

    print(f"📁 Folder already exists: {custom_kaggle_dir}")

# STEP 3: Check if kaggle.json exists

if not os.path.isfile(kaggle_json_path):

    print(f"❌ kaggle.json not found at: {kaggle_json_path}")

    print("👉 Please download it from your Kaggle account and place it here.")

    exit()

else:

    print(f"✅ Found kaggle.json at: {kaggle_json_path}")

# STEP 4: Set environment variable to point to the custom folder

os.environ["KAGGLE_CONFIG_DIR"] = custom_kaggle_dir

print(f"🔧 Environment variable KAGGLE_CONFIG_DIR set to: {custom_kaggle_dir}")

# STEP 5: Authenticate with Kaggle API

api = KaggleApi()

try:

    api.authenticate()

    print("✅ Kaggle API authenticated successfully.")

except Exception as e:

    print("❌ Authentication failed:", e)

    exit()

# STEP 6: List datasets (search example: "dog")

try:

    datasets = api.dataset_list(search="dog", max_size=5)

    print("📦 Available Datasets:")

    for dataset in datasets:

        print("-", dataset.title)

except Exception as e:

    print("❌ Failed to list datasets:", e)
 