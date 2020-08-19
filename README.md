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

## kakao developers api key
1. kakao developers에 회원가입을 한 뒤, 로그인 하여 '내 어플리케이션(<https://developers.kakao.com/console/app>)'으로 접속한다.
2. '어플리케이션 추가하기'를 클릭한다.
3. '어플리케이션 추가' 팝업이 뜨면 내용(앱 아이콘, 앱 이름, 회사 이름)을 입력하고 저장한다.<br>
   정보가 정확하지 않은 경우 서비스 이용이 제한될 수 있다고 한다.
   ![app_registry](https://github.com/miumida/kakao_tts/blob/master/images/kakao_developers_app_registry.png?raw=true)<br>
4. 추가된 내 어플리케이션으로 들어가서 '내 애플리케이션 > 앱 설정 > 요약 정보 > 앱키 > REST API 키'를 복사한다.
5. 복사한 api 키를 설정할 때 입력해준다.
6. '내 애플리케이션 > 제품 설정 > 음성 > 활성화 설정'에서 상태를 ON으로 변경해준다.
![app_tts_on](https://github.com/miumida/kakao_tts/blob/master/images/kakao_developers_app_tts_on.png?raw=true)<br>

<br>

## 참고사이트
[1] Kakao Developers | 음성 합성하기 (<https://developers.kakao.com/docs/latest/ko/voice/rest-api#text-to-speech>)<br>
[2] Kakao Developers | 카카오 SSML 가이드 (https://developers.kakao.com/assets/guide/kakao_ssml_guide.pdf)<br>

[version-shield]: https://img.shields.io/badge/version-v1.0.0-orange.svg
[hakc-shield]: https://img.shields.io/badge/HAKC-Enjoy-blue.svg
[hacs-shield]: https://img.shields.io/badge/HACS-Custom-red.svg
