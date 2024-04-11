import pytest_perf
from pytest_benchmark.fixture import BenchmarkFixture


def test_something(benchmark: BenchmarkFixture) -> None:
    benchmark(lambda: pytest_perf.cases.sleep_for_two_secs())


def test_something_else(benchmark: BenchmarkFixture) -> None:
    benchmark(lambda: pytest_perf.cases.sleep_for_three_secs())


def test_not_benchmarked() -> None:
    assert True
