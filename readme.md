# Unofficial RunPod Image with CUDA 12.4, PyTorch 2.4, and Preinstalled Unsloth

This is an unofficial Docker image that builds upon the JupyterHub RunPod image. It includes CUDA 12.4, PyTorch 2.4, and preinstalls the Unsloth library.

## RunPod Template

You can deploy this image using the following RunPod template:

[RunPod Template](https://runpod.io/console/deploy?template=za4ivljvyt&ref=2rmge3zj)

## Docker Hub

The image is available on Docker Hub:

[Docker Hub Repository](https://hub.docker.com/repository/docker/district987/runpodxunsloth)

## Building the Image Yourself

If you prefer to build the image yourself, you can use the following commands:

1. **Clone the repository (if applicable):**

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Build the Docker image:**

   ```sh
   docker build -t yourusername/yourimage:vX.X.X .
   ```

   Replace `yourusername` with your Docker Hub username, `yourimage` with the desired image name, and `vX.X.X` with the version number.

3. **Push the Docker image to Docker Hub (optional):**

   ```sh
   docker push yourusername/yourimage:tag
   ```

   Replace `yourusername` with your Docker Hub username, `yourimage` with the image name, and `tag` with the desired tag (e.g., `vX.X.X`).

## Automating the Build and Push Process

To automate the build and push process, you can use the provided Python script `build_and_push.py`. This script uses `argparse` to take the username, image name, and version number as command-line arguments.

### Usage:

```sh
python build_and_push.py yourusername yourimagename vX.X.X
```

### Example:

```sh
python build_and_push.py mydockeruser mypytorchimage v1.0.0
```

### Optional `--no-push` Flag:

To build the image without pushing it to Docker Hub, use the `--no-push` flag:

```sh
python build_and_push.py mydockeruser mypytorchimage v1.0.0 --no-push
```

## Requirements

- Docker installed and configured on your system.
- Docker Hub account (if pushing the image to Docker Hub).
- Python 3.x for running the automation script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [RunPod](https://runpod.io/) for providing the base image.
- [Unsloth](https://github.com/unslothai/unsloth) for the Unsloth library.
