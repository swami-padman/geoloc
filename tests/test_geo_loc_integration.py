
import pytest
from click.testing import CliRunner

from geoloc.datamodels.location_info import ZipLocationInfo, CityStateLocationInfo
from geoloc.geoloc_util import cli
from geoloc.logger.log_utils import LogUtils

logger_util = LogUtils(file_name="logs/geo-loc-tests.log")
logger = logger_util.get_logger()

@pytest.fixture
def runner():
    return CliRunner()


def test_get_location_from_city_state(runner, mocker):

    mock_response = {
        'name': 'Lincoln',
        'country': 'USA',
        'state': 'IN',
        'lat': 40.6155947,
        'lon': -86.2099948
    }
    mocker.patch('geoloc.services.geoloc_services.get_geoloc_from_state_and_city', return_value=CityStateLocationInfo(**mock_response))

    # Call CLI with a city and state
    result = runner.invoke(cli, ['--locations', 'Lincoln, IN'])

    # Check the output
    assert result.exit_code == 0
    assert "City: Lincoln" in result.output
    assert "Country: US" in result.output
    assert "State: Indiana" in result.output
    assert "Latitude: 40.6155947" in result.output
    assert "Longitude: -86.2099948" in result.output


def test_get_location_from_zip(runner, mocker):
    # Mock the service call to return a predefined response
    mock_response = {
        'zip': '01801',
        'country': 'US',
        'name': 'Woburn',
        'lat': 42.4829,
        'lon': -71.1574
    }
    mocker.patch('geoloc.services.geoloc_services.get_geoloc_from_zip_code', return_value=ZipLocationInfo(**mock_response))

    # Call CLI with a zip code
    result = runner.invoke(cli, ['--locations', '01801'])

    # Check the output
    assert result.exit_code == 0
    assert "Zip: 01801" in result.output
    assert "Country: US" in result.output
    assert "State: Woburn" in result.output
    assert "Latitude: 42.4829" in result.output
    assert "Longitude: -71.1574" in result.output


def test_error_handling(runner, mocker):
    # Mock the service call to return an error
    mocker.patch('geoloc.services.geoloc_services.get_geoloc_from_state_and_city',
                 return_value={"error": "Invalid location"})

    # Call CLI with an invalid location
    result = runner.invoke(cli, ['--locations', 'Invalid Location'])

    # Check the output
    assert result.exit_code == 0
    assert "Incorrect Zip code sent Invalid Location" in result.output
