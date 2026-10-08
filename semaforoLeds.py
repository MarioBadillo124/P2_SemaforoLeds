import RPi.GPIO as GPIO
import time

LED_ROJO = 18      # GPIO 18 (pin físico 12)
LED_AMARILLO = 24  # GPIO 24 (pin físico 18)
LED_VERDE = 23     # GPIO 23 (pin físico 16)

try:
    # 1. Configurar modo de numeración BCM
    GPIO.setmode(GPIO.BCM)
    # 2. Desactivar advertencias (opcional)
    GPIO.setwarnings(False)
    # 3. Configurar pin como salida
    GPIO.setup(LED_ROJO, GPIO.OUT, initial=GPIO.LOW)
    print("Control de LED iniciado (Modo BCM)")
    print(f"Usando GPIO {LED_ROJO} (Pin físico 12)")
    
    GPIO.setup(LED_AMARILLO, GPIO.OUT, initial=GPIO.LOW)
    print(f"Usando GPIO {LED_AMARILLO} (Pin físico 18)")
    
    GPIO.setup(LED_VERDE, GPIO.OUT, initial=GPIO.LOW)
    print(f"Usando GPIO {LED_VERDE} (Pin físico 16)")
    
    # 4. Loop principal - Secuencia de semáforo
    while True:
        # --- VERDE ---
        GPIO.output(LED_VERDE, GPIO.HIGH)
        print("LED VERDE ENCENDIDO")
        time.sleep(10)
        GPIO.output(LED_VERDE, GPIO.LOW)
        
        # --- AMARILLO ---
        GPIO.output(LED_AMARILLO, GPIO.HIGH)
        print("LED AMARILLO ENCENDIDO")
        time.sleep(3)
        GPIO.output(LED_AMARILLO, GPIO.LOW)
        
        # --- ROJO ---
        GPIO.output(LED_ROJO, GPIO.HIGH)
        print("LED ROJO ENCENDIDO")
        time.sleep(10)
        GPIO.output(LED_ROJO, GPIO.LOW)
        
except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario")
finally:
    # 5. Limpieza - Restaurar pines a estado seguro
    GPIO.cleanup()
    print("GPIO limpiado. Programa finalizado.")