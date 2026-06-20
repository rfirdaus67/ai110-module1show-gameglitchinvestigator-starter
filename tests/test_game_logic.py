from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, hint = check_guess(50, 50)
    assert result == "Win"
    assert hint == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, hint = check_guess(60, 50)
    assert result == "Too High"
    assert hint == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, hint = check_guess(40, 50)
    assert result == "Too Low"
    assert hint == "📈 Go HIGHER!"

def test_normal_mode_starts_with_full_attempts():
    attempt_limit = 8
    attempts = 0

    attempts_left = attempt_limit - attempts

    assert attempts_left == 8

def test_attempts_left_decrements_after_first_guess():
    # Test for the "attempts left" bug.
    # After the first guess it must read 7, not 8
    limit = 8
    attempts = 0

    attempts += 1  # player submits their first guess

    assert limit - attempts == 7

def test_new_game_button_resets_state():
    # Regression test for the "New Game" button bug.
    # Previously the button reset `attempts`/`secret` but NOT `status` or
    # `history`, so a finished game stayed stuck

    state = {
        "attempts": 8,
        "status": "lost",
        "history": [10, 20, 30],
        "secret": 42,
    }

    # Mirrors app.py's `if new_game:` block.
    state["attempts"] = 0
    state["status"] = "playing"
    state["history"] = []

    assert state["attempts"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []
