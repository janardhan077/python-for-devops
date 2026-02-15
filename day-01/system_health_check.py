import psutil
def cpu_check () :
    cpu_thershold =int(input("enter the thershold : "))
    disk_thershold = int(input("enter  when u need to get the disk alert :"))
    memory_thershold = int(input(" enter teh memmory thershold :"))
    current_cpu = psutil.cpu_percent(interval=1)
    print("current__cpu",current_cpu)
    current_disk = psutil.disk_usage('/').percent
    print ("current_disk ",current_disk)
    current_memory =psutil.virtual_memory().percent
    print("current_memory" , current_memory)
    if current_cpu >= cpu_thershold & current_disk >= disk_thershold & current_memory > memory_thershold :
        print("the thershold is not normal ......")
    else:
        print ("safe to go ")
