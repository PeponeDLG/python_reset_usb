#!/usr/bin/env python3
"""
Plantilla básica de demonio para Systemd
Guarda como: /usr/local/bin/mi_servicio.py
"""

import os
import sys
import time
import logging
import signal
from datetime import datetime

class MiServicio:
    def __init__(self):
        self.activo = True
        self.setup_logging()
        self.setup_señales()
    
    def setup_logging(self):
        """Configurar sistema de logs"""
        log_dir = "/var/log"
        os.makedirs(log_dir, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            handlers=[
                logging.FileHandler(f"{log_dir}/mi_servicio.log"),
                logging.StreamHandler()
            ]
        )
        self.log = logging.getLogger(__name__)
    
    def setup_señales(self):
        """Manejar señales de sistema"""
        signal.signal(signal.SIGTERM, self.manejar_apagado)
        signal.signal(signal.SIGINT, self.manejar_apagado)
    
    def manejar_apagado(self, signum, frame):
        """Apagado elegante"""
        self.log.info(f"Señal {signum} recibida, apagando...")
        self.activo = False
    
    def ciclo_principal(self):
        """Lógica principal del servicio"""
        self.log.info("🚀 Servicio iniciado")
        
        contador = 0
        while self.activo:
            try:
                contador += 1
                
                # EJEMPLO: Tu lógica aquí
                self.log.info(f"Ciclo #{contador} - {datetime.now()}")
                
                # Simular trabajo
                time.sleep(5)
                
                # Ejemplo: verificar recursos
                if contador % 10 == 0:
                    self.verificar_recursos()
                    
            except Exception as e:
                self.log.error(f"Error en ciclo: {e}")
                time.sleep(10)
        
        self.log.info("🛑 Servicio detenido")
    
    def verificar_recursos(self):
        """Ejemplo de función de mantenimiento"""
        import psutil
        cpu = psutil.cpu_percent()
        memoria = psutil.virtual_memory().percent
        self.log.info(f"Recursos: CPU={cpu}%, Memoria={memoria}%")
    
    def ejecutar(self):
        """Punto de entrada principal"""
        try:
            self.ciclo_principal()
        except Exception as e:
            self.log.critical(f"Error crítico: {e}")
            sys.exit(1)

if __name__ == "__main__":
    servicio = MiServicio()
    servicio.ejecutar()
