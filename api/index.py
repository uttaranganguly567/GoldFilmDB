import os
import sys

# Add the project root directory to sys.path so 'app' and 'main' can be imported anywhere
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from main import app
