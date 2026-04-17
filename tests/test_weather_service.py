import pytest
from unittest.mock import patch, Mock

from weather_service import get_weather


def test_get_weather_returns_json():
    dummy_data = {"temp": 25, "condition": "Sunny"}
    mock_response = Mock()
    mock_response.json.return_value = dummy_data

    with patch("weather_service.requests.get", return_value=mock_response) as mock_get:
        result = get_weather("lima")
        mock_get.assert_called_once_with("https://api.weather.com/v3/weather/lima")
        assert result == dummy_data


def test_get_weather_different_location():
    dummy_data = {"temp": 10, "condition": "Cloudy"}
    mock_response = Mock()
    mock_response.json.return_value = dummy_data

    with patch("weather_service.requests.get", return_value=mock_response) as mock_get:
        result = get_weather("london")
        mock_get.assert_called_once_with("https://api.weather.com/v3/weather/london")
        assert result == dummy_data


def test_get_weather_empty_response():
    dummy_data = {}
    mock_response = Mock()
    mock_response.json.return_value = dummy_data

    with patch("weather_service.requests.get", return_value=mock_response):
        result = get_weather("unknown")
        assert result == {}
