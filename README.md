# Flask demo app

## Install anaconda

[Anaconda](https://www.continuum.io/downloads)

## Create virtual environment from file

Use [environment.yml](environment.yml) to create a conda environment

```bash
conda env create -f environment.yml
```

## Running python application

```bash
python app.py
```

```output
 * Running on http://0.0.0.0:5000/
 * Restarting with reloader
```

You can see the app working at [http://localhost:5000/](http://localhost:5000/)

## Issues
After closing the web application you have to kill the process by grepping for 'python app.py' and kill it

```bash
ps aux | grep "python app.py"
```

```output
username           554  12.0  0.4  2767156  64300 s002  S     7:22PM   1:26.78 /Users/username/miniconda3/envs/opencv/bin/python app.py
```


## Reference

- [Conda environment tutorial](http://www.naren.me/2017-02-28-Using-Anaconda-for-creating-virtual-environment/)
- [Conda docs](https://conda.io/docs/using/envs.html)
- [Flask video streaming](https://github.com/miguelgrinberg/flask-video-streaming)