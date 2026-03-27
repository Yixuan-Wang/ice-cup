# `ice-cup-sgl`

> [!WARNING]
> As of now, you need to manually pin `nvidia-cudnn-cu12` to be `>=9.15.0` to resolve a known CuDNN bug.
> ```toml
> [tool.uv]
> override-dependencies = [
>    "nvidia-cudnn-cu12>=9.15.0"
> ]

Prepackaged [SGLang](https://www.sglang.io/) environment recipes.

See the offical [document](https://docs.sglang.io/), [repo](https://github.com/sgl-project/sglang) and [release](https://github.com/sgl-project/sglang/releases) for more details on SGLang and [changelog](./CHANGELOG.md) for prepackaged environment updates.
