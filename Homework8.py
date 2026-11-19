## Student Practice: Complete Pattern

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
        # initialize a file variable to None so it can be safely closed in the finally block at the end
        file = None
        try:
            # TODO: Open file
            # open the file for reading use the 'r' read mode
            file = open(filename, "r")
            # if the file opens print the success message
            print(f"Opened file '{filename}' successfully.")
        except FileNotFoundError as e :
            # TODO: Handle missing file
            print(f"File '{filename}' not found: {e}")
            return None
        except PermissionError as e:
            # TODO: Handle permission issues
            print(f"Permission denied for file '{filename}': {e}")
            return None
        else:
            # TODO: Process file content (only if opened successfully)
            content = file.read()
            print(f"Content read successfully: {len(content)} characters")
            return content
        finally:
            # TODO: Ensure file is closed
            if file:
                file.close()
                print(f"Closed file '{filename}'.")

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
            if self.name == "Database":
                self.resource = f"Connection to {self.name}"
                print(f"Acquired {self.name} resource: {self.resource}")
            else:
                raise RuntimeError(f"Failed to acquire {self.name}")

        def release(self):
            """Release resource - must always happen."""
            # TODO: Implement cleanup
            if self.resource:
                print(f"Released {self.name} resource: {self.resource}")
                self.resource = None

        def use(self):
            """Use resource - only if acquired."""
            # TODO: Implement usage
            if self.resource:
                print(f"Using {self.name}: {self.resource}")
                return f"Result from {self.resource}"
            else:
                return None

    # Test resource management
    rm = ResourceManager("Database")
    # TODO: Use try-except-else-finally to manage resource
    try:
        # aquire the resource
        rm.acquire()
        # if there is a runtimeerror it will be caught
    except RuntimeError as e:
        print(f"Error: {e}")
    else:
        result = rm.use()
        print(f"Operation result: {result}")
    finally:
        rm.release()

# Run the practice
practice_3_complete_pattern()


# practice 2 custom exceptions
# This essentially wants from me to make custom exceptions for a tic-tac-toe game


def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 5: Custom Exceptions")
    print("="*50)

    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass
    # invalid move error
    # an invalid move should be raised when a position is occupied or it goes out of bounds
    # to make invalid moves real wed need to make those no no rules a variable so we call them reason
    class InvalidMoveError(GameError):
        """Invalid game move."""
        # make a class that takes position and reason for the invalid move
        def __init__(self, position, reason):
            # store the position and reason for the invalid move
            self.position = position
            self.reason = reason
            # call the class if an invalid move is determind
            super().__init__(f"Invalid move at {position}: {reason}")

    # new class game over error
    # to be completely honest why does this need to be an error i hardly know how to apply this
    # if the winner wins the game should just end right
    # oh wait its the flag that ends it the word error confused me i thought it was trying to catch moves after the game is over
    class GameOverError(GameError):
        """Game has ended."""
        # make a class that represents the game being over and stores the winner
        # if its a tie we can set the winner to None then
        def __init__(self, winner):
            # store the winner of the game
            self.winner = winner
            # call the class if the game is over with the winner
            super().__init__(f"Game over. Winner: {winner}")


    # TODO 2: Use custom exceptions
    # make the game now
    # make it as a class
    class TicTacToe:
        # make a board as a class it dosen't need peramaters in the init
        def __init__(self):
            # initialize the board as a 3x3 grid of empty spaces
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            # set the current player to 'X'
            self.current_player = 'X'
            # set the game over flag to False initially so the game is actually playable 
            self.game_over = False

        def make_move(self, row, col):
            # TODO: Raise GameOverError if game_over is True
            # TODO: Raise InvalidMoveError if position is taken
            # TODO: Raise InvalidMoveError if position is out of bounds
            print("Making move at", row, col)
            if self.game_over:
                raise GameOverError(self.current_player)
            if not (0 <= row < 3 and 0 <= col < 3):
                raise InvalidMoveError((row, col), "Out of bounds")
            if self.board[row][col] != ' ':
                raise InvalidMoveError((row, col), "Position already taken")
            self.board[row][col] = self.current_player
            # switch player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            # check for a winner or tie
            winner = self.check_winner()
            if winner or self.is_tie():
                self.game_over = True
                raise GameOverError(winner)

    # Test the game
    game = TicTacToe()

    test_moves = [
        (0, 0),  # Valid
        (0, 0),  # Already taken
        (5, 5),  # Out of bounds
    ]

    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"✅ Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"❌ Invalid move: {e}")
        except GameOverError as e:
            print(f"🏁 Game over: {e}")

# Run the practice
practice_2_custom_exceptions()



def practice_3_complete_system():
    """
    Build a complete error handling system
    """
    print("\n" + "="*50)
    print("EXERCISE 6: Complete Error Handler")
    print("="*50)

    # TODO: Build a file processing system with proper error handling

    class FileProcessor:
        def __init__(self):
            self.processed_files = []
            self.failed_files = []

        def process_file(self, filename):
            """
            Process a single file with complete error handling.
            """
            # TODO: Implement with try-except-else-finally
            # TODO: Handle FileNotFoundError
            # TODO: Handle PermissionError
            # TODO: Handle general exceptions
            # TODO: Ensure file is closed
            pass

        def process_directory(self, directory):
            """
            Process all files in directory, collecting errors.
            """
            # TODO: Process each file
            # TODO: Continue on errors
            # TODO: Track successes and failures
            pass

        def get_report(self):
            """
            Get processing report.
            """
            # TODO: Return summary of processing
            pass

    # Test the processor
    processor = FileProcessor()

    test_files = [
        "valid.txt",
        "missing.txt",
        "/root/restricted.txt"
    ]

    for filename in test_files:
        processor.process_file(filename)

    report = processor.get_report()
    print(f"Report: {report}")

# Run the practice
practice_3_complete_system()
```

