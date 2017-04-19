# Flask demo app

## Install anaconda

[Anaconda](https://www.continuum.io/downloads)

## Create virtual environment from file

Use [environment.yml](environment.yml) to create a conda environment

```zsh
conda env create -f environment.yml
```

## Running python application

```zsh
python app.py
```

Output

```zsh
 * Running on http://0.0.0.0:5000/
 * Restarting with reloader
```

You can see the app working at [http://localhost:5000/](http://localhost:5000/)

## Issues

After closing the web application you have to kill the process by grepping for 'python app.py' and kill it

```zsh
ps aux | grep "python app.py"
username           554  12.0  0.4  2767156  64300 s002  S     7:22PM   1:26.78 /Users/username/miniconda3/envs/opencv/bin/python app.py

kill -9 554
```

## TODO

- [ ] [Test Camera with Rest Interface](http://blog.cudmore.io/post/2015/12/06/camera-with-a-rest-interface/)

## Reference

- [Camera with Rest Interface](http://blog.cudmore.io/post/2015/12/06/camera-with-a-rest-interface/)
- [Conda environment tutorial](http://www.naren.me/2017-02-28-Using-Anaconda-for-creating-virtual-environment/)
- [Conda docs](https://conda.io/docs/using/envs.html)
- [Flask video streaming](https://github.com/miguelgrinberg/flask-video-streaming)
- [REST API Http Requests for Humans with Flask](http://www.bogotobogo.com/python/python-REST-API-Http-Requests-for-Humans-with-Flask.php)
- [Building beautiful REST APIs using Flask, Swagger UI and Flask-RESTPlus](http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/)
- [Flask-Restful_S3_File_Upload.py](https://gist.github.com/RishabhVerma/7228939)
- [](http://code.runnable.com/UiPcaBXaxGNYAAAL/how-to-upload-a-file-to-the-server-in-flask-for-python)