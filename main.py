Configurar /etc/sudoers para poder ejecutar comandos como super usuario

    # Editor de el fichero de superusuarios
    sudo visudo

    # Permitir que el usuario 'tu_usuario' ejecute comandos específicos sin password
    tu_usuario ALL=(ALL) NOPASSWD: /bin/systemctl restart servicio_especifico
    tu_usuario ALL=(ALL) NOPASSWD: /usr/bin/apt update
    tu_usuario ALL=(ALL) NOPASSWD: /sbin/reboot

    # O para un script específico
    tu_usuario ALL=(ALL) NOPASSWD: /ruta/completa/de/tu_script.py