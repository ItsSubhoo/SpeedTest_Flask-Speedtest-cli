from flask import Flask, jsonify, render_template
import speedtest
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speedtest')
def run_speedtest():
    try:
        server = speedtest.Speedtest()
        server.get_best_server()

        results = {'download': [], 'upload': []}
        test_duration = 5  # Total duration of the test in seconds
        sample_interval = 1  # Interval between samples in seconds

        start_time = time.time()
        while time.time() - start_time < test_duration:
            download_speed = server.download() / 1_000_000  # Convert to Mbps
            upload_speed = server.upload() / 1_000_000  # Convert to Mbps
            results['download'].append(round(download_speed, 2))
            results['upload'].append(round(upload_speed, 2))
            time.sleep(sample_interval)

        return jsonify({
            'download_speeds': results['download'],
            'upload_speeds': results['upload']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
