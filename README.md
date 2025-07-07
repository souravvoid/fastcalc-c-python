# fastcalc-c-python
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
- How to write C functions for speed
- How to load compiled code from Python using `ctypes`
- How real-world libraries integrate C with Python
