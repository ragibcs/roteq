# Roteq

**Roteq** is a simple and lightweight Python package that lets you render websites and YouTube videos directly inside Jupyter Notebook (`.ipynb`) cells.

It helps you create more interactive notebooks by embedding external web content seamlessly.

---

## 🚀 Features

* 🌐 Render any website inside a notebook
* ▶️ Embed YouTube videos with a single function call
* 📓 Works with Jupyter Notebook & JupyterLab
* ⚡ Minimal and easy-to-use API
* 🧩 No heavy dependencies

---

## 📦 Installation

Install from PyPI:

```bash
pip install roteq
```

Or install from source:

```bash
git clone https://github.com/ragibcs/roteq.git
cd roteq
pip install .
```

---

## 🧑‍💻 Usage

### Render a Website

```python
from roteq import render_site

render_site("https://example.com")
```

---

### Embed a YouTube Video

```python
from roteq import render_youtube

render_youtube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
```

---

### Advanced: Custom Iframe

```python
from roteq import display_iframe

display_iframe(
    url="https://example.com",
    width=800,
    height=400
)
```

---

## ⚙️ How It Works

Roteq uses HTML iframe rendering inside Jupyter environments to display external content directly within notebook cells.

---

## 📁 Project Structure

```
roteq/
│── roteq/
│   ├── __init__.py
│   ├── core.py
│   └── utils.py
│
├── examples/
├── tests/
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

## 📌 Use Cases

* 📊 Data science reports with embedded references
* 🎓 Educational notebooks with video content
* 📖 Interactive tutorials
* 🧪 Experiment dashboards

---

## ⚠️ Limitations

* Some websites block iframe embedding (X-Frame-Options / CSP)
* Requires internet connection
* Performance depends on notebook environment

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`feature-name`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 🐛 Issues

If you find bugs or want new features, open an issue on GitHub.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you find this project useful, give it a ⭐ on GitHub!
