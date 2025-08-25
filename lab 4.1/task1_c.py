import re

def validate_indian_mobile(number):
    """
    Validates an Indian mobile number.
    
    Args:
        number (str): The mobile number to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    cleaned_number = re.sub(r'[\s\-\(\)]', '', str(number))
    
    if len(cleaned_number) != 10:
        return False
    
    if not cleaned_number.isdigit():
        return False
    
    if cleaned_number[0] not in ['6', '7', '8', '9']:
        return False
    
    return True

def main():
    print("=" * 30)
    
    while True:
        mobile_number = input("\nEnter a mobile number (or 'quit' to exit): ").strip()
        
        if mobile_number.lower() == 'quit':
            print("Goodbye!")
            break

        if validate_indian_mobile(mobile_number):
            print(f"✅ Valid Indian mobile number: {mobile_number}")
        else:
            print(f"❌ Invalid Indian mobile number: {mobile_number}")
            print("   Number must:")
            print("   - Have exactly 10 digits")
            print("   - Start with 6, 7, 8, or 9")
            print("   - Contain only digits")

if __name__ == "__main__":
    main()

