import json
import logging
from typing import Optional, Dict, Any

import requests

logger = logging.getLogger(__name__)


class ApiUtils:
    

    def __init__(self):
        self.base_url = "http://api.openweathermap.org/geo/1.0/"
        self.txt_headers = {"Content-Type": "text/plain"}
        self.json_headers = {"Content-Type": "application/json"}
        self.appid = "f897a99d971b5eef57be6fafa0d83239"

    def _make_request(self, method: str,
                      endpoint: str,
                      headers: Optional[Dict[str, str]] = None,
                      auth_token: Optional[str] = None,
                      verify_api: bool = False, return_type: Optional[Any] = None) -> Any:

        response_json = None
        response = None
        if auth_token:
            headers["Authorization"] = "Bearer " + auth_token
        try:
            response = requests.request(method, endpoint, headers=headers, verify=verify_api)

        except requests.ConnectionError:
            logger.debug("Unable to connect to API, check internet connection.")

        try:
            if 'application/json' in response.headers.get("Content-Type") and response.status_code == 200:
                response = response.json()
                if isinstance(response, list) and return_type is not None:
                    return [return_type(**item) for item in response]
                if isinstance(response, dict) and return_type is not None:
                    return return_type(**response)

            else:
                logger.debug("Content-Type is not application/json or response code is not 200")
                return None
        except ValueError as e:
            logger.debug(f"Error parsing JSON: {e}")
            return None
        except KeyError as e:
            logger.debug(f"Content-Type header not found: {e}")
        return None

    def get_request_with_auth_token(self, endpoint: str,
                                    return_type: Optional[Any] = None) -> dict | None | list[str]:
        logger.debug(f"GET -> {self.base_url} + {endpoint} + &appid={self.appid}")
        response = self._make_request("GET", endpoint=self.base_url + endpoint + f"&appid={self.appid}",
                                      headers=self.json_headers, return_type=return_type)
        if isinstance(response, list):
            logger.debug(f"Response received - len: {len(response)}")
            if len(response) > 0:
                return response[0]
        elif isinstance(response, dict):
            logger.debug(f"Response received: {response}")
            return response
        elif isinstance(response, return_type):
            logger.debug(f"Response received: {response}")
            return response
        return None
