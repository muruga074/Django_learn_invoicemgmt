import os
from pathlib import Path
from dotenv import load_dotenv

# Get the base directory
BASE_DIR = Path(__file__).resolve().parent

# Print the directory path
print(f"Base Directory: {BASE_DIR}")

# Load the .env file
env_path = os.path.join(BASE_DIR, '.env')
print(f"Looking for .env file at: {env_path}")
print(f"File exists: {os.path.exists(env_path)}")

load_dotenv(env_path)

# Print environment variables
print("\nEnvironment Variables:")
print(f"MYSQL_ADDON_HOST: {os.getenv('MYSQL_ADDON_HOST')}")
print(f"MYSQL_ADDON_DB: {os.getenv('MYSQL_ADDON_DB')}")
print(f"MYSQL_ADDON_USER: {os.getenv('MYSQL_ADDON_USER')}")
