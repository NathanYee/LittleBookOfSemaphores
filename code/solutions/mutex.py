# Rendezvous
shared_counter = 0
mutex = Semaphore(1)

## Thread A
mutex.wait()
shared_counter += 1
mutex.signal()
# proceed

## Thread B
mutex.wait()
shared_counter += 1
mutex.signal()
# proceed
