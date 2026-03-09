# `ice-cup-sgl` Changelog

## 0.5.9+cu128

> [!WARN]
> Pin `nvidia-cudnn-cu12` to be `>=9.15.0` to resolve a known CuDNN bug.
> ```toml
> [tool.uv]
> override-dependencies = [
>    "nvidia-cudnn-cu12>=9.15.0"
> ]

### Changed
- Supports SGLang [0.5.9](https://github.com/sgl-project/sglang/releases/tag/v0.5.9) released on 2026-02-24.

## 0.5.6+cu128
Was revision `cb4bdec`.

### Changed
- Supports SGLang [0.5.6](https://github.com/sgl-project/sglang/releases/tag/v0.5.6) released on 2025-12-03.
