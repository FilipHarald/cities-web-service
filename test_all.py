import pytest
import src.cities_api as cities_api

def test_format_cities():
    payload = {
            "data": [{
                "id": 659,
                "city": "Abu Dhabi",
                "country": "United Arab Emirates",
                "excessive-prop": "..."
                }]
            }
    res = cities_api.format_cities(payload)
    assert isinstance(res, list)
    assert len(res[0]) == 3
    assert res[0]["id"] == 659
    assert res[0]["city"] == "Abu Dhabi"
    assert res[0]["country"] == "United Arab Emirates"

def test_available_cities():
    with pytest.raises(AssertionError):
        cities_api.get_available("bad")
    with pytest.raises(AssertionError):
        cities_api.get_available(-1)

def test_near_cities():
    with pytest.raises(AssertionError):
        cities_api.get_near("bad", 100)
    with pytest.raises(AssertionError):
        cities_api.get_near(-1, 100)
    with pytest.raises(AssertionError):
        cities_api.get_near(1, "bad")
    with pytest.raises(AssertionError):
        cities_api.get_near(1, -1)

