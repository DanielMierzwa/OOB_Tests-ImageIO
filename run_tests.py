import pytest
from scripts.report_generator import generate_report

def run_tests():
    exit_code = pytest.main()
    print(f"Tests finished with exit code: {exit_code}")

    return exit_code

if __name__ == "__main__":
    run_tests()
    generate_report("results.xml", "coverage.xml", "raport.md")
