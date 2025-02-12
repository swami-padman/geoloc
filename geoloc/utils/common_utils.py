import logging

logger = logging.getLogger(__name__)


def assert_and_print_values(actual: list, expected: list) -> None:
    logger.debug(f"Checking city name {actual.name}")
    assert actual.name in expected, "Incorrect city found"
    logger.debug(f"Checking country is {actual.country}")
    assert actual.country in expected, "Incorrect country found"
    logger.debug(f"Checking lat is {actual.lat}")
    assert actual.lat in expected, "Incorrect latitude found"
    logger.debug(f"Checking lon is {actual.lon}")
    assert actual.lon in expected, "Incorrect longitude found"
