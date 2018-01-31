height = 100
bouncetime = 10
routes = 0
for i in range(bouncetime):
    height = 0.5 * height
    routes += height * 2
totalroutes = routes + 100
print(height)
print(totalroutes)
