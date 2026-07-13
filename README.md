# 🚀 PyChronicle

> **A Python Time Travel Debugger using Abstract Syntax Tree (AST)**

PyChronicle is a Python-based **Time Travel Debugger** that records the execution of a Python program and allows users to inspect previous execution states.

Instead of only debugging step-by-step in the forward direction, PyChronicle captures runtime execution events, stores them in a SQLite database, and enables users to navigate backward and forward through the execution timeline.

---

# 📌 Project Objectives

- Parse Python source code using AST
- Rewrite AST for runtime tracing
- Capture runtime execution events
- Store execution history in SQLite
- Reconstruct previous program states
- Navigate through execution timeline
- Provide a Terminal-based debugging interface

---

# ✨ Features

- ✅ AST Parsing
- ✅ AST Rewriting
- ✅ Runtime Tracing
- ✅ SQLite Storage
- ✅ Timeline Navigation
- 🔄 State Reconstruction
- 🔄 Variable Replay
- 🔄 Snapshot Generation
- 🔄 Terminal UI
- 🔄 Timeline Visualization

---

# 🛠️ Tech Stack

- Python 3.x
- AST (Abstract Syntax Tree)
- SQLite
- Git & GitHub
- VS Code

---

# 📁 Project Structure

```text
PyChronicle/
│
├── examples/
│
├── src/
│   ├── ast_engine/
│   ├── storage/
│   ├── tracer/
│   ├── ui/
│   └── utils/
│
├── main.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Banumister/PyChronicle.git
```

Move into the project

```bash
cd PyChronicle
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 🔄 Workflow

```text
Python Program
       │
       ▼
 AST Parser
       │
       ▼
 AST Rewriter
       │
       ▼
 Runtime Tracer
       │
       ▼
 SQLite Storage
       │
       ▼
 Timeline Navigation
       │
       ▼
 State Reconstruction
       │
       ▼
 Terminal User Interface
```

---

# 📈 Current Progress

## ✅ Completed (Implemented)

- Project Setup
- GitHub Setup
- AST Parser
- AST Rewriter
- Runtime Tracer
- SQLite Storage
- Timeline Navigation
- Initial Program State

---

## 🚧 Remaining Work

- State Reconstruction
- Variable Replay
- Snapshot Generation
- Time-Travel Debugging
  - Step Forward
  - Step Backward
  - Jump to Event
  - Restore Previous Program State
- Terminal User Interface
- Timeline Visualization
- User Interaction
- Testing
- Documentation
- Integration Testing
- Bug Fixing
- Final Project Packaging

## 🚀 Future Enhancements

- GUI support
- Variable history visualization
- Breakpoint support
- Export execution timeline

## 🚧 Remaining Work

- State Reconstruction
- Variable Replay
- Snapshot Generation
- Time-Travel Debugging
  - Step Forward
  - Step Backward
  - Jump to Event
  - Restore Previous Program State
- Terminal User Interface
- Timeline Visualization
- User Interaction
- Testing
- Documentation
- Integration Testing
- Bug Fixing
- Final Project Packaging

# 📌 Known Limitations

- Currently supports Python source code only.
- Terminal UI is under development.
- State reconstruction is still in progress.
- Additional testing and optimization are ongoing.

# 👥 Contributors

- Miller
- Purva Raut
- Dharani
- Chandru

# 📄 License

This project is developed as part of the **Infotact Internship Program**.
