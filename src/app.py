"""
Main Application Entry Point for RAG Wikipedia Assistant
--------------------------------------------------------
"""

import sys
import os
import logging

# ------------------------------------------------------------
# Ensure all src submodules are importable (no __init__.py needed)
# ------------------------------------------------------------
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from rag_chain.rag import start_bot  # ✅ Works without __init__.py


# ------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


# ------------------------------------------------------------
# Main Function
# ------------------------------------------------------------
def main():
    """
    Entry point of the application.
    Initializes and runs the Gemini-powered RAG Wikipedia Assistant.
    """
    logger.info("🚀 Launching RAG Wikipedia Assistant...")

    try:
        start_bot()
        logger.info("✅ RAG process completed successfully.")
    except KeyboardInterrupt:
        logger.warning("🛑 Process interrupted by user.")
    except Exception as e:
        logger.exception(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
