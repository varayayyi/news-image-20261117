"""
News Image Daily - 17 November 2026 Entrypoint.
Copies the authored world news synthesis infographic to the designated output path.
"""

import os
import shutil
from pathlib import Path


def copy_entry_image():
    """Locate entry.png in the repository and copy it to the grader output directory."""
    current_dir = Path(__file__).resolve().parent
    source_path = current_dir / "entry.png"

    if not source_path.exists():
        raise FileNotFoundError(f"Source graphic missing: {source_path}")

    # Determine destination directory from environment variable or default to /output
    out_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_dir = Path(out_dir_env)
    out_dir.mkdir(parents=True, exist_ok=True)

    dest_path = out_dir / "entry.png"
    shutil.copyfile(source_path, dest_path)
    print(f"Successfully staged news graphic to: {dest_path}")


if __name__ == "__main__":
    copy_entry_image()
