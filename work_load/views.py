import json
import subprocess
import yaml
from django.http import JsonResponse
from kubernetes import client, config

from django.shortcuts import render

# Create your views here.
"""
通过ns名称获取deployment
"""


def get_deploy(request):
    try:
        ns = request.GET.get('ns')
        cmd = "kubectl get deploy -n " + ns + " --output=json"
        output = subprocess.check_output(cmd, shell=True)
        deploys_info = json.loads(output)
        json_info = {"code": 200, "message": "success", "result": deploys_info}
        return JsonResponse(json_info)
    except Exception as e:
        json_info = {"code": 500, "message": str(e)}
        return JsonResponse(json_info)


"""
基础deployment模板方法,生成yml,内部容器名就是容器镜像名,这里deployment标签和Pod标签统一
"""


def base_deploy_yml(name, labels, replicas, image, containerPort):
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
                "matchLabels": labels
            },
            "template": {
                "metadata": {
                    "labels": labels
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


"""
通过表单创建一个deployment
"""


def create_deploy(request):
    try:
        form_info = json.loads(request.body)
        yaml_info = base_deploy_yml(form_info["name"], form_info["labels"], form_info["replicas"], form_info["image"],
                                    form_info["containerPort"])
        yaml_data = yaml.safe_load(yaml_info)
        # 加载k8s集群配置
        config.load_kube_config()
        # 创建api客户端
        api_instance = client.AppsV1Api()
        api_instance.create_namespaced_deployment(body=yaml_data, namespace=form_info["namespace"])

        return JsonResponse({"code": 200, "message": "Deployment: " + form_info["name"] + " 成功创建"})
    except Exception as e:
        json_info = {"code": 500, "message": str(e)}
        return JsonResponse(json_info)


"""
删除资源
"""


def delete_resource(request):
    try:
        post_info = json.loads(request.body)
        namespace = post_info["namespace"]
        type = post_info["type"]
        name = post_info["name"]
        cmd = "kubectl delete " + type + " " + name + " -n " + namespace
        output = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        output = output.replace('"', '')
        json_info = {"code": 200, "message": f"{output}"}
        return JsonResponse(json_info)
    except Exception as e:
        json_info = {"code": 500, "message": f"{e}"}
        return JsonResponse(json_info)
