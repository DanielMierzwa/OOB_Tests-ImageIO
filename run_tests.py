import pytest
from scripts.report_generator import generate_report
from scripts.build_imageio_from_commit import main as build_imageio_from_commit
import argparse
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', choices=['functional', 'performance', 'all'], default='functional')
    args = parser.parse_args()
    
    cmd = ["pytest"]
    if args.type == 'functional':
        cmd.extend(["tests/functional/", "--benchmark-skip"])
    elif args.type == 'performance':
        cmd.extend(["tests/performance/", "--benchmark-only"])
    else:
        cmd.append("tests/")

    print(f"Uruchamiam: {' '.join(cmd)}")
    sys.exit(subprocess.run(cmd).returncode)

if __name__ == "__main__":
    build_imageio_from_commit()
    main()
    generate_report("results.xml", "coverage.xml", "raport.md")
