import random


def generate_random_number(min_val, max_val):
    """
    Generate a random integer within the range [min_val, max_val].

    Args:
        min_val (int): The minimum possible value.
        max_val (int): The maximum possible value.

    Returns:
        int: A random integer between min_val and max_val.
    """
    return random.randint(min_val, max_val)


def choose_random_operator():
    """
    Choose a random mathematical operator (+, -, *).

    Returns:
        str: A random operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])


def create_math_problem(n1, n2, operator):
    """
    Create a math problem string and calculate its solution.

    Args:
        n1 (int): The 1st number in the problem.
        n2 (int): The 2nd number in the problem.
        operator (str): The mathematical operator ('+', '-', '*').

    Returns:
        tuple: A tuple containing the problem as a string and the correct answer.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+':
        solution = n1 + n2
    elif operator == '-':
        solution = n1 - n2
    elif operator == '*':
        solution = n1 * n2
    else:
        raise ValueError("Invalid operator provided.")
    return problem, solution


def math_quiz_game():
    """
    Run a simple math quiz game where the user answers math problems.

    The user is presented with a series of randomly generated math problems.
    Points are awarded for each correct answer.
    """
    score = 0
    total_questions = 5  # Total number of quiz questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    print(f"You will answer {total_questions} questions. Let's begin!\n")

    for question_number in range(1, total_questions + 1):
        # Generate problem
        n1 = generate_random_number(1, 10)
        n2 = generate_random_number(1, 5)
        operator = choose_random_operator()

        # Create math problem and calculate the solution
        problem, solution = create_math_problem(n1, n2, operator)

        # Display the question to the user
        print(f"Question {question_number}: {problem}")

        # Handle user input with error checking
        try:
            user_input = input("Your answer: ").strip()
            user_answer = int(user_input)  # Validate user input
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")
            continue  # Skip this question and move to the next

        # Check the user's answer
        if user_answer == solution:
            print("Correct! You earned a point.\n")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {solution}.\n")

    # Display final score
    print(f"Game over! Your score is: {score}/{total_questions}")
    print("Thank you for playing!")


if name == "main":
    math_quiz_game()
