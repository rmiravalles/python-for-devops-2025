# Kubernetes CLI

## Overview

For this project, we'll develop a script for a CLI that will help us obtain information about our Kubernetes cluster. With this script, we'll obtain the names of the Pods running in the cluster, and their images. We'll also be able to filter this data by namespace. This CLI will be built with the help of the Kubernetes Python library, which provides a convenient way to interact with the Kubernetes API.

## The Kubernetes Python Client

The [Kubernetes Python client](https://github.com/kubernetes-client/python) is a Python library that allows you to interact with the Kubernetes API. It provides a convenient way to perform operations on Kubernetes resources, such as Pods, Services, Deployments, and more. The library is built on top of the Kubernetes API and provides a Pythonic interface to interact with it.

The Kubernetes Python client is available on [PyPI](https://pypi.org/project/kubernetes/) and can be installed using pip:

```bash
pip install kubernetes
```

## The Kubernetes API

The Kubernetes API is a RESTful API that allows you to interact with the Kubernetes cluster. The API is organized into resources, which represent the different objects in the cluster. Each resource has a set of operations that can be performed on it, such as creating, updating, and deleting resources.
The Kubernetes API is organized into different groups, each of which contains a set of resources.

## The requirements.txt file

The `requirements.txt` file is a standard file used in Python projects to specify the dependencies required for the project. It lists the packages and their versions that need to be installed in order to run the project. The `requirements.txt` file for this project should contain the following lines:

```
kubernetes==32.0.1
tabulate==0.9.0
```
This file specifies the versions of the `kubernetes` and `tabulate` libraries that are required for the project. The `kubernetes` library is used to interact with the Kubernetes API, while the `tabulate` library is used to format the output of the script in a tabular format.

## Understanding the code

```python
from kubernetes import client, config
```

This line imports the `client` and `config` modules from the Kubernetes Python client library. The `client` module provides the API client for interacting with the Kubernetes API, while the `config` module provides functions for loading the Kubernetes configuration.

```python
def main():
    # Load the Kubernetes configuration
    config.load_kube_config()
```

This function loads the Kubernetes configuration from the default location. The configuration file is usually located at `~/.kube/config` and contains the information needed to connect to the Kubernetes cluster, such as the API server URL, authentication credentials, and namespaces.

```python
    # Create a Kubernetes API client
    v1 = client.CoreV1Api()
```

This line creates a Kubernetes API client for the CoreV1 API group. The CoreV1 API group contains the most commonly used resources in Kubernetes, such as Pods, Services, and Namespaces.

```python
    # Get the list of all Pods in the cluster
    pods = v1.list_pod_for_all_namespaces(watch=False)
```

This line retrieves the list of all Pods in the cluster. The `list_pod_for_all_namespaces` method returns a list of Pod objects, which contain information about each Pod, such as its name, namespace, and status. This is the equivalent of running the `kubectl get pods --all-namespaces` command in the CLI.

```python
    # Print the names and images of the Pods
    for pod in pods.items:
        print(f"Pod Name: {pod.metadata.name}, Image: {pod.spec.containers[0].image}")
```

This loop iterates over the list of Pods and prints the name and image of each Pod. The `metadata` attribute contains the metadata of the Pod, such as its name and namespace, while the `spec` attribute contains the specification of the Pod, including the containers and their images.

```python
def get_pod_images(pod) -> list:
    # Get the images of the containers in the pod
    images = []
    for container in pod.spec.containers:
        images.append(container.image)
    return images
```

This function takes a Pod object as an argument and returns a list of the images of the containers in the Pod. The `spec` attribute contains the specification of the Pod, including the containers and their images. The function iterates over the list of containers and appends their images to the list.

We can, however, improve the code by using a list comprehension to create the list of images in a more concise way:

```python
def get_pod_images(pod) -> list:
    # Get the images of the containers in the pod
    return [container.image for container in pod.spec.containers]
```

## Using the tabulate library to format the output

The `tabulate` library is a Python library that allows you to format tabular data in a variety of ways. It can be used to create tables in plain text, HTML, and other formats. The library is available on [PyPI](https://pypi.org/project/tabulate/) and can be installed using pip:

```bash
pip install tabulate
```

## Using the argparse library to parse command-line arguments

The `argparse` library is a Python library that allows you to parse command-line arguments. It provides a convenient way to define the arguments that your script accepts and automatically generates help messages. The library is part of the Python standard library, so you don't need to install it separately.


