from __future__ import division
import time
import Adafruit_PCA9685

'''import logging
logging.basicConfig(level=logging.DEBUG)'''

pwm11_ADDRESS = 0x40
pwm2_ADDRESS = 0x41

pwm11 = Adafruit_PCA9685.PCA9685(pwm11_ADDRESS)
pwm2 = Adafruit_PCA9685.PCA9685(pwm12_ADDRESS)

min_pulse = 150
desired_pulse = 400 #????

#set frequency to 60hz

pwm11.set_pwm1_freq(60)
pwm2.set_pwm1_freg(60)

# set servo channel numbers for pwm1

servo1_channel = 0
servo2_channel = 1
servo3_channel = 2
servo4_channel = 3
servo5_channel = 4
servo6_channel = 5
servo7_channel = 6
servo8_channel = 7
servo9_channel = 8
servo10_channel = 9
servo11_channel = 10
servo12_channel = 11
servo13_channel = 12
servo14_channel = 13
servo15_channel = 14
servo16_channel = 15

# set servo channel numbers for pwm2

servo17_channel = 0
# more to  come here

'''def set_servo_pulse(channel, pulse):
    pulse_length = 1000000
    pulse_length //= 60
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096 #12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm1.set_pwm1(channel, 0, pulse)'''
#stage 1 servo control
def feeding(seconds1, seconds2, seconds3, seconds4):

    pwm1.set_pwm1(servo1_channel, 0, desired_pulse)
    # turn on pump 1
    time.sleep(seconds1)
    pwm1.set_pwm1(servo1_channel, 0, min_pulse)
    # turn off pump 1
    time.sleep(seconds2)
    pwm1.set_pwm1(servo4_channel, 0, desired_pulse)
    # turn on pump 2
    time.sleep(seconds3)
    pwm1.set_pwm1(servo4_channel, 0, min_pulse)
    #turn off pump 2
    time.sleep(seconds4)

def column1_priming(seconds_running, seconds_stopping):

    pwm1.set_pwm1(servo7_channel, 0, desired_pulse)
    pwm1.set_pwm1(servo11_channel, 0, desired_pulse)
    pwm1.set_pwm1(servo13_channel, 0, desired_pulse)
    pwm1.set_pwm1(servo15_channel, 0, desired_pulse)
    # turn on HPP
    time.sleep(seconds_running)

    pwm1.set_pwm1(servo7_channel, 0, min_pulse)
    pwm1.set_pwm1(servo11_channel, 0, min_pulse)
    pwm1.set_pwm1(servo13_channel, 0, min_pulse)
    pwm1.set_pwm1(servo15_channel, 0, min_pulse)
    # turn off HPP?
    time.sleep(seconds_stopping)

def column2_priming(seconds_running, seconds_stopping):
    pwm1.set_pwm1(servo6_channel, 0, desired_pulse)
    pwm1.set_pwm1(servo12_channel, 0, desired_pulse)
    pwm1.set_pwm1(servo14_channel, 0, desired_pulse)
    pwm1.set_pwm1(servo15_channel, 0, desired_pulse)
    # turn on HPP
    time.sleep(seconds_running)

    pwm1.set_pwm1(servo6_channel, 0, min_pulse)
    pwm1.set_pwm1(servo12_channel, 0, min_pulse)
    pwm1.set_pwm1(servo14_channel, 0, min_pulse)
    pwm1.set_pwm1(servo15_channel, 0, min_pulse)
    # turn off HPP
    time.sleep(seconds_stopping)

def harvesting(seconds1, seconds2, seconds3, seconds4, seconds5, seconds6):
    pwm1.set_pwm1(servo2_channel, 0, desired_pulse)
    # turn on P1
    time.sleep(seconds1)
    pwm1.set_pwm1(servo2_channel, 0, min_pulse)
    # turn off P1
    time.sleep(seconds2)

    pwm1.set_pwm1(servo3_channel, 0, desired_pulse)
    pwm1.set_pwm1(servo8_channel, 0, desired_pulse)
    pwm1.set_pwm1(servo11_channel, 0, desired_pulse)
    pwm1.set_pwm1(servo13_channel, 0, desired_pulse)
    pwm1.set_pwm1(servo15_channel, 0, desired_pulse)
    #HPP on
    time.sleep(seconds3)

    pwm1.set_pwm1(servo3_channel, 0, min_pulse)
    pwm1.set_pwm1(servo8_channel, 0, min_pulse)
    time.sleep(seconds4)

    pwm1.set_pwm1(servo7_channel, 0, desired_pulse)
    time.sleep(seconds5)

    pwm1.set_pwm1(servo7_channel, 0, min_pulse)
    pwm1.set_pwm1(servo11_channel, 0, min_pulse)
    pwm1.set_pwm1(servo13_channel, 0, min_pulse)
    pwm1.set_pwm1(servo15_channel, 0, min_pulse)
    time.sleep(seconds6)
