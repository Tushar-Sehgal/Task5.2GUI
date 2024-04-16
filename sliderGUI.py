import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setmode(GPIO.BCM)
led_pins = {"Red": 17, "Green": 27, "Blue": 22}

# Initializing GPIO channels as outputs
for pin in led_pins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Initializing PWM instances after setting up GPIO channels
pwms = {color: GPIO.PWM(pin, 100) for color, pin in led_pins.items()}
for pwm in pwms.values():
    pwm.start(0)

def update_pwm(color, value):
    pwms[color].ChangeDutyCycle(value)

root = tk.Tk()
root.title("LED Intensity Control Panel")
root.geometry("400x300")

# Adding sliders for PWM control
sliders = []
for color in led_pins:
    label = tk.Label(root, text=f"{color} Intensity")
    label.pack(anchor=tk.W)

    slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value, color=color: update_pwm(color, int(value)))
    slider.pack(anchor=tk.W)
    sliders.append(slider)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(side=tk.BOTTOM)

root.mainloop()

# Clean up PWM instances
for pwm in pwms.values():
    pwm.stop()

# Clean up GPIO
GPIO.cleanup()
