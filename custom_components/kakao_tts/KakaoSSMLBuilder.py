# -*- coding: utf-8 -*-
# Original Source by ssml-builder(https://github.com/Reverseblade/ssml-builder)
import re


class Speech:

    #interpret-as
    #단일 사용 가능
    #spell-out : 영어 단어를 개별 알파벳으로 읽어줌
    #digits : 숫자를 개별적으로 읽어줌 (일, 이, 삼..)
    #telephone: 전화번호로 읽어줌
    #kakao:none : kakao:effect의 tone 처리 시, 원형 그대로를 보호해주고, 연결된 조사를 자연스럽게 변경해줌.
    #kakao:score : 스코어를 읽어줌 (예 3:1 → 3대1)
    #kakao:vocative : 호격 조사 처리를 하도록 함
    #
    #format attribute를 반드시 지정해주어야 함
    #date : 날짜로 읽어줌
    #time : 시간으로 읽어줌
    #kakao:number : 숫자 표현. 한글식(한/하나, 두/둘, 세/셋), 한자식(일, 이, 삼)으로 읽어줌
    VALID_INTERPRET_AS = ( 'spell-out', 'digits', 'telephone',
                           'kakao:none', 'kakao:score', 'kakao:vocative',
                           'date', 'time', 'kakao:number' )

    VALID_PROSODY_ATTRIBUTES = {
        #rate
        #slow : 0.9 / medium : 1.0 (default) / fast : 1.1
        #SSML 표준의 경우 최대값 50% (1.5에 해당), 최소값 -33.3% (0.7에 해당)이므로 표준에 부합
        'rate': ('slow', 'medium', 'fast'),

        #volume
        #soft : 0.7 / medium:1.0 (default) / loud : 1.4
        #SSML 표준의 경우 최대값 +4.08dB (1.6배에 해당), 최소값 정의 없음이므로 표준에 부합
        'volume': ('soft', 'medium', 'loud')
    }

    #WOMAN_READ_CALM : 여성 차분한 낭독체 (default)
    #MAN_READ_CALM : 남성 차분한 낭독체
    #WOMAN_DIALOG_BRIGHT : 여성 밝은 대화체
    #MAN_DIALOG_BRIGHT : 남성 밝은 대화체
    VALID_VOICE_NAMES = ('WOMAN_READ_CALM', 'MAN_READ_CALM', 'WOMAN_DIALOG_BRIGHT', 'MAN_DIALOG_BRIGHT')

    def __init__(self):
        self.speech = ""

    def speak(self):
        """
        <speak>
        :return:
        """
        return '<speak>{}</speak>'.format(self.speech)

    def add_text(self, value):
        """
        add text
        :return:
        """
        self.speech += value
        return self

    def say_as(self, value, interpret_as, is_nested=False):
        """
        <say_as>
        :param value:
        :param interpret_as:
        :param is_nested:
        :return:
        """

        if interpret_as not in self.VALID_INTERPRET_AS:
            raise ValueError('The interpret-as provided to say_as is not valid')

        ssml = '<say-as interpret-as="{interpret_as}">' \
               '{value}</say-as>'.format(interpret_as=interpret_as, value=value)

        if is_nested:
            return ssml

        self.speech += ssml
        return self

    def prosody(self, value, rate='medium', volume='medium', is_nested=False):
        """
        <prosody>
        :param value:
        :param rate:
        :param volume:
        :param is_nested:
        :return:
        """

        if rate not in self.VALID_PROSODY_ATTRIBUTES['rate']:
            if re.match(r'^\d+%$', rate) is None:
                raise ValueError('The rate provided to prosody is not valid')

        if volume not in self.VALID_PROSODY_ATTRIBUTES['volume']:
            raise ValueError('The volume provided to prosody is not valid')

        ssml = '<prosody rate="{rate}" volume="{volume}">' \
               '{value}</prosody>'.format(rate=rate, volume=volume, value=value)

        if is_nested:
            return ssml

        self.speech += ssml
        return self

    def sub(self, value, alias, is_nested=False):
        """
        <sub>
        :param value:
        :param alias:
        :param is_nested:
        :return:
        """

        ssml = '<sub alias="{}">{}</sub>'.format(alias, value)

        if is_nested:
            return ssml

        self.speech += ssml
        return self

    def voice(self, value, name, is_nested=False):
        """
        <voice>
        :param value:
        :param name:
        :return:
        """

        if name not in self.VALID_VOICE_NAMES:
            raise ValueError('The name provided to voice is not valid')

        ssml = '<voice name="{}">{}</voice>'.format(name, value)

        if is_nested:
            return ssml

        self.speech += '<voice name="{}">{}</voice>'.format(name, value)
        return self

    def pause(self, time, is_nested=False):
        """
        <break>
        :param time:
        :param is_nested:
        :return:
        """

        ssml = '<break time="{}"/>'.format(time)

        if is_nested:
            return ssml

        self.speech += ssml
        return self

    #kakao:effect tone=friendly
    def friendly(self, value, is_nested=False):
        """
        :param value:
        :param is_nested:
        :return:
        """

        ssml = '<kakao:effect tone="friendly">{}</kakao:effect>'.format(value)

        if is_nested:
            return ssml

        self.speech += ssml
        return self

    def audio(self, src, is_nested=False):
        """
        :param src:
        :param is_nested:
        :return:
        """

        ssml = '<audio src="{}" />'.format(src)

        if is_nested:
            return ssml

        self.speech += ssml
        return self

    def escape(self):
        """
        escapes any special characters that will cause SSML to be invalid
        :return:
        """
        pass
