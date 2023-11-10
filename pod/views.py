import json
import subprocess
from django.http import JsonResponse

from django.shortcuts import render

# Create your views here.

"""
获取某个ns的Pods
"""


def get_by_ns(request):
    ns = request.GET.get('ns')
    cmd = "kubectl get pod -n " + ns + " --output=json"
    output = subprocess.check_output(cmd, shell=True)
    pods_info = json.loads(output)
    json_info = {"code": 200, "message": "success", "result": pods_info}

    return JsonResponse(json_info)


"""
删除某个Pod 必须删除其控制器
"""

# def delete(request):


"""
传递参数，创建Pod
"""
