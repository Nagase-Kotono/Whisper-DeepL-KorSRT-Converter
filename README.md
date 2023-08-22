# Whisper-DeepL-KorSRT-Converter

## 프로젝트 소개, 시작하기 및 사용 방법

이 프로젝트는 `subsai`를 통해 `whisper` 등의 음성 인식 모델을 쉽게 실행하여, 음성 및 동영상의 내용을 텍스트로 변환하며 결과를 JSON 형태로 저장합니다. 이렇게 저장된 영어 텍스트는 `DeepL API`를 이용하여 한국어로 번역됩니다. 그 후, 번역된 한국어 텍스트는 `.srt` 자막 형식으로 변환되어 저장됩니다.

### 주요 기능
- `subsai`를 활용하여 `whisper` 등의 모델로 음성 및 동영상의 내용을 영어 텍스트로 변환
- `DeepL API`를 이용한 영어 텍스트의 한국어 번역
- 번역된 한국어 텍스트의 `.srt` 자막 형식 변환

### 사전 요구사항
- Python 3.10 이상
- `subsai`를 통한 `.json` 형태로 영어로 받아쓰기된 결과물. [subsai 레포지토리](https://github.com/abdeladim-s/subsai)에서 결과물 제작 방법을 확인하시기 바랍니다.
- `DeepL API` 사용을 위한 API 키. [DeepL 공식 웹사이트](https://www.deepl.com/pro-api?cta=header-pro-api)에서 무료 회원가입을 통해 API 키를 받을 수 있습니다.

### 설치하기
1. 필요한 파이썬 라이브러리 설치
```
pip install deepl
```

### 사용 방법

1. **영어로 된 JSON 파일을 한국어로 번역하기 (`deeplapi.py`)**

   변역을 위한 `deeplapi.py` 스크립트를 실행하기 전에 몇 가지 파라미터를 수정해야 합니다

   ```python
   # Parameters
   auth_key = "123456789"  # 실제 DeepL 인증 키로 교체하세요.
   target_lang = "KO"
   file_path = "/Users/hotch/Downloads/test.json"  # JSON 파일 경로로 교체하세요.
   ```

   파라미터를 수정한 후 `deeplapi.py` 스크립트를 실행하면, 변역 진행 상황이 표시되며 완료되면 자동으로 종료됩니다.

2. 번역된 JSON 파일을 .srt 형식으로 변환하기

   다음과 같이 명령을 실행하여 번역된 JSON 파일을 .srt 형식으로 변환할 수 있습니다

   ```
   python convert_to_srt.py --input /Users/hotch/VSC/python/translated_test.json --output /Users/hotch/VSC/python/ttt.srt
   ```

   위의 명령에서 `--input` 옵션에는 변환하려는 번역된 JSON 파일의 경로를, `--output` 옵션에는 변환된 .srt 파일을 저장하려는 경로를 지정합니다.

## 라이선스

이 프로젝트는 MIT 라이선스로 라이선스되어 있습니다. 프로젝트를 자유롭게 사용, 수정, 배포할 수 있습니다. 단, 원작자에 대한 책임은 면제됩니다. (자세한 정보는 LICENSE 파일을 참조하시기 바랍니다.)

본 프로젝트에서는 `subsai`를 사용하고 있습니다. `subsai`는 GNU General Public License version 3.0 (GPL-3.0) 라이선스를 사용하고 있으므로, 해당 라이선스의 조건을 준수해야 합니다. `subsai`를 사용하거나 수정할 경우, 해당 라이선스 문서를 참고하시기 바랍니다.

## Thanks

이 프로젝트는 다음 분들의 도움과 지원으로 완성할 수 있었습니다.

- `subsai`를 개발한 [abdeladim-s](https://github.com/abdeladim-s)님
- 번역 API 서비스를 제공하는 [DeepL](https://www.deepl.com/)
- `whisper` 모델을 개발한 [OpenAI](https://www.openai.com/)
- 프로젝트 아이디어를 제공해준 제 삼촌
