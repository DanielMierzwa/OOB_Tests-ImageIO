from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from importlib.metadata import version
import xml.etree.ElementTree as ET
import os, sys, platform, socket, configparser


def get_test_results(xml_file):
    if not os.path.exists(xml_file):
        print(f"Error: Plik {xml_file} nie istnieje.")
        return None
    
    tree = ET.parse(xml_file)
    root = tree.getroot()

    total_tests = failures = errors = skipped = time = 0

    for testsuite in root.iter('testsuite'):
        total_tests += int(testsuite.attrib.get('tests', 0))
        failures += int(testsuite.attrib.get('failures', 0))
        errors += int(testsuite.attrib.get('errors', 0))
        skipped += int(testsuite.attrib.get('skipped', 0))
        time += float(testsuite.attrib.get('time', 0))

    passed = total_tests - failures - errors - skipped

    return {
        "total": total_tests,
        "passed": passed,
        "failures": failures,
        "errors": errors,
        "skipped": skipped,
        "time": time,
        "failed_tests": root.findall(".//testcase[failure]")
    }

def get_coverage_data(cov_file):
    if not os.path.exists(cov_file):
        print(f"Error: Plik {cov_file} nie istnieje.")
        return None
    
    tree = ET.parse(cov_file)
    root = tree.getroot()

    line_rate = float(root.attrib.get('line-rate', 0))
    percentage = round(line_rate * 100, 2)
    
    return {
        "line_rate": line_rate,
        "percentage": percentage
    }

def get_report_timestamp():
    try:
        report_time = datetime.now(ZoneInfo("Europe/Warsaw"))
    except ZoneInfoNotFoundError:
        report_time = datetime.now().astimezone()

    return report_time.strftime("%Y-%m-%d %H:%M %Z")

def get_hostname():
    return os.getenv("RUNNER_NAME") or socket.gethostname()

def get_dependencies(requirements_file="requirements.txt"):
    if not os.path.exists(requirements_file):
        return [f"requirements file not found: {requirements_file}"]

    dependencies = []

    with open(requirements_file, encoding="utf-8") as file:
        for line in file:
            dependency = line.strip()

            if dependency and not dependency.startswith("#"):
                dependencies.append(dependency)

    return dependencies

def get_pytest_config(pytest_ini_file="pytest.ini"):
    if not os.path.exists(pytest_ini_file):
        return {"error": f"pytest config not found: {pytest_ini_file}"}

    parser = configparser.ConfigParser()
    parser.read(pytest_ini_file, encoding="utf-8")

    if "pytest" not in parser:
        return {"error": "missing [pytest] section"}

    return {
        "testpaths": parser["pytest"].get("testpaths", "").strip(),
        "addopts": parser["pytest"].get("addopts", "").strip(),
    }


def create_header(output_file, test_results, coverage_data):
    if test_results["failures"] + test_results["errors"] == 0:
        pass_badge = ['Passed', 'success']
    else:
        pass_badge = ['Failed', 'critical']

    color = "green" if coverage_data['percentage'] > 90 else "yellow" if coverage_data['percentage'] > 75 else "red"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Wyniki testów: [ImageIO](https://pypi.org/project/ImageIO/)\n\n" + " ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)\n\n")
        f.write("**Build Status:** " + 
                f"![{pass_badge[0]}](https://img.shields.io/badge/Status-{pass_badge[0]}-{pass_badge[1]}?style=flat-square)" + 
                f" ![Coverage](https://img.shields.io/badge/Coverage-{coverage_data['percentage']}%25-{color}?style=flat-square)\n\n")
        f.write("**Metadata:** " + 
                "![PyPI version](https://img.shields.io/pypi/v/imageio?style=flat-square)" + 
                " ![Python versions](https://img.shields.io/pypi/pyversions/imageio?style=flat-square)" + 
                " ![PyPI - License](https://img.shields.io/pypi/l/imageio?style=flat-square)\n\n\n" + 
                "---\n\n")
        
def create_test_summary(output_file, test_results):
    with open(output_file, 'a') as f:
        f.write("## Summary Statistics\n\n")
        f.write("| Metric | Value |\n")
        f.write("| :--- | :--- |\n")
        f.write(f"| **Total tests** | `{test_results['total']}` |\n")
        f.write(f"| **Passed** | `{test_results['passed']}` |\n")
        f.write(f"| **Failed** | `{test_results['failures']}` |\n")
        f.write(f"| **Errors** | `{test_results['errors']}` |\n")
        f.write(f"| **Skipped** | `{test_results['skipped']}` |\n")
        f.write(f"| **Duration** | `{test_results['time']}s` |\n\n")
        f.write("---\n\n")

def create_enviroment_details(output_file):
    dependencies = get_dependencies()
    pytest_config = get_pytest_config()

    with open(output_file, 'a', encoding="utf-8") as f:
        f.write("## Test Environment Details\n\n")
        f.write(f"**Timestamp:** `{get_report_timestamp()}`\n")
        f.write(f"**Environment:** `Python {sys.version.split()[0]} | {platform.system()} {platform.release()}`\n\n")
        f.write(f"* **Host:** `{get_hostname()}`\n" + 
                f"* **Interpreter:** `CPython {sys.version.split()[0]}`\n" +
                f"* **Dependencies:**\n")
        for dependency in dependencies:
            f.write(f"  * `{dependency}`\n")
        f.write(f"* **Pytest Config:**\n")
        if "error" in pytest_config:
            f.write(f"  * `{pytest_config['error']}`\n")
        else:
            if pytest_config["testpaths"]:
                f.write(f"  * `testpaths`: `{pytest_config['testpaths']}`\n")

            if pytest_config["addopts"]:
                f.write("  * `addopts`:\n")
                for option in pytest_config["addopts"].splitlines():
                    option = option.strip()
                    if option:
                        f.write(f"    * `{option}`\n")
        f.write("\n\n---\n\n")

def create_failure_report(output_file, test_results):
    if not test_results["failed_tests"]:
        return
    
    with open(output_file, 'a') as f:
        f.write("## Failure Report\n\n")
        for testcase in test_results["failed_tests"]:

            name = testcase.attrib.get('name')
            classname = testcase.attrib.get('classname')
            failure_node = testcase.find('failure')
            failure_type = failure_node.attrib.get('type', 'No type')
            failure_traceback = failure_node.text or 'No traceback available'

            f.write(f"### `{classname}.{name}`\n")
            f.write(f"> **Failure Type:** `{failure_type}`\n>\n")
            f.write(f"> ```python\n")
            for line in failure_traceback.strip().split('\n'):
                f.write(f"> {line}\n")
            f.write("> ```\n\n---\n\n")

def create_footer(output_file):
    with open(output_file, 'a') as f:
        f.write("*Generated by: [OOB Tests - ImageIO](https://github.com/DanielMierzwa/OOB_Tests-ImageIO)*")

def generate_report(xml_file, cov_file, output_file):
    print(f"Generating report from {xml_file} and {cov_file} into {output_file}...")

    TEST_RESULTS = get_test_results(xml_file)
    COVERAGE_DATA = get_coverage_data(cov_file)

    create_header(output_file, TEST_RESULTS, COVERAGE_DATA)
    create_test_summary(output_file, TEST_RESULTS)
    create_enviroment_details(output_file)
    create_failure_report(output_file, TEST_RESULTS)
    create_footer(output_file)

    print(f"Generation finished! Report saved into {output_file}.")

if __name__ == "__main__":
    generate_report('results.xml', 'coverage.xml', 'raport.md')
