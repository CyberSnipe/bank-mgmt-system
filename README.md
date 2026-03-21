# SecureBank - Bank Management System

**Assignment 3** – SecureBank subsystem with domain-driven design, services, persistence, routing, and CLI menu.

A simple yet structured **bank management system** implemented in Python, demonstrating clean architecture principles:
- Domain models
- Repository pattern for persistence (JSON-based)
- Service layer for business logic
- Basic routing / menu-driven CLI interface

Built as a modular monolith suitable for educational purposes.

## Features

- User authentication (admin / customer roles)
- Account management (create/view accounts, deposit, withdraw, transfer)
- Transaction history
- Basic reporting (balance, transaction summary)
- JSON file persistence (no external database required)
- Menu-driven CLI interface
- Input validation and error handling

## Project Structure

```text
bank_mgmt_system/
├── src/
│   └── bank_mgmt_system/
│       ├── init.py
│       ├── main.py               # CLI entry point & menu loop
│       ├── domain/               # Business entities (User, Account, Transaction)
│       ├── services/             # Business logic (AccountService, TransactionService)
│       ├── repository/           # Data access layer (JSON repositories)
│       ├── routing/              # Menu / command routing logic
│       └── utils.py              # Helpers (input validation, JSON I/O, etc.)
├── data/                         # Runtime data (users.json, accounts.json, transactions.json)
├── tests/                        # Unit tests (pytest)
├── pyproject.toml                # Project metadata & dependencies
├── README.md                     # This file
└── requirements.txt              # For non-PEP-621 environments
```

## Requirements

- Python 3.12+
- Dependencies:
  - numpy
  - pandas
  - pytest (dev)

## Setup Instructions

1. **Clone the repository** (or download ZIP)

   ```bash
   git clone https://github.com/CyberSnipe/bank-mgmt-system
   cd bank_mgmt_system