from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import random
import time
import math
import urllib.request
import concurrent

if __name__ == "__main__":
    
    print("--------")
    print("Modify list elements")
    
    # # create large list
    large_list = [random.randint(0, 9) for _ in range(99999)]
    
    # standard
    start_time = time.time()
    double_large_list = [2*x for x in large_list]
    print("standard list comprehension took --- %s seconds ---" % (time.time() - start_time))
    
    # threads
    with ThreadPoolExecutor(max_workers=4) as executor:
        start_time = time.time()
        double_func= executor.map(lambda x: 2*x, large_list)
        
        double_large_list = [x for x in double_func]
        print("threads took --- %s seconds ---" % (time.time() - start_time))
    
    # process
    def double(number:int)->int:
        return 2 * number
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        start_time = time.time()
        double_func= executor.map(double, large_list)
        
        double_large_list = [x for x in double_func]
        print("processes took --- %s seconds ---" % (time.time() - start_time))

    # example from docs
    PRIMES = [
        112272535095293,
        112582705942171,
        112272535095293,
        115280095190773,
        115797848077099,
        1099726899285419]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        sqrt_n = int(math.floor(math.sqrt(n)))
        for i in range(3, sqrt_n + 1, 2):
            if n % i == 0:
                return False
        return True

    print("--------")
    print("Prime numbers")
    
    # standard
    start_time = time.time()
    double_large_list = [(number, is_prime(number)) for number in PRIMES]
    print(double_large_list)
    print("standard list comprehension took --- %s seconds ---" % (time.time() - start_time))
    
    # threads
    with ThreadPoolExecutor(max_workers=4) as executor:
        start_time = time.time()
        double_func= executor.map(lambda x: 2*x, large_list)
        
        double_large_list = [x for x in double_func]
        print("threads took --- %s seconds ---" % (time.time() - start_time))
        
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
        
    print("prime multi-processes took --- %s seconds ---" % (time.time() - start_time))

    print("--------")
    print("URL request")
 
    # example from docs
    URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://nonexistent-subdomain.python.org/']
    
    # Retrieve a single page and report the URL and contents
    def load_url(url, timeout):
        with urllib.request.urlopen(url, timeout=timeout) as conn:
            return conn.read()
    
    # standard loop
    start_time = time.time()
    for url in URLS:
        try:
            data = load_url(url, 60)
            print(data.result())
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
    print("url request loop took --- %s seconds ---" % (time.time() - start_time))
    
    
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))
                # When one thread is blocked (e.g., waiting for I/O), the OS can switch to another thread to continue execution.
                # This allows other threads to run while one thread is waiting, improving overall efficiency.
    print("url request threads took --- %s seconds ---" % (time.time() - start_time))
    
    
    def url_multi_process(url):
        try:
            data = load_url(url, 60)
        except Exception as exc:
            return('%r generated an exception: %s' % (url, exc))
        else:
            return('%r page is %d bytes' % (url, len(data)))
    
    # multi-process
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=5) as executor:
        process_requests = executor.map(url_multi_process, URLS)
        for response in process_requests:
            print(response)
        
    print("url request multi-processes took --- %s seconds ---" % (time.time() - start_time))
