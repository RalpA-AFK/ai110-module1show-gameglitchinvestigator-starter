"""Game logic helpers for the Number Guessing Game.

This module contains pure functions that are easy to test.
"""


def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """Parse user input into an int guess.

    Returns:
        (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int) -> str:
    """Compare guess to secret and return an outcome.

    Returns:
        "Win" if guess == secret
        "Too High" if guess > secret
        "Too Low" if guess < secret
    """
    # Ensure we only compare integers. This prevents unexpected logic when
    # guess/secret values are missing or of the wrong type.
    if not isinstance(guess, int) or not isinstance(secret, int):
        raise TypeError("guess and secret must be integers")

    if guess == secret:
        return "Win"
    elif guess > secret:
        return "Too High"
    else:
        return "Too Low"


def hint_message(outcome: str) -> str:
    """Return the user-facing hint message for a given outcome."""
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too High":
        return "📉 Go LOWER!"
    if outcome == "Too Low":
        return "📈 Go HIGHER!"
    return ""


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # Reward faster wins with more points, but always give at least 10 points.
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    # Each wrong guess deducts points.
    return current_score - 5
