from datetime import datetime
import re
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


def to_timestamp(str_date):
    return int(datetime.timestamp(datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')))

@app.route('/earthquakes', methods=['GET'])
def deprembilgi():
    try:
        response = requests.get('http://www.koeri.boun.edu.tr/scripts/lst0.asp')
        content = response.text

        ext = content.split('<pre>')
        ext = ext[1].split('--------------')
        ext = ext[2].split('</pre>')
        ext = re.sub(r'[\r\n]{2,}', '|', ext[0])
        ext = re.sub(r'[ ]{2,}', ',', ext)

        split = ext.split('|')
        new_data = []

        for e in split:
            if len(new_data) > int(request.args.get('length', 0)):
                break
            r = e.split(',')
            if r[0] != "":
                sehir = re.findall(r'\((.*?)\)', r[7])
                sehir = sehir[0] if sehir else ""
                tar = r[0].split(' ')
                new_data.append({
                    'tarih': tar[0].replace('.', '-'),
                    'saat': tar[1],
                    'enlem': r[1],
                    'boylam': r[2],
                    'depth': r[3],
                    'buyukluk_md': r[4].replace('-', '0'),
                    'mag': r[5],
                    'buyukluk_mw': r[6].replace('-', '0'),
                    'lokasyon': r[7],
                    'sehir': sehir,
                    'timestamp': to_timestamp(f'{tar[0].replace(".", "-")} {tar[1]}')
                })

        return jsonify({'status': True, 'result': new_data})

    except Exception as e:
        return jsonify({'status': False, 'error': str(e)})

@app.errorhandler(404)
def sayfayok(e):
    return jsonify({'status': False, 'error': '404 Not Found'}), 404


if __name__ == '__main__':
    app.run(port=8000)
