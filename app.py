"""
Main Application Entry Point for RAG Wikipedia Assistant
--------------------------------------------------------

This script initializes the RAG pipeline, ensures that
the `.env_example` configuration file exists (creates it if missing),
and launches the Gemini-powered Retrieval-Augmented Generation system.
"""

import sys
import os
import logging

# ------------------------------------------------------------
# Ensure all src submodules are importable (no __init__.py needed)
# ------------------------------------------------------------
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from rag_chain.rag import start_bot


# ------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


# ------------------------------------------------------------
# Default .env_example Content
# ------------------------------------------------------------
DEFAULT_ENV_CONTENT = """# Example environment variables for RAG Wikipedia Assistant

# API key for the language model (e.g., OpenAI, Gemini)
GOOGLE_API_KEY=""

# Wikipedia topic to scrape (set dynamically in config or .env)
WIKIPEDIA_TOPIC="Artificial Intelligence"

# Optional: chunk size for text splitting
CHUNK_SIZE=500
CHUNK_OVERLAP=100
"""


# ------------------------------------------------------------
# Ensure .env_example Exists
# ------------------------------------------------------------
def ensure_env_exists():
    """
    Checks if `.env_example` file exists in the project root.
    If not, creates it with default configuration values.
    """
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    env_path = os.path.join(project_root, ".env_example")

    if not os.path.exists(env_path):
        with open(env_path, "w", encoding="utf-8") as f:
            f.write(DEFAULT_ENV_CONTENT)
        logger.info("🆕 Created default .env_example configuration file.")
    else:
        logger.info("✅ Found existing .env_example configuration file.")

    return env_path


# ------------------------------------------------------------
# Main Function
# ------------------------------------------------------------
def main():
    """
    Entry point for running the RAG Wikipedia Assistant.
    Ensures environment configuration and launches the assistant.
    """
    logger.info("🚀 Launching RAG Wikipedia Assistant...")

    try:
        env_path = ensure_env_exists()
        logger.info(f"⚙️ Using environment configuration: {env_path}")

        start_bot()
        logger.info("✅ RAG process completed successfully.")
    except KeyboardInterrupt:
        logger.warning("🛑 Process interrupted by user.")
    except Exception as e:
        logger.exception(f"❌ An unexpected error occurred: {e}")


# ------------------------------------------------------------
# Application Entry Point
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
