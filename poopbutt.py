def practice_2_exception_hierarchy():
    """
    Practice with exception hierarchy
    """
    print("\n" + "="*50)
    print("EXERCISE 2: Exception Hierarchy")
    print("="*50)

    # TODO 1: Catch multiple related exceptions efficiently
    def access_data(data_structure, key):
        """
        Access data[key] whether data is list or dict.
        Return None if key doesn't exist.
        """
        try:
            return data_structure[key]
        except LookupError:
            return None

    # Test with different data structures
    test_list = [10, 20, 30]
    test_dict = {"a": 1, "b": 2}

    print(f"List[1]: {access_data(test_list, 1)}")
    print(f"List[10]: {access_data(test_list, 10)}")
    print(f"Dict['a']: {access_data(test_dict, 'a')}")
    print(f"Dict['z']: {access_data(test_dict, 'z')}")

    # TODO 2: Order exception handlers correctly
    def parse_value(value):
        """
        Try to parse value as int, then float, then return as string.
        """
        # TODO: Fix the order of exception handler
        try:
            return int(value)
        except ValueError: # Add specific exceptions in correct order
            pass

        return str(value)

    # Test parsing
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = parse_value(val)
        print(f"Parsing '{val}': {result} (type: {type(result).__name__})")

# Run the practice
practice_2_exception_hierarchy()





def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "="*50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("="*50)

    # TODO 1: File processor with complete error handling
    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """
        file = None
        try:
            # TODO: Open file
            print(f"opening the file: {filename}")
            file = open(filename, "r")
            print(f"file opened successfully: {filename}")
            
        except FileNotFoundError:
            # TODO: Handle missing file
            if file:
                file.close()
            print(f"File not found: {filename}")
            
        except PermissionError:
            # TODO: Handle permission issues
            if file:
                file.close()
            print(f"Permission error: {filename}")
        else:
            # TODO: Process file content (only if opened successfully)
            if file:
                openend_file = file.read()
                print(f"processing the file: {filename}")
                return openend_file
            
        finally:
            # TODO: Ensure file is closed
            if file:
                file.close()
            print(f"closing the file: {filename}")

    # Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/file"]
    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    # TODO 2: Resource manager
    class ResourceManager:
        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self):
            """Acquire resource - might fail."""
            # TODO: Implement with possible RuntimeError
            if self.resource is None:
                raise RuntimeError("Not connected to database")
            pass

        def release(self):
            """Release resource - must always happen."""
            # TODO: Implement cleanup
            
            pass

        def use(self):
            """Use resource - only if acquired."""
            # TODO: Implement usage
            pass

    # Test resource management
    rm = ResourceManager("Database")
    # TODO: Use try-except-else-finally to manage resource

# Run the practice
practice_3_complete_pattern()