from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

path = os.path.dirname(os.path.abspath("__file__"))
ROOT_DIR = Path(Path(path).resolve().parent.parent)
