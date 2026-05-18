import subprocess
import sys
import os
import json
import shutil
import stat
import glob
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

IMAGEIO_REPO_URL = "https://github.com/imageio/imageio.git"
PINNED_COMMIT = "971b83e"  # ImageIO v2.37.3
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BUILD_DIR = os.path.join(PROJECT_ROOT, ".build", "imageio-src")
BUILD_INFO_FILE = os.path.join(PROJECT_ROOT, "imageio_build_info.json")

def get_timestamp():
    try:
        build_time = datetime.now(ZoneInfo("Europe/Warsaw"))
    except ZoneInfoNotFoundError:
        build_time = datetime.now().astimezone()

    return build_time.strftime("%Y-%m-%d %H:%M %Z")

# Windows tego wymaga
def _force_remove_readonly(func, path, exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def run(cmd, cwd=None):
    print(f"  > {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(f"FATAL: command failed with exit code {result.returncode}")
    return result


def main():
    print("=" * 60)
    print("  ImageIO – Build from GitHub commit")
    print("=" * 60)
    print(f"  Repository : {IMAGEIO_REPO_URL}")
    print(f"  Commit     : {PINNED_COMMIT}")
    print(f"  Build dir  : {BUILD_DIR}")
    print()

    if os.path.exists(BUILD_DIR):
        print("[1/6] Removing previous build directory...")
        shutil.rmtree(BUILD_DIR, onexc=_force_remove_readonly)
    else:
        print("[1/6] No previous build directory found – skipping cleanup.")

    os.makedirs(BUILD_DIR, exist_ok=True)

    print("[2/6] Cloning imageio repository...")
    run(["git", "clone", "--no-checkout", IMAGEIO_REPO_URL, BUILD_DIR])

    print(f"[3/6] Checking out commit {PINNED_COMMIT}...")
    run(["git", "checkout", PINNED_COMMIT], cwd=BUILD_DIR)


    result = run(["git", "rev-parse", "HEAD"], cwd=BUILD_DIR)
    full_sha = result.stdout.strip()
    print(f"       Full SHA: {full_sha}")


    print("[4/6] Building wheel...")
    run([sys.executable, "-m", "build", "--wheel", BUILD_DIR])


    dist_dir = os.path.join(BUILD_DIR, "dist")
    wheels = glob.glob(os.path.join(dist_dir, "*.whl"))
    if not wheels:
        sys.exit("FATAL: No .whl file found after build.")
    wheel_path = wheels[0]
    wheel_name = os.path.basename(wheel_path)
    print(f"       Wheel: {wheel_name}")


    print("[5/6] Installing wheel...")
    run([sys.executable, "-m", "pip", "install", "--force-reinstall", wheel_path])


    print("       Verifying import...")
    run([sys.executable, "-c",
         "import imageio.v3; import importlib.metadata; "
         "print('  imageio location:', imageio.__file__); "
         "print('  imageio version :', importlib.metadata.version('imageio'))"])


    print("[6/6] Writing build metadata...")
    build_info = {
        "repository": IMAGEIO_REPO_URL,
        "commit_short": PINNED_COMMIT,
        "commit_full": full_sha,
        "wheel_file": wheel_name,
        "install_method": "wheel from local build",
        "build_timestamp": get_timestamp(),
    }
    with open(BUILD_INFO_FILE, "w", encoding="utf-8") as f:
        json.dump(build_info, f, indent=2)
    print(f"       Metadata saved to {BUILD_INFO_FILE}")

    print()
    print("=" * 60)
    print("  Build complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
