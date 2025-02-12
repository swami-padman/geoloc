import logging

from geoloc.geoloc_util import get_geo_loc
from geoloc.utils.common_utils import assert_and_print_values
from tests.base_test import BaseTest

logger = logging.getLogger(__name__)


class TestGeoLoc(BaseTest):

    def test_geo_loc_with_state(self):
        logger.info("Testing geoloc-util with City and State")
        rc = get_geo_loc(all_locations=["Atlanta,GA"])
        logger.debug(f"Geoloc-util {rc}")
        logger.info("Testing with state")
        logger.debug("Checking if error message is returned, it should not")
        assert "error" not in rc[0], "No error found"
        assert_and_print_values(rc[0], ["Atlanta", "US", 33.7489924, -84.3902644])

    def test_geo_loc_with_zip(self):
        logger.info("Testing geoloc-util with Zip")
        rc = get_geo_loc(all_locations=["01801"])
        logger.debug(f"Geoloc-util {rc}")
        assert_and_print_values(rc[0], ["Woburn", "US", 42.4829, -71.1574])

    def test_geo_loc_with_invalid_zip(self):
        rc = get_geo_loc(all_locations=["000"])
        assert "error" in rc[0], "Unexpected message found"

    def test_geo_loc_with_invalid_zip2(self):
        rc = get_geo_loc(all_locations=["11111"])
        assert rc[0].get(
            "error") == "Non existent data given, please check if the zip code is correct 11111", "Incorrect info found"

    def test_geo_loc_with_invalid_city(self):
        rc = get_geo_loc(all_locations=["WWWburn, MA"])
        assert rc[0].get("error") == 'Non existent data given, please check if the State and City are correct WWWburn and MA', "No error found"

    def test_geo_loc_with_invalid_state(self):
        rc = get_geo_loc(all_locations=["Boston, DD"])
        assert rc[0].get("error") == 'Non existent data given, please check if the State and City are correct Boston and DD', "No error found"

    def test_geo_loc_with_extra_spaces_city_state(self):
        rc = get_geo_loc(all_locations=["  Boston   , MA   "])
        assert_and_print_values(rc[0], ["Boston", "US", 42.3554334, -71.060511])

    def test_geo_loc_with_extra_spaces_zip(self):
        rc = get_geo_loc(all_locations=["  01810   "])
        assert_and_print_values(rc[0], ["Andover", "US", 42.6496, -71.1565])

    def test_geo_loc_with_empty_city_state(self):
        rc = get_geo_loc(all_locations=["     ,    "])
        assert rc[0].get(
            "error") == 'Incorrect City or State sent', "No error found"

    def test_geo_loc_with_empty_zip(self):
        rc = get_geo_loc(all_locations=[""])
        assert rc[0].get("error") == 'Incorrect Zip code', "No error found"

    def test_geo_loc_with_empty_zip2(self):
        rc = get_geo_loc(all_locations=["         "])
        assert rc[0].get("error") == 'Incorrect Zip code', "No error found"
