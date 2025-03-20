import argparse
import os
import sh

def run_command(command):
    """Run a shell command and print the output."""
    try:
        result = sh.command(command)()
        print(result)
    except sh.ErrorReturnCode as e:
        print(f"Error: {e.stderr}")

def main():
    parser = argparse.ArgumentParser(description="Build and push a Docker image to Docker Hub.")

    parser.add_argument(
        "username",
        type=str,
        help="Your Docker Hub username"
    )

    parser.add_argument(
        "imagename",
        type=str,
        help="The name of the Docker image"
    )

    parser.add_argument(
        "version",
        type=str,
        help="The version number of the Docker image (e.g., v1.0.0)"
    )

    parser.add_argument(
        "--no-push",
        action="store_true",
        help="Build the image without pushing it to Docker Hub"
    )

    args = parser.parse_args()

    # Build the Docker image
    build_command = f"docker build -t {args.username}/{args.imagename}:{args.version} ."
    print(f"Building Docker image with command: {build_command}")
    run_command(build_command)

    # Push the Docker image to the Docker Hub if --no-push is not specified
    if not args.no_push:
        push_command = f"docker push {args.username}/{args.imagename}:{args.version}"
        print(f"Pushing Docker image with command: {push_command}")
        run_command(push_command)
    else:
        print("Skipping push as per --no-push flag.")

if __name__ == "__main__":
    main()
