# 19-02-2025

# Multi Tasking

# 1. Process Based Multi tasking : Eash Task is a separate independent process
# 2. Thread Based Multi Tasking  : Each task is an independent part of the same program

# OS level

# Threaded : An indepenednt part of program
# A flow of execution is considered as a thread


'''
Threaded : An indepenednt part of program
A flow of execution is considered as a thread
Thread : it is python object

For every thread independent job is available

Gmail Example For Thread : For every request separate thread is allocated by server

'''

# print(__builtins__ )
# print(__cached__ )


# from time import *
# from threading import *

# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi")
#             sleep(1)

# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             sleep(1)

# t1 = Hi()
# t2 = Hello()

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("End")

# from time import sleep
# from threading import Thread

# def print_hi():
#     for _ in range(5):
#         print("Hi")
#         sleep(1)

# def print_hello():
#     for _ in range(5):
#         print("Hello")
#         sleep(1)

# # Creating thread objects
# t1 = Thread(target=print_hi)
# t2 = Thread(target=print_hello)

# # Starting threads
# t1.start()
# t2.start()

# # Ensuring main thread waits for both to finish
# t1.join()
# t2.join()

# print("End")

# from time import sleep, time
# from threading import Thread

# class Hi(Thread):
#     def run(self):
#         for _ in range(5):
#             print("Hi")
#             sleep(1)

# class Hello(Thread):
#     def run(self):
#         for _ in range(5):
#             print("Hello")
#             sleep(1)

# # Measure start time
# start_time = time()

# # Creating threads
# t1 = Hi()
# t2 = Hello()

# # Starting threads
# t1.start()
# t2.start()

# # Ensuring main thread waits for both to finish
# t1.join()
# t2.join()

# # Measure end time
# end_time = time()

# # Print total execution time
# print(f"Total execution time: {end_time - start_time:.2f} seconds")


# from time import time
# from concurrent.futures import ThreadPoolExecutor

# def print_hi():
#     print("Hi")

# def print_hello():
#     print("Hello")

# # Measure start time
# start_time = time()

# # Using ThreadPoolExecutor to run 5 "Hi" and 5 "Hello" calls simultaneously
# with ThreadPoolExecutor() as executor:
#     for _ in range(50000):
#         executor.submit(print_hi)
#         executor.submit(print_hello)

# # Measure end time
# end_time = time()

# # Print total execution time
# print(f"Total execution time: {end_time - start_time:.2f} seconds")

from concurrent.futures import ThreadPoolExecutor
import requests
import time

# List of URLs to scrape
urls = [
    "https://www.example.com",
    "https://www.wikipedia.org",
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
]

# Function to download a webpage
def fetch_page(url):
    print(f"Fetching: {url}")
    response = requests.get(url)  # Simulate web request
    print(f"Completed: {url} - Status Code: {response.status_code}")

# Measure start time
start_time = time.time()

# Using ThreadPoolExecutor to fetch multiple pages concurrently
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(fetch_page, urls)  # Executes fetch_page for each URL

# Measure end time
end_time = time.time()

# Print total execution time
print(f"Total execution time: {end_time - start_time:.2f} seconds")
