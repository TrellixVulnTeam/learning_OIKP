import os
import multiprocessing


def square(number):
    result = number * number
    #we can use the "os" module in python to print out the Process ID assigned to the call of this function
    #assigned by the operating system
    process_id = os.getpid()

    #we can also use "current_process().name" method to get the name of the process object.
    process_name = multiprocessing.current_process().name

    print(f"Process ID : {process_id}")
    print(f"Proceess_name : {process_name}")
    print(f"The number {number} squares to {result}.")

if __name__ == '__main__':
    processes = []

    for number in range(20):
        process = multiprocessing.Process(target=square,args=(number,))
        processes.append(process)
        #processes are spawned by creaing a Process object and then calling its start() method
        process.start()
