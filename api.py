import requests


class PetAPI:
    _SERVICE_KEY = "496081b3-9c44-4acc-8afa-e53044221eaa"
    _ENDPOINT_URL = "http://api.kcisa.kr/openapi/API_TOU_050/request"
    _HEADER = {"Content-Type": "application/json", "Accept": "application/json"}

    def __init__(self):
        pass

    def get_response(self, keyword, num_of_rows="23000", page_no="1", category=""):
        url = (
            self._ENDPOINT_URL
            + f"?serviceKey={self._SERVICE_KEY}&numOfRows={num_of_rows}&pageNo={page_no}&keyword={keyword}&category={category}"
        )

        response = requests.get(url=url, headers=self._HEADER)

        return response.content.decode()
