import subprocess
data =subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
profiles=[i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
profiles
for i in profiles:
    #running 2nd cmd command by using check_output()
    results=subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear'])
    results=results.decode("utf-8").split("\n")
    #Storing passwords by converting them into a list
    results=[b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    #Printing Wifi names and their corresponding passwords using try and except method
    try:
        print("{:<30} | {:<}".format(i,results[0]))
    except IndexError:
        print("{:<30} | {:<}".format(i,""))






        