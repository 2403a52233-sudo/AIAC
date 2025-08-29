try:
    with open("input.txt", "r") as input_file:
        data = input_file.readlines()
    
    with open("output.txt", "w") as output_file:
        for line in data:
            output_file.write(line.upper())
    
    print("Processing done")
except FileNotFoundError:
    print("Error: Input file not found")
except Exception as e:
    print(f"An error occurred: {e}")
