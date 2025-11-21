"""
Reads employees.csv and finds the highest-paid employee in each department.
Also prints two formatted automated test cases showing expected vs actual output.
"""

import csv
from collections import defaultdict


def ai_choose_highest_salary(employee_list):
    """
    Select the employee with the highest salary.
    This simulates AI-assisted decision-making.
    
    Args:
        employee_list (list): List of employee dictionaries, each containing 'Name', 
                             'Department', and 'Salary' keys.
    
    Returns:
        dict: The employee dictionary with the highest salary value.
    
    Raises:
        ValueError: If the employee_list is empty.
    """
    return max(employee_list, key=lambda x: x["Salary"])


def read_employee_file(filename):
    """
    Read the CSV file and convert each row into a dictionary.
    Also convert Salary from string → float.
    
    Args:
        filename (str): Path to the CSV file containing employee data.
                       Expected columns: Name, Department, Salary
    
    Returns:
        list: List of employee dictionaries with parsed salary values (float).
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If Salary column contains non-numeric values.
    """
    employees = []
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["Salary"] = float(row["Salary"])
            employees.append(row)
    return employees


def find_highest_paid_per_department(employees):
    """
    Group employees by department, then use the AI-assisted function
    to determine the highest-paid employee in each group.
    
    Args:
        employees (list): List of employee dictionaries containing 'Name', 
                         'Department', and 'Salary' keys.
    
    Returns:
        dict: Dictionary mapping department names (str) to employee dictionaries (dict)
              of the highest-paid employee in each department.
    
    Example:
        >>> employees = [
        ...     {"Name": "Alice", "Department": "HR", "Salary": 60000},
        ...     {"Name": "Bob", "Department": "HR", "Salary": 65000}
        ... ]
        >>> result = find_highest_paid_per_department(employees)
        >>> result["HR"]["Name"]
        'Bob'
    """
    dept_groups = defaultdict(list)

    # Build department groups
    for emp in employees:
        dept_groups[emp["Department"]].append(emp)

    # Pick highest salary per department
    return {
        dept: ai_choose_highest_salary(emp_list)
        for dept, emp_list in dept_groups.items()
    }


def print_results(results):
    """
    Display final highest-paid employee per department.
    
    Formats and prints results in a human-readable table showing each department
    with its highest-paid employee and their salary.
    
    Args:
        results (dict): Dictionary mapping department names to employee dictionaries,
                       as returned by find_highest_paid_per_department().
    
    Returns:
        None: Prints results to stdout.
    """
    print("\nHighest Paid Employee Per Department")
    print("--------------------------------------")
    for dept, emp in results.items():
        print(f"{dept}: {emp['Name']} (${emp['Salary']:.2f})")


def run_printed_test_cases():
    """
    Show two formatted test cases:
    • Input data
    • Expected output
    • Actual output
    • PASS/FAIL
    
    This function demonstrates the correctness of the employee selection logic
    through two example scenarios with expected vs. actual results.
    
    Returns:
        None: Prints formatted test case results to stdout.
    """

    print("\n==============================")
    print("       TEST CASES")
    print("==============================\n")

    # -------- TEST CASE 1 --------
    # Simple test: find highest salary in a small 2-person department
    test1_input = [
        {"Name": "A", "Department": "X", "Salary": 100},
        {"Name": "B", "Department": "X", "Salary": 150}
    ]
    expected_output_1 = "B"
    actual_output_1 = ai_choose_highest_salary(test1_input)["Name"]

    print("TEST CASE 1")
    print("Input:", test1_input)
    print("Expected Output:", expected_output_1)
    print("Actual Output:", actual_output_1)
    print("STATUS:", "PASS" if actual_output_1 == expected_output_1 else "FAIL")
    print("\n----------------------------------\n")

    # -------- TEST CASE 2 --------
    # Complex test: find highest salary across multiple departments
    test2_input = [
        {"Name": "Alice", "Department": "HR", "Salary": 60000},
        {"Name": "Bob", "Department": "HR", "Salary": 65000},
        {"Name": "Eve", "Department": "IT", "Salary": 90000}
    ]
    expected_output_2 = {"HR": "Bob", "IT": "Eve"}

    result2 = find_highest_paid_per_department(test2_input)
    actual_output_2 = {dept: emp["Name"] for dept, emp in result2.items()}

    print("TEST CASE 2")
    print("Input:", test2_input)
    print("Expected Output:", expected_output_2)
    print("Actual Output:", actual_output_2)
    print("STATUS:", "PASS" if actual_output_2 == expected_output_2 else "FAIL")
    print("\n----------------------------------\n")

if __name__ == "__main__":
    # Read real CSV and display results
    employees = read_employee_file("employees.csv")
    results = find_highest_paid_per_department(employees)
    print_results(results)
