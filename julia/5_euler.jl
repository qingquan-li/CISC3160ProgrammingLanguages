# euler(): returns the unique positive integer whose square has the form
# 1_2_3_4_5_6_7_8_9_0, where each "_" is a single digit.

function euler()
    # Any 19‐digit integer of the form 1_2_3_...9_0 must lie between
    # 1020304050607080900 and 1929394959697989990
    # Lower and upper bounds for n, derived from
    # 1_020_304_050_607_080_900 <= n^2 <= 1_929_394_959_697_989_990
    low  = Int(ceil(sqrt(1_020_304_050_607_080_900)))
    high = Int(floor(sqrt(1_929_394_959_697_989_990)))

    # Round low up to the next multiple of 10, and high down
    low  += (10 - low  % 10) % 10
    high -=  high % 10

    # Precompile a regex that matches "1?2?3?4?5?6?7?8?9?0", exactly 19 chars
    pat = r"^1.2.3.4.5.6.7.8.9.0$"

    for n in low:10:high
        s = string(n^2)
        # Only 19-digit squares can match
        if length(s) == 19 && occursin(pat, s)
            return n
        end
    end

    error("No solution found")
end

# Example invocation:
println("Solution n = ", euler())
println("n^2 = ", euler()^2)
# Solution n = 1389019170
# n^2 = 1929374254627488900