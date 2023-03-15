# https://www.countbayesie.com/blog/2022/11/30/understanding-convolutions-in-probability-a-mad-science-perspective?utm_campaign=Data_Elixir&utm_source=Data_Elixir_416

# distribution f
human_limb_dist = [0.1, 0.21, 0.19, 0.45, 0.05]

# distribution g
crab_limb_dist = [0.025, 0.05, 0.09, 0.12, 0.09, 0.18,
                   0.21, 0.145, 0.04, 0.025, 0.025]

MAX_LIMBS = 14

# distribution h
# list of 0, MAX_LIMBS long
monster_dist = [0]*(MAX_LIMBS + 1)

# Next we'll iterate through each human limb count. 
# For each human limb count we'll look up each crab limb count, 
# sum the total count for our index into the final result 
# and multiply the probabilities, 
# and add that to the existing value in the monster_dist.

# iterate through all possible human limb counts
for human_limb_idx, p_human_count in enumerate(human_limb_dist):
    # then multiply that probability with the corresonding crab limb count
    for crab_limb_idx, p_crab_count in enumerate(crab_limb_dist):
        # this is the index in the monster_dist
        crab_human_sum = human_limb_idx + crab_limb_idx
        p_crab_human_sum = p_human_count * p_crab_count
        monster_dist[crab_human_sum] += p_crab_human_sum
        
def conv_t(f, g, t):
    return sum([
        f[i]*g[t-i] for i in range(len(f))
        # we need do some bounds checking in our code
        if t-i < len(g) and (t-i) >= 0
    ])