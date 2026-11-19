# CS1350 Computer Science II Error Handling and Exceptions

## Week 11 Session 1

**What We'll Learn Today:**

- Why exceptions are better than error codes
- Python's exception hierarchy
- How to handle errors gracefully
- Writing robust, production-ready code
- Creating custom exceptions
- Best practices for error handling

# UNIT 1: Cleanup and Context Managers

## Lecture: Automatic Resource Management

### The Problem with Manual Cleanup

```python
# Easy to forget cleanup
file = open('data.txt')
data = file.read()
# Oops! Forgot file.close()

# What if exception occurs?
file = open('data.txt')
data = file.read()
process_data(data)  # Might raise exception!
file.close()  # Never reached if exception!
```

### The with Statement Solution

```python
# Automatic cleanup with context managers
with open('data.txt') as file:
    data = file.read()
    process_data(data)
# File automatically closed, even if exception!
```

### How Context Managers Work

```python
# Context manager protocol
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self  # This becomes the 'as' variable

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        # Return False to propagate exceptions
        return False

# Using it
with MyContextManager() as manager:
    print("Inside with block")
# Automatically calls __exit__
```

### Built-in Context Managers

```python
# File operations
with open('file.txt') as f:
    content = f.read()

# Thread locks
import threading
lock = threading.Lock()
with lock:
    # Critical section
    shared_resource += 1

# Decimal precision
from decimal import localcontext
with localcontext() as ctx:
    ctx.prec = 50  # 50 digit precision
    # High precision calculations here
```

### Creating Context Managers with contextlib

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    print("Starting timer...")
    try:
        yield  # This is where the with block runs
    finally:
        elapsed = time.time() - start
        print(f"Elapsed: {elapsed:.2f} seconds")

# Using it
with timer():
    import time
    time.sleep(1)
    print("Doing work...")
```

# UNIT 2: Raising and Custom Exceptions

## Lecture: Creating Your Own Exceptions

### Raising Exceptions

```python
# Basic raise
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age cannot exceed 150")
    return age

# Re-raising exceptions
def process_data(data):
    try:
        result = risky_operation(data)
    except ValueError:
        print("Logging error...")
        raise  # Re-raise the same exception

# Raising from another exception
try:
    config = parse_config(file)
except ParseError as e:
    raise ConfigurationError("Invalid config") from e
```

### Creating Custom Exceptions

```python
# Basic custom exception
class CustomError(Exception):
    """Base class for custom exceptions."""
    pass

# With custom attributes
class ValidationError(Exception):
    def __init__(self, field, value, message):
        self.field = field
        self.value = value
        super().__init__(f"{field}: {message} (got {value})")

# Exception hierarchy for an application
class AppError(Exception):
    """Base exception for our application."""
    pass

class DatabaseError(AppError):
    """Database-related errors."""
    pass

class NetworkError(AppError):
    """Network-related errors."""
    pass

class AuthenticationError(AppError):
    """Authentication failures."""
    def __init__(self, username):
        self.username = username
        super().__init__(f"Authentication failed for {username}")
```

### When to Create Custom Exceptions

**Good reasons:**

1. Domain-specific errors (InvalidEmailError, InsufficientFundsError)
2. Different handling needed (RetryableError vs FatalError)
3. Additional context needed (error codes, details)
4. API clarity

**Bad reasons:**

1. Just to rename built-ins
2. No special handling needed
3. Standard exceptions fit perfectly

## Instructor Demo: Application Exception System

```python
# Let's build a complete exception system for an app
print("🏗️ APPLICATION EXCEPTION SYSTEM")
print("=" * 50)

# Custom exception hierarchy
class BankError(Exception):
    """Base class for banking exceptions."""
    pass

class AccountError(BankError):
    """Account-related errors."""
    pass

class InsufficientFundsError(AccountError):
    """Not enough money in account."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.shortage = amount - balance
        super().__init__(
            f"Insufficient funds: balance=${balance:.2f}, "
            f"attempted=${amount:.2f}, short by=${self.shortage:.2f}"
        )

class AccountNotFoundError(AccountError):
    """Account doesn't exist."""
    def __init__(self, account_id):
        self.account_id = account_id
        super().__init__(f"Account {account_id} not found")

class TransactionError(BankError):
    """Transaction-related errors."""
    pass

class InvalidAmountError(TransactionError):
    """Invalid transaction amount."""
    def __init__(self, amount, reason):
        self.amount = amount
        self.reason = reason
        super().__init__(f"Invalid amount ${amount}: {reason}")

# Bank account implementation
class BankAccount:
    def __init__(self, account_id, initial_balance=0):
        if initial_balance < 0:
            raise InvalidAmountError(initial_balance, "Initial balance cannot be negative")

        self.account_id = account_id
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount, "Deposit must be positive")

        self.balance += amount
        self.transaction_history.append(('deposit', amount))
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount, "Withdrawal must be positive")

        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)

        self.balance -= amount
        self.transaction_history.append(('withdraw', amount))
        return self.balance

    def transfer_to(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("Can only transfer to another BankAccount")

        try:
            self.withdraw(amount)
            other_account.deposit(amount)
            print(f"✅ Transferred ${amount:.2f}")
        except InsufficientFundsError:
            print(f"❌ Transfer failed: insufficient funds")
            raise  # Re-raise for caller to handle

# Banking system
class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, initial_balance=0):
        if account_id in self.accounts:
            raise AccountError(f"Account {account_id} already exists")

        account = BankAccount(account_id, initial_balance)
        self.accounts[account_id] = account
        return account

    def get_account(self, account_id):
        if account_id not in self.accounts:
            raise AccountNotFoundError(account_id)
        return self.accounts[account_id]

    def process_transaction(self, from_id, to_id, amount):
        """Process a transfer with complete error handling."""
        try:
            from_account = self.get_account(from_id)
            to_account = self.get_account(to_id)

            from_account.transfer_to(to_account, amount)

        except AccountNotFoundError as e:
            print(f"❌ Account error: {e}")
            return False

        except InsufficientFundsError as e:
            print(f"❌ Funds error: {e}")
            print(f"   Shortage: ${e.shortage:.2f}")
            return False

        except InvalidAmountError as e:
            print(f"❌ Amount error: {e}")
            return False

        except BankError as e:
            print(f"❌ Banking error: {e}")
            return False

        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            raise  # Re-raise unexpected errors

        else:
            print(f"✅ Transaction successful!")
            return True

