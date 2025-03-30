import requests
from .filters import Filters
from typing import Dict, List
from .helpers import load_json


class GdeltDoc:
    """
    API client for the GDELT 2.0 Doc API
    """

    def __init__(self, json_parsing_max_depth: int = 100) -> None:
        """
        Params
        ------
        json_parsing_max_depth
            A parameter for the json parsing function that removes illegal character. If 100 it will remove at max
            100 characters before exiting with an exception
        """
        self.max_depth_json_parsing = json_parsing_max_depth

    def article_search(self, filters: Filters) -> Dict[str, List[Dict]]:
        """
        Make a query against the `ArtList` API to return a DataFrame of news articles that
        match the supplied filters.

        Params
        ------
        filters
            A `gdelt-doc.Filters` object containing the filter parameters for this query.
        """

        articles = self._query("artlist", filters.query_string)

        return articles

    def _query(self, mode: str, query_string: str) -> Dict:
        """
        Submit a query to the GDELT API and return the results as a parsed JSON object.

        Params
        ------
        mode
            The API mode to call. Must be one of "artlist", "timelinevol",
            "timelinevolraw", "timelinetone", "timelinelang", "timelinesourcecountry".

        query_string
            The query parameters and date range to call the API with.

        Returns
        -------
        Dict
            The parsed JSON response from the API.
        """
        if mode not in [
            "artlist",
            "timelinevol",
            "timelinevolraw",
            "timelinetone",
            "timelinelang",
            "timelinesourcecountry",
        ]:
            raise ValueError(f"Mode {mode} not in supported API modes")

        headers = {
            "User-Agent": f"milank-ctrl"
        }

        response = requests.get(
            f"https://api.gdeltproject.org/api/v2/doc/doc?query={query_string}&mode={mode}&format=json&sort=datadesc",
            headers=headers
        )
        if response.status_code not in [200, 202]:
            raise ValueError("The gdelt gdelt returned a non-successful statuscode. This is the response message: {}".
                             format(response.text))

        # Response is text/html if it's an error and application/json if it's ok
        if "text/html" in response.headers["content-type"]:
            raise ValueError(f"The query was not valid. The API error message was: {response.text.strip()}")

        return load_json(response.content, self.max_depth_json_parsing)