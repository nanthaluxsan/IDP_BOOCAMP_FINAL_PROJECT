import os
import argparse
import toxigen_hate_bert
import logging
import ocr_extraction

# # Suppress C++ library warnings
# os.environ["FLAGS_minloglevel"] = "2"  # Removed extra space
# os.environ["GLOG_minloglevel"] = "2"

# # Suppress PPOCR Python warnings
# logging.getLogger("ppocr").setLevel(logging.ERROR)  # Added closing parenthesis


if __name__ == "__main__":
    meme_path = r"D:\study_further\Senzemate\Project\memes"
    texts = ocr_extraction.extract_text_from_images(meme_path)
    total_outputs = toxigen_hate_bert.hateful_detect(texts)
    print(total_outputs)
