# Prerequisites
- Docker Desktop
- Minikube (or a similar tool)
- Kubectl
- Helm

# Steps to follow
- Once you're done with prereqs, clone this repo: `git clone https://github.com/hoquenazmul/test-helm-chart.git`
- Navigate to `test-helm-chart` directory, install the helm chart by executing `helm install dj-webapp dj-helm-chart`
- For port-forwarding, run this cmd: `kubectl --namespace default port-forward service/djwebapp 8800:8000`
- then open your favorite browser, go to http://127.0.0.1:8800/demo/

If you're interested in viewing the Dockerfile used to build the `hoquenazmul/hello-dj` image, you can find it [here](https://raw.githubusercontent.com/hoquenazmul/test-helm-chart/main/before-helm-chart/hello_dj/Dockerfile).
