import unittest
import os
import tempfile
import io
import contextlib
import importlib.util
import pprint


def load_module():
    path = os.path.join(os.path.dirname(__file__), "1.py")
    spec = importlib.util.spec_from_file_location("employee_module", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class EmployeeModuleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module()

    # Helper function to print detailed test info
    def show(self, title, inp, expected, actual):
        print("\n==============================")
        print(f" {title}")
        print("==============================")
        print("Input:")
        pprint.pprint(inp)
        print("\nExpected:")
        pprint.pprint(expected)
        print("\nActual:")
        pprint.pprint(actual)
        # Determine PASS/FAIL with flexible rules so descriptive expectations
        # (like "contains formatted salary strings") behave sensibly.
        pass_status = False
        try:
            if expected == actual:
                pass_status = True
            elif isinstance(expected, str) and isinstance(actual, str):
                lexp = expected.lower()
                if lexp.startswith("contains"):
                    # If the expectation mentions 'salary', check for formatted $ amounts
                    if "salary" in lexp:
                        import re

                        pass_status = bool(re.search(r"\$\d", actual))
                    else:
                        # Check that descriptive words appear in the actual output
                        tokens = [t for t in lexp.split()[1:] if t]
                        pass_status = all(tok in actual.lower() for tok in tokens)
                else:
                    pass_status = False
            else:
                pass_status = False
        except Exception:
            pass_status = False

        print("\nSTATUS:", "PASS" if pass_status else "FAIL")
        print("------------------------------")

    def test_ai_choose_highest_salary_basic(self):
        sample = [
            {"Name": "A", "Department": "X", "Salary": 100},
            {"Name": "B", "Department": "X", "Salary": 150},
            {"Name": "C", "Department": "X", "Salary": 120},
        ]
        best = self.mod.ai_choose_highest_salary(sample)
        expected = {"Name": "B", "Department": "X", "Salary": 150}
        self.show("TEST 1: Highest Salary Basic", sample, expected, best)
        self.assertEqual(best["Name"], "B")
        self.assertEqual(best["Salary"], 150)

    def test_ai_choose_highest_salary_empty_raises(self):
        with self.assertRaises(ValueError):
            self.mod.ai_choose_highest_salary([])

    def test_find_highest_paid_per_department_basic(self):
        sample = [
            {"Name": "Alice", "Department": "HR", "Salary": 60000},
            {"Name": "Bob", "Department": "HR", "Salary": 65000},
            {"Name": "Eve", "Department": "IT", "Salary": 90000},
        ]
        res = self.mod.find_highest_paid_per_department(sample)
        expected = {"HR": {"Name": "Bob", "Department": "HR", "Salary": 65000},
                    "IT": {"Name": "Eve", "Department": "IT", "Salary": 90000}}
        self.show("TEST 2: Highest Paid Per Dept Basic", sample, expected, res)
        self.assertEqual(res["HR"]["Name"], "Bob")
        self.assertEqual(res["IT"]["Name"], "Eve")

    def test_find_highest_paid_per_department_tie_keeps_first(self):
        sample = [
            {"Name": "First", "Department": "X", "Salary": 100},
            {"Name": "Second", "Department": "X", "Salary": 100},
        ]
        res = self.mod.find_highest_paid_per_department(sample)
        expected = {"X": {"Name": "First", "Department": "X", "Salary": 100}}
        self.show("TEST 3: Salary Tie", sample, expected, res)
        self.assertEqual(res["X"]["Name"], "First")

    def test_read_employee_file_parses_salary_float(self):
        fd, fname = tempfile.mkstemp(suffix=".csv", text=True)
        os.close(fd)
        try:
            with open(fname, "w", newline="") as f:
                f.write("Name,Department,Salary\n")
                f.write("John,Eng,12345.67\n")
            employees = self.mod.read_employee_file(fname)
            expected = [{"Name": "John", "Department": "Eng", "Salary": 12345.67}]
            self.show("TEST 4: Read Employee File", "CSV File", expected, employees)
            self.assertEqual(len(employees), 1)
            emp = employees[0]
            self.assertEqual(emp["Name"], "John")
            self.assertEqual(emp["Department"], "Eng")
            self.assertIsInstance(emp["Salary"], float)
            self.assertAlmostEqual(emp["Salary"], 12345.67)
        finally:
            try:
                os.remove(fname)
            except Exception:
                pass

    def test_print_results_output_contains_formatted_salary(self):
        results = {
            "HR": {"Name": "Bob", "Department": "HR", "Salary": 65000.0},
            "IT": {"Name": "Eve", "Department": "IT", "Salary": 90000.0},
        }
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.mod.print_results(results)
        out = buf.getvalue()
        self.show("TEST 5: Print Results", results, "contains formatted salary strings", out)
        self.assertIn("Highest Paid Employee Per Department", out)
        self.assertIn("HR: Bob ($65000.00)", out)
        self.assertIn("IT: Eve ($90000.00)", out)

    def test_run_printed_test_cases_reports_pass(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.mod.run_printed_test_cases()
        out = buf.getvalue()
        self.show("TEST 6: Printed Test Cases", "run_printed_test_cases()", "PASS", "PASS" if "STATUS: PASS" in out else "FAIL")
        self.assertIn("TEST CASE 1", out)
        self.assertIn("TEST CASE 2", out)
        self.assertIn("STATUS: PASS", out)


if __name__ == "__main__":
    unittest.main()
