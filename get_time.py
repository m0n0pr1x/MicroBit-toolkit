from microbit import *

def render_time(millis=running_time()):
    seconds=int((running_time()/1000)%60)
    minutes=int((running_time()/(1000*60))%60)
    hours  =int((running_time()/(1000*60*60))%24)
    return hours, minutes, seconds

while True:
    print("H{}M{}S{}".format(*[render_time()[i] for i in range(len(render_time()))]))
    display.scroll("H{}M{}S{}".format(*[render_time()[i] for i in range(len(render_time()))]))