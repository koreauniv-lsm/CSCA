# Concept of CSCA (Cache Side Channel Attack / Lab 9)
This repository contains two proof-of-concept of cache side-channel attack (i.e., Flush+Reload). 
As all PoCs are only successfully mounted on Intel CPUs with Ubuntu, please checks your environment.
We demonstrated the demos in Ubuntu 16.04 LTS and Intel core i5-7400 3.00 GHz.

## Setup
```
$ git clone https://github.com/koreauniv-lsm/CSCA.git
$ cd CSCA
```

<details>
  <summary>
     If you are not a student of Korea University's system security practice course, you need to (click toggle) and install conda and matplotlib as follows. 
  </summary>
  <div markdown="1">
    
    
    $ wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
    $ bash Anaconda3-2019.10-Linux-x86_64.sh
    $ source ~/.bashrc
    $ conda create --name name-of-virtual-env
    $ conda activate name-of-virtual-env
    $ conda install matplotlib
    
  </div>
</details>
    


## PoC1

The PoC1 shows the overall concept for Flush+Reload to operate in one process. (to be extended to Meltdown later)

In the demo, we declare probe_array, which is a set of cache lines, and access only one specific cache line among them, and visually show the difference in latency between accessed and non-accessed cache lines.

In addition, after saving the visually expressed graph, it is sent by e-mail to the user's account. (Using mutt program)

### How to execute the PoC1 
* The target cache line to be input must be entered from 0 to 256. (because probe_array is of size 256 pages) 
```
$ cd poc1
$ ./run.sh {Target_cache_line}
```

### Proceed
* You can check the target cache line, and result of cache line is same (241) 

![image](https://user-images.githubusercontent.com/98804474/152308189-176ff781-cbb3-4720-bb2b-5e8afe12d3f2.png)

* Also you can get an intuitive Flush+Reload image with threshold.

![image](https://user-images.githubusercontent.com/98804474/152308520-71a71cf2-831f-489d-82d8-5718986f7ac4.png)

* Finally, the picture is sent to the e-mail address set by the user.

![image](https://user-images.githubusercontent.com/98804474/152308953-3d5a79ca-28c4-4df7-920e-810697a4248e.png)

* You can check the picture in your mail box (or spam box)

![image](https://user-images.githubusercontent.com/98804474/152309177-d1e9f889-a12b-4294-b915-99841c607571.png)



## PoC2

The PoC2 probes that the victim accesses the specific target file (i.e., target.txt), repeatedly.
In this demo. the spy and victim achieve a memory sharing on *a target file*.

You can test this PoC2 codes in two ways.

### How to execute the PoC2 (victim: shell command)
<pre>
<code>
$ cd poc2
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

* Installing conda is based on [Installing Anaconda in Linux os][link]

[link]: https://outoftheblackbox.site/linux-%EB%A6%AC%EB%88%85%EC%8A%A4%EC%97%90-%EC%95%84%EB%82%98%EC%BD%98%EB%8B%A4-%EC%84%A4%EC%B9%98/

* **cacheutils.h** is based on [IAIK/flush_flush][iaikff]

[iaikff]: https://github.com/IAIK/flush_flush

* **PoC2** is based on [taehunk/simpleFR][simpleFR]

[simpleFR]: https://github.com/taehunk/simpleFR
