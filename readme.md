[tf2up.ml](http://tf2up.ml) - TensorFlow 2.0 upgrader service
===
> [![GitHub license](https://img.shields.io/github/license/lc0/tf2up.svg)](https://github.com/lc0/tf2up/blob/master/LICENSE)
> [![Twitter](https://img.shields.io/twitter/url/https/github.com/lc0/tf2up.svg?style=social)](https://twitter.com/intent/tweet?hashtags=TensorFlow&original_referer=http%3A%2F%2Ftf2up.ml%2F&ref_src=twsrc%5Etfw&related=lc0d3r&text=http%3A%2F%2Ftf2up.ml%20-%20%40TensorFlow%202.0%20upgrader%20service%2C%20even%20easier%20upgrade%20to%20%23TensorFlow%202.0%20by%20%40lc0d3r&tw_p=tweetbutton&url=http%3A%2F%2Ftf2up.ml%2F)

<p align="center"><a href="http://tf2up.ml"><img src="./src/static/images/tf2.png" width="250"></a></p>

Idea is to make upgrade process to <strong>TensorFlow</strong> 2.0 of your Jupyter notebooks even easier!<br>

Bookmarklet
===
```
javascript:(function(){ window.open(window.location.toString().replace(/.*github\.com\/(.*)/, 'http://tf2up.ml/\$1')); })()
```

Demo
===
![](http://g.recordit.co/pb20z8rkY0.gif)

How it works
===
This project is standing on the shoulders of giants:
- TensorFlow's [tf_upgrade_v2](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/compatibility) with brand new support of [inline jupyter notebook conversion](https://github.com/tensorflow/tensorflow/pull/25680)
- [nbdime](https://github.com/jupyter/nbdime) for generating nice diffs for before and after
- [Kubernetes + Helm](https://kubernetes.io/) for deploying this tiny service


Contributing
===
In order to run locally:

Main part: we need to build a docker image and run with local `NBDIME_URL`
```sh
make build -e
```
Start nbdime container in a separate terminal
```sh
make nbbuild nbrun
```
Now you can run the docker image with
```sh
make run
```


Kudos
===
Thanks to all amazing people, that in one or another way helped this project:
- [@DynamicWebPaige](https://twitter.com/DynamicWebPaige) for supporting and making TF community awesome
- [Daria Korkuna](https://www.dariakorkuna.com/) for creating the logo
- [Martin Wicke](https://twitter.com/martin_wicke) for TF2, cake, and feedback
- [Jerry Kurata](https://twitter.com/jerrykur) for testing the early versions of the upgrader</li>

Citation
===
```
@misc{sis,
    author = {Sergii Khomenko},
    title = {tf2up.ml: TensorFlow 2.0 upgrader service},
    howpublished = {\url{https://github.com/lc0/tf2up}}
}
```

---
> GitHub [@lc0](https://github.com/lc0) &nbsp;&middot;&nbsp;
> Twitter [@lc0d3r](https://twitter.com/lc0d3r) &nbsp;&middot;&nbsp;
> [Code and Gradients](https://codeand.gradients.ml/)