# Test the system
print("\nTesting Banking System:")
print("-" * 40)

bank = BankingSystem()

# Create accounts
try:
    alice = bank.create_account("A001", 1000)
    bob = bank.create_account("B001", 500)
    print(f"Created Alice's account: ${alice.balance:.2f}")
    print(f"Created Bob's account: ${bob.balance:.2f}")
except BankError as e:
    print(f"Setup failed: {e}")

# Test transactions
print("\nTransaction Tests:")
print("-" * 40)

# Good transaction
bank.process_transaction("A001", "B001", 200)

# Insufficient funds
bank.process_transaction("B001", "A001", 1000)

# Invalid account
bank.process_transaction("A001", "C001", 100)

# Negative amount
try:
    alice.withdraw(-50)
except InvalidAmountError as e:
    print(f"❌ Caught invalid amount: {e}")

print("\nFinal Balances:")
print("-" * 40)
print(f"Alice: ${alice.balance:.2f}")
print(f"Bob: ${bob.balance:.2f}")
```

## Student Practice: Custom Exceptions

```python
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

    class InvalidMoveError(GameError):
        """Invalid game move."""
        # TODO: Add __init__ with position and reason
        pass

    class GameOverError(GameError):
        """Game has ended."""
        # TODO: Add __init__ with winner
        pass

    # TODO 2: Use custom exceptions
    class TicTacToe:
        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False

        def make_move(self, row, col):
            # TODO: Raise GameOverError if game_over is True
            # TODO: Raise InvalidMoveError if position is taken
            # TODO: Raise InvalidMoveError if position is out of bounds
            pass

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
```

# UNIT 3: Best Practices and Real-World Patterns

## Lecture: Exception Handling Best Practices

### Do's and Don'ts

**DON'T: Catch everything silently**

```python
# NEVER DO THIS!
try:
    dangerous_operation()
except:
    pass  # Silently ignoring all errors!
```

**DO: Be specific and informative**

```python
try:
    result = dangerous_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise  # Or handle appropriately
```

### Common Anti-patterns

**1. Using exceptions for flow control:**

```python
# using exception for normal flow
def find_index(lst, item):
    try:
        return lst.index(item)
    except ValueError:
        return -1  # Using exception for expected case

# check first
def find_index(lst, item):
    if item in lst:
        return lst.index(item)
    return -1
```

**2. Losing exception context:**

```python
# BAD - loses original exception
try:
    process()
except Exception as e:
    raise ValueError("Failed")  # Lost original!

# GOOD - preserve context
try:
    process()
except Exception as e:
    raise ValueError("Failed") from e  # Preserves chain
```

### EAFP vs LBYL

**EAFP (Easier to Ask Forgiveness than Permission):**

```python
# Pythonic - try first, handle errors
try:
    value = my_dict[key]
except KeyError:
    value = default_value
```

**LBYL (Look Before You Leap):**

```python
# Less Pythonic - check first
if key in my_dict:
    value = my_dict[key]
else:
    value = default_value
```

### Logging Exceptions

```python
import logging

logger = logging.getLogger(__name__)

try:
    risky_operation()
except Exception as e:
    # Log with traceback
    logger.exception("Operation failed")

    # Or log with custom level
    logger.error(f"Failed: {e}", exc_info=True)
```

```
# Best practices summary
print("\n" + "="*50)
print("BEST PRACTICES SUMMARY:")
print("="*50)

best_practices = """
1. ✅ Be specific with exception types
2. ✅ Preserve exception context with 'from'
3. ✅ Use logging for production debugging
4. ✅ Implement retry logic for transient errors
5. ✅ Use circuit breakers to prevent cascades
6. ✅ Aggregate errors when processing batches
7. ✅ Clean up resources with finally/context managers
8. ❌ Never catch all exceptions silently
9. ❌ Don't use exceptions for normal flow control
10. ❌ Avoid bare except clauses
"""

print(best_practices)
```

## Student Practice: Complete Error Handler

```python
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

## Session Summary

### What You Learned Today

1. **Exception Basics**: Why exceptions are better than error codes
2. **Exception Hierarchy**: Python's exception class structure
3. **Complete Pattern**: try-except-else-finally flow
4. **Context Managers**: Automatic resource management with 'with'
5. **Custom Exceptions**: Creating domain-specific exceptions
6. **Best Practices**: Production-ready error handling patterns

### Key Exception Handling Patterns

```python
# Complete error handling pattern
try:
    risky_operation()
except SpecificError as e:
    handle_known_error(e)
except Exception as e:
    log_unexpected_error(e)
    raise
else:
    success_action()
finally:
    cleanup_always()

# Context manager for resources
with open('file.txt') as f:
    process(f)  # Auto-closed

# Custom exceptions
class AppError(Exception):
    pass

# Retry decorator
@retry(attempts=3)
def unstable_operation():
    pass
```
