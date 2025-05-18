# sphere_volume(r): a function that computes the volume of a sphere,
# given its radius r.

function sphere_volume(r)
    return (4/3) * pi * r^3
end

# Example usage:
radius = 5.0
volume = sphere_volume(radius)
println("The volume of a sphere with radius $radius is $volume")
# The volume of a sphere with radius 5.0 is 523.5987755982989
