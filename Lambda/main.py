import json
import base64
import boto3

polly = boto3.client('polly')


def lambda_handler(event, context):
    pitch_values = {
        '0': 'x-low',
        '1': 'low',
        '2': 'medium',
        '3': 'high',
        '4': 'x-high'
    }

    if 'text' not in event or 'voiceId' not in event or 'pitch' not in event:
        raise ValueError(
            "Input event must contain 'text', 'voiceId', and 'pitch' keys")

    text = event['text']
    voice_id = event['voiceId']
    pitch_str = event['pitch']
    pitch_str = event['pitch']

    print(f'pitch_str = {pitch_str}')

    if pitch_str not in pitch_values:
        raise ValueError(
            "Invalid pitch value. Must be one of: '0', '1', '2', '3', '4'")

    pitch_value = pitch_values[pitch_str]

    ssml = f'<speak><prosody pitch="{pitch_value}">{text}</prosody></speak>'

    print(f'pitch_value = {pitch_value}')

    try:
        response = polly.synthesize_speech(
            Text=ssml,
            VoiceId=voice_id,
            OutputFormat='mp3',
            TextType='ssml',
            Engine='standard',
            LanguageCode='en-US',
            SampleRate='22050'
        )
        audio_stream = response['AudioStream'].read()
        audio_base64 = base64.b64encode(audio_stream).decode('utf-8')
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'audio/mpeg',
                # Update this with your domain or '*' for public access
                'Access-Control-Allow-Origin': 'http://txt2speechbucket.s3-website.us-east-2.amazonaws.com'
            },
            'body': audio_base64,
            'isBase64Encoded': True
        }
    except Exception as error:
        print(error)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(error)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
