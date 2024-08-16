FROM mcr.microsoft.com/devcontainers/rust:dev-1-bookworm

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential ca-certificates ccache \
    cmake curl libjpeg-dev libpng-dev strace \
    llvm-dev libclang-dev clang ccache apache2-utils git-lfs \
    screen bsdmainutils pip python3-dev python3-venv python-is-python3 \
    nodejs npm pkg-config linux-perf software-properties-common

# install cuda
RUN cd /tmp && \
wget https://developer.download.nvidia.com/compute/cuda/repos/debian12/x86_64/cuda-keyring_1.1-1_all.deb && \
dpkg -i cuda-keyring_1.1-1_all.deb
RUN add-apt-repository -y contrib
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install cuda-toolkit-12-5
ENV PATH="/usr/local/cuda/bin:$PATH"


RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV VIRTUAL_ENV="/opt/venv"

# more packages for this image
RUN pip install \
 torch transformers bitsandbytes \
 pytest ujson numpy requests mypy maturin[zig] \
 guidance huggingface_hub tokenizers jsonschema \
 pandas matplotlib plotly wheel
RUN pip uninstall -y guidance

RUN cargo install rustfilt

USER root