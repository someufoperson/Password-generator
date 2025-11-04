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
|--symbols|Indicates the need to use additional characters|

Additional characters: !@#$%^&*()-_=+[]{}<>?,./:;

## 💻 Use from terminal

If you need to quickly run a script directly from the terminal with specified parameters, then these instructions are for you.

1. Open PowerShell in the folder where `pyproject.toml` is located.
2. Install the package (without a virtual machine):
``` Python
py -m pip install --user .
```
3. All that remains is to add the folder with scripts to PATH on Windows so that the gen_pass command is available from any terminal.
```
setx PATH "%PATH%;%USERPROFILE%\AppData\Roaming\Python\Python313\Scripts"
```
4. Try this shit
```
gen_pass --length 25 --symbols
```