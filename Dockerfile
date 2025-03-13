# Use an official runpod runtime as a parent image
FROM runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL=/bin/bash
ENV HF_HUB_ENABLE_HF_TRANSFER=1

RUN pip install --upgrade pip
RUN pip install --no-cache-dir huggingface_hub[hf_transfer]
RUN pip install --no-cache-dir xformers torch BitsandBytes triton transformers accelerate datasets vllm
RUN pip install git+https://github.com/unslothai/unsloth-zoo.git
RUN pip install "unsloth[cu124-torch240] @ git+https://github.com/unslothai/unsloth.git"

# Run start.sh when the container launches
CMD [ "/start.sh" ]