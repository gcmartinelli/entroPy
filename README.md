## Entropy
Python binary file entropy visualizer.

Inspired by [Red Balloon](https://youtu.be/zvP2FEfOSsk?t=619)

### Dependencies
* [Python 3](https://python.org)
* [Pillow library](https://python-pillow.org/)
* [Numpy library](https://numpy.org)

### Installation
`pip install -r requirements.txt`

### Running
Run `python entropy.py filename [blocksize:optional]`

Darker areas have lower entropy.

### Example
![17MB binary, 16 blocksize](imgs/ex3.png)
- 17mb binary, blocksize of 16

![17MB binary, 64 blocksize](imgs/ex1.png)
- 17mb binary, blocksize of 64

![17MB binary, 256 blocksize](imgs/ex2.png)
- 17mb binary, blocksize of 256
