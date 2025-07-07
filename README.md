
````
# ⚡ FastCalc: A Fast Arithmetic Engine Using C + Python

**FastCalc** is a beginner-friendly yet powerful project that connects **Python with C** using the `ctypes` module.  
It acts like a mini version of how **NumPy**, **PyTorch**, and other high-performance libraries speed up Python code using C behind the scenes.

> 🧠 I built this to **understand how C functions can be used inside Python** for speed, just like real libraries do.

---

## 📦 What This Project Does

- Handles **addition**, **subtraction**, **multiplication**, and **division**  
- Takes two numbers and an operator as input  
- Uses **C** for fast backend arithmetic  
- Uses **Python** for simple input/output  
- Works in **Linux** and **Windows (with WSL or MinGW)**

---

## 🤔 Why I Built It — Motivation

> Libraries like **NumPy** and **PyTorch** use C/C++ for performance-critical code.  
> I wanted to **learn how this magic works** by building a basic version myself — where Python imports a `.so` or `.dll` and runs native C logic inside it.

This project helped me understand:

- ✅ How to write C functions for speed  
- ✅ How to load compiled code from Python using `ctypes`  
- ✅ How real-world libraries integrate C with Python  

---

## ⚙️ How to Run the Project (Linux / Windows)

### 🐧 Linux (Ubuntu, Debian, Fedora, etc.)

#### Step 1: Install Requirements

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install build-essential python3
````

On Fedora:

```bash
sudo dnf install gcc python3
```

#### Step 2: Compile the C Code to Shared Library

```bash
gcc -shared -fPIC -o calc.so calc.c
```

#### Step 3: Run the Python File

```bash
python3 main.py
```

---

### 🪟 Windows (Using MinGW)

#### Step 1: Install Tools

* [Install Python 3](https://python.org)
* [Install MinGW](https://www.mingw-w64.org/)

#### Step 2: Compile `calc.c` into DLL

```bash
gcc -shared -o calc.dll -Wl,--out-implib,libcalc.a calc.c
```

#### Step 3: Modify `main.py` for Windows

Change:

```python
from ctypes import CDLL
lib = CDLL('./calc.so')
```

To:

```python
from ctypes import WinDLL
lib = WinDLL('./calc.dll')
```

# Step 4: Run the Python File

```bash
python main.py
```

---

# 📁 Project Structure

```
fastcalc-c-python/
├── calc.c             # C backend logic
├── calc.so / calc.dll # Compiled shared library (Linux / Windows)
├── main.py            # Python frontend
└── README.md
```

---

# 🧠 Limitations (for now)

* 🚫 No error handling (e.g., divide-by-zero)
* 🚫 Only works on integers (`int`), not floats yet
* 🚫 CLI-only (no GUI yet)



# 👨‍💻 Author

Built with ❤️ by **Sourav**

📫 [Connect with me on LinkedIn](https://www.linkedin.com/in/sourav-873471302/)



> ⭐ If this helped you understand how C and Python work together — feel free to star the repo and share!

````



