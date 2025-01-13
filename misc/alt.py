import matplotlib.pyplot as plt
import numpy as np

fontname = 'Apple LiGothic'
fontname = ['AppleGothic', 'sans-serif']
fontname = ['Apple LiGothic', 'sans-serif']
plt.rcParams['font.family'] = fontname

# Define the data: Middle Chinese tones and their corresponding Vietnamese tones
middle_chinese_tones = ['平声 (level)', '上声 (rising)', '去声 (departing)', '入声 (checked)']
vietnamese_tones = ['Thanh ngang', 'Thanh sắc', 'Thanh hỏi', 'Thanh nặng']
voicing_categories = ['Voiceless', 'Sub-voiced', 'Fully voiced']

# Mapping from Middle Chinese tone categories to Vietnamese tone categories
tone_mapping = {
    '平声 (level)': ['Thanh ngang', 'Thanh huyền', 'Thanh nặng'],
    '上声 (rising)': ['Thanh sắc', 'Thanh hỏi', 'Thanh hỏi'],
    '去声 (departing)': ['Thanh sắc', 'Thanh nặng', 'Thanh nặng'],
    '入声 (checked)': ['Thanh nặng', 'Thanh nặng', 'Thanh nặng']
}

# Voicing level mapping
voicing_mapping = {
    '平声 (level)': ['Voiceless', 'Sub-voiced', 'Fully voiced'],
    '上声 (rising)': ['Voiceless', 'Sub-voiced', 'Fully voiced'],
    '去声 (departing)': ['Voiceless', 'Sub-voiced', 'Fully voiced'],
    '入声 (checked)': ['Voiceless', 'Sub-voiced', 'Fully voiced']
}

# Tone pitches corresponding to the tones in Vietnamese
tone_pitches = {
    'Thanh ngang': [33],
    'Thanh huyền': [21],
    'Thanh nặng': [21, 21],
    'Thanh sắc': [313],
    'Thanh hỏi': [35, 35],
}

# Prepare data for plotting
middle_chinese_indices = np.arange(len(middle_chinese_tones))
vietnamese_tone_data = []
for tone in middle_chinese_tones:
    vietnamese_tone_data.append(tone_mapping[tone])

# Plotting the graph
fig, ax = plt.subplots(figsize=(10, 6))

# Create a bar plot for each Middle Chinese tone category with its corresponding Vietnamese tones
for i, mc_tone in enumerate(middle_chinese_tones):
    y_pos = np.array([i] * len(vietnamese_tone_data[i]))  # The y positions for the different tones in the same category
    ax.scatter(vietnamese_tone_data[i], y_pos, label=mc_tone, s=100)

ax.set_yticks(middle_chinese_indices)
ax.set_yticklabels(middle_chinese_tones)
ax.set_xlabel('Vietnamese Tone Categories')
ax.set_title('Correspondence Between Middle Chinese Tones and Vietnamese Tones (Hanoi)')

plt.legend()
plt.show()
