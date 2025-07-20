import pytest
from ..utils import *

# mylogger = logging.getLogger()

testdata = [
    ("google.com", "Google"),
    ("https://docs.pytest.org/en/stable/", "pytest documentation"),
    (
        "datacamp.com/",
        "Learn Data Science and AI Online | DataCamp",
    ),
]


@pytest.mark.parametrize("url, expected_title", testdata)
def test_get_url(driver: WebDriver, url, expected_title):

    navigate_to(driver=driver, url=url)

    actual_title = get_title(driver)
    mylogger.info(f"Page Title : {actual_title}")

    assert (
        actual_title == expected_title
    ), f"Actual Title: '{actual_title}', Expected Title: '{expected_title}'"
