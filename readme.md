# Terminal Logger and Loader

This repository provides a set of utilities for working with terminal-based applications. It includes a terminal logger with different log levels, a custom loader for showing progress in the terminal, and other helpful features for managing console output.

## Features

- **Terminal Class:**
  - `clear()`: Clears the terminal screen.
  - `set_title()`: Sets the terminal window's title (Windows only).
  - `loader()`: Displays a loading spinner with a customizable message.

- **Logger Class:**
  - Custom logging functionality with different log levels: `INFO`, `SUCCESS`, `FAILED`, and `DEBUG`.
  - Option to log messages with timestamps and optional military time formatting.
  - Log output can be printed to the terminal and saved to a file.

- **Customizable Log Levels:**
  - `FAILED`: Represents a failure state.
  - `SUCCESS`: Represents a successful operation.
  - `INFO`: Represents an informational message.
  - `DEBUG`: Represents debug-level messages.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/Dev-Sacrifice/Simple-Console.git
```
