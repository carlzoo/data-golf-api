from data_golf.api.model import Model
from data_golf.config import DGConfig
from data_golf.http import HttpClient
from data_golf.api.general import General


class DGCInvalidApiKey(Exception):
    pass


class DataGolfClient:
    def __init__(
        self,
        api_key: str,
        verbose: bool = False,
        timeout: int = 15,
        ssl_verify: bool = True,
    ) -> None:
        self._validate_api_key(api_key)

        self._config = DGConfig(
            api_key=api_key, verbose=verbose, timeout=timeout, ssl_verify=ssl_verify
        )
        self._http_client = HttpClient(self._config)

        # Endpoints
        self.general = General(self._http_client)
        self.model = Model(self._http_client)

    def _validate_api_key(self, api_key: str) -> None:
        """
        Private method to validate the API key.
        :param api_key:
        :return:
        """
        if not isinstance(api_key, str):
            raise DGCInvalidApiKey("API key must be a string.")
        if not api_key:
            raise DGCInvalidApiKey("API key cannot be empty.")
