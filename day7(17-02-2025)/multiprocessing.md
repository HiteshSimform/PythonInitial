## **Multiprocessing in Python**

Python’s `multiprocessing` module allows you to run multiple processes in parallel, leveraging multiple CPU cores. This is particularly useful for CPU-bound tasks, as Python’s **Global Interpreter Lock (GIL)** limits threads from executing Python bytecode in parallel.

---

## **🔹 Why Use Multiprocessing?**
- **Utilize multiple CPU cores**: Unlike threading, which is limited by the GIL, multiprocessing creates separate processes, each with its own Python interpreter.
- **Speed up CPU-bound tasks**: Great for tasks like mathematical computations, image processing, and data analysis.
- **Avoid GIL limitations**: Since each process has its own memory space, it runs independently.
- **Parallel execution**: Unlike threads, processes can run truly concurrently.

---

## **🔹 Basics of Multiprocessing**
### **1️⃣ Creating a Process**
You can create a new process using the `multiprocessing.Process` class.

```python
import multiprocessing

def worker():
    """Function to run in a separate process"""
    print("Worker process is running")

if __name__ == "__main__":
    process = multiprocessing.Process(target=worker)
    process.start()  # Start the process
    process.join()   # Wait for process to finish
```

✅ **Explanation**:
- `multiprocessing.Process(target=worker)`: Creates a new process that will run the `worker()` function.
- `start()`: Starts the process.
- `join()`: Ensures the main program waits until the process finishes.

---

### **2️⃣ Using Multiple Processes**
```python
import multiprocessing

def worker(num):
    """Worker function"""
    print(f"Worker {num} is running")

if __name__ == "__main__":
    processes = []
    for i in range(5):  # Create 5 processes
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()  # Ensure all processes complete
```
✅ **Explanation**:
- We create **5 processes**, each executing `worker(i)`.
- `args=(i,)` passes arguments to the function.
- `join()` ensures all processes complete before the script exits.

---

## **🔹 Multiprocessing with Pool (Process Pooling)**
### **3️⃣ Using `multiprocessing.Pool`**
The `Pool` class helps manage multiple processes efficiently.

```python
import multiprocessing

def square(n):
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
    print(results)  # Output: [1, 4, 9, 16, 25]
```
✅ **Why use a Pool?**
- **Automatically manages worker processes**.
- **Distributes tasks efficiently** among processes.

---

### **4️⃣ Using `apply()`**
`apply()` runs a function in one process and returns the result.

```python
import multiprocessing

def cube(n):
    return n ** 3

if __name__ == "__main__":
    with multiprocessing.Pool(processes=2) as pool:
        result = pool.apply(cube, (3,))
    print(result)  # Output: 27
```

✅ **Key Differences**:
- `map()`: Runs a function on a list of values in **parallel**.
- `apply()`: Runs a function on **a single value**, blocking execution.

---

### **5️⃣ Using `apply_async()` for Asynchronous Execution**
```python
import multiprocessing

def power(n):
    return n ** 2

if __name__ == "__main__":
    with multiprocessing.Pool(processes=2) as pool:
        result = pool.apply_async(power, (5,))
        print(result.get())  # Output: 25
```
✅ **Why use `apply_async()`?**
- **Runs in the background** without blocking execution.
- `get()` fetches the result when needed.

---

## **🔹 Inter-Process Communication (IPC)**
Since processes don’t share memory, we use:
1. **Queues** (`multiprocessing.Queue`)
2. **Pipes** (`multiprocessing.Pipe`)
3. **Shared Memory** (`multiprocessing.Value` & `multiprocessing.Array`)

### **6️⃣ Using `Queue` for Process Communication**
```python
import multiprocessing

def worker(q):
    q.put("Hello from Process!")

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()
    print(q.get())  # Fetch data from queue
    p.join()
```
✅ **Why use `Queue`?**
- Allows **safe communication** between processes.
- Ensures data is transferred **without conflicts**.

---

### **7️⃣ Using `Pipe` for Two-Way Communication**
```python
import multiprocessing

def sender(conn):
    conn.send("Hello from sender!")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=sender, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # Output: "Hello from sender!"
    p.join()
```
✅ **Why use `Pipe`?**
- Enables **direct** two-way communication.
- More **lightweight** than a queue.

---

## **🔹 Shared Memory Between Processes**
### **8️⃣ Using `Value` (Shared Variable)**
```python
import multiprocessing

def increment(shared_value):
    shared_value.value += 1

if __name__ == "__main__":
    shared_value = multiprocessing.Value("i", 10)  # Integer with initial value 10
    p = multiprocessing.Process(target=increment, args=(shared_value,))
    p.start()
    p.join()
    print(shared_value.value)  # Output: 11
```
✅ **Why use `Value`?**
- Allows **simple data sharing** between processes.
- Supports basic types (`int`, `float`).

---

### **9️⃣ Using `Array` (Shared List)**
```python
import multiprocessing

def update(shared_array):
    shared_array[0] = 100  # Modify first element

if __name__ == "__main__":
    shared_array = multiprocessing.Array("i", [1, 2, 3])
    p = multiprocessing.Process(target=update, args=(shared_array,))
    p.start()
    p.join()
    print(shared_array[:])  # Output: [100, 2, 3]
```
✅ **Why use `Array`?**
- **Shares lists** between processes.
- **Thread-safe access**.

---

## **🔹 Multiprocessing vs. Multithreading**
| Feature | Multiprocessing | Multithreading |
|---------|---------------|---------------|
| **Parallel Execution** | ✅ Yes (Uses multiple CPUs) | ❌ No (GIL limits Python threads) |
| **Best For** | CPU-bound tasks | I/O-bound tasks |
| **Memory Usage** | Higher (Separate memory space for each process) | Lower (Shared memory) |
| **Overhead** | High (Process creation is expensive) | Low (Threads are lightweight) |

---

## **🔹 When to Use Multiprocessing?**
✅ **Heavy CPU-bound tasks** (e.g., Image processing, Machine learning, Data crunching).  
✅ **Parallel execution required** (Utilizing multiple cores).  
✅ **Avoiding GIL limitations** (Threads can’t run Python bytecode in parallel).  

🚀 **Would you like a real-world example for your project?**