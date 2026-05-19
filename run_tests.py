import pytest
from scripts.report_generator import generate_report
from scripts.build_imageio_from_commit import main as build_imageio_from_commit

def run_tests():
    exit_code = pytest.main()
    print(f"Tests finished with exit code: {exit_code}")

    return exit_code

if __name__ == "__main__":
    build_imageio_from_commit()
    run_tests()
    generate_report("results.xml", "coverage.xml", "raport.md")
