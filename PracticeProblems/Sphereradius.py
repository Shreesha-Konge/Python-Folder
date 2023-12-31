# Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    result= (4/3) * (3.14) * (rad**3)
    return result
rad=int(input('Enter radius: '))
print(vol(rad))
