def fahr_to_celsius(temp_fahrenheit):
  converted_tmp = (temp_fahrenheit - 32) / 1.8
  return converted_tmp

def temp_classifier(temp_celsius):
  if temp_celsius < -2:#Check from the most strict value.
    return 0
  elif temp_celsius < 2:
    return 1
  elif temp_celsius < 15:
    return 2
  else:
    return 3 