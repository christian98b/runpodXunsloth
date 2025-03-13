This is an unofficial image that uses the jupyterhub RunPod image with cuda12.4 and pytorch 2.4 and preinstalls unsloth.

Runpod template:
https://runpod.io/console/deploy?template=za4ivljvyt&ref=2rmge3zj

dockerhub:
https://hub.docker.com/repository/docker/district987/runpodxunsloth

Build it yourself:

`docker build -t yourusername/yourimage:vX.X.X .`

In case you want to push it to the hub:

`docker push yourusername/yourimage:tag`
