import json

from django.shortcuts import render
from django.http import JsonResponse
import subprocess


# Create your views here.
def get_ns(request):
    try:
        cmd = "kubectl get ns --output=json"
        output = subprocess.check_output(cmd, shell=True)
        ns_info = json.loads(output)
        json_info = {"code": 200, "message": "success", "result": ns_info}
        return JsonResponse(json_info)
    except Exception as e:
        json_info = {"code": 500, "message": f"{e}"}
        return JsonResponse(json_info)
