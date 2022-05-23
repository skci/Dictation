import azure.cognitiveservices.speech as speechsdk
import datetime


def get_speech(lang, rate, say_as, text):
    """
    将text转为语音输出
    :param text: 待抓换的文字
    :return: 返回声音到默认扬声器
    """
    file_name = str(datetime.datetime.now()).replace(' ', '.').replace('-', '.').replace(':', '.')
    speech_config = speechsdk.SpeechConfig(subscription="b52583aad67a4876993dbe1e467dc170", region="japaneast")

    # 自定义音频格式
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio24Khz48KBitRateMonoMp3)

    # 自定义输出
    filename = "static/wav/%s.mp3" % file_name
    audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)
    # audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # Speaker设置
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    ssml_front = """<speak version='1.0' xml:lang='zh-CN' xmlns='http://www.w3.org/2001/10/synthesis' 
    xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml"><voice 
    name='en-US-JennyMultilingualNeural'><lang xml:lang="%s"><prosody rate="%s">
    """ % (lang, rate)

    ssml_center = ""
    if say_as:
        for i in text:
            i = """<break time="1000ms" /><say-as interpret-as="%s">%s</say-as>""" % (say_as, i)
            ssml_center += i
    else:
        for i in text:
            i = """<break time="1000ms" />""" + str(i)
            ssml_center += i

    ssml_behind = """</prosody></lang></voice></speak>"""

    ssml = ssml_front + ssml_center + ssml_behind
    # print('ssml语句：' + ssml)

    speech_synthesis_result = speech_synthesizer.speak_ssml_async(ssml).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("语音合成成功：{}".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("语音合成取消：{}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("错误信息: {}".format(cancellation_details.error_details))

    return filename
