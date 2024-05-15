from flask import Flask, request, jsonify

from test.newparse import find_shortest_on_floor

app = Flask(__name__)


@app.route('/find_path', methods=['GET'])
def find_path():
    start = request.args.get('start')
    end = request.args.get('end')
    if start and end:
        try:
            path = find_shortest_on_floor(start, end)
            return jsonify({'path': path})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'Missing start or end parameter'}), 400


if __name__ == '__main__':
    app.run(debug=True)
