started=False
while True:
    command=input("enter the instr").upper()
    if command=='START':
        if started:
            print("already started")
        else:
            print('start the car')
            started=True
        
            
    elif command=='stop':
        if not started:
            print("car already stopped")
        else:
            print('stop the car')
            started=False
    elif command=='quit':
        print('to quit')
        break
    else:
        print('unknown')
        
