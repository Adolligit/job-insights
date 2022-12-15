from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "job") == 3454
    assert count_ocurrences("data/jobs.csv", "New York") == 597
    assert count_ocurrences("data/jobs.csv", "369") == 10