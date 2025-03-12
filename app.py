from flask import Flask, jsonify, request
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

app = Flask(__name__)

@app.route('/sub', methods=['GET'])
def sub():
    video_id = request.args.get('video_id')

    try:
        subtitles = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        formatted_subtitles = formatter.format_transcript(subtitles)
        return jsonify({'video_id': video_id, 'subtitles': formatted_subtitles})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)