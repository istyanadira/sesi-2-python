import time

try:
    while True:
        now = time.localtime()
        ms = int((time.time() % 1) * 1000)
        current_time = time.strftime('%H:%M:%S', now) + f'.{ms:03d}'
        print(f'\r{current_time}', end='', flush=True)
        time.sleep(0.01)
except KeyboardInterrupt:
    print("\nProgram dihentikan.")
