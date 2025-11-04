# 🔑 CLI-generation password
<div align="center"><img src=https://img.shields.io/badge/Python-%3E%3D3.9-blue></div>



<div align="center">
    <img width="96" height="96" src="https://img.icons8.com/liquid-glass/96/password.png" alt="password"/>
</div>

A miniature helper for generating passwords. The standard Python library `secrets` is used instead of `random` to ensure more reliable generation, although it seems like it doesn't matter anyway🙈

## 🚀 Getting Started

### Requirements

- `Python >=3.9`

```cmd
git clone https://github.com/someufoperson/Password-generator/tree/main
```

```
python generation-password.py
```

### Additional parameters

| Parameter | Description |
|-----------|-------------|
|--length 16|Specifies the length of the password to be generated (default is 16 characters)|
|--use-symbols|Indicates the need to use additional characters|

Additional characters: !@#$%^&*()-_=+[]{}<>?,./:;

## Use from terminal
