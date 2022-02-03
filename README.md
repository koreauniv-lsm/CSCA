# Concept of CSCA (Cache Side Channel Attack / Lab 9: Flush+Reload)
This repository contains two proof-of-concept of cache side-channel attack (i.e., Flush+Reload). 
As all PoCs are only successfully mounted on Intel CPUs with Ubuntu, please checks your environment.
We demonstrated the demos in Ubuntu 16.04 LTS and Intel core i5-7400 3.00 GHz.

## PoC1

## PoC2

The PoC2 probes that the victim accesses the specific target file (i.e., target.txt), repeatedly.
In this demo. the spy and victim achieve a memory sharing on *a target file*.

You can test this PoC2 codes in two ways.

### How to execute the PoC2 (victim: shell command)
<pre>
<code>
$ make

// spy
$ ./spy target.txt

// victim
$ cat target.txt
</code>
</pre>

### How to execute the PoC2 (victim: process)
<pre>
<code>
$ make

// spy
$ ./spy target.txt

// victim
$ ./victim target.txt
</code>
</pre>

<br>


## Reference

* **cacheutils.h** is based on [IAIK/flush_flush][iaikff]

[iaikff]: https://github.com/IAIK/flush_flush

* **PoC2** is based on [taehunk/simpleFR][simpleFR]

[simpleFR]: https://github.com/taehunk/simpleFR
