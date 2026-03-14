import pytest
from scripts.report_generator import generate_report

def run_tests():
    args = [
        "tests/",
        "--cov=imageio",
        "--cov-report=xml:coverage.xml",
        "--junitxml=results.xml"
    ]
    
    exit_code = pytest.main(args)
    
    print(f"Tests finished with exit code: {exit_code}")

if __name__ == "__main__":
    run_tests()
    generate_report("results.xml", "coverage.xml", "raport.xml")
