import math


class Selection:

  def __init__(self, selections, question, unselect='○', select='●'):
    self.unselected_symbol = unselect
    self.selected_symbol = select

    self.selections = list(selections.keys())
    self.functions = list(selections.values())
    if len(self.selections) != len(self.functions):
      raise ValueError(
        'The number of selections and functions must be the same.')

    self.question = question

    self.max_selections = len(selections)
    self.selection = 1

    self.questions_per_page = 5
    self.pages = math.ceil(len(self.selections) / self.questions_per_page)
    self.current_page = 1

  def move_selection(self, move_integer):
    """
    Moves the selection by the given integer. Postives go down while negatives go up.

    Parameters:
     - move_integer (int): The integer to move the selection by.
    """
    if move_integer > 0:
      self.selection = min(self.selection + move_integer, self.max_selections)
    if move_integer < 0:
      self.selection = max(self.selection + move_integer, 1)
    self.current_page = math.ceil(self.selection / self.questions_per_page)

  def _is_selected(self, option):
    """
    A helper function that checks if the given option is selected.

    Parameters:
     - option (int): The numberic placement for the current option.

    Returns:
     - bool: True if the option is selected, False otherwise.
    """
    if self.selection == option:
      return self.selected_symbol
    return self.unselected_symbol

  def get_message(self):
    """
    Returns the message for the current page. Automatically grows the message to fit the questions per page.

    Returns:
     - str: The message for the current page.
    """
    message = f'{self.question}\n\n'
    start = (self.current_page - 1) * self.questions_per_page
    end = min(start + self.questions_per_page, self.max_selections)

    for i in range(start, end):
      message += f"{self._is_selected(i+1)} {self.selections[i]}\n"

    if self.pages > 1:
      message += f"\nPage {self.current_page}/{self.pages}"
    return message

  def get_choice(self):
    """
    Returns the function for the current selection. Should be used when the user has made a choice.

    Returns:
     - function: The function for the current selection.
    """
    return self.functions[self.selection - 1]
