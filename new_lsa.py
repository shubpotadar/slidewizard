# import json
# from lsa_summarizer import LsaSummarizer
# from nltk.corpus import stopwords
# import statistics
# import shutil

# source_file = "djsnake.json"
# backup_file = "original_text_backup.json"
# shutil.copyfile(source_file, backup_file)

# with open(source_file, "r", encoding='utf-8') as file:
#     json_data = json.load(file)

# subheadings = json_data["subheadings"]
# text_lengths = []

# for subheading in subheadings:
#     content = subheading["content"]
#     text_lengths.extend([len(text) for text in content])

# average_text_length = statistics.mean(text_lengths)
# summarizer = LsaSummarizer()

# stopwords = stopwords.words('english')
# summarizer.stop_words = stopwords

# for subheading in subheadings:
#     content = subheading["content"]
#     summarized_content = []
#     for text in content:
#         if len(text) > average_text_length:
#             summarized_text = " ".join(summarizer(text, 2))
#             summarized_content.append(summarized_text)
#     subheading["content"] = summarized_content

# with open(backup_file, "w", encoding='utf-8') as file:
#     json.dump(json_data, file, indent=4)

# print("Summarized content has been overwritten in the original JSON file.")
import json
from lsa_summarizer import LsaSummarizer
from nltk.corpus import stopwords
import statistics
import shutil

source_file = "./static/1.json"
backup_file = "./static/original_text_backup.json"
shutil.copyfile(source_file, backup_file)

with open(source_file, "r", encoding='utf-8') as file:
    json_data = json.load(file)

subheadings = json_data["subheadings"]
text_lengths = []

for subheading in subheadings:
    content = subheading["content"]
    text_lengths.extend([len(text.split()) for text in content])

average_text_length = statistics.mean(text_lengths)
summarizer = LsaSummarizer()

stopwords = stopwords.words('english')
summarizer.stop_words = stopwords

for subheading in subheadings:
    content = subheading["content"]
    summarized_content = []
    for text in content:
        word_count = len(text.split())
        if word_count > 50:
            summarized_text = " ".join(summarizer(text, 3))
            summarized_content.append(summarized_text)
        elif word_count > 30:
            summarized_text = " ".join(summarizer(text, 2))
            summarized_content.append(summarized_text)
        elif word_count < 20:
            summarized_text = " ".join(summarizer(text, 1))
            summarized_content.append(summarized_text)
        else:
            summarized_content.append(text)
    subheading["content"] = summarized_content

with open(source_file, "w", encoding='utf-8') as file:
    json.dump(json_data, file, indent=4)

print("Summarized content has been overwritten in the original JSON file.")
