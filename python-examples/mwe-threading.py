# import threading
# import time
# import random

# def todo(name):
#     delay = random.uniform(0.1, 5.0)  # Random delay between 0.1 and 5.0 seconds
#     print(f"Thread {name} démarré")
#     time.sleep(delay)
#     print(f"Thread {name} en cours d'exécution après {delay:.2f} secondes")

# threads = []
# for i in range(3):
#     thread = threading.Thread(target=todo, args=(f"#{i+1}",))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# BARRIER
import threading
import time

# Barrière pour 3 threads
barrier = threading.Barrier(3)

def thread_task(name):
    print(f"{name} commence sa tâche")
    time.sleep(1)
    print(f"{name} attend les autres à la barrière")
    barrier.wait()  # Attend ici que 3 threads arrivent
    print(f"{name} continue après la barrière")

# Créer et démarrer les threads
for i in range(3):
    threading.Thread(target=thread_task, args=(f"Thread-{i}",)).start()