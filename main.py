"""
News Image Daily - 17 November 2026 Entrypoint.
Copies the authored world news synthesis infographic to the designated output path.
Includes verification of image presence, size constraints, and destination readiness.
"""

import os
import shutil
import sys
from pathlib import Path


def copy_entry_image() -> None:
    """Locate entry.png in the repository and copy it to the grader output directory."""
    current_dir = Path(__file__).resolve().parent
    source_path = current_dir / "entry.png"

    if not source_path.exists():
        print(f"Error: Missing source news graphic at {source_path}", file=sys.stderr)
        sys.exit(1)

    # Verify graphic file size conforms to <= 1 MiB limit
    file_size = source_path.stat().st_size
    max_size = 1024 * 1024  # 1 MiB
    if file_size > max_size:
        print(f"Error: Image size ({file_size} bytes) exceeds 1 MiB limit", file=sys.stderr)
        sys.exit(1)

    # Determine destination directory from environment variable or default to /output
    out_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_dir = Path(out_dir_env)
    out_dir.mkdir(parents=True, exist_ok=True)

    dest_path = out_dir / "entry.png"
    shutil.copyfile(source_path, dest_path)
    print(f"Successfully staged news graphic ({file_size} bytes) to: {dest_path}")


if __name__ == "__main__":
    copy_entry_image()

