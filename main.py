from apscheduler.schedulers.background import BackgroundScheduler
from config import SCHEDULER_CONFIG
from tasks import actualizar_precios, enviar_correos_recordatorio, generar_informe_ventas

def iniciar_scheduler():
    scheduler = BackgroundScheduler()
    
    scheduler.add_job(actualizar_precios, 'interval', hours=6, id='actualizar_precios')
    scheduler.add_job(enviar_correos_recordatorio, 'interval', days=1, id='enviar_correos_recordatorio', hour=9)
    scheduler.add_job(generar_informe_ventas, 'cron', day_of_week='mon-fri', hour=18, id='generar_informe_ventas')

    scheduler.start()
    print("Scheduler iniciado")

if __name__ == "__main__":
    iniciar_scheduler()

    try:
        # Mantener el script en ejecución
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Scheduler detenido")
