# bogosort [![Travis](https://img.shields.io/travis/chunkhang/bogosort.svg)](https://travis-ci.org/chunkhang/bogosort)

An implementation of the infamous [bogosort](https://en.wikipedia.org/wiki/Bogosort), albeit imperfect due to the [pseudorandomness](https://docs.python.org/2/library/random.html#random.shuffle). Briefly, bogosort works by shuffling the list of numbers until it is sorted. Now you can marvel at the miraculous sorting algorithm's simplicity and efficiency. It might take seconds; it might take hours. Take a sip of coffee, and witness real magic at work.

## Note

<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python" width="200px"> </img>
<br/>
bogosort requires [Python 3](http://www.diveintopython3.net/installing-python.html).

## Instructions

Everything is in one file: [bogosort.py](https://raw.githubusercontent.com/chunkhang/bogosort/master/bogosort.py)

```sh
# Download
$ curl -O https://raw.githubusercontent.com/chunkhang/bogosort/master/bogosort.py
# Run
$ python -B bogosort.py
```

## Sample Output

```sh
Numbers (Use space):
8  8  130  90  930  2  1  9  18  123
Starting bogosort...
--------------------------------------------------------------------------------
#0: [8, 8, 130, 90, 930, 2, 1, 9, 18, 123]
#1: [130, 18, 90, 2, 8, 9, 8, 930, 123, 1]
#2: [18, 1, 8, 90, 123, 930, 130, 9, 2, 8]
#3: [8, 90, 9, 18, 123, 8, 930, 1, 2, 130]
#4: [123, 2, 90, 9, 8, 130, 18, 1, 930, 8]
#5: [2, 930, 9, 8, 8, 18, 1, 130, 123, 90]
#6: [8, 18, 90, 8, 2, 130, 9, 930, 1, 123]
#7: [90, 8, 18, 930, 9, 130, 123, 8, 2, 1]
#8: [8, 90, 2, 123, 1, 9, 18, 130, 930, 8]
#9: [8, 130, 1, 930, 123, 18, 90, 9, 8, 2]
#10: [9, 8, 8, 90, 2, 123, 930, 1, 18, 130]
#11: [2, 930, 9, 90, 8, 123, 18, 130, 1, 8]
#12: [8, 930, 123, 18, 130, 9, 90, 2, 8, 1]
#13: [8, 1, 8, 18, 9, 2, 90, 930, 130, 123]
. 
.
.
#1295723: [123, 930, 2, 1, 18, 9, 130, 8, 90, 8]
#1295724: [1, 8, 123, 90, 9, 930, 18, 130, 8, 2]
#1295725: [1, 2, 930, 130, 9, 18, 90, 123, 8, 8]
#1295726: [9, 18, 8, 90, 1, 2, 123, 130, 930, 8]
#1295727: [930, 8, 123, 90, 18, 2, 9, 8, 130, 1]
#1295728: [130, 90, 123, 8, 2, 8, 9, 930, 18, 1]
#1295729: [2, 90, 930, 123, 18, 9, 8, 1, 8, 130]
#1295730: [9, 8, 2, 8, 1, 130, 123, 18, 930, 90]
#1295731: [1, 8, 9, 8, 90, 18, 930, 130, 123, 2]
#1295732: [1, 9, 90, 930, 18, 123, 130, 2, 8, 8]
#1295733: [2, 930, 8, 90, 1, 18, 8, 123, 9, 130]
#1295734: [8, 930, 2, 130, 123, 1, 8, 18, 90, 9]
#1295735: [8, 90, 9, 130, 8, 930, 18, 123, 1, 2]
#1295736: [1, 2, 8, 8, 9, 18, 90, 123, 130, 930]
--------------------------------------------------------------------------------
Bogosort completed for 10 elements.
Shuffles done: 1,295,736
Time elapsed : 17s
```

## Contact

Report bugs or suggest features: <br />
[Marcus Mu](http://marcusmu.me) - chunkhang@gmail.com
