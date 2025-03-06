# 1. Web scraping
from .PgsFile import PGScraper
from .PgsFile import audiovisual_downloader
from .PgsFile import headers, encode_chinese_keyword_for_url

# 2. Package/library management
from .PgsFile import install_package, uninstall_package
from .PgsFile import run_script, run_command
from .PgsFile import get_library_location
from .PgsFile import conda_mirror_commands

# 3. Text data retrieval
from .PgsFile import get_data_text, get_data_lines, get_json_lines, get_tsv_lines
from .PgsFile import get_data_excel, get_data_json, get_data_tsv, extract_misspelled_words_from_docx
from .PgsFile import get_data_html_online, get_data_html_offline
from .PgsFile import get_data_table_url, get_data_table_html_string

# 4. Text data storage
from .PgsFile import write_to_txt, write_to_excel, write_to_json, write_to_json_lines, append_dict_to_json, save_dict_to_excel
from .PgsFile import write_to_excel_normal

# 5. File/folder process
from .PgsFile import FilePath, FileName, DirList
from .PgsFile import get_subfolder_path, get_full_path
from .PgsFile import makedirec, makefile
from .PgsFile import source_path, next_folder_names, get_directory_tree_with_meta, find_txt_files_with_keyword
from .PgsFile import remove_empty_folders, remove_empty_txts, remove_empty_lines, remove_empty_last_line, move_file, copy_file
from .PgsFile import concatenate_excel_files
from .PgsFile import set_permanent_environment_variable
from .PgsFile import delete_permanent_environment_variable
from .PgsFile import get_env_variable

# 6. Data cleaning
from .PgsFile import BigPunctuation, StopTags, Special, yhd
from .PgsFile import ZhStopWords, EnPunctuation, get_stopwords
from .PgsFile import nltk_en_tags, nltk_tag_mapping, thulac_tags, ICTCLAS2008, LangCodes, pgs_abbres_words
from .PgsFile import check_contain_chinese, check_contain_number
from .PgsFile import replace_chinese_punctuation_with_english
from .PgsFile import replace_english_punctuation_with_chinese
from .PgsFile import clean_list, clean_text, clean_text_with_abbreviations, clean_line_with_abbreviations
from .PgsFile import extract_chinese_punctuation, generate_password, sort_strings_with_embedded_numbers

# 7. NLP (natural language processing)
from .PgsFile import strQ2B_raw, strQ2B_words
from .PgsFile import ngrams, bigrams, trigrams, everygrams, compute_similarity
from .PgsFile import word_list, batch_word_list
from .PgsFile import cs, cs1, sent_tokenize, word_tokenize, word_tokenize2

# 8. Maths
from .PgsFile import len_rows, check_empty_cells
from .PgsFile import format_float, decimal_to_percent, Percentage
from .PgsFile import get_text_length_kb, extract_numbers

# 9. Visualization
from .PgsFile import replace_white_with_transparency
from .PgsFile import simhei_default_font_path_MacOS_Windows
from .PgsFile import get_font_path

name = "PgsFile"