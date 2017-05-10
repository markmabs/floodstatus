import RPi.GPIO as GPIO

# BCM to WiringPi pin numbers
P0 = 17 # GREEN LED pin
P00 = 27 # YELLOW LED pin
P000 = 22 # RED LED pin

P1 = 18 # LEVEL1 Button pin
P11 = 23 # LEVEL2 Button pin
P111 = 24 # LEVEL3 Button pin

def Init():
    GPIO.setwarnings(False) # suppress GPIO used message
    GPIO.setmode(GPIO.BCM) # use BCM pin numbers
    
    GPIO.setup(P0, GPIO.OUT) # set GREEN LED pin as output
    GPIO.setup(P00, GPIO.OUT) # set YELLOW LED pin as output
    GPIO.setup(P000, GPIO.OUT) # set RED LED pin as output
    
    
    # also use internal pull-up so we don't need external resistor
    GPIO.setup(P1, GPIO.IN, pull_up_down=GPIO.PUD_UP)# set LEVEL1 button pin as input
    GPIO.setup(P11, GPIO.IN, pull_up_down=GPIO.PUD_UP)# set LEVEL2 button pin as input
    GPIO.setup(P111, GPIO.IN, pull_up_down=GPIO.PUD_UP)# set LEVEL3 button pin as input
    
def greenon():
    GPIO.output(P0, GPIO.HIGH)
def greenoff():
    GPIO.output(P0, GPIO.LOW)
def yellowon():
    GPIO.output(P00, GPIO.HIGH)
def yellowoff():
    GPIO.output(P00, GPIO.LOW)
def redon():
    GPIO.output(P000, GPIO.HIGH)
def redoff():
    GPIO.output(P000, GPIO.LOW)
   
def ReadButton():    
    if  GPIO.input(P1)==0 and GPIO.input(P11)==1 and GPIO.input(P111)==1:
        greenon()
        yellowoff()
        redoff()
        return True
    
    if  GPIO.input(P1)==1 and GPIO.input(P11)==1 and GPIO.input(P111)==1:
        greenoff()
        yellowoff()
        redoff()
        return False
    
def ReadButton1():   
    if  GPIO.input(P1)==0 and GPIO.input(P11)==0 and GPIO.input(P111)==1:
        greenoff()
        yellowon()
        redoff()
        return True
    
   
    
def ReadButton11():   
    if  GPIO.input(P1)==0 and GPIO.input(P11)==0 and GPIO.input(P111)==0:
        greenoff()
        yellowoff()
        redon()
        return True
    

    
