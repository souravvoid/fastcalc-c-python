
---

````markdown
# ⚡ FastCalc: A Fast Arithmetic Engine Using C + Python

**FastCalc** is a beginner-friendly yet powerful project that connects **Python with C** using the `ctypes` module.  
It acts like a mini version of how **NumPy**, **PyTorch**, and other high-performance libraries speed up Python code using C under the hood.

> 🧠 I built this to **understand how C functions can be used inside Python** for speed — just like real libraries do.

---

## 📦 What This Project Does

- Handles **addition**, **subtraction**, **multiplication**, and **division**
- Takes two numbers and an operator (`+`, `-`, `*`, `/`) as input
- Uses **C** for fast backend arithmetic
- Uses **Python** for user-friendly input/output
- Supports **floating-point numbers** (like `3.3`, `5.5`)
- Works in **Linux** and **Windows (via WSL or MinGW)**

---

## 🤔 Why I Built It — Motivation

> Libraries like **NumPy**, **PyTorch**, and **TensorFlow** use C/C++ for their performance-critical code.  
> I wanted to **learn how this performance bridge works** by building a basic version myself — where Python imports a `.so` (Linux) or `.dll` (Windows) and calls native C functions.

This project helped me understand:

- ✅ How to write C functions for speed  
- ✅ How to load compiled C code into Python using `ctypes`  
- ✅ How real-world libraries connect low-level and high-level logic  

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

#### Step 2: Compile the C Code

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

* [Install Python 3](https://www.python.org)
* [Install MinGW](https://www.mingw-w64.org/)

#### Step 2: Compile `calc.c` into DLL

```bash
gcc -shared -o calc.dll -Wl,--out-implib,libcalc.a calc.c
```

#### Step 3: Modify `main.py` for Windows

Replace:

```python
from ctypes import CDLL
lib = CDLL('./calc.so')
```

With:

```python
from ctypes import WinDLL
lib = WinDLL('./calc.dll')
```

#### Step 4: Run the Python File

```bash
python main.py
```

---

## 🧠 Limitations (for now)

* 🚫 No error handling for divide-by-zero (returns 0 silently)
* 🚫 No support for complex expressions like `a + b * c` (just two numbers)
* 🚫 CLI-only (no GUI or web app — yet!)

---

## 📁 Project Structure

```
fastcalc-c-python/
├── calc.c             # C backend logic
├── calc.so / calc.dll # Compiled shared library (Linux / Windows)
├── main.py            # Python frontend logic
└── README.md          # You're here
```

---

## ✅ Sample Output

```
Enter the value of a: 3.3
Enter the value of b: 4.7
Enter operation (+, -, *, /): *
Result: 15.51
```

---

## 👨‍💻 Author

Built with ❤️ by **Sourav**

📫 [Connect with me on LinkedIn](https://www.linkedin.com/in/sourav-873471302/)

---

> ⭐ If this helped you understand how C and Python work together — feel free to star the repo and share it with friends!

````

---

✅ Now you can:

1. **Save this content to `README.md`**
2. Then use:

```bash
git add README.md
git commit -m "Update README with full guide, usage, and motivation"
git push
````



