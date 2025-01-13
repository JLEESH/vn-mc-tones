import matplotlib.pyplot as plt
import networkx as nx

# note: the examples are incorrect ; replace with correct examples in the future
# the graphs are also overly simplistic ;
# refer to actual-vn-mc-tones-correspondance.png taken from Wikipedia:
# https://zh.wikipedia.org/wiki/%E5%9B%9B%E8%81%B2
# TODO: enhance factual accuracy

fontname = 'Apple LiGothic'
fontname = ['AppleGothic', 'sans-serif']
fontname = ['Apple LiGothic', 'sans-serif']
plt.rcParams['font.family'] = fontname

# Define Middle Chinese tones and Vietnamese tones
middle_chinese_tones = [
    "Yin Level (陰平)", "Yang Level (陽平)", 
    "Yin Rising (陰上)", "Yang Rising (陽上)", 
    "Yin Departing (陰去)", "Yang Departing (陽去)", 
    "Yin Entering (陰入)", "Yang Entering (陽入)"
]

vietnamese_tones = [
    "Ngang (level)", "Huyền (low falling)", 
    "Hỏi (rising/falling)", "Ngã (broken/rising)", 
    "Sắc (rising)", "Nặng (stopped)", 
    #"Sắc (with /p/, /t/, /k/ finals)", "Nặng (with /p/, /t/, /k/ finals)"
]

# Define voiced and voiceless initials
voiced_initials = ["b", "d", "g", "z", "l", "m", "n", "r", "ng", "v", "zh", "j"]
voiceless_initials = ["p", "t", "k", "s", "ch", "th", "ph", "tr", "h", "c", "q", "x"]

# Define examples for each tone category
examples = {
    "Yin Level (陰平)": ["thiên (天)", "nhân (人)", "quân (君)"],
    "Yang Level (陽平)": ["hành (行)", "tài (才)", "nô (奴)"],
    "Yin Rising (陰上)": ["khả (可)", "bản (本)", "vắn (穩)"],
    "Yang Rising (陽上)": ["ngã (仰)", "thượng (上)", "mễnh (猛)"],
    "Yin Departing (陰去)": ["chứng (証)", "giải (解)", "thiêu (召)"],
    "Yang Departing (陽去)": ["nặng (能)", "hạn (限)", "phạn (飯)"],
    "Yin Entering (陰入)": ["kết (結)", "bạt (拔)", "trực (直)"],
    "Yang Entering (陽入)": ["thực (實)", "phúc (福)", "hục (學)"]
}

# Create a graph
graph = nx.DiGraph()

# Add nodes for Middle Chinese tones and Vietnamese tones
graph.add_nodes_from(middle_chinese_tones, layer="Middle Chinese")
graph.add_nodes_from(vietnamese_tones, layer="Vietnamese")

# Define edges representing transformations
transformations = [
    ("Yin Level (陰平)", "Ngang (level)", "Voiceless initials"),
    ("Yang Level (陽平)", "Huyền (low falling)", "Voiced initials"),
    ("Yin Rising (陰上)", "Hỏi (rising/falling)", "Voiceless initials"),
    ("Yang Rising (陽上)", "Ngã (broken/rising)", "Voiced initials"),
    ("Yin Departing (陰去)", "Sắc (rising)", "All initials"),
    ("Yang Departing (陽去)", "Nặng (stopped)", "All initials"),
    #("Yin Entering (陰入)", "Sắc (with /p/, /t/, /k/ finals)", "All initials"),
    #("Yang Entering (陽入)", "Nặng (with /p/, /t/, /k/ finals)", "All initials"),
    ("Yin Entering (陰入)", "Sắc (rising)", "All initials"),
    ("Yang Entering (陽入)", "Nặng (stopped)", "All initials")
]

# Add edges to the graph
for mc_tone, vn_tone, condition in transformations:
    graph.add_edge(mc_tone, vn_tone, label=condition)

# Define positions for nodes to preserve order
yang_offset = -0.4
yang_height = 0.9
vnlr_offset = -0.45
vnud_offset = 0.1
pos = {
    # Middle Chinese tones (row 1)
    "Yin Level (陰平)": (0, 1), "Yang Level (陽平)": (1 + yang_offset, yang_height),
    "Yin Rising (陰上)": (2, 1), "Yang Rising (陽上)": (3 + yang_offset, yang_height),
    "Yin Departing (陰去)": (4, 1), "Yang Departing (陽去)": (5 + yang_offset, yang_height),
    "Yin Entering (陰入)": (6, 1), "Yang Entering (陽入)": (7 + yang_offset, yang_height),
    # Vietnamese tones (row 2)
    "Ngang (level)": (0, 0), "Huyền (low falling)": (1 + vnlr_offset, vnud_offset),
    "Hỏi (rising/falling)": (2, 0), "Ngã (broken/rising)": (3 + vnlr_offset, vnud_offset),
    "Sắc (rising)": (4, 0), "Nặng (stopped)": (5 + vnlr_offset, vnud_offset),
    #"Sắc (with /p/, /t/, /k/ finals)": (6, 0), "Nặng (with /p/, /t/, /k/ finals)": (7, 0)
}

# Plot the graph
plt.figure(figsize=(12, 5))

nx.draw_networkx_nodes(graph, pos, node_size=2000, node_color="lightblue")
nx.draw_networkx_edges(graph, pos, arrowstyle="-|>", arrowsize=2, edge_color="black")
nx.draw_networkx_labels(graph, pos, font_size=10, font_weight="bold", font_family=fontname)

# Draw edge labels
edge_labels = nx.get_edge_attributes(graph, "label")
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=9, font_family=fontname)

# Title and display
plt.title("Development of Middle Chinese Tones to Vietnamese Tones", fontsize=14)
plt.axis('off')
plt.tight_layout()


# show examples as legend
legend_sl = []
for tone, words in examples.items():
    legend_sl.append(f"{tone}:\t{',\t'.join(words)}")
#''.join(legend_sl)

bx = 1.02
by = 0.01
plt.legend(legend_sl, loc=4, bbox_to_anchor=(bx, by))

# Save and show the image
plt.savefig("middle_chinese_to_vietnamese_tones_v4.png")
plt.show()


# Print voiced and voiceless initials and examples
print("Voiced initials:", voiced_initials)
print("Voiceless initials:", voiceless_initials)
print("Examples for tone categories:")
for tone, words in examples.items():
    print(f"  {tone}: {', '.join(words)}")
