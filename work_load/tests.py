import yaml
from collections import OrderedDict


def base_deploy_yml(name, labels, replicas, matchLabels, template_labels, image, containerPort, namespace):
    # 构建YAML字典结构
    yaml_dict = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {
            "name": name,
            "labels": labels
        },
        "spec": {
            "replicas": replicas,
            "selector": {
                "matchLabels": matchLabels
            },
            "template": {
                "metadata": {
                    "labels": template_labels
                },
                "spec": {
                    "containers": [{
                        "name": name,
                        "image": image,
                        "ports": [{
                            "containerPort": containerPort
                        }]
                    }]
                }
            }
        }
    }

    # 将YAML字典转换为字符串
    yaml_content = yaml.dump(yaml_dict, sort_keys=False)

    # 返回生成的YAML内容
    return yaml_content


# 示例用法
if __name__ == "__main__":
    name = "nginx-deployment"
    labels = {"app": "nginx"}
    replicas = 3
    matchLabels = {"app": "nginx"}
    template_labels = {"app": "nginx"}
    image = "nginx:1.14.2"
    containerPort = 80
    namespace = "default"

    deployment_yaml = base_deploy_yml(name, labels, replicas, matchLabels, template_labels, image, containerPort,
                                      namespace)
    print(deployment_yaml)
