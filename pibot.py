import RPi.GPIO as gpio
import time
import commands
import os

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(22, gpio.OUT)

gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

gpio.output(12, True)
gpio.output(16, True)
                    
gpio.output(7, True)
gpio.output(11, True)

def cpu_temp():
        tempFile = open("/sys/class/thermal/thermal_zone0/temp")
        cpu_temp = tempFile.read()
        tempFile.close()
        return float(cpu_temp)/1000

def gpu_temp():
        gpu_temp = commands.getoutput('/opt/vc/bin/vcgencmd measure_temp').replace('temp=', '').replace('\'C', '')
        return  float(gpu_temp)

def rightMotorGoForward():
        gpio.output(18, True)
        gpio.output(22, False)

def leftMotorGoForward():
        gpio.output(13, True)
 		gpio.output(15, False)

def rightMotorGoBackword():
        gpio.output(18, False)
        gpio.output(22, True)

def leftMotorGoBackword():
        gpio.output(13, False)
        gpio.output(15, True)

def stopMotors():
        gpio.output(18, False)
        gpio.output(22, False)

        gpio.output(13, False)
        gpio.output(15, False)

def goForward():
        rightMotorGoForward()
        leftMotorGoForward()
 		time.sleep(2)
        stopMotors()

def goBackword():
        leftMotorGoBackword()
        rightMotorGoBackword()
        time.sleep(2)
        stopMotors()

def goLeft():
        leftMotorGoBackword()
        rightMotorGoForward()
        time.sleep(1)
        stopMotors()

def goRight():
        leftMotorGoForward()
        rightMotorGoBackword()
        time.sleep(1)
        stopMotors()

def main():
        while True:

                direction  = raw_input("Choose your direction:")
                print "Your pressed: " + direction
                if direction == "w":
                        print "Going forward"
                        goForward()
                if direction == "s":
                        print "Going backword"
                        goBackword()
                if direction == "a":
                        print "Going left"
                        goLeft()
                if direction == "d":
                        print "Going right"
                        goRight()
                if direction == "z":
                        print "Brake"
                        stopMotors()
                if direction == "t":
                        print "CPU temperature is:", cpu_temp()
                        print "GPU temperature is", gpu_temp()

if __name__ == '__main__':
        main()

