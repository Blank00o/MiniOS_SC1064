TOTAL_MEMORY = 1024
used_memory = 0


def memory_status():
    free_mem = TOTAL_MEMORY - used_memory

    print("\nMemory Status")
    print("-" * 25)
    print(f"Total Memory: {TOTAL_MEMORY} MB")
    print(f"Used Memory : {used_memory} MB")
    print(f"Free Memory : {free_mem} MB")


def allocate(size):
    global used_memory

    if used_memory + size > TOTAL_MEMORY:
        print("Not enough memory.")
        return

    used_memory += size
    print(f"{size} MB allocated.")


def free_memory(size):
    global used_memory

    if size > used_memory:
        print("Cannot free memory.")
        return

    used_memory -= size
    print(f"{size} MB released.")