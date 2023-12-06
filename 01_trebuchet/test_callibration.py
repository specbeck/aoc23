from callibration import find_callibration_values

def test_find_callibration_values():
    assert find_callibration_values("1abc2") == 12
    assert find_callibration_values("pqr3stu8vwx") == 38
    assert find_callibration_values("a1b2c3d4e5f") == 15
    assert find_callibration_values("treb7uchet") == 77
    assert find_callibration_values("two1nine") == 29
    assert find_callibration_values("eightwothree") == 83
    assert find_callibration_values("abcone2threexyz") == 13
    assert find_callibration_values("xtwone3four") == 24
    assert find_callibration_values("4nineeightseven2") == 42
    assert find_callibration_values("zoneight234") == 14
    assert find_callibration_values("7pqrstsixteen") == 76
    