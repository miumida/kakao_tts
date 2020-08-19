# KAKAO 음성합성 API TTS

![HAKC][hakc-shield]
![HACS][hacs-shield]
![Version v1.0.0][version-shield]

카카오 음성합성 API를 이용한 TTS for Home Assistant 입니다.<br>
사용을 위해서는 kakao developers에서 api key를 발급받아야 합니다.<br>
<br>

## Version history
| Version | Date        | 내용              |
| :-----: | :---------: | ----------------------- |
| v1.0.0  | 2020.08.19  | First version  |

<br>

## Installation
### Manual
- HA 설치 경로 아래 custom_components 에 파일을 넣어줍니다.<br>
  `<config directory>/custom_components/kakao_tts/__init__.py`<br>
  `<config directory>/custom_components/kakao_tts/manifest.json`<br>
  `<config directory>/custom_components/kakao_tts/tts.py`<br>
  `<config directory>/custom_components/kakao_tts/KakaoSSMLBuilder.py`<br>
- configuration.yaml 파일에 설정을 추가합니다.<br>
- Home-Assistant 를 재시작합니다<br>
### HACS
- HACS > Integretions > 우측상단 메뉴 > Custom repositories 선택
- 'https://github.com/miumida/kakao_tts' 주소 입력, Category에 'integration' 선택 후, 저장
- HACS > Integretions 메뉴 선택 후, kakao_tts 검색하여 설치

<br>

## Usage
### configuration
- HA 설정에 kakao_tts를 추가합니다.<br>
```yaml
tts:
  - platform: kakao_tts
    api_key: [your api key]
    voice: 'WOMAN_DIALOG_BRIGHT'
```

<br>

### 기본 설정값

|옵션|내용|
|--|--|
|platform| (필수) kakao_tts  |
|api_key| (필수) kakao developers api key |
|voice| (옵션) 목소리 |

<br>

### 목소리(voice)

|목소리|내용|
|--|--|
|WOMAN_READ_CALM|여성 차분한 낭독체(default)|
|MAN_READ_CALM | 남성 차분한 낭독체|
|WOMAN_DIALOG_BRIGHT | 여성 밝은 대화체|
|MAN_DIALOG_BRIGHT | 남성 밝은 대화체|

<br>

## 참고사이트
[1] Kakao Developers | 음성 합성하기 (<https://developers.kakao.com/docs/latest/ko/voice/rest-api#text-to-speech>)<br>
[1] Kakao Developers | 카카오 SSML 가이드 (https://developers.kakao.com/assets/guide/kakao_ssml_guide.pdf)<br>

[version-shield]: https://img.shields.io/badge/version-v1.0.0-orange.svg
[hakc-shield]: https://img.shields.io/badge/HAKC-Enjoy-blue.svg
[hacs-shield]: https://img.shields.io/badge/HACS-Custom-red.svg
