from types import SimpleNamespace

genPara = SimpleNamespace()
genPara.worldGen = SimpleNamespace()
genPara.biomeMap = SimpleNamespace()
genPara.tempPrecip = SimpleNamespace()


## World Generation Options

# How many hills should there be. More hill weight means it is more likely to generate hills
genPara.worldGen.hillWeight = 14
# How many mountains ther should be. More mountain weight means they are more likely to generate,
# and means that generation requirements will be more lenient
genPara.worldGen.mountainWeight = 4
# How fragmented should the world be. Higher values will encourage more landmass splitting and more rivers
genPara.worldGen.islandWeight = 3
# How many structures should be generated.
genPara.worldGen.structureWeight = 3
# How deep water should be. Higher values will mean water is more likely to be deeper
genPara.worldGen.oceanDepths = 3
# How much water there should be. Higher values will mean there is more water and less land.
genPara.worldGen.waterWeight = 5
# How uniform islands should be. Lower values are more chaotic, higher values are smoother.
# THIS SETTING IS SENSITIVE. CHANGING BY EVEN A COUPLE CAN RESULT IN HUGE, UNEXPECTED CHANGES
genPara.worldGen.uniformity = 72
# World Size (length and width)
genPara.worldGen.height = 750
genPara.worldGen.length = 750
# How many small scale rivers should spawn. Higher values will encourage more rivers.
genPara.worldGen.riverWeight = 0.8
# What is the minimum number of rivers we should spawn. Note actual values may be lower as invalid rivers will "die" but still count to this total
genPara.worldGen.minRivers = 8



## Biome generation options

# How fragmented the world should be. Higher values means biomes are likely to be smaller
genPara.biomeMap.frag = 7
# The minimum size of a biome. Higher values means the smallest biomes will be larger, but will likely have little effect on larger biomes
genPara.biomeMap.minSize = 50
# The maximum size of a biome. Higher values means the largest biomes will be larger, but will likely have little effect on smaller biomes
genPara.biomeMap.maxSize = 7500
# The maximum "temperature" variation inside biomes. Higher values means biomes will be less picky about temperature, which can cause cold/hot biomes to generate adjacent to one another
genPara.biomeMap.tempDiff = 7
# The maximum "precipitation" variation inside biomes. Higher values means biomes will be less picky about precipitation, which can cause cold/hot biomes to generate adjacent to one another
genPara.biomeMap.precipDiff = 7
# What biomes to not generate in the world. Ocean is not permitted, and plains will still be the default biome.
genPara.biomeMap.banList = []
# How much wood should generate. Lower values means sparser forests with less forest biomes, higher means denser forests and more forest biomes
genPara.biomeMap.woodWeight = 15
# How thick beaches should be. Larger values means larger beaches. Beaches always take priority if they meet generation requirements
genPara.biomeMap.beachThickness = 3
# How uniform biomes should be. Lower values generate biomes with more chaotic edges, while higher generate biomes with more linear edges
genPara.biomeMap.uniformity = 45



# Generation options for temperature and precipitation maps

# The maximum per tile temperature difference. If adjacent tiles are distant in temperature, this may be ignored.
genPara.tempPrecip.tempDiff = 1
# The maximum tile temperature difference over 20 tiles (Manhattan). Recommended to be about 5x the above value.
genPara.tempPrecip.tempDiffLarge = 5
# The maximum per tile precipitation difference
genPara.tempPrecip.precipDiff = 1
# The maximum tile precipitation difference over 20 tiles (Manhattan). Recommended to be about 5x the above value.
genPara.tempPrecip.precipDiffLarge = 5
# What is considered a "hot" temperature. 0-100 range, must be higher than consideredCold by atleast 2.
genPara.tempPrecip.consideredHot = 65
# What is considered a "cold" temperature. 0-100 range, must be lower than consideredHot by atleast 2.
genPara.tempPrecip.consideredCold = 20
# What is considered a "neutral" temperature. Must be between consideredCold and consideredHot. 0-100 range.
genPara.tempPrecip.consideredNeutral = 50
# How many hot, cold and neutral temperature pips should the temperature map start with.
genPara.tempPrecip.startHot = 5
genPara.tempPrecip.startCold = 5
genPara.tempPrecip.startNeutral = 8
# How far apart should points (minimum) be placed (Manhattan). Note if the algorithm fails 12 times to randomly find a point that is x points away, it will place it anyways.
genPara.tempPrecip.minimumPointDist = 85
