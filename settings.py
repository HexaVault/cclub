from types import SimpleNamespace

genPara = SimpleNamespace()
genPara.worldGen = SimpleNamespace()
genPara.biomeMap = SimpleNamespace()

# How many hills should there be. More hill weight means it is more likely to generate hills
genPara.worldGen.hillWeight = 14
# How many mountains ther should be. More mountain weight means they are more likely to generate,
# and means that generation requirements will be more lenient
genPara.worldGen.mountainWeight = 4
# How fragmented should the world be. Higher will mean the world is more fragmented into multiple islands, and vice versa.
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

# How fragmented the world should be. Higher values means biomes are likely to be smaller
genPara.biomeMap.frag = 7
# The minimum size of a biome. Higher values means the smallest biomes will be larger, but will likely have little effect on larger biomes
genPara.biomeMap.minSize = 50
# The maximum size of a biome. Higher values means the largest biomes will be larger, but will likely have little effect on smaller biomes
genPara.biomeMap.maxSize = 7500
# The maximum "temperature" variation between biomes. Higher values means warm/cold biomes might generate near each other
genPara.biomeMap.tempDiff = 7
# The maximum "precipitation" variation between biomes. Higher values means wet/dry biomes might generate near each other
genPara.biomeMap.precipDiff = 7
# What biomes to not generate in the world.
genPara.biomeMap.banList = []
# How much wood should generate. Lower values means sparser forests with less forest biomes, higher means denser forests and more forest biomes
genPara.biomeMap.woodWeight = 15
# How thick beaches should be. Larger values means larger beaches. Beaches always take priority if they meet generation requirements
genPara.biomeMap.beachThickness = 3
# How uniform biomes should be. Lower values generate biomes with more chaotic edges, while higher generate biomes with more linear edges
genPara.biomeMap.uniformity = 45
