from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = Path(Path(__file__).resolve().parent.parent)

RAW_DATA_DIR = ROOT_DIR / "data/raw"
PROCESSED_DATA_DIR = ROOT_DIR / "data/processed"
MODELS_DIR = ROOT_DIR / "models"
METRICS_DIR = ROOT_DIR / "metrics"