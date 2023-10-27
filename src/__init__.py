from pathlib import Path
import os

path = os.path.dirname(os.path.abspath("__file__"))
ROOT_DIR = Path(Path(path).resolve())

RAW_DATA_DIR = ROOT_DIR / "data/raw"
PROCESSED_DATA_DIR = ROOT_DIR / "data/processed"
TEST_DATA_DIR = ROOT_DIR / "data/test"
MODELS_DIR = ROOT_DIR / "models"
METRICS_DIR = ROOT_DIR / "metrics"