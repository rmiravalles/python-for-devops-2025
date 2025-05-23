#Alert router

For this project, we will create an alert router to route alerts to a channel. The alert router is a simple service that listens for alerts and routes them to the appropriate channel based on the alert type. The alert router will be implemented in Python and will use the FastAPI framework to create a REST API.

We'll use three tools to implement the monitoring system:
- **Prometheus**: A monitoring system and time series database.
- **Alertmanager**: A tool to handle alerts generated by Prometheus.
- **cadvisor**: A tool to monitor container metrics and expose them to Prometheus.

## The docker-compose file
The docker-compose file will define the services we need to run the monitoring system. The file will include the following services:
- **Prometheus**: The monitoring system and time series database.
- **Alertmanager**: The tool to handle alerts generated by Prometheus.
- **cadvisor**: The tool to monitor container metrics and expose them to Prometheus.
- **alert-router**: The alert router service that will route alerts to the appropriate channel.

The Prometheus, Alertmanager, and cadvisor services use the official Docker images. The alert-router service will be built from the Dockerfile in the alert-router directory.

## Containerizing the alert-router

The alert-router service will be containerized using Docker. The Dockerfile will define the image for the alert-router service. The image will be based on the official Python image and will include the FastAPI framework and the required dependencies.

The Dockerfile will also include the following steps:
- Copy the source code to the image.
- Install the required dependencies.
- Expose the port for the FastAPI service.
- Set the command to run the FastAPI service using uvicorn.

### The alert-router service will be built using the following command:
```bash
docker build -t alert-router:test .
```
### The alert-router service will be run using the following command:
```bash
docker run -d -p 8000:8000 alert-router:test
```

After adding the alert-router service to the docker-compose file, we can run the following command to start all the services:
```bash
docker-compose build
docker-compose up -d
```