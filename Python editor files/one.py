#one.py

def func():
  print('FUNCTION IN ONE.PY')

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
  print('ONE.PY IS BEING RUN DIRECTLY!')
else:
  print('ONE.PY IS BEEN IMPORTED')