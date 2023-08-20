from kubernetes import client, config

def create_deployment(api_instance):
    deployment = client.V1Deployment(
        metadata=client.V1ObjectMeta(name="my-flask-app"),
        spec=client.V1DeploymentSpec(
            replicas=1,
            selector=client.V1LabelSelector(match_labels={"app": "my-flask-app"}),
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(labels={"app": "my-flask-app"}),
                spec=client.V1PodSpec(
                    containers=[
                        client.V1Container(
                            name="my-flask-container",
                            image="069684535409.dkr.ecr.us-east-1.amazonaws.com/my_cloud_native_monitoring_app_image",
                            ports=[client.V1ContainerPort(container_port=5000)]
                        )
                    ]
                )
            )
        )
    )
    api_instance.create_namespaced_deployment(namespace="default", body=deployment)

def create_service(api_instance):
    service = client.V1Service(
        metadata=client.V1ObjectMeta(name="my-flask-service"),
        spec=client.V1ServiceSpec(
            selector={"app": "my-flask-app"},
            ports=[client.V1ServicePort(port=5000)]
        )
    )
    api_instance.create_namespaced_service(namespace="default", body=service)

def main():
    config.load_kube_config()
    api_client = client.ApiClient()
    apps_v1_api = client.AppsV1Api(api_client)
    core_v1_api = client.CoreV1Api(api_client)
    create_deployment(apps_v1_api)
    create_service(core_v1_api)

if __name__ == "__main__":
    main()
