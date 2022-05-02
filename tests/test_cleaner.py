import numpy as np
from strings_fuzz import cleaner

# === trim ===
def test_trim():
    test = ["   .  hello world .+ hi ++_./", " ^ go ", " does this work", "No need to trim this", "", None]
    expect = ["hello world .+ hi", "go", "does this work", "No need to trim this", "", None]
    result = [cleaner.trim(x) for x in test]
    assert np.array_equal(expect, result)

# === replace_non_breaking_space ===
def test_replace_non_breaking_space():
    test = ["\xa0This has\xa0a space", "This has no space", "", None]
    expect = [" This has a space", "This has no space", "", None]
    result = [cleaner.replace_non_breaking_space(x) for x in test]
    assert np.array_equal(expect, result)

# === replace_multiple_spaces ===
def test_replace_multiple_spaces():
    test = ["This one      has too many spaces ", "   Spaces in front", "  Spaces   everywhere   ", "", None]
    expect = ["This one has too many spaces ", " Spaces in front", " Spaces everywhere ", "", None]
    result = [cleaner.replace_multiple_spaces(x) for x in test]
    assert np.array_equal(expect, result)

# === remove_space_parenthesis ===
def test_remove_space_parenthesis():
    test = ["(   No need for space    )", "(No need to clean)", "This is (really) clean", "", None]
    expect = ["(No need for space)", "(No need to clean)", "This is (really) clean", "", None]
    result = [cleaner.remove_space_parenthesis(x) for x in test]
    assert np.array_equal(expect, result)

# === remove_meaningless ===
def test_remove_meaningless():
    test = ["7---", "...___++=", "3626three seven", "This has meaning", "This 2", "", None]
    expect = [None, None, None, "This has meaning", "This 2", "", None]
    result = [cleaner.remove_meaningless(x) for x in test]
    assert np.array_equal(expect, result)