# -*- coding: utf-8 -*-
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR.joinpath('data')
FIGURES_DIR = PROJECT_DIR.joinpath('reports/figures/')


# Load environment variables into the global scope with:
#
# SOME_ENV_VAR = os.getenv("SOME_ENV_VAR")
#
# And in a project file:
#
# from src.config import *

