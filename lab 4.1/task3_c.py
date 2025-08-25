def extract_student_info(student_dict):
    """
    Extract student information from a nested dictionary.
    
    Args:
        student_dict (dict): A nested dictionary containing student information
        
    Returns:
        tuple: (full_name, branch, cgpa) or None if information is missing
    """
    try:
    
        first_name = student_dict.get('personal_info', {}).get('first_name', '')
        last_name = student_dict.get('personal_info', {}).get('last_name', '')
        full_name = f"{first_name} {last_name}".strip()

        branch = student_dict.get('academic_info', {}).get('branch', '')
        
        cgpa = student_dict.get('academic_info', {}).get('sgpa', '')
        
        if full_name and branch and cgpa != '':
            return full_name, branch, cgpa
        else:
            return None
            
    except Exception as e:
        print(f"Error extracting student information: {e}")
        return None

def get_student_input():
    """
    Get student information from user input.
    
    Returns:
        dict: A nested dictionary containing student information
    """
    print("\nEnter Student Information:")
    print("-" * 30)
    
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    branch = input("Enter branch: ").strip()
    sgpa = input("Enter SGPA: ").strip()

    try:
        sgpa = float(sgpa) if sgpa else 0.0
    except ValueError:
        print("Invalid SGPA format. Setting SGPA to 0.0")
        sgpa = 0.0

    student_dict = {
        "personal_info": {
            "first_name": first_name,
            "last_name": last_name
        },
        "academic_info": {
            "branch": branch,
            "sgpa": sgpa
        }
    }
    
    return student_dict

def main():
    print("Student Information Parser")
    print("=" * 50)
    
    student_data = get_student_input()
    
    result = extract_student_info(student_data)
    
    if result:
        full_name, branch, cgpa = result
        print("\nExtracted Student Information:")
        print(f"Student Information: {full_name}")
        print(f"Full Name: {full_name}")
        print(f"Branch: {branch}")
        print(f"CGPA: {cgpa}")
    else:
        print("\nCould not extract complete student information.")
        print("Please ensure all required fields (first_name, last_name, branch, sgpa) are provided.")

if __name__ == "__main__":
    main()