processes = []
pid_counter = 1


def run_process(name):
    global pid_counter

    process = {
        "pid": pid_counter,
        "name": name,
        "status": "RUNNING"
    }

    processes.append(process)

    print("Process started.")
    print(f"PID: {pid_counter}")

    pid_counter += 1


def list_processes():

    if len(processes) == 0:
        print("No running processes.")
        return

    print("\nPID\tNAME\tSTATUS")

    for p in processes:
        print(f"{p['pid']}\t{p['name']}\t{p['status']}")


def kill_process(pid):

    for p in processes:
        if p["pid"] == pid:
            processes.remove(p)
            print(f"Process {pid} terminated.")
            return

    print("Error: Process does not exist.")