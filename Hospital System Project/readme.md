# Hospital Patient Queue Management System

The Hospital Patient Queue Management System is a Python-based command-line application designed to manage patient queues in a hospital. It utilizes object-oriented programming (OOP) principles and includes three main classes: `Patient`, `Specialization`, and `OperationsManager`. This project provides a simple yet effective way to handle patient data and queue management within a hospital setting.

The Hospital Patient Queue Management System is an illustration of OOP concepts in Python. It consists of three primary classes, each serving a specific purpose:

### Patient

The `Patient` class represents an individual patient and includes the following attributes:

- `name`: The name of the patient.
- `status`: The patient's status, which can be 0 (normal), 1 (urgent), or 2 (super-urgent).

This class provides methods for string representation and status formatting for patients.

### Specialization

The `Specialization` class manages patient queues within different specializations. It offers functionalities such as:

- Adding patients with various urgency levels.
- Retrieving the next patient from the queue.
- Removing patients by name.
- Checking queue capacity.

### OperationsManager

The `OperationsManager` class serves as the user interface for interacting with the `Specialization` instances. Users can perform actions like:

- Adding new patients to specializations.
- Listing patients in specializations.
- Retrieving the next patient.
- Removing patients.
- Ending the program gracefully.

