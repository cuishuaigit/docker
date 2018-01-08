#!/usr/bin/env python
#__author:  CuiShuai
#date: 2018/1/8

import requests
import  json
import traceback

repo_ip = '10.10.229.43'
repo_port = 5000

def getImagesname(repo_ip,repo_port):
    docker_images = []
    try:
        url = "http://" + repo_ip + ":" + str(repo_port) + "/v2/_catalog"
        recv = requests.get(url).content.strip()
        recv_dic = json.loads(recv)
        images_type = recv_dic['repositories']
        for i in images_type:
            url = "http://" + repo_ip + ":" + str(repo_port) + "/v2/" + str(i) + "/tags/list"
            recv = requests.get(url).content.strip()
            recv_dic = json.loads(recv)
            image_name = recv_dic['name']
            image_tag = recv_dic['tags']
            for i in image_tag:
                docker_name = repo_ip + ":" + str(repo_port) +  "/" + image_name + ":" + i
                docker_images.append(docker_name)
        print(docker_images)
    except:
        traceback.print_exc()
    return docker_images
a=getImagesname(repo_ip,repo_port)
