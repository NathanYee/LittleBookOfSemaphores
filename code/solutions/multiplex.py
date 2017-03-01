# Rendezvous
in_room = 0
mutex = Semaphore(2)

## Thread A
mutex.wait()
in_room += 1
in_room -= 1
mutex.signal()
# proceed

## Thread B
mutex.wait()
in_room += 1
in_room -= 1
mutex.signal()
# proceed

## Thread C
mutex.wait()
in_room += 1
in_room -= 1
mutex.signal()
# proceed
