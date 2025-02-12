import logging

from geoloc.datamodels.location_info import  ZipLocationInfo, CityStateLocationInfo
from geoloc.utils.api_utils import ApiUtils

logger = logging.getLogger(__name__)


def get_geoloc_from_state_and_city(city: str, state: str) -> dict:

    if len(city) > 2 and len(state) == 2:
        logger.debug(f"Input {city} has more than 2 chars,{state} is exactly 2 chars")
        rc = ApiUtils().get_request_with_auth_token(endpoint=f"direct?q={city},{state}" + ",US", return_type=CityStateLocationInfo)
    else:
        logger.debug(f"Input {city} has less than 2 chars,{state} is not equal 2 chars")
        logger.warning(f"Given input params cannot be used for api call, returning error dict")
        return {"error": f"Incorrect City or State sent"}

    if rc is None:
        logger.warning(f"Given input params to api, returned empty, returning error dict")
        return {"error": f"Non existent data given, please check if the State and City are correct {city} and {state}"}

    return rc


def get_geoloc_from_zip_code(zip_code: str) -> dict:
    if len(zip_code) == 5:
        logger.debug(f"Input {zip_code} is exactly 5 chars")
        rc = ApiUtils().get_request_with_auth_token(endpoint=f"zip?zip={zip_code}" + ",US", return_type=ZipLocationInfo)
    else:
        logger.warning(f"Input {zip_code} is NOT 5 chars")
        logger.warning(f"Given input params cannot be used for api call, returning error dict")
        return {"error": f"Incorrect Zip code"}

    if rc is None:
        logger.warning(f"Given input params to api, returned empty, returning error dict")
        return {"error": f"Non existent data given, please check if the zip code is correct {zip_code}"}

    return rc
