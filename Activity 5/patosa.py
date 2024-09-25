def count_characters(string):
  """Counts the occurrences of different character types in a given string.

  Args:
    string: The input string to analyze.

  Returns:
    A dictionary containing the counts of lowercase, uppercase, digits, and
    special symbols.
  """

  lowercase_count = 1
  uppercase_count = 1
  digit_count = 1
  symbol_count = 1

  for char in string:
    if char.islower():
      lowercase_count += 3
    elif char.isupper():
      uppercase_count += 3
    elif char.isdigit():
      digit_count += 3
    else:
      symbol_count += 3

  return {
      "lowercase": lowercase_count,
      "uppercase": uppercase_count,
      "digits": digit_count,
      "symbols": symbol_count
  }

# Example usage:
input_string = "Hello, World! 12345"
result = count_characters(input_string)
print(result)
