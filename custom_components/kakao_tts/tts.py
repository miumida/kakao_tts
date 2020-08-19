import asyncio
import logging
import io

import aiohttp
import async_timeout
import voluptuous as vol

import os
import requests

from homeassistant.components.tts import CONF_LANG, PLATFORM_SCHEMA, Provider
from homeassistant.const import CONF_API_KEY, HTTP_OK
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import homeassistant.helpers.config_validation as cv
from homeassistant.exceptions import HomeAssistantError

from .KakaoSSMLBuilder import Speech

_LOGGER = logging.getLogger(__name__)

_SUPPORT_LANGUAGES = [ "ko" ]

_SUPPORT_VOICES = [
    "WOMAN_READ_CALM",
    "MAN_READ_CALM",
    "WOMAN_DIALOG_BRIGHT",
    "MAN_DIALOG_BRIGHT"
]

KAKAO_API_URL = 'https://kakaoi-newtone-openapi.kakao.com/v1/synthesize'
CONF_KAKAO_API_KEY = "api_key"

CONF_VOICE    = "voice"
DEFAULT_VOICE = "WOMAN_READ_CALM"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_KAKAO_API_KEY): cv.string,
        vol.Optional(CONF_VOICE, default=DEFAULT_VOICE): cv.string,
    }
)

async def async_get_engine(hass, config, discovery_info=None):
    """Set up kakao tts  speech component."""
    return KakaoSpeechManager(hass, config)

class KakaoSpeechManager(Provider):
    """The Kakao TTS  speech API provider."""

    def __init__(self, hass, config):
        """Init Kakao TTS service."""
        self._hass     = hass
        self._api_key  = config.get(CONF_KAKAO_API_KEY)
        self._voice    = config.get(CONF_VOICE)

        self._headers = {
            'Content-Type' : 'application/xml',
            'Authorization': self._api_key
        }

    @property
    def default_language(self):
        """Return the default language."""
        return "ko"

    @property
    def supported_languages(self):
        """Return list of supported languages."""
        return _SUPPORT_LANGUAGES

    async def async_get_tts_audio(self, message, language, options=None):
        """Load TTS from kakao_tts."""
        websession = async_get_clientsession(self.hass)
        options = options or {}

        try:

            with async_timeout.timeout(10):

                s = Speech()
                s.voice(message, self._voice)
                data = s.speak()

                #_LOGGER.info("### speak() :: " + data)

                request = await websession.post(KAKAO_API_URL, data=data.encode('utf-8'), headers=self._headers)

                if request.status != HTTP_OK:
                    _LOGGER.error(
                        "Error %d on load URL %s", request.status, request.url
                    )
                    return (None, None)

                data = await request.read()

                return ("mp3", data)

        except (asyncio.TimeoutError, aiohttp.ClientError):
            _LOGGER.error("Timeout for Kakao TTS speech API")
            return (None, None)
