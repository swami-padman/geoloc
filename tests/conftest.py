import logging

import pytest

logger = logging.getLogger(__name__)


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logstart(location) -> None:
    logger.info("---------------------------------------------------------------------------------------------------")
    logger.info(f"Starting the test: {location[2]}")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logfinish(location) -> None:
    logger.info(f"Completed the test: {location[2]}")
    logger.info("---------------------------------------------------------------------------------------------------")


@pytest.hookimpl(tryfirst=True)
def pytest_report_teststatus(report):
    if report.when == 'call':
        logger.info(f"Test Status: {report.outcome}")