[tf2up.ml](http://tf2up.ml) - TensorFlow 2.0 upgrader service
===
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
In order run run locally:

Main part: we need to build docker image and run with local `NBDIME_URL`
```sh
make build -e
```
Start nbdime container in a separate terminal
```sh
make nbrun
```
Now you can run docker image with
```sh
make run NBDIME_URL=http://host.docker.internal:8081/d/
```


Kudos
===
Thanks to all amazing people, that in one or another way helped this project:
- [@DynamicWebPaige](https://twitter.com/DynamicWebPaige) for supporting and making TF community awesome
- [Daria Korkuna](https://www.dariakorkuna.com/) for creating logo
- [Martin Wicke](https://twitter.com/martin_wicke) for TF2, cake, and feedback
- [Jerry Kurata](https://twitter.com/jerrykur) for testing the early versions of the upgrader</li>


---
> GitHub [@lc0](https://github.com/lc0) &nbsp;&middot;&nbsp;
> Twitter [@lc0d3r](https://twitter.com/lc0d3r) &nbsp;&middot;&nbsp;
> [Code and Gradients](https://codeand.gradients.ml/)
