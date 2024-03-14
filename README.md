# LocystSelection Library

LocystSelection is a Python library that provides a flexible selection interface for multiple choices with pagination. It allows users to create selection menus with customizable options and associated functions, making it easy to implement interactive selection processes in Python applications.

## How to Use

- Clone the repository.
- Import the `Selection` class into your Python environment.
- Follow the example code below to create new selection menus and interact with them.

## Usage

```python
import LocystSelection
import os

def Add(x, y):
  return x + y

def Sub(x, y):
  return x - y

def Times(x, y):
  return x * y

def Div(x, y):
  return x / y

def test2():
  input('test2')

def test4():
  input('test4')

# Create a selection menu
operation_selection = LocystSelection.Selection(question='What operation would you like to perform for x: 1 and y: 1? Use ^ to go up and v to go down',
                                selections={'Addition': Add, 'Subtraction': Sub, 'Multiplication': Times, 'divide': Div})

# Interact with the selection menu
getting_input = True
x = 1
y = 1
while getting_input:
    os.system('clear')
    print(operation_selection.get_message())
    user_input = input("> ")
    if not user_input:
        getting_input = False
        if callable(operation_selection.get_choice()):
            print(operation_selection.get_choice()(x, y)) # Calls the selected function
            input()
        else:
            print("Invalid choice, function not available.")
        input()

    elif user_input == "^":
        operation_selection.move_selection(move_integer=-1)
    elif user_input == "v":
        operation_selection.move_selection(move_integer=1)
    else:
        print('invalid choice')
```

## Configuration

The `Selection` class supports the following configurations:

- `question`: The question or prompt to display at the top of the selection menu.
- `selections`: A dictionary containing the options available for selection, where the keys are the option names and the values are the associated functions.
- `unselect`: Optional parameter to specify the symbol for unselected options (default is '○').
- `select`: Optional parameter to specify the symbol for selected options (default is '●').
- `questions_per_page`: Optional parameter to specify the number of questions to display per page in the selection menu (default is 5).

## To-do

- Add a way to dynamically change the message
