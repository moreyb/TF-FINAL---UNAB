from apscheduler.schedulers.background import BackgroundScheduler
from tasks import ActualizarPrecios, EnviarCorreosRecordatorio, GenerarInformeVentas
from config import SCHEDULER_CONFIG

class SchedulerManager:
    def __init__(self):
        self.scheduler = BackgroundScheduler(**SCHEDULER_CONFIG)
    
    def configurar_tareas(self):
        self.scheduler.add_job(ActualizarPrecios().ejecutar, 'interval', hours=6, id='actualizar_precios')
        self.scheduler.add_job(EnviarCorreosRecordatorio().ejecutar, 'interval', days=1, id='enviar_correos_recordatorio', hour=9)
        self.scheduler.add_job(GenerarInformeVentas().ejecutar, 'cron', day_of_week='mon-fri', hour=18, id='generar_informe_ventas')
    
    def iniciar_scheduler(self):
        self.scheduler.start()
        print("Scheduler iniciado")
    
    def detener_scheduler(self):
        self.scheduler.shutdown()
        print("Scheduler detenido")

if __name__ == "__main__":
    manager = SchedulerManager()
    manager.configurar_tareas()

    try:
        # Mantener el script en ejecución
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        manager.detener_scheduler()
        print("Scheduler detenido")

