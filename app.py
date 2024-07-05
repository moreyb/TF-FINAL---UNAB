from flask import Flask, jsonify
from scheduler_manager import SchedulerManager

app = Flask(__name__)
scheduler_manager = SchedulerManager()
scheduler_manager.configurar_tareas()

@app.route('/start_scheduler', methods=['POST'])
def start_scheduler():
    scheduler_manager.iniciar_scheduler()
    return jsonify({"message": "Scheduler iniciado"})

@app.route('/stop_scheduler', methods=['POST'])
def stop_scheduler():
    scheduler_manager.detener_scheduler()
    return jsonify({"message": "Scheduler detenido"})

@app.route('/run_task', methods=['POST'])
def run_task():
    # Aquí podrías ejecutar una tarea específica manualmente
    ActualizarPrecios().ejecutar()
    return jsonify({"message": "Tarea ejecutada manualmente"})

if __name__ == "__main__":
    app.run(debug=True)
