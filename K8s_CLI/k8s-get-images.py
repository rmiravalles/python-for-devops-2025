#!/usr/bin/env python3

# This script lists all pods in all namespaces and their associated container images.

import argparse

from colorama import Fore, Style
from kubernetes import client, config
from kubernetes.client import V1Pod
from tabulate import tabulate


# Load kubeconfig from default location (~/.kube/config)
config.load_kube_config()
v1 = client.CoreV1Api()

# Define the command-line arguments
parser = argparse.ArgumentParser(
    description="List all pods and their images.",
    prog='k8s-get-images.py'
    )
parser.add_argument('--namespace', "-n", type=str, help='Filter pods by namespace')

args = parser.parse_args()

# The table header
header = [
    f"{Fore.GREEN}{Style.BRIGHT}POD NAME{Style.RESET_ALL}",
    f"{Fore.YELLOW}{Style.BRIGHT}IMAGE{Style.RESET_ALL}"
    ]


def get_pods() -> list:
    # Get all pods in all namespaces
    return v1.list_pod_for_all_namespaces().items


def get_pod_images(pod: V1Pod) -> list:
    # Get the images of the containers in the pod
    return [container.image for container in pod.spec.containers]



def string_to_color(string: str, color: str) -> str:
    return f"{Fore.CYAN}{string}{Style.RESET_ALL}"

def main():
    args = parser.parse_args()
    print(args)
    table = []
    for pod in get_pods():
        # Collect pod name and its images
        images = get_pod_images(pod)
        table.append([f"{Fore.GREEN}{Style.BRIGHT}{pod.metadata.name}{Style.RESET_ALL}", ', '.join(images)])

    print(tabulate(table, headers=header))


if __name__ == "__main__":
    main()
