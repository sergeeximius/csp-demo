import json
import os
from datetime import datetime

from flask import Flask, jsonify, request

app = Flask(__name__)

# Директория для сохранения отчетов
REPORTS_DIR = "csp-reports"
if not os.path.exists(REPORTS_DIR):
    os.makedirs(REPORTS_DIR)

@app.route('/csp-violation-report-endpoint', methods=['POST'])
def csp_report():
    # Проверяем Content-Type
    if request.content_type != 'application/csp-report':
        return 'Unsupported Media Type', 415

    # Получаем данные отчета
    report = request.get_json(force=True)  # force=True позволяет обработать любой Content-Type
    timestamp = datetime.now().isoformat().replace(':', '-').replace('.', '-')
    report_file = os.path.join(REPORTS_DIR, f"report-{timestamp}.json")

    # Сохраняем отчет в файл
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"CSP report saved: {report_file}")
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
