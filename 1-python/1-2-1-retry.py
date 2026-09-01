# this is an example of a retry loop

from time import sleep


def progress(delay: int):
    for i in range(delay):
        if i % 2 == 0:
            print("x", end="", flush=True)
        else:
            print("o", end="", flush=True)
        sleep(1)
        print("\b", end="", flush=True)



TIMES = 5
BACKOFF = 5

print("Starting retry loop...")
for attempt in range(TIMES):
    print(f"Attempt {attempt + 1} of {TIMES}")
    delay = BACKOFF * attempt
    print(f"Sleeping for {delay} seconds before next attempt...")
    #sleep(delay)
    progress(delay)

    print("Retrying...")


