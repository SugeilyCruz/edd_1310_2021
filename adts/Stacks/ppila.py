from pilas import Stack

pl=Stack()
pl.push('a')
pl.push('x')
pl.to_string()
pl.push('b')
pl.push('y')
pl.to_string()
var=pl.pop()
pl.to_string()
print(f"var={var}")
