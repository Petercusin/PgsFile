# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 23:44:04 2021

@author: Petercusin
"""

import os, sys
def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <=ch<= u'\u9fff':
            return True
    return False

def check_contain_number(uchar):
    number=[]
    for w in uchar:
        if u'\u0030'<= w <= u'\u0039':
            number.append(w)
    if len(number)!=0:
        return True
    else:
        return False

def extract_chinese_punctuation(text):
    import re
    pattern=re.compile(r'[\u3000-\u303f\u4e00-\u9fff\uf900-\ufaff\uff00-\uffef]')
    matches=pattern.findall(text)
    return matches

def Percentage(num):
    '''
    Parameters
    ----------
    num : TYPE float
        DESCRIPTION. 0.236489

    Returns
    -------
    result : TYPE string
        DESCRIPTION. 23.64%

    '''
    result=str(num*100)[:5]+"%"
    # result=num*100
    return result

def decimal_to_percent(decimal):
    '''
    Parameters
    ----------
    decimal : TYPE float
        DESCRIPTION. 0.236489

    Returns
    -------
    percent_str : TYPE string
        DESCRIPTION. 23.65%

    '''
    percent=decimal * 100
    percent_str="{:.2f}%".format(percent)
    return percent_str

try:
    import chardet
except ImportError:
    print("chardet library not found. Installing...")
    install_package("chardet")
    import chardet  # Re-import after installation
    
def get_data_text(path):
    '''
    Parameters
    ----------
    path : str
        The path to the text file to read.
        Supports common text encoding formats, like utf-8, unicode, ansi, gbk etc.

    Returns
    -------
    text : str
        The text content from the target file.
        Returns None if the file cannot be read with any of the specified encodings.
    '''
    # Get the size of the file
    file_size = os.path.getsize(path)

    # Read the file to detect encoding
    with open(path, 'rb') as f:
        if file_size < 1024:
            raw_data = f.read()  # Read the entire file if it's small
        else:
            raw_data = f.read(1024)  # Read the first 1024 bytes

        result = chardet.detect(raw_data)
        encoding = result['encoding']

    # Read the entire file using the detected encoding
    if encoding:
        with open(path, 'r', encoding=encoding, errors="ignore") as f:
            return f.read()
    else:
        return None

def get_data_lines(path, no_line_breaks=False):
    '''
    Parameters
    ----------
    path : str
        The path to the text file to read.
        Supports common text encoding formats, like utf-8, unicode, ansi, gbk etc.

    Returns
    -------
    lines : list
        A list containing all the non-empty paragraphs of the target file.
    '''
    
    # Get the size of the file
    file_size = os.path.getsize(path)

    # Read the file to detect encoding
    with open(path, 'rb') as f:
        if file_size < 1024:
            raw_data = f.read()  # Read the entire file if it's small
        else:
            raw_data = f.read(1024)  # Read the first 1024 bytes

        result = chardet.detect(raw_data)
        encoding = result['encoding']

    # Read the entire file using the detected encoding
    if encoding:
        with open(path, 'r', encoding=encoding, errors="ignore") as f:
            if no_line_breaks is False:
                lines = [l.strip() for l in f.readlines() if len(l.strip()) != 0]
            else:
                lines = f.readlines()
            return lines
    else:
        return None


def write_to_txt(file_path,text,mode=None,encoding=None):
    '''
    Parameters
    ----------
    file_path : TYPE string
        DESCRIPTION.
    text : TYPE
        DESCRIPTION. string
    mode : TYPE, optional # w;a+
        DESCRIPTION. The default is None.
    encoding : TYPE, optional # utf-8
        DESCRIPTION. The default is None.

    Returns
    -------
    None.

    '''
    if mode is None:
        mode="w"
    else:
        mode=mode
    if encoding is None:
        encoding="utf-8"
    else:
        encoding=encoding    
    f=open(file_path,mode=mode,encoding=encoding)
    f.write(text.strip()+"\n")
    f.close()

def get_data_excel(excel_path,column_id,sheet_name=None):
    '''
    Parameters
    ----------
    excel_path : TYPE
        DESCRIPTION. data_python.xlsx
        
    column_id : TYPE Int 0,1,2,3
        DESCRIPTION. 0 means the first column, 1 means the second.
        
    sheet_name : TYPE, optional
        DESCRIPTION. The default is None.

    Returns
    -------
    TYPE list
        DESCRIPTION. return a list of data.
    '''
    
    import pandas as pd
    if sheet_name is None:
        sheet_name=0
    else:
       sheet_name=sheet_name  
    df=pd.read_excel(excel_path,keep_default_na=False, sheet_name=sheet_name,header=None) 
    inter=df.iloc[0:,column_id] #提取第二列所有行  
    return list(inter)

def write_to_excel(excel_path, data, sheet_name=None, index=None):
    '''
    Parameters
    ----------
    excel_path : TYPE
        DESCRIPTION. results.xlsx
        
    data : TYPE, dict
        DESCRIPTION. data = {'翻译': 24, '教学': 8, '数智': 6, '时代': 6, '财经': 6, '新': 4}
        
    sheet_name : TYPE, optional
        DESCRIPTION. The default is None.
        
    index : TYPE, optional
        DESCRIPTION. The default is None.
        
    Returns
    -------
    None.

    '''
    import pandas as pd
    if sheet_name is None:
        sheet_name="sheet1"
    else:
       sheet_name=sheet_name
    if index is None:
        index=False
    else:
        index=True        

    col = list(data.keys())
    freq = list(data.values())
    dic_of_list={"items": col, "counts": freq}
        
    df=pd.DataFrame(dic_of_list)
    df.style.to_excel(excel_path, sheet_name=sheet_name,startcol=0, index=index)

def write_to_excel_normal(excel_path,dic_of_list,sheet_name=None,index=None):
    '''
    Parameters
    ----------
    excel_path : TYPE
        DESCRIPTION. D:\results.xlsx
        
    dic_of_list : TYPE
        DESCRIPTION. {"col":["a","b","c","d"],"freq":[1,2,3,4]}
        
    sheet_name : TYPE, optional
        DESCRIPTION. The default is None.
        
    index : TYPE, optional
        DESCRIPTION. The default is None.
        
    Returns
    -------
    None.

    '''
    import pandas as pd
    if sheet_name is None:
        sheet_name="sheet1"
    else:
       sheet_name=sheet_name
    if index is None:
        index=False
    else:
        index=True        
        
    df=pd.DataFrame(dic_of_list)
    df.style.to_excel(excel_path, sheet_name=sheet_name,startcol=0, index=index)
    
def get_data_tsv(file_path):
    '''
    Parameters
    ----------
    file_path : TYPE string
        DESCRIPTION. which endswith .tsv file

    Returns
    -------
    my_dic : TYPE dict
        DESCRIPTION. generation of a dictionary made of each Chinese sentence as key and its equivalent English sentence as value.
        
    '''
    import pandas as pd
    df=pd.read_csv(file_path,sep='\t')
    en_list=df.iloc[0:,0]
    zh_list=df.iloc[0:,1]
    my_dic=dict(zip(en_list,zh_list))
    return my_dic

def get_tsv_lines(csv_path, delimiter=None):
    '''
    Parameters
    ----------
    get_tsv_lines : TYPE data.tsv
        DESCRIPTION.

    Returns
    -------
    csv.reader(f, delimiter=dit) : generator
        DESCRIPTION. generator object get_tsv_lines
    '''
    if delimiter is None:
        dit="\t"
    else:
        dit=delimiter
    import csv
    try:
        with open(csv_path, 'r', encoding="utf-8") as f:
            reader=csv.reader(f, delimiter=dit) #change delimiter from \t into comma
            for row in reader:
                yield row
    except:
        with open(csv_path, 'r', encoding="utf-8-sig") as f:
            reader=csv.reader(f, delimiter=dit) #change delimiter from \t into comma
            for row in reader:
                yield row    
    
def get_data_json(json_path):
    '''
    Parameters
    ----------
    json_path : TYPE data.json
        DESCRIPTION.

    Returns
    -------
    load_dict : TYPE dict
        DESCRIPTION. return a dict of data.
    '''
    import json
    try:
        f=open(json_path,"r",encoding="utf-8")
        load_dict=json.load(f)    
        f.close()
        return load_dict            
    except:
        f=open(json_path,"r",encoding="utf-8-sig")
        load_dict=json.load(f)   
        f.close()
        return load_dict

def get_json_lines(json_path):
    '''
    Parameters
    ----------
    json_path : TYPE data.json
        DESCRIPTION.

    Returns
    -------
    json.loads(line) : generator
        DESCRIPTION. return a list of dict.
    '''
    import json
    try:   
        with open(json_path, 'r', encoding='utf-8') as f:
            for line in f:
                yield json.loads(line)
    except:
        with open(json_path, 'r', encoding='utf-8-sig') as f:
            for line in f:
                yield json.loads(line)        

def write_to_json(json_path,my_dic):
    '''
    Parameters
    ----------
    json_path : TYPE string
        DESCRIPTION. data.json
        
    my_dic : TYPE dict or list
        DESCRIPTION. 
            type1: {"pans":1}
            type2: {"word":["a","b","c"]}
            type3: [{"pans":1},{"glenna":2}]
            type4: [{"word":["a","b","c"]},{"freq":[1,2,3,4,5,6]}]

    Returns
    -------
    None.

    '''
    import json
    f2=open(json_path, "w", encoding="utf-8", errors="ignore")
    f2.write(json.dumps(my_dic,ensure_ascii=False)) #ensure_ascii=False 让中文不再乱码
    f2.close() 

def write_to_json_lines(json_path,my_json_data):
    '''
    Parameters
    ----------
    json_path : TYPE string
        DESCRIPTION. data.json
        
    my_json_data : TYPE dict or list
        DESCRIPTION. 
            type1: {"pans":1}
            type2: {"word":["a","b","c"]}
            type3: [{"pans":1},{"glenna":2}]
            type4: [{"word":["a","b","c"]},{"freq":[1,2,3,4,5,6]}]

    Returns
    -------
    None.

    '''
    import json
    file=open(json_path, 'w', encoding="utf-8", errors="ignore")
    if type(my_json_data) is dict:
        for key, value in my_json_data.items():
            json_str=json.dumps({key: value},ensure_ascii=False)
            file.write(json_str + '\n')
    else:
         for dic in my_json_data:
            json_str=json.dumps(dic,ensure_ascii=False)
            file.write(json_str + '\n')              
    file.close()


# Function to append a dictionary to a JSON file
def append_dict_to_json(file_path, data_dict):
    try:
        import json
        with open(file_path, 'a', encoding="utf-8") as file:
            json_string = json.dumps(data_dict, ensure_ascii=False)
            file.write(json_string + '\n')
        # print(f"Dictionary appended to {file_path}")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def FilePath(root):
    '''读取所有文件，列出每个文件的路径'''
    import os
    Filelist=[]
    for home, dirs, files in os.walk(root):
        for filename in files:
            Filelist.append(os.path.join(home, filename))
    return Filelist

def FileName(file_path):
    import os
    inter=os.path.basename(file_path)
    return inter

def makedirec(path):
    import os
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        return
    return(makedirec(path))

def get_folder_size(folder_path):
    total_size=0
    import os
    for path, dirs, files in os.walk(folder_path):
        for file in files:
            file_path=os.path.join(path, file)
            total_size += os.path.getsize(file_path)
    return total_size

def format_size(size):
    units=["B", "KB", "MB", "GB", "TB"]
    index=0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    return f"{size:.2f} {units[index]}"

def get_directory_tree_with_meta(start_path, indent='', show_meta=False, max_directories=5, current_level=1):
    import os
    if not os.path.isdir(start_path):
        print(f"{start_path} is not a valid directory.")
        return

    files=os.listdir(start_path)
    directories=[]
    for file in files:
        path=os.path.join(start_path, file)
        if os.path.isdir(path):
            directories.append(file)

    total_directories=len(directories)
    visible_directories=directories
    if current_level > 1 and total_directories > max_directories:
        visible_directories=directories[:max_directories]

    for i, directory in enumerate(visible_directories):
        path=os.path.join(start_path, directory)
        is_last_directory=i==len(visible_directories) - 1
        print(f"{indent}{'└──' if is_last_directory else '├──'} {directory}", end=' ')
        if show_meta and (current_level <= 4 or current_level==2):
            file_count=sum([1 for _, _, files in os.walk(path) for _ in files])
            folder_size=get_folder_size(path)
            formatted_size=format_size(folder_size)
            print(f"({file_count}, {formatted_size})")
        else:
            print()
        if os.path.isdir(path):
            sub_indent=indent + ('│   ' if not is_last_directory else '    ')
            get_directory_tree_with_meta(path, sub_indent, show_meta, max_directories, current_level=current_level + 1)

    if current_level > 1 and total_directories > max_directories:
        remaining_directories=total_directories - max_directories
        print(f"{indent}└── ... (and {remaining_directories} more directories)")
        # current_level=-1 will show all folders' info.

def get_full_path(*path_components):
    """
    Combines multiple path components into a single, full path using os.path.join.

    Args:
        *path_components: Variable number of path components (strings).

    Returns:
        str: The combined full path.
    """
    return os.path.join(*path_components)

def get_subfolder_path(parent_folder, subfolder_name):
    import os
    subfolder_name=subfolder_name.strip()
    for root, dirs, files in os.walk(parent_folder):
        if subfolder_name in dirs:
            subfolder_path=os.path.join(root, subfolder_name)
            return subfolder_path

    # 如果未找到目标子文件夹，则返回 None 或其他适当的值
    return None

BigPunctuation="""!"#$&\'()*+,-/:;<=>?@[\\]^_`{|}.%~＂＃＄％＆＇?。（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､\u3000、〃〈〉《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏﹑﹔·！？｡。``''"""   #除去英文标点.%
StopTags="""◆: 、/ 。/ ---/ -/ --/ -- :/ ;/ ?/ ??/ ?┖ @/ [/ ]/ ^/ ‘/ ’/ "/ "/ 〈/ 〉/ 《/ 》/ 【/ 】/ >/ ∶/ ■/ ●/ ·/ …/ !/ #/ %,/ %/ \'/ (/ )/ */ +/ ,/ -/ // np v n w m a x t q j ni ns d i f u p g nz c r id s k h o e / #?/ --/""" #用来停用词性标注
Special="""∶ ■ ● ① ② ③ × ℃ Ⅲ ④ ⑤ ◆ ⑥ ± ⑦ ⑧ → ⑨ ▲ ⑩ ─ ÷ μ γ β Ⅱ Ⅰ ‰ □ 〇 ○ Ⅴ Ⅳ ★ ﹐ ° ※ ︰ α ― ≠ █ о θ ω ⒈ ⒉ ⒊ н ≤ ì ǎ ≥ р т с к й а и Ⅵ é è ﹢ ﹝ ﹞  ā ⒋ ù π ◇ Ω Ф ы Я п К в у м ǒ ü á ǔ ⒌ ⒍ 䦆 Ⅹ Ⅶ ← """
ZhStopWords="""——— 》）， ）÷（１－ ”， ）、 ＝（ : → ℃  & * 一一 ~~~~ ’ .  『 .一 ./ --  』 ＝″ 【 ［＊］ ｝＞ ［⑤］］ ［①Ｄ］ ｃ］ ｎｇ昉 ＊ // ［ ］ ［②ｅ］ ［②ｇ］ ＝｛ } ，也  ‘ Ａ ［①⑥］ ［②Ｂ］  ［①ａ］ ［④ａ］ ［①③］ ［③ｈ］ ③］ １．  －－  ［②ｂ］ ’‘  ×××  ［①⑧］ ０：２  ＝［ ［⑤ｂ］ ［②ｃ］  ［④ｂ］ ［②③］ ［③ａ］ ［④ｃ］ ［①⑤］ ［①⑦］ ［①ｇ］ ∈［  ［①⑨］ ［①④］ ［①ｃ］ ［②ｆ］ ［②⑧］ ［②①］ ［①Ｃ］ ［③ｃ］ ［③ｇ］ ［②⑤］ ［②②］ 一. ［①ｈ］ .数 ［］ ［①Ｂ］ 数/ ［①ｉ］ ［③ｅ］ ［①①］ ［④ｄ］ ［④ｅ］ ［③ｂ］ ［⑤ａ］ ［①Ａ］ ［②⑧］ ［②⑦］ ［①ｄ］ ［②ｊ］ 〕〔 ］［ :// ′∈ ［②④ ［⑤ｅ］ １２％ ｂ］ ... ................... …………………………………………………③ ＺＸＦＩＴＬ ［③Ｆ］ 」 ［①ｏ］ ］∧′＝［  ∪φ∈ ′｜ ｛－ ②ｃ ｝ ［③①］ Ｒ．Ｌ． ［①Ｅ］ Ψ －［＊］－ ↑ .日  ［②ｄ］ ［② ［②⑦］ ［②②］ ［③ｅ］ ［①ｉ］ ［①Ｂ］ ［①ｈ］ ［①ｄ］ ［①ｇ］ ［①②］ ［②ａ］ ｆ］ ［⑩］ ａ］ ［①ｅ］ ［②ｈ］ ［②⑥］ ［③ｄ］ ［②⑩］ ｅ］ 〉 】 元／吨 ［②⑩］ ２．３％ ５：０   ［①］ :: ［②］ ［③］ ［④］ ［⑤］ ［⑥］ ［⑦］ ［⑧］ ［⑨］  …… —— ? 、 。 “ ” 《 》 ！ ， ： ； ？ ． , ． ' ?  · ——— ── ?  — < > （ ） 〔 〕 [ ] ( ) - + ～ × ／ / ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ Ⅲ В " ; # @ γ μ φ φ． ×  Δ ■ ▲ sub exp  sup sub Lex  ＃ ％ ＆ ＇ ＋ ＋ξ ＋＋ － －β ＜ ＜± ＜Δ ＜λ ＜φ ＜＜=＝ ＝☆ ＝－ ＞ ＞λ ＿ ～± ～＋ ［⑤ｆ］ ［⑤ｄ］ ［②ｉ］ ≈  ［②Ｇ］ ［①ｆ］ ＬＩ ㈧  ［－ ...... 〉 ［③⑩］ 第二 一番 一直 一个 一些 许多 种 有的是 也就是说 末##末 啊 阿 哎 哎呀 哎哟 唉 俺 俺们 按 按照 吧 吧哒 把 罢了 被 本 本着 比 比方 比如 鄙人 彼 彼此 边 别 别的 别说 并 并且 不比 不成 不单 不但 不独 不管 不光 不过 不仅 不拘 不论 不怕 不然 不如 不特 不惟 不问 不只 朝 朝着 趁 趁着 乘 冲 除 除此之外 除非 除了 此 此间 此外 从 从而 打 待 但 但是 当 当着 到 得 的 的话 等 等等 地 第 叮咚 对 对于 多 多少 而 而况 而且 而是 而外 而言 而已 尔后 反过来 反过来说 反之 非但 非徒 否则 嘎 嘎登 该 赶 个 各 各个 各位 各种 各自 给 根据 跟 故 故此 固然 关于 管 归 果然 果真 过 哈 哈哈 呵 和 何 何处 何况 何时 嘿 哼 哼唷 呼哧 乎 哗 还是 还有 换句话说 换言之 或 或是 或者 极了 及 及其 及至 即 即便 即或 即令 即若 即使 几 几时 己 既 既然 既是 继而 加之 假如 假若 假使 鉴于 将 较 较之 叫 接着 结果 借 紧接着 进而 尽 尽管 经 经过 就 就是 就是说 据 具体地说 具体说来 开始 开外 靠 咳 可 可见 可是 可以 况且 啦 来 来着 离 例如 哩 连 连同 两者 了 临 另 另外 另一方面 论 嘛 吗 慢说 漫说 冒 么 每 每当 们 莫若 某 某个 某些 拿 哪 哪边 哪儿 哪个 哪里 哪年 哪怕 哪天 哪些 哪样 那 那边 那儿 那个 那会儿 那里 那么 那么些 那么样 那时 那些 那样 乃 乃至 呢 能 你 你们 您 宁 宁可 宁肯 宁愿 哦 呕 啪达 旁人 呸 凭 凭借 其 其次 其二 其他 其它 其一 其余 其中 起 起见 起见 岂但 恰恰相反 前后 前者 且 然而 然后 然则 让 人家 任 任何 任凭 如 如此 如果 如何 如其 如若 如上所述 若 若非 若是 啥 上下 尚且 设若 设使 甚而 甚么 甚至 省得 时候 什么 什么样 使得 是 是的 首先 谁 谁知 顺 顺着 似的 虽 虽然 虽说 虽则 随 随着 所 所以 他 他们 他人 它 它们 她 她们 倘 倘或 倘然 倘若 倘使 腾 替 通过 同 同时 哇 万一 往 望 为 为何 为了 为什么 为着 喂 嗡嗡 我 我们 呜 呜呼 乌乎 无论 无宁 毋宁 嘻 吓 相对而言 像 向 向着 嘘 呀 焉 沿 沿着 要 要不 要不然 要不是 要么 要是 也 也罢 也好 一 一般 一旦 一方面 一来 一切 一样 一则 依 依照 矣 以 以便 以及 以免 以至 以至于 以致 抑或 因 因此 因而 因为 哟 用 由 由此可见 由于 有 有的 有关 有些 又 于 于是 于是乎 与 与此同时 与否 与其 越是 云云 哉 再说 再者 在 在下 咱 咱们 则 怎 怎么 怎么办 怎么样 怎样 咋 照 照着 者 这 这边 这儿 这个 这会儿 这就是说 这里 这么 这么点儿 这么些 这么样 这时 这些 这样 正如 吱 之 之类 之所以 之一 只是 只限 只要 只有 至 至于 诸位 着 着呢 自 自从 自个儿 自各儿 自己 自家 自身 综上所述 总的来看 总的来说 总的说来 总而言之 总之 纵 纵令 纵然 纵使 遵照 作为 兮 呃 呗 咚 咦 喏 啐 喔唷 嗬 嗯 嗳""" 

EnPunctuation="""!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"""
nltk_en_tags={'CC': '并列连词', 'CD': '基数词', 'DT': '限定符', 'EX': '存在词', 'FW': '外来词', 'IN': '介词或从属连词', 'JJ': '形容词', 'JJR': '比较级的形容词', 'JJS': '最高级的形容词', 'LS': '列表项标记', 'MD': '情态动词', 'NN': '名词单数', 'NNS': '名词复数', 'NNP': '专有名词', 'NNPS': '专有名词复数', 'PDT': '前置限定词', 'POS': '所有格结尾', 'PRP': '人称代词', 'PRP$': '所有格代词', 'RB': '副词', 'RBR': '副词比较级', 'RBS': '副词最高级', 'RP': '小品词', 'SYM': '符号', 'UH': '感叹词', 'VB': '动词原型', 'VBD': '动词过去式', 'VBG': '动名词或现在分词', 'VBN': '动词过去分词', 'VBP': '非第三人称单数的现在时', 'VBZ': '第三人称单数的现在时', 'WDT': '以wh开头的限定词', 'WP': '以wh开头的代词', 'WP$': '以wh开头的所有格代词', 'WRB': '以wh开头的副词', 'TO': 'to'}
nltk_tag_mapping={'NN': 'Noun', 'NNS': 'Noun', 'NNP': 'Noun', 'NNPS': 'Noun', 'VB': 'Verb', 'VBD': 'Verb', 'VBG': 'Verb', 'VBN': 'Verb', 'VBP': 'Verb', 'VBZ': 'Verb', 'JJ': 'Adjective', 'JJR': 'Adjective', 'JJS': 'Adjective', 'RB': 'Adverb', 'RBR': 'Adverb', 'RBS': 'Adverb', 'IN': 'Preposition', 'PRP': 'Pronoun', 'PRP$': 'Pronoun', 'DT': 'Determiner', 'CC': 'Conjunction', 'CD': 'Numeral', 'UH': 'Interjection', 'FW': 'Foreign Word', 'TO': 'Particle', 'EX': 'Existential "there"', 'MD': 'Modal Auxiliary', 'WDT': 'Wh-determiner', 'WP': 'Wh-pronoun', 'WP$': 'Possessive wh-pronoun', 'WRB': 'Wh-adverb', 'SYM': 'Symbol', 'RP': 'Particle', 'POS': 'Possessive ending', 'PDT': 'Predeterminer', 'LS': 'List item marker', 'NIL': 'Missing tag'}

ICTCLAS2008={'a': '形容词', 'ad': '副形词', 'ag': '形容词性语素', 'al': '形容词性惯用语', 'an': '名形词', 'b': '区别词', 'bl': '区别词性惯用语', 'c': '连词', 'cc': '并列连词', 'd': '副词', 'dg': '副词性语素', 'dl': '副词性惯用语', 'e': '叹词', 'ew': '句末标点', 'f': '方位词', 'h': '前缀', 'k': '后缀', 'm': '数词', 'mg': '数词性语素', 'mq': '数量词', 'n': '名词', 'ng': '名词性语素', 'nl': '名词性惯用语', 'nr': '汉语人名', 'nr1': '汉语姓氏', 'nr2': '汉语名字', 'nrf': '音译人名', 'nrj': '日语人名', 'ns': '地名', 'nsf': '音译地名', 'nt': '机构团体名', 'nz': '其他专名', 'o': '拟声词', 'p': '介词', 'pba': '介词“把”', 'pbei': '介词“被”', 'q': '量词', 'qt': '时量词', 'qv': '动量词', 'r': '代词', 'rg': '代词性语素', 'rr': '人称代词', 'ry': '疑问代词', 'rys': '处所疑问代词', 'ryt': '时间疑问代词', 'ryv': '谓词性疑问代词', 'rz': '指示代词', 'rzs': '处所指示代词', 'rzt': '时间指示代词', 'rzv': '谓词性指示代词', 's': '处所词', 't': '时间词', 'tg': '时间词性语素', 'u': '助词', 'udel': '的、底', 'ude2': '地', 'ude3': '得', 'udeng': '等、等等、云云', 'udh': '......的话', 'uguo': '过', 'ule': '了', 'ulian': '连', 'uls': '来讲、来说；而言、说来', 'usuo': '所', 'uyy': '一样、一般；似的、般', 'uzhe': '着', 'uzhi': '之', 'v': '动词', 'vd': '副动词', 'vf': '趋向动词', 'vg': '动词性语素', 'vi': '不及物动词', 'vl': '动词性惯用语', 'vn': '名动词', 'vshi': '动词“是”', 'vx': '形式动词', 'vyou': '动词“有”', 'w': '标点符号', 'wd': '逗号', 'wky': '右括号', 'wkz': '左括号', 'wm': '冒号', 'wn': '顿号', 'wp': '破折号', 'ws': '省略号', 'wy': '引号', 'x': '字符串', 'y': '语气词', 'z': '状态词'}

ICTCLAS3={
  "n": "名词",
  "nr": "人名",
  "nr1": "汉语姓氏",
  "nr2": "汉语名字",
  "nrj": "日语人名",
  "nrf": "音译人名",
  "ns": "地名",
  "nsf": "音译地名",
  "nt": "机构团体名",
  "nz": "其它专名",
  "nl": "名词性惯用语",
  "ng": "名词性语素",
  "t": "时间词",
  "tg": "时间词性语素",
  "s": "处所词",
  "f": "方位词",
  "v": "动词",
  "vd": "副动词",
  "vn": "名动词",
  "vshi": "动词“是”",
  "vyou": "动词“有”",
  "vf": "趋向动词",
  "vx": "形式动词",
  "vi": "不及物动词（内动词）",
  "vl": "动词性惯用语",
  "vg": "动词性语素",
  "a": "形容词",
  "ad": "副形词",
  "an": "名形词",
  "ag": "形容词性语素",
  "al": "形容词性惯用语",
  "b": "区别词",
  "bl": "区别词性惯用语",
  "z": "状态词",
  "r": "代词",
  "rr": "人称代词",
  "rz": "指示代词",
  "rzt": "时间指示代词",
  "rzs": "处所指示代词",
  "rzv": "谓词性指示代词",
  "ry": "疑问代词",
  "ryt": "时间疑问代词",
  "rys": "处所疑问代词",
  "ryv": "谓词性疑问代词",
  "rg": "代词性语素",
  "m": "数词",
  "mq": "数量词",
  "q": "量词",
  "qv": "动量词",
  "qt": "时量词",
  "d": "副词",
  "p": "介词",
  "pba": "介词“把”",
  "pbei": "介词“被”",
  "c": "连词",
  "cc": "并列连词",
  "u": "助词",
  "uzhe": "着",
  "ule": "了 喽",
  "uguo": "过",
  "ude1": "的 底",
  "ude2": "地",
  "ude3": "得",
  "usuo": "所",
  "udeng": "等 等等 云云",
  "uyy": "一样 一般 似的 般",
  "udh": "的话",
  "uls": "来讲 来说 而言 说来",
  "uzhi": "之",
  "ulian": "连 （“连小学生都会”）",
  "e": "叹词",
  "y": "语气词",
  "o": "拟声词",
  "h": "前缀",
  "k": "后缀",
  "x": "字符串",
  "xe": "Email字符串",
  "xs": "微博会话分隔符",
  "xm": "表情符合",
  "xu": "网址URL",
  "w": "标点符号",
  "wkz": "左括号，全角：（ 〔  ［  ｛  《 【  〖 〈   半角：( [ { <",
  "wky": "右括号，全角：） 〕  ］ ｝ 》  】 〗 〉 半角： ) ] { >",
  "wyz": "左引号，全角：“ ‘ 『",
  "wyy": "右引号，全角：” ’ 』",
  "wj": "句号，全角：。",
  "ww": "问号，全角：？ 半角：?",
  "wt": "叹号，全角：！ 半角：!",
  "wd": "逗号，全角：， 半角：,",
  "wf": "分号，全角：； 半角： ;",
  "wn": "顿号，全角：、",
  "wm": "冒号，全角：： 半角： :",
  "ws": "省略号，全角：……  …",
  "wp": "破折号，全角：――   －－   ――－   半角：---  ----",
  "wb": "百分号千分号，全角：％ ‰   半角：%",
  "wh": "单位符号，全角：￥ ＄ ￡  °  ℃  半角：$"
}

thulac_tags={'n': '名词', 'np': '人名', 'ns': '地名', 'ni': '机构名', 'nz': '其它专名', 'm': '数词', 'q': '量词', 'mq': '数量词', 't': '时间词', 'f': '方位词', 's': '处所词', 'v': '动词', 'a': '形容词', 'd': '副词', 'h': '前接成分', 'k': '后接成分', 'i': '习语', 'j': '简称', 'r': '代词', 'c': '连词', 'p': '介词', 'u': '助词', 'y': '语气助词', 'e': '叹词', 'o': '拟声词', 'g': '语素', 'w': '标点', 'x': '其它'}

LangCodes={'AA': ['阿法尔语', 'Afar'], 'AB': ['阿布哈兹语', 'Abkhaz'], 'AE': ['阿维斯陀语', 'Avestan'], 'AF': ['阿非利堪斯语', 'Afrikaans'], 'AK': ['阿坎语', 'Akan, Twi-Fante'], 'AM': ['阿姆哈拉语', 'Amharic'], 'AN': ['阿拉贡语', 'Aragonese'], 'AR': ['阿拉伯语', 'Arabic'], 'AS': ['阿萨姆语', 'Assamese'], 'AV': ['阿瓦尔语', 'Avaric'], 'AY': ['艾马拉语', 'Aymara'], 'AZ': ['阿塞拜疆语', 'Azerbaijani'], 'BA': ['巴什基尔语', 'Bashkir'], 'BE': ['白俄罗斯语', 'Belarusian'], 'BG': ['保加利亚语', 'Bulgarian'], 'BH': ['比哈尔语', 'Bihari'], 'BI': ['比斯拉玛语', 'Bislama'], 'BM': ['班巴拉语', 'Bambara'], 'BN': ['孟加拉语', 'Bengali'], 'BO': ['藏语', 'Tibetan Standard, Central Tibetan'], 'BR': ['布列塔尼语', 'Breton'], 'BS': ['波斯尼亚语', 'Bosnian'], 'CA': ['加泰隆语', 'Catalan;\xa0Valencian'], 'CE': ['车臣语', 'Chechen'], 'CH': ['查莫罗语', 'Chamorro'], 'CO': ['科西嘉语', 'Corsican'], 'CR': ['克里语', 'Cree'], 'CS': ['捷克语', 'Czech'], 'CU': ['教会斯拉夫语', 'Old Church Slavonic, Church Slavic, Church Slavonic, Old Bulgarian, Old Slavonic'], 'CV': ['楚瓦什语', 'Chuvash'], 'CY': ['威尔士语', 'Welsh'], 'DA': ['丹麦语', 'Danish'], 'DE': ['德语', 'German'], 'DV': ['迪维希语', 'Divehi; Dhivehi; Maldivian;'], 'DZ': ['不丹语', 'Dzongkha'], 'EE': ['埃维语', 'Ewe'], 'EL': ['现代希腊语', 'Greek, Modern'], 'EN': ['英语', 'English'], 'EO': ['世界语', 'Esperanto'], 'ES': ['西班牙语', 'Spanish; Castilian'], 'ET': ['爱沙尼亚语', 'Estonian'], 'EU': ['巴斯克语', 'Basque'], 'FA': ['波斯语', 'Persian'], 'FF': ['富拉语', 'Fula; Fulah; Pulaar; Pular'], 'FI': ['芬兰语', 'Finnish'], 'FJ': ['斐济语', 'Fijian'], 'FO': ['法罗斯语', 'Faroese'], 'FR': ['法语', 'French'], 'FY': ['弗里西亚语', 'Western Frisian'], 'GA': ['爱尔兰语', 'Irish'], 'GD': ['盖尔语（苏格兰语）', 'Scottish Gaelic; Gaelic'], 'GL': ['加利西亚语', 'Galician'], 'GN': ['瓜拉尼语', 'Guaraní'], 'GU': ['古吉拉特语', 'Gujarati'], 'GV': ['马恩岛语', 'Manx'], 'HA': ['豪萨语', 'Hausa'], 'HE': ['希伯来语', 'Hebrew\xa0(modern)'], 'HI': ['印地语', 'Hindi'], 'HO': ['希里莫图语', 'Hiri Motu'], 'HR': ['克罗地亚语', 'Croatian'], 'HT': ['海地克里奥尔语', 'Haitian; Haitian Creole'], 'HU': ['匈牙利语', 'Hungarian'], 'HY': ['亚美尼亚语', 'Armenian'], 'HZ': ['赫雷罗语', 'Herero'], 'I.E.': ['国际语E', 'Interlingue'], 'IA': ['国际语A', 'Interlingua'], 'ID': ['印尼语', 'Indonesian'], 'IG': ['伊博语', 'Igbo'], 'II': ['四川彝语（诺苏语）', 'Nuosu'], 'IK': ['依努庇克语', 'Inupiaq'], 'IO': ['伊多语', 'Ido'], 'IS': ['冰岛语', 'Icelandic'], 'IT': ['意大利语', 'Italian'], 'IU': ['伊努伊特语', 'Inuktitut'], 'JA': ['日语', 'Japanese'], 'JV': ['爪哇语', 'Javanese'], 'KA': ['格鲁吉亚语', 'Georgian'], 'KG': ['刚果语', 'Kongo'], 'KI': ['基库尤语', 'Kikuyu, Gikuyu'], 'KJ': ['夸尼亚玛语', 'Kwanyama, Kuanyama'], 'KK': ['哈萨克语', 'Kazakh'], 'KL': ['格陵兰语', 'Kalaallisut, Greenlandic'], 'KM': ['高棉语', 'Khmer, Cambodian'], 'KN': ['坎纳达语', 'Kannada'], 'KO': ['朝鲜语', 'Korean'], 'KR': ['卡努里语', 'Kanuri'], 'KS': ['克什米尔语', 'Kashmiri'], 'KU': ['库尔德语', 'Kurdish'], 'KV': ['科米语', 'Komi'], 'KW': ['康沃尔语', 'Cornish'], 'KY': ['吉尔吉斯语', 'Kirghiz, Kyrgyz'], 'LA': ['拉丁语', 'Latin'], 'LB': ['卢森堡语', 'Luxembourgish, Letzeburgesch'], 'LG': ['干达语', 'Luganda'], 'LI': ['林堡语', 'Limburgish, Limburgan, Limburger'], 'LN': ['林加拉语', 'Lingala'], 'LO': ['老挝语', 'Lao'], 'LT': ['立陶宛语', 'Lithuanian'], 'LU': ['卢巴—加丹加语', 'Luba-Katanga'], 'LV': ['拉脱维亚语', 'Latvian'], 'MG': ['马达加斯加语', 'Malagasy'], 'MH': ['马绍尔语', 'Marshallese'], 'MI': ['毛利语', 'Māori'], 'MK': ['马其顿语', 'Macedonian'], 'ML': ['马拉亚拉姆语', 'Malayalam'], 'MN': ['蒙古语', 'Mongolian'], 'MR': ['马拉提语', 'Marathi (Marāṭhī)'], 'MS': ['马来语', 'Malay'], 'MT': ['马耳他语', 'Maltese'], 'MY': ['缅甸语', 'Burmese'], 'NA': ['瑙鲁语', 'Nauru'], 'NB': ['挪威布克摩尔语', 'Norwegian Bokmål'], 'ND': ['北恩德贝勒语', 'North Ndebele'], 'NE': ['尼泊尔语', 'Nepali'], 'NG': ['恩敦加语', 'Ndonga'], 'NL': ['荷兰语', 'Dutch'], 'NN': ['尼诺斯克挪威语', 'Norwegian Nynorsk'], 'NO': ['挪威语', 'Norwegian'], 'NR': ['南恩德贝勒语', 'South Ndebele'], 'NV': ['纳瓦霍语', 'Navajo, Navaho'], 'NY': ['尼扬贾语', 'Chichewa; Chewa; Nyanja'], 'OC': ['普罗旺斯语', 'Occitan'], 'OJ': ['奥吉布瓦语', 'Ojibwe, Ojibwa'], 'OM': ['阿芳•奥洛莫语', 'Oromo'], 'OR': ['奥利亚语', 'Oriya'], 'OS': ['奥塞梯语', 'Ossetian, Ossetic'], 'PA': ['旁遮普语', 'Panjabi, Punjabi'], 'PI': ['巴利语', 'Pāli'], 'PL': ['波兰语', 'Polish'], 'PS': ['普什图语', 'Pashto, Pushto'], 'PT': ['葡萄牙语', 'Portuguese'], 'QU': ['凯楚亚语', 'Quechua'], 'RM': ['罗曼语', 'Romansh'], 'RN': ['基隆迪语', 'Kirundi'], 'RO': ['罗马尼亚语', 'Romanian,\xa0Moldavian, Moldovan'], 'RU': ['俄语', 'Russian'], 'RW': ['基尼阿万达语', 'Kinyarwanda'], 'SA': ['梵语', 'Sanskrit (Saṁskṛta)'], 'SC': ['撒丁语', 'Sardinian'], 'SD': ['信德语', 'Sindhi'], 'SE': ['北萨摩斯语', 'Northern Sami'], 'SG': ['桑戈语', 'Sango'], 'SI': ['僧加罗语', 'Sinhala, Sinhalese'], 'SK': ['斯洛伐克语', 'Slovak'], 'SL': ['斯洛文尼亚语', 'Slovene'], 'SM': ['萨摩亚语', 'Samoan'], 'SN': ['绍纳语', 'Shona'], 'SO': ['索马里语', 'Somali'], 'SQ': ['阿尔巴尼亚语', 'Albanian'], 'SR': ['塞尔维亚语', 'Serbian'], 'SS': ['塞斯瓦特语', 'Swati'], 'ST': ['南索托语', 'Southern Sotho'], 'SU': ['巽他语', 'Sundanese'], 'SV': ['瑞典语', 'Swedish'], 'SW': ['斯瓦希里语', 'Swahili'], 'TA': ['泰米尔语', 'Tamil'], 'TE': ['泰卢固语', 'Telugu'], 'TG': ['塔吉克语', 'Tajik'], 'TH': ['泰语', 'Thai'], 'TI': ['提格里尼亚语', 'Tigrinya'], 'TK': ['土库曼语', 'Turkmen'], 'TL': ['他加禄语', 'Tagalog'], 'TN': ['塞茨瓦纳语', 'Tswana'], 'TO': ['汤加语', 'Tongan'], 'TR': ['土耳其语', 'Turkish'], 'TS': ['宗加语', 'Tsonga'], 'TT': ['塔塔尔语', 'Tatar'], 'TW': ['特威语', 'Twi'], 'TY': ['塔希提语', 'Tahitian'], 'UG': ['维吾尔语', 'Uighur, Uyghur'], 'UK': ['乌克兰语', 'Ukrainian'], 'UR': ['乌尔都语', 'Urdu'], 'UZ': ['乌兹别克语', 'Uzbek'], 'VE': ['文达语', 'Venda'], 'VI': ['越南语', 'Vietnamese'], 'VO': ['沃拉普克语', 'Volapük'], 'WA': ['瓦隆语', 'Walloon'], 'WO': ['沃洛夫语', 'Wolof'], 'XH': ['科萨语', 'Xhosa'], 'YI': ['依地语', 'Yiddish'], 'YO': ['约鲁巴语', 'Yoruba'], 'ZA': ['壮语', 'Zhuang, Chuang'], 'ZH': ['汉语（中文）', 'Chinese'], 'ZU': ['祖鲁语', 'Zulu']}

claws_c7_tags = {
    "APPGE": {
        "description": "possessive pronoun, pre-nominal",
        "chinese_translation": "前置所有格代词",
        "examples": ["my", "your", "our"]
    },
    "AT": {
        "description": "article",
        "chinese_translation": "冠词",
        "examples": ["the", "no"]
    },
    "AT1": {
        "description": "singular article",
        "chinese_translation": "单数冠词",
        "examples": ["a", "an", "every"]
    },
    "BCL": {
        "description": "before-clause marker",
        "chinese_translation": "从句引导标记",
        "examples": ["in order (that)", "in order (to)"]
    },
    "CC": {
        "description": "coordinating conjunction",
        "chinese_translation": "并列连词",
        "examples": ["and", "or"]
    },
    "CCB": {
        "description": "adversative coordinating conjunction",
        "chinese_translation": "转折并列连词",
        "examples": ["but"]
    },
    "CS": {
        "description": "subordinating conjunction",
        "chinese_translation": "从属连词",
        "examples": ["if", "because", "unless", "so", "for"]
    },
    "CSA": {
        "description": "as (as conjunction)",
        "chinese_translation": "连词as",
        "examples": ["as"]
    },
    "CSN": {
        "description": "than (as conjunction)",
        "chinese_translation": "连词than",
        "examples": ["than"]
    },
    "CST": {
        "description": "that (as conjunction)",
        "chinese_translation": "连词that",
        "examples": ["that"]
    },
    "CSW": {
        "description": "whether (as conjunction)",
        "chinese_translation": "连词whether",
        "examples": ["whether"]
    },
    "DA": {
        "description": "after-determiner or post-determiner capable of pronominal function",
        "chinese_translation": "后位限定词(可代指)",
        "examples": ["such", "former", "same"]
    },
    "DA1": {
        "description": "singular after-determiner",
        "chinese_translation": "单数后位限定词",
        "examples": ["little", "much"]
    },
    "DA2": {
        "description": "plural after-determiner",
        "chinese_translation": "复数后位限定词",
        "examples": ["few", "several", "many"]
    },
    "DAR": {
        "description": "comparative after-determiner",
        "chinese_translation": "比较级后位限定词",
        "examples": ["more", "less", "fewer"]
    },
    "DAT": {
        "description": "superlative after-determiner",
        "chinese_translation": "最高级后位限定词",
        "examples": ["most", "least", "fewest"]
    },
    "DB": {
        "description": "before determiner or pre-determiner capable of pronominal function",
        "chinese_translation": "前位限定词(可代指)",
        "examples": ["all", "half"]
    },
    "DB2": {
        "description": "plural before-determiner",
        "chinese_translation": "复数前位限定词",
        "examples": ["both"]
    },
    "DD": {
        "description": "determiner (capable of pronominal function)",
        "chinese_translation": "限定词(可代指)",
        "examples": ["any", "some"]
    },
    "DD1": {
        "description": "singular determiner",
        "chinese_translation": "单数限定词",
        "examples": ["this", "that", "another"]
    },
    "DD2": {
        "description": "plural determiner",
        "chinese_translation": "复数限定词",
        "examples": ["these", "those"]
    },
    "DDQ": {
        "description": "wh-determiner",
        "chinese_translation": "wh-限定词",
        "examples": ["which", "what"]
    },
    "DDQGE": {
        "description": "wh-determiner, genitive",
        "chinese_translation": "属格wh-限定词",
        "examples": ["whose"]
    },
    "DDQV": {
        "description": "wh-ever determiner",
        "chinese_translation": "wh-ever类限定词",
        "examples": ["whichever", "whatever"]
    },
    "EX": {
        "description": "existential there",
        "chinese_translation": "存在型there",
        "examples": ["there"]
    },
    "FO": {
        "description": "formula",
        "chinese_translation": "公式语",
        "examples": []
    },
    "FU": {
        "description": "unclassified word",
        "chinese_translation": "未分类词",
        "examples": []
    },
    "FW": {
        "description": "foreign word",
        "chinese_translation": "外来词",
        "examples": []
    },
    "GE": {
        "description": "germanic genitive marker",
        "chinese_translation": "日耳曼语属格标记",
        "examples": ["'", "s"]
    },
    "IF": {
        "description": "for (as preposition)",
        "chinese_translation": "介词for",
        "examples": ["for"]
    },
    "II": {
        "description": "general preposition",
        "chinese_translation": "普通介词",
        "examples": []
    },
    "IO": {
        "description": "of (as preposition)",
        "chinese_translation": "介词of",
        "examples": ["of"]
    },
    "IW": {
        "description": "with, without (as prepositions)",
        "chinese_translation": "介词with/without",
        "examples": ["with", "without"]
    },
    "JJ": {
        "description": "general adjective",
        "chinese_translation": "普通形容词",
        "examples": []
    },
    "JJR": {
        "description": "general comparative adjective",
        "chinese_translation": "普通比较级形容词",
        "examples": ["older", "better", "stronger"]
    },
    "JJT": {
        "description": "general superlative adjective",
        "chinese_translation": "普通最高级形容词",
        "examples": ["oldest", "best", "strongest"]
    },
    "JK": {
        "description": "catenative adjective",
        "chinese_translation": "链接形容词",
        "examples": ["able in be able to", "willing in be willing to"]
    },
    "MC": {
        "description": "cardinal number, neutral for number",
        "chinese_translation": "基数词(数中性)",
        "examples": ["two", "three"]
    },
    "MC1": {
        "description": "singular cardinal number",
        "chinese_translation": "单数基数词",
        "examples": ["one"]
    },
    "MC2": {
        "description": "plural cardinal number",
        "chinese_translation": "复数基数词",
        "examples": ["sixes", "sevens"]
    },
    "MCGE": {
        "description": "genitive cardinal number, neutral for number",
        "chinese_translation": "属格基数词(数中性)",
        "examples": ["two's", "100's"]
    },
    "MCMC": {
        "description": "hyphenated number",
        "chinese_translation": "连字符数字",
        "examples": ["40-50", "1770-1827"]
    },
    "MD": {
        "description": "ordinal number",
        "chinese_translation": "序数词",
        "examples": ["first", "second", "next", "last"]
    },
    "MF": {
        "description": "fraction, neutral for number",
        "chinese_translation": "分数(数中性)",
        "examples": ["quarters", "two-thirds"]
    },
    "ND1": {
        "description": "singular noun of direction",
        "chinese_translation": "单数方位名词",
        "examples": ["north", "southeast"]
    },
    "NN": {
        "description": "common noun, neutral for number",
        "chinese_translation": "普通名词(数中性)",
        "examples": ["sheep", "cod", "headquarters"]
    },
    "NN1": {
        "description": "singular common noun",
        "chinese_translation": "单数普通名词",
        "examples": ["book", "girl"]
    },
    "NN2": {
        "description": "plural common noun",
        "chinese_translation": "复数普通名词",
        "examples": ["books", "girls"]
    },
    "NNA": {
        "description": "following noun of title",
        "chinese_translation": "头衔后置名词",
        "examples": ["M.A."]
    },
    "NNB": {
        "description": "preceding noun of title",
        "chinese_translation": "头衔前置名词",
        "examples": ["Mr.", "Prof."]
    },
    "NNL1": {
        "description": "singular locative noun",
        "chinese_translation": "单数方位名词",
        "examples": ["Island", "Street"]
    },
    "NNL2": {
        "description": "plural locative noun",
        "chinese_translation": "复数方位名词",
        "examples": ["Islands", "Streets"]
    },
    "NNO": {
        "description": "numeral noun, neutral for number",
        "chinese_translation": "数量名词(数中性)",
        "examples": ["dozen", "hundred"]
    },
    "NNO2": {
        "description": "numeral noun, plural",
        "chinese_translation": "复数数量名词",
        "examples": ["hundreds", "thousands"]
    },
    "NNT1": {
        "description": "temporal noun, singular",
        "chinese_translation": "单数时间名词",
        "examples": ["day", "week", "year"]
    },
    "NNT2": {
        "description": "temporal noun, plural",
        "chinese_translation": "复数时间名词",
        "examples": ["days", "weeks", "years"]
    },
    "NNU": {
        "description": "unit of measurement, neutral for number",
        "chinese_translation": "计量单位(数中性)",
        "examples": ["in", "cc"]
    },
    "NNU1": {
        "description": "singular unit of measurement",
        "chinese_translation": "单数计量单位",
        "examples": ["inch", "centimetre"]
    },
    "NNU2": {
        "description": "plural unit of measurement",
        "chinese_translation": "复数计量单位",
        "examples": ["ins.", "feet"]
    },
    "NP": {
        "description": "proper noun, neutral for number",
        "chinese_translation": "专有名词(数中性)",
        "examples": ["IBM", "Andes"]
    },
    "NP1": {
        "description": "singular proper noun",
        "chinese_translation": "单数专有名词",
        "examples": ["London", "Jane", "Frederick"]
    },
    "NP2": {
        "description": "plural proper noun",
        "chinese_translation": "复数专有名词",
        "examples": ["Browns", "Reagans", "Koreas"]
    },
    "NPD1": {
        "description": "singular weekday noun",
        "chinese_translation": "单数星期名词",
        "examples": ["Sunday"]
    },
    "NPD2": {
        "description": "plural weekday noun",
        "chinese_translation": "复数星期名词",
        "examples": ["Sundays"]
    },
    "NPM1": {
        "description": "singular month noun",
        "chinese_translation": "单数月份名词",
        "examples": ["October"]
    },
    "NPM2": {
        "description": "plural month noun",
        "chinese_translation": "复数月份名词",
        "examples": ["Octobers"]
    },
    "PN": {
        "description": "indefinite pronoun, neutral for number",
        "chinese_translation": "不定代词(数中性)",
        "examples": ["none"]
    },
    "PN1": {
        "description": "indefinite pronoun, singular",
        "chinese_translation": "单数不定代词",
        "examples": ["anyone", "everything", "nobody", "one"]
    },
    "PNQO": {
        "description": "objective wh-pronoun",
        "chinese_translation": "宾格wh-代词",
        "examples": ["whom"]
    },
    "PNQS": {
        "description": "subjective wh-pronoun",
        "chinese_translation": "主格wh-代词",
        "examples": ["who"]
    },
    "PNQV": {
        "description": "wh-ever pronoun",
        "chinese_translation": "wh-ever类代词",
        "examples": ["whoever"]
    },
    "PNX1": {
        "description": "reflexive indefinite pronoun",
        "chinese_translation": "反身不定代词",
        "examples": ["oneself"]
    },
    "PPGE": {
        "description": "nominal possessive personal pronoun",
        "chinese_translation": "名词性物主代词",
        "examples": ["mine", "yours"]
    },
    "PPH1": {
        "description": "3rd person sing. neuter personal pronoun",
        "chinese_translation": "第三人称单数中性人称代词",
        "examples": ["it"]
    },
    "PPHO1": {
        "description": "3rd person sing. objective personal pronoun",
        "chinese_translation": "第三人称单数宾格人称代词",
        "examples": ["him", "her"]
    },
    "PPHO2": {
        "description": "3rd person plural objective personal pronoun",
        "chinese_translation": "第三人称复数宾格人称代词",
        "examples": ["them"]
    },
    "PPHS1": {
        "description": "3rd person sing. subjective personal pronoun",
        "chinese_translation": "第三人称单数主格人称代词",
        "examples": ["he", "she"]
    },
    "PPHS2": {
        "description": "3rd person plural subjective personal pronoun",
        "chinese_translation": "第三人称复数主格人称代词",
        "examples": ["they"]
    },
    "PPIO1": {
        "description": "1st person sing. objective personal pronoun",
        "chinese_translation": "第一人称单数宾格人称代词",
        "examples": ["me"]
    },
    "PPIO2": {
        "description": "1st person plural objective personal pronoun",
        "chinese_translation": "第一人称复数宾格人称代词",
        "examples": ["us"]
    },
    "PPIS1": {
        "description": "1st person sing. subjective personal pronoun",
        "chinese_translation": "第一人称单数主格人称代词",
        "examples": ["I"]
    },
    "PPIS2": {
        "description": "1st person plural subjective personal pronoun",
        "chinese_translation": "第一人称复数主格人称代词",
        "examples": ["we"]
    },
    "PPX1": {
        "description": "singular reflexive personal pronoun",
        "chinese_translation": "单数反身代词",
        "examples": ["yourself", "itself"]
    },
    "PPX2": {
        "description": "plural reflexive personal pronoun",
        "chinese_translation": "复数反身代词",
        "examples": ["yourselves", "themselves"]
    },
    "PPY": {
        "description": "2nd person personal pronoun",
        "chinese_translation": "第二人称代词",
        "examples": ["you"]
    },
    "RA": {
        "description": "adverb, after nominal head",
        "chinese_translation": "名词后置副词",
        "examples": ["else", "galore"]
    },
    "REX": {
        "description": "adverb introducing appositional constructions",
        "chinese_translation": "同位语引导副词",
        "examples": ["namely", "e.g."]
    },
    "RG": {
        "description": "degree adverb",
        "chinese_translation": "程度副词",
        "examples": ["very", "so", "too"]
    },
    "RGQ": {
        "description": "wh- degree adverb",
        "chinese_translation": "wh-程度副词",
        "examples": ["how"]
    },
    "RGQV": {
        "description": "wh-ever degree adverb",
        "chinese_translation": "wh-ever类程度副词",
        "examples": ["however"]
    },
    "RGR": {
        "description": "comparative degree adverb",
        "chinese_translation": "比较级程度副词",
        "examples": ["more", "less"]
    },
    "RGT": {
        "description": "superlative degree adverb",
        "chinese_translation": "最高级程度副词",
        "examples": ["most", "least"]
    },
    "RL": {
        "description": "locative adverb",
        "chinese_translation": "方位副词",
        "examples": ["alongside", "forward"]
    },
    "RP": {
        "description": "prep. adverb, particle",
        "chinese_translation": "介词副词/小品词",
        "examples": ["about", "in"]
    },
    "RPK": {
        "description": "prep. adv., catenative",
        "chinese_translation": "链接介词副词",
        "examples": ["about in be about to"]
    },
    "RR": {
        "description": "general adverb",
        "chinese_translation": "普通副词",
        "examples": []
    },
    "RRQ": {
        "description": "wh- general adverb",
        "chinese_translation": "wh-普通副词",
        "examples": ["where", "when", "why", "how"]
    },
    "RRQV": {
        "description": "wh-ever general adverb",
        "chinese_translation": "wh-ever类普通副词",
        "examples": ["wherever", "whenever"]
    },
    "RRR": {
        "description": "comparative general adverb",
        "chinese_translation": "比较级普通副词",
        "examples": ["better", "longer"]
    },
    "RRT": {
        "description": "superlative general adverb",
        "chinese_translation": "最高级普通副词",
        "examples": ["best", "longest"]
    },
    "RT": {
        "description": "quasi-nominal adverb of time",
        "chinese_translation": "准名词性时间副词",
        "examples": ["now", "tomorrow"]
    },
    "TO": {
        "description": "infinitive marker",
        "chinese_translation": "不定式标记",
        "examples": ["to"]
    },
    "UH": {
        "description": "interjection",
        "chinese_translation": "感叹词",
        "examples": ["oh", "yes", "um"]
    },
    "VB0": {
        "description": "be, base form (finite i.e. imperative, subjunctive)",
        "chinese_translation": "be动词原形(限定形式，如祈使/虚拟)",
        "examples": []
    },
    "VBDR": {
        "description": "were",
        "chinese_translation": "were",
        "examples": ["were"]
    },
    "VBDZ": {
        "description": "was",
        "chinese_translation": "was",
        "examples": ["was"]
    },
    "VBG": {
        "description": "being",
        "chinese_translation": "being",
        "examples": ["being"]
    },
    "VBI": {
        "description": "be, infinitive",
        "chinese_translation": "be不定式",
        "examples": ["To be or not...", "It will be ..."]
    },
    "VBM": {
        "description": "am",
        "chinese_translation": "am",
        "examples": ["am"]
    },
    "VBN": {
        "description": "been",
        "chinese_translation": "been",
        "examples": ["been"]
    },
    "VBR": {
        "description": "are",
        "chinese_translation": "are",
        "examples": ["are"]
    },
    "VBZ": {
        "description": "is",
        "chinese_translation": "is",
        "examples": ["is"]
    },
    "VD0": {
        "description": "do, base form (finite)",
        "chinese_translation": "do动词原形(限定形式)",
        "examples": []
    },
    "VDD": {
        "description": "did",
        "chinese_translation": "did",
        "examples": ["did"]
    },
    "VDG": {
        "description": "doing",
        "chinese_translation": "doing",
        "examples": ["doing"]
    },
    "VDI": {
        "description": "do, infinitive",
        "chinese_translation": "do不定式",
        "examples": ["I may do...", "To do..."]
    },
    "VDN": {
        "description": "done",
        "chinese_translation": "done",
        "examples": ["done"]
    },
    "VDZ": {
        "description": "does",
        "chinese_translation": "does",
        "examples": ["does"]
    },
    "VH0": {
        "description": "have, base form (finite)",
        "chinese_translation": "have动词原形(限定形式)",
        "examples": []
    },
    "VHD": {
        "description": "had (past tense)",
        "chinese_translation": "had(过去式)",
        "examples": ["had"]
    },
    "VHG": {
        "description": "having",
        "chinese_translation": "having",
        "examples": ["having"]
    },
    "VHI": {
        "description": "have, infinitive",
        "chinese_translation": "have不定式",
        "examples": []
    },
    "VHN": {
        "description": "had (past participle)",
        "chinese_translation": "had(过去分词)",
        "examples": ["had"]
    },
    "VHZ": {
        "description": "has",
        "chinese_translation": "has",
        "examples": ["has"]
    },
    "VM": {
        "description": "modal auxiliary",
        "chinese_translation": "情态助动词",
        "examples": ["can", "will", "would"]
    },
    "VMK": {
        "description": "modal catenative",
        "chinese_translation": "链接情态动词",
        "examples": ["ought", "used"]
    },
    "VV0": {
        "description": "base form of lexical verb",
        "chinese_translation": "实义动词原形",
        "examples": ["give", "work"]
    },
    "VVD": {
        "description": "past tense of lexical verb",
        "chinese_translation": "实义动词过去式",
        "examples": ["gave", "worked"]
    },
    "VVG": {
        "description": "-ing participle of lexical verb",
        "chinese_translation": "实义动词-ing分词",
        "examples": ["giving", "working"]
    },
    "VVGK": {
        "description": "-ing participle catenative",
        "chinese_translation": "链接-ing分词",
        "examples": ["going in be going to"]
    },
    "VVI": {
        "description": "infinitive",
        "chinese_translation": "不定式",
        "examples": ["to give...", "It will work..."]
    },
    "VVN": {
        "description": "past participle of lexical verb",
        "chinese_translation": "实义动词过去分词",
        "examples": ["given", "worked"]
    },
    "VVNK": {
        "description": "past participle catenative",
        "chinese_translation": "链接过去分词",
        "examples": ["bound in be bound to"]
    },
    "VVZ": {
        "description": "-s form of lexical verb",
        "chinese_translation": "实义动词-s形式",
        "examples": ["gives", "works"]
    },
    "XX": {
        "description": "not, n't",
        "chinese_translation": "否定词not/n't",
        "examples": ["not", "n't"]
    },
    "ZZ1": {
        "description": "singular letter of the alphabet",
        "chinese_translation": "单数字母",
        "examples": ["A", "b"]
    },
    "ZZ2": {
        "description": "plural letter of the alphabet",
        "chinese_translation": "复数字母",
        "examples": ["A's", "b's"]
    }
}

spacy_pos_tags = {
    "$": {
        "description": "Dollar sign",
        "chinese_translation": "美元符号",
        "examples": ["$"]
    },
    "''": {
        "description": "Closing quotation mark",
        "chinese_translation": "闭合引号",
        "examples": ["'"]
    },
    ",": {
        "description": "Comma",
        "chinese_translation": "逗号",
        "examples": [","]
    },
    "-LRB-": {
        "description": "Left round bracket (i.e., '(')",
        "chinese_translation": "左圆括号",
        "examples": ["("]
    },
    "-RRB-": {
        "description": "Right round bracket (i.e., ')')",
        "chinese_translation": "右圆括号",
        "examples": [")"]
    },
    ".": {
        "description": "Sentence-final punctuation",
        "chinese_translation": "句末标点",
        "examples": ["."]
    },
    ":": {
        "description": "Colon, semi-colon, or dash",
        "chinese_translation": "冒号、分号或破折号",
        "examples": [":", ";", "-"]
    },
    "ADD": {
        "description": "Email address",
        "chinese_translation": "电子邮件地址",
        "examples": ["example@example.com"]
    },
    "AFX": {
        "description": "Affix",
        "chinese_translation": "词缀",
        "examples": ["un-", "re-", "-ing"]
    },
    "CC": {
        "description": "Coordinating conjunction",
        "chinese_translation": "并列连词",
        "examples": ["and", "but", "or"]
    },
    "CD": {
        "description": "Cardinal number",
        "chinese_translation": "基数",
        "examples": ["one", "two", "three"]
    },
    "DT": {
        "description": "Determiner",
        "chinese_translation": "限定词",
        "examples": ["the", "a", "an"]
    },
    "EX": {
        "description": "Existential 'there'",
        "chinese_translation": "存在句中的there",
        "examples": ["there"]
    },
    "FW": {
        "description": "Foreign word",
        "chinese_translation": "外来词",
        "examples": ["rendezvous", "schadenfreude"]
    },
    "HYPH": {
        "description": "Hyphen",
        "chinese_translation": "连字符",
        "examples": ["-"]
    },
    "IN": {
        "description": "Preposition or subordinating conjunction",
        "chinese_translation": "介词或从属连词",
        "examples": ["in", "on", "at", "if", "because"]
    },
    "JJ": {
        "description": "Adjective",
        "chinese_translation": "形容词",
        "examples": ["happy", "sad", "big"]
    },
    "JJR": {
        "description": "Adjective, comparative",
        "chinese_translation": "形容词比较级",
        "examples": ["happier", "sadder", "bigger"]
    },
    "JJS": {
        "description": "Adjective, superlative",
        "chinese_translation": "形容词最高级",
        "examples": ["happiest", "saddest", "biggest"]
    },
    "LS": {
        "description": "List item marker",
        "chinese_translation": "列表项标记",
        "examples": ["1.", "2.", "3."]
    },
    "MD": {
        "description": "Modal",
        "chinese_translation": "情态动词",
        "examples": ["can", "could", "may"]
    },
    "NFP": {
        "description": "Superfluous punctuation",
        "chinese_translation": "多余的标点符号",
        "examples": ["..."]
    },
    "NN": {
        "description": "Noun, singular or mass",
        "chinese_translation": "单数或质量名词",
        "examples": ["cat", "water", "sand"]
    },
    "NNP": {
        "description": "Proper noun, singular",
        "chinese_translation": "单数专有名词",
        "examples": ["John", "London", "Everest"]
    },
    "NNPS": {
        "description": "Proper noun, plural",
        "chinese_translation": "复数专有名词",
        "examples": ["Smiths", "Alps"]
    },
    "NNS": {
        "description": "Noun, plural",
        "chinese_translation": "复数名词",
        "examples": ["cats", "dogs", "houses"]
    },
    "PDT": {
        "description": "Predeterminer",
        "chinese_translation": "前位限定词",
        "examples": ["all", "both", "half"]
    },
    "POS": {
        "description": "Possessive ending",
        "chinese_translation": "所有格结尾",
        "examples": ["'s"]
    },
    "PRP": {
        "description": "Personal pronoun",
        "chinese_translation": "人称代词",
        "examples": ["I", "you", "he"]
    },
    "PRP$": {
        "description": "Possessive pronoun",
        "chinese_translation": "所有格代词",
        "examples": ["my", "your", "his"]
    },
    "RB": {
        "description": "Adverb",
        "chinese_translation": "副词",
        "examples": ["quickly", "happily", "sadly"]
    },
    "RBR": {
        "description": "Adverb, comparative",
        "chinese_translation": "副词比较级",
        "examples": ["faster", "happier", "more quickly"]
    },
    "RBS": {
        "description": "Adverb, superlative",
        "chinese_translation": "副词最高级",
        "examples": ["fastest", "happiest", "most quickly"]
    },
    "RP": {
        "description": "Particle",
        "chinese_translation": "小品词",
        "examples": ["up", "down", "off"]
    },
    "SYM": {
        "description": "Symbol",
        "chinese_translation": "符号",
        "examples": ["+", "=", "<"]
    },
    "TO": {
        "description": "'to'",
        "chinese_translation": "'to'",
        "examples": ["to"]
    },
    "UH": {
        "description": "Interjection",
        "chinese_translation": "感叹词",
        "examples": ["oh", "ah", "wow"]
    },
    "VB": {
        "description": "Verb, base form",
        "chinese_translation": "动词原形",
        "examples": ["run", "jump", "eat"]
    },
    "VBD": {
        "description": "Verb, past tense",
        "chinese_translation": "动词过去式",
        "examples": ["ran", "jumped", "ate"]
    },
    "VBG": {
        "description": "Verb, gerund or present participle",
        "chinese_translation": "动词动名词或现在分词",
        "examples": ["running", "jumping", "eating"]
    },
    "VBN": {
        "description": "Verb, past participle",
        "chinese_translation": "动词过去分词",
        "examples": ["run", "jumped", "eaten"]
    },
    "VBP": {
        "description": "Verb, non-3rd person singular present",
        "chinese_translation": "动词非第三人称单数现在式",
        "examples": ["run", "jump", "eat"]
    },
    "VBZ": {
        "description": "Verb, 3rd person singular present",
        "chinese_translation": "动词第三人称单数现在式",
        "examples": ["runs", "jumps", "eats"]
    },
    "WDT": {
        "description": "Wh-determiner",
        "chinese_translation": "Wh限定词",
        "examples": ["which", "that", "what"]
    },
    "WP": {
        "description": "Wh-pronoun",
        "chinese_translation": "Wh代词",
        "examples": ["who", "whom", "what"]
    },
    "WP$": {
        "description": "Possessive wh-pronoun",
        "chinese_translation": "所有格Wh代词",
        "examples": ["whose"]
    },
    "WRB": {
        "description": "Wh-adverb",
        "chinese_translation": "Wh副词",
        "examples": ["where", "when", "why"]
    },
    "XX": {
        "description": "Unknown",
        "chinese_translation": "未知",
        "examples": []
    },
    "_SP": {
        "description": "Space",
        "chinese_translation": "空格",
        "examples": [" "]
    },
    "``": {
        "description": "Opening quotation mark",
        "chinese_translation": "开放引号",
        "examples": ["`"]
    }
}


def word_list(split_words):
    """
    Parameters
    ----------
    split_words : TYPE list of strings
        DESCRIPTION.
            ['I','could',"n't",'believe','it','.','I','do',"n't",'like','it','.']

    Returns
    -------
    final_dic : TYPE list of tuples
        DESCRIPTION. 
            [('I', 2), ("n't", 2), ('it', 2), ('.', 2), ('could', 1), ('believe', 1), ('do', 1), ('like', 1)]
    """
    from collections import Counter
    my_dic=dict(Counter(split_words))
    final_dic=sorted(my_dic.items(),key=lambda x:x[1],reverse=True)
    return final_dic    

def batch_word_list(input_root):
    '''
    Parameters
    ----------
    input_root : TYPE string
        DESCRIPTION.
            It's a folder path like seg_only.
            Based on tokenized text.

    Returns
    -------
    sorted_words : TYPE list made of tuples.
        DESCRIPTION. 
            Caption: [(word, [word_freq, document_freq])]
            [('the', [543, 15]),
            ('and', [333, 15]),
            ('for', [98, 13]),
            ('Python', [40, 9]),
            ('English', [21, 2]),
            ('PgsFile', [12, 2]),
            ('beginners', [2, 2]),
            ('literature', [1, 1]),]
    '''
    from PgsFile import get_data_text as gt, FilePath as fp, BigPunctuation as bp
    # input_root=r"047_Scraping\seg_only"
    file_names=fp(input_root)
    
    from collections import defaultdict
    word_counts=defaultdict(lambda: [0, 0])
    
    for file_name in file_names:
        words=[w for w in gt(file_name).split() if w not in bp]
        for word in set(words):
            word_counts[word][0] += words.count(word)
            word_counts[word][1] += 1
    sorted_words=sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words 

def clean_list(meta):
    """
    Parameters
    ----------
    meta : TYPE list
        DESCRIPTION. # ['\n\n\t\t\t\t\t','来源：新民晚报','\xa0\xa0\xa0\xa0\n\t\t\t\t\t','\n\n\t\t\t\t\t\n\t\t\t\t\t\t','记者：陆梓华']

    Returns
    -------
    result : TYPE string
        DESCRIPTION.
            来源：新民晚报
            记者：陆梓华
            作者：陆梓华
            编辑：裘颖琼
            2022-07-21 17:47
    """
    result="\n".join([line.strip() for line in meta if line.strip()!="|" and len(line.strip())!=0])
    return result

yhd=["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36','Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)','Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0','Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)','Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5','Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5','Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5','Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1','Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6','NOKIA5700/ UCWEB7.0.2.37/28/999','Openwave/ UCWEB7.0.2.37/28/999','Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10','Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11','Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11','UCWEB7.0.2.37/28/999']

def source_path(relative_path):
    import sys,os
    if getattr(sys, 'frozen', False): 
        base_path=sys._MEIPASS
    else:
        base_path=os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def next_folder_names(folder):
    import os
    folder_namelist=next(os.walk(folder))[1]
    return folder_namelist

def remove_empty_txts(folder_path):
    import os
    files=FilePath(folder_path)
    target_list0=[]
    for file in files:
        lines=get_data_lines(file)
        if len(lines)==0:
            target_file0=file
            if os.path.exists(target_file0):
                os.remove(target_file0)
                target_list0.append(target_file0)
            else:
                print('no such file:%s' % file)
    print("{} deleted.".format(str(len(target_list0))+" files"))
    print(target_list0)

def remove_empty_folders(folder_path):
    import os
    dir_list=[]
    for root,dirs,files in os.walk(folder_path): 
        dir_list.append(root)
    delet_root=[]
    for root in dir_list[::-1]:
        if not os.listdir(root): 
            delet_root.append(root)
            os.rmdir(root)
    print(delet_root)
    print("Folders removed: ",len(delet_root))

def remove_file(file_path):
    import os
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f'{file_path} removed!')
    else:
        print(f"{file_path} doesn't exist")
            
def concatenate_excel_files(directory_path, output_file):
    # List to hold DataFrames
    dataframes = []

    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            file_path = os.path.join(directory_path, filename)
            df = pd.read_excel(file_path)
            dataframes.append(df)

    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Write the combined DataFrame to a new Excel file
    combined_df.to_excel(output_file, index=False)
    print(f"Combined Excel file saved as {output_file}")
    
def remove_empty_lines(folder_path):
    files=FilePath(folder_path)
    for file in files:
        lines=get_data_lines(file)
        new_lines=[para for para in lines if para not in ["\u200d\n"," \n", "\n", "\n ", "\n\n", "\r\n", "\xa0", "\u3000\u3000", "\xa0\n", "\xa0\xa0\n"]]
        f2=open(file,"w",encoding="utf-8")
        for i in new_lines:
            f2.write(i)
        f2.close()

def remove_empty_last_line(folder_path):
    files=FilePath(folder_path)
    end_empty_files=[]
    for file in files:
        lines=get_data_lines(file)
        new_lines=[]
        f2=open(file,"w",encoding="utf-8", errors="ignore")
        for i in range(len(lines)):
            if i==len(lines)-1:
                if "\n" in lines[i]:
                    lines[i]=lines[i].strip("\n")
                    end_empty_files.append(file)
                    f2.write(lines[i])
                else:
                    if "" in lines[i]: #""在最后一行的处理办法
                        lines[i]=lines[i].strip(" ")
                        end_empty_files.append(file)
                        f2.write(lines[i])
                    else:
                        f2.write(lines[i])
            else:
                lines[i]=lines[i]
                f2.write(lines[i])
        f2.close()
    print(end_empty_files,str(len(end_empty_files))+" files found with last line empty!")

def find_txt_files_with_keyword(root_folder, keyword, case_sensitive=None):
    """
    Find all .txt files whose names contain the specified keyword in a multi-level folder structure.

    Args:
        root_folder (str): The path to the root folder where the search should start.
        keyword (str): The keyword to search for in the file names.

    Returns:
        A list of file paths that match the search criteria.
    """
    import fnmatch,os
    matches=[]
    if case_sensitive is None or case_sensitive==False:
        for root, dirnames, filenames in os.walk(root_folder):
            for filename in fnmatch.filter(filenames, '*' + keyword + '*.txt'):
                matches.append(os.path.join(root, filename))
    elif case_sensitive==True:
        import re
        pattern=re.compile(r'.*' + re.escape(keyword) + r'.*\.txt')
        for root, dirnames, filenames in os.walk(root_folder):
            for filename in filenames:
                if pattern.match(filename):
                    matches.append(os.path.join(root, filename))
    return matches    

import fnmatch
def find_user_files_in_upper_folder(directory, user_file_name):
    # Get the direct upper folder path
    upper_folder = os.path.dirname(os.path.abspath(directory))

    # List to store matching file paths
    matching_files = []

    # Walk through the upper folder
    for root, dirs, files in os.walk(upper_folder):
        for filename in fnmatch.filter(files, f'{user_file_name}.user'):
            matching_files.append(os.path.join(root, filename))

    return matching_files

# Standard sentence tokenizer.
def sent_tokenize(text, lang=None):
    import pysbd
    if lang is None:
        lang="en"
    else:
        lang=lang
    seg = pysbd.Segmenter(language=lang, clean=False)
    sent_list = seg.segment(text)    
    return sent_list

def cs(para): 
    """
    #中文分句
    ---------
    Returns
    list
    """

    import re
    # import zhon
    # rst=re.findall(zhon.hanzi.sentence, para)
    # return rst  #['我买了一辆车。', '妈妈做的菜，很好吃！']
    para=re.sub(r'([。！？\?])([^”’])', r"\1\n\2", para)  # 单字符断句符
    para=re.sub(r'(\.{6})([^”’])', r"\1\n\2", para)  # 英文省略号
    para=re.sub(r'(\…{2})([^”’])', r"\1\n\2", para)  # 中文省略号
    para=re.sub(r'([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
    # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para=para.rstrip()  # 段尾如果有多余的\n就去掉它
    # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    paras=[s.strip() for s in para.split("\n") if s.strip()]
    return paras


def cs1(text):
    """
    #英文分句 
    using regular expression
    ---------
    Returns
    list
    """    
    import re
    alphabets="([A-Za-z])"
    prefixes="(Mr|St|Mrs|Ms|Dr)[.]"
    suffixes="(Inc|Ltd|Jr|Sr|Co)"
    starters=r"(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
    acronyms="([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites="[.](com|net|org|io|gov)"
    digits="([0-9])"
    
    text=" " + text + "  "
    text=text.replace("\n"," ")
    text=re.sub(prefixes,"\\1<prd>",text)
    text=re.sub(websites,"<prd>\\1",text)
    text=re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    if "..." in text: text=text.replace("...","<prd><prd><prd>")
    if "Ph.D" in text: text=text.replace("Ph.D.","Ph<prd>D<prd>")
    text=re.sub(r"\s" + alphabets + "[.] "," \\1<prd> ",text)
    text=re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text=re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text=re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text=re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text=re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text=re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text=text.replace(".”","”.")
    if "\"" in text: text=text.replace(".\"","\".")
    if "!" in text: text=text.replace("!\"","\"!")
    if "?" in text: text=text.replace("?\"","\"?")
    text=text.replace(".",".<stop>")
    text=text.replace("?","?<stop>")
    text=text.replace("!","!<stop>")
    text=text.replace("<prd>",".")
    sentences=text.split("<stop>")
    sentences=sentences[:-1]
    sentences=[s.strip() for s in sentences]
    if len(sentences)==0:
        sentences=sent_tokenize(text)
    else:
        sentences=sentences
    return sentences

def word_tokenize(text, pos_tagged=False):
    '''
    Parameters
    ----------
    text : TYPE, string like: "无独有偶，这个消息如晴天霹雳，霍尔姆斯听到后不知所措。中国电影家协会和中国作家协会，中国翻译协会是做慈善的。"
        DESCRIPTION.
    pos_tagged : TYPE, optional
        DESCRIPTION. The default is False.

    Returns
    -------
    words : TYPE, list like: ['无独有偶', '，', '这个', '消息', '如', '晴天霹雳', '，', '霍尔姆斯', '听到', '后', '不知所措', '。', '中国', '电影', '家', '协会', '和', '中国', '作家', '协会', '，', '中国', '翻译', '协会', '是', '做', '慈善', '的', '。', '']
        DESCRIPTION.

    '''
    words=None
    try:
        try:
            from nlpir import ictclas #调用中科院分词器ICTCLAS
        except Exception as err:
            print("installing nlpir/ICTCLAS...")
            from PgsFile import install_package as ip
            ip("nlpir-python")

        from nlpir import ictclas    
        if pos_tagged is False:
            words=ictclas.segment(text, pos_tagged=False) 
        else:
            words=ictclas.segment(text, pos_tagged=True) 
    except Exception as err:
        if "expired" in str(err):
            try:
                from nlpir import tools
                tools.update_license()
                print("\n\nThe user file is ready. Please restart your kernel and run the Python script!")
            except Exception as err2:
                print("\n*****SOLUTION WARNING! \nYOU MAY NEED A VPN TO TRY THIS SERVICE!*****\n\n", err2)
        else:
            try:
                if "Can not open" in str(err):
                    user_folder=get_library_location("PgsFile")+"/PgsFile/models"
                    destination_folder=get_library_location("nlpir-python")+"/nlpir/Data"
                    source_file=find_user_files_in_upper_folder(user_folder, "NLPIR")[0]
                    copy_file(source_file, destination_folder)  
                    print("The user file is ready. Please restart your kernel and run the Python script!")
                else:
                    print(err)
            except Exception as rer:
                print(rer)

    return words  

import re
from abc import ABC, abstractmethod
from typing import Iterator, List, Tuple
class TokenizerI(ABC):
    """
    A processing interface for tokenizing a string.
    Subclasses must define ``tokenize()`` or ``tokenize_sents()`` (or both).
    """

    @abstractmethod
    def tokenize(self, s: str) -> List[str]:
        """
        Return a tokenized copy of *s*.

        :rtype: List[str]
        """
        if overridden(self.tokenize_sents):
            return self.tokenize_sents([s])[0]

    def span_tokenize(self, s: str) -> Iterator[Tuple[int, int]]:
        """
        Identify the tokens using integer offsets ``(start_i, end_i)``,
        where ``s[start_i:end_i]`` is the corresponding token.

        :rtype: Iterator[Tuple[int, int]]
        """
        raise NotImplementedError()

    def tokenize_sents(self, strings: List[str]) -> List[List[str]]:
        """
        Apply ``self.tokenize()`` to each element of ``strings``.  I.e.:

            return [self.tokenize(s) for s in strings]

        :rtype: List[List[str]]
        """
        return [self.tokenize(s) for s in strings]

    def span_tokenize_sents(
        self, strings: List[str]
    ) -> Iterator[List[Tuple[int, int]]]:
        """
        Apply ``self.span_tokenize()`` to each element of ``strings``.  I.e.:

            return [self.span_tokenize(s) for s in strings]

        :yield: List[Tuple[int, int]]
        """
        for s in strings:
            yield list(self.span_tokenize(s))

class MacIntyreContractions:
    """
    List of contractions adapted from Robert MacIntyre's tokenizer.
    """

    CONTRACTIONS2 = [
        r"(?i)\b(can)(?#X)(not)\b",
        r"(?i)\b(d)(?#X)('ye)\b",
        r"(?i)\b(gim)(?#X)(me)\b",
        r"(?i)\b(gon)(?#X)(na)\b",
        r"(?i)\b(got)(?#X)(ta)\b",
        r"(?i)\b(lem)(?#X)(me)\b",
        r"(?i)\b(more)(?#X)('n)\b",
        r"(?i)\b(wan)(?#X)(na)(?=\s)",
    ]
    CONTRACTIONS3 = [r"(?i) ('t)(?#X)(is)\b", r"(?i) ('t)(?#X)(was)\b"]
    CONTRACTIONS4 = [r"(?i)\b(whad)(dd)(ya)\b", r"(?i)\b(wha)(t)(cha)\b"]
            
class NLTKWordTokenizer(TokenizerI):
    """
    The NLTK tokenizer that has improved upon the TreebankWordTokenizer.

    This is the method that is invoked by ``word_tokenize()``.  It assumes that the
    text has already been segmented into sentences, e.g. using ``sent_tokenize()``.

    The tokenizer is "destructive" such that the regexes applied will munge the
    input string to a state beyond re-construction. It is possible to apply
    `TreebankWordDetokenizer.detokenize` to the tokenized outputs of
    `NLTKDestructiveWordTokenizer.tokenize` but there's no guarantees to
    revert to the original string.
    """

    # Starting quotes.
    STARTING_QUOTES = [
        (re.compile("([«“‘„]|[`]+)", re.U), r" \1 "),
        (re.compile(r"^\""), r"``"),
        (re.compile(r"(``)"), r" \1 "),
        (re.compile(r"([ \(\[{<])(\"|\'{2})"), r"\1 `` "),
        (re.compile(r"(?i)(\')(?!re|ve|ll|m|t|s|d|n)(\w)\b", re.U), r"\1 \2"),
    ]

    # Ending quotes.
    ENDING_QUOTES = [
        (re.compile("([»”’])", re.U), r" \1 "),
        (re.compile(r"''"), " '' "),
        (re.compile(r'"'), " '' "),
        (re.compile(r"\s+"), " "),
        (re.compile(r"([^' ])('[sS]|'[mM]|'[dD]|') "), r"\1 \2 "),
        (re.compile(r"([^' ])('ll|'LL|'re|'RE|'ve|'VE|n't|N'T) "), r"\1 \2 "),
    ]

    # For improvements for starting/closing quotes from TreebankWordTokenizer,
    # see discussion on https://github.com/nltk/nltk/pull/1437
    # Adding to TreebankWordTokenizer, nltk.word_tokenize now splits on
    # - chevron quotes u'\xab' and u'\xbb'
    # - unicode quotes u'\u2018', u'\u2019', u'\u201c' and u'\u201d'
    # See https://github.com/nltk/nltk/issues/1995#issuecomment-376741608
    # Also, behavior of splitting on clitics now follows Stanford CoreNLP
    # - clitics covered (?!re|ve|ll|m|t|s|d)(\w)\b

    # Punctuation.
    PUNCTUATION = [
        (re.compile(r'([^\.])(\.)([\]\)}>"\'' "»”’ " r"]*)\s*$", re.U), r"\1 \2 \3 "),
        (re.compile(r"([:,])([^\d])"), r" \1 \2"),
        (re.compile(r"([:,])$"), r" \1 "),
        (
            re.compile(r"\.{2,}", re.U),
            r" \g<0> ",
        ),  # See https://github.com/nltk/nltk/pull/2322
        (re.compile(r"[;@#$%&]"), r" \g<0> "),
        (
            re.compile(r'([^\.])(\.)([\]\)}>"\']*)\s*$'),
            r"\1 \2\3 ",
        ),  # Handles the final period.
        (re.compile(r"[?!]"), r" \g<0> "),
        (re.compile(r"([^'])' "), r"\1 ' "),
        (
            re.compile(r"[*]", re.U),
            r" \g<0> ",
        ),  # See https://github.com/nltk/nltk/pull/2322
    ]

    # Pads parentheses
    PARENS_BRACKETS = (re.compile(r"[\]\[\(\)\{\}\<\>]"), r" \g<0> ")

    # Optionally: Convert parentheses, brackets and converts them to PTB symbols.
    CONVERT_PARENTHESES = [
        (re.compile(r"\("), "-LRB-"),
        (re.compile(r"\)"), "-RRB-"),
        (re.compile(r"\["), "-LSB-"),
        (re.compile(r"\]"), "-RSB-"),
        (re.compile(r"\{"), "-LCB-"),
        (re.compile(r"\}"), "-RCB-"),
    ]

    DOUBLE_DASHES = (re.compile(r"--"), r" -- ")

    # List of contractions adapted from Robert MacIntyre's tokenizer.
    _contractions = MacIntyreContractions()
    CONTRACTIONS2 = list(map(re.compile, _contractions.CONTRACTIONS2))
    CONTRACTIONS3 = list(map(re.compile, _contractions.CONTRACTIONS3))

    def tokenize(
        self, text: str, convert_parentheses: bool = False, return_str: bool = False
    ) -> List[str]:
        r"""Return a tokenized copy of `text`.

        >>> from nltk.tokenize import NLTKWordTokenizer
        >>> s = '''Good muffins cost $3.88 (roughly 3,36 euros)\nin New York.  Please buy me\ntwo of them.\nThanks.'''
        >>> NLTKWordTokenizer().tokenize(s) # doctest: +NORMALIZE_WHITESPACE
        ['Good', 'muffins', 'cost', '$', '3.88', '(', 'roughly', '3,36',
        'euros', ')', 'in', 'New', 'York.', 'Please', 'buy', 'me', 'two',
        'of', 'them.', 'Thanks', '.']
        >>> NLTKWordTokenizer().tokenize(s, convert_parentheses=True) # doctest: +NORMALIZE_WHITESPACE
        ['Good', 'muffins', 'cost', '$', '3.88', '-LRB-', 'roughly', '3,36',
        'euros', '-RRB-', 'in', 'New', 'York.', 'Please', 'buy', 'me', 'two',
        'of', 'them.', 'Thanks', '.']


        :param text: A string with a sentence or sentences.
        :type text: str
        :param convert_parentheses: if True, replace parentheses to PTB symbols,
            e.g. `(` to `-LRB-`. Defaults to False.
        :type convert_parentheses: bool, optional
        :param return_str: If True, return tokens as space-separated string,
            defaults to False.
        :type return_str: bool, optional
        :return: List of tokens from `text`.
        :rtype: List[str]
        """
        if return_str:
            warnings.warn(
                "Parameter 'return_str' has been deprecated and should no "
                "longer be used.",
                category=DeprecationWarning,
                stacklevel=2,
            )

        for regexp, substitution in self.STARTING_QUOTES:
            text = regexp.sub(substitution, text)

        for regexp, substitution in self.PUNCTUATION:
            text = regexp.sub(substitution, text)

        # Handles parentheses.
        regexp, substitution = self.PARENS_BRACKETS
        text = regexp.sub(substitution, text)
        # Optionally convert parentheses
        if convert_parentheses:
            for regexp, substitution in self.CONVERT_PARENTHESES:
                text = regexp.sub(substitution, text)

        # Handles double dash.
        regexp, substitution = self.DOUBLE_DASHES
        text = regexp.sub(substitution, text)

        # add extra space to make things easier
        text = " " + text + " "

        for regexp, substitution in self.ENDING_QUOTES:
            text = regexp.sub(substitution, text)

        for regexp in self.CONTRACTIONS2:
            text = regexp.sub(r" \1 \2 ", text)
        for regexp in self.CONTRACTIONS3:
            text = regexp.sub(r" \1 \2 ", text)

        # We are not using CONTRACTIONS4 since
        # they are also commented out in the SED scripts
        # for regexp in self._contractions.CONTRACTIONS4:
        #     text = regexp.sub(r' \1 \2 \3 ', text)

        return text.split()

    def span_tokenize(self, text: str) -> Iterator[Tuple[int, int]]:
        r"""
        Returns the spans of the tokens in ``text``.
        Uses the post-hoc nltk.tokens.align_tokens to return the offset spans.

            >>> from nltk.tokenize import NLTKWordTokenizer
            >>> s = '''Good muffins cost $3.88\nin New (York).  Please (buy) me\ntwo of them.\n(Thanks).'''
            >>> expected = [(0, 4), (5, 12), (13, 17), (18, 19), (19, 23),
            ... (24, 26), (27, 30), (31, 32), (32, 36), (36, 37), (37, 38),
            ... (40, 46), (47, 48), (48, 51), (51, 52), (53, 55), (56, 59),
            ... (60, 62), (63, 68), (69, 70), (70, 76), (76, 77), (77, 78)]
            >>> list(NLTKWordTokenizer().span_tokenize(s)) == expected
            True
            >>> expected = ['Good', 'muffins', 'cost', '$', '3.88', 'in',
            ... 'New', '(', 'York', ')', '.', 'Please', '(', 'buy', ')',
            ... 'me', 'two', 'of', 'them.', '(', 'Thanks', ')', '.']
            >>> [s[start:end] for start, end in NLTKWordTokenizer().span_tokenize(s)] == expected
            True

        :param text: A string with a sentence or sentences.
        :type text: str
        :yield: Tuple[int, int]
        """
        raw_tokens = self.tokenize(text)

        # Convert converted quotes back to original double quotes
        # Do this only if original text contains double quote(s) or double
        # single-quotes (because '' might be transformed to `` if it is
        # treated as starting quotes).
        if ('"' in text) or ("''" in text):
            # Find double quotes and converted quotes
            matched = [m.group() for m in re.finditer(r"``|'{2}|\"", text)]

            # Replace converted quotes back to double quotes
            tokens = [
                matched.pop(0) if tok in ['"', "``", "''"] else tok
                for tok in raw_tokens
            ]
        else:
            tokens = raw_tokens

        yield from align_tokens(tokens, text)

# Standard word tokenizer.
_treebank_word_tokenizer = NLTKWordTokenizer()
def word_tokenize2(text, preserve_line=False):
    """
    Return a tokenized copy of *text*,
    using NLTK's recommended word tokenizer
    (currently an improved :class:`.TreebankWordTokenizer`
    along with :class:`.PunktSentenceTokenizer`
    for the specified language).

    :param text: text to split into words
    :type text: str
    :param language: the model name in the Punkt corpus
    :type language: str
    :param preserve_line: A flag to decide whether to sentence tokenize the text or not.
    :type preserve_line: bool
    """
    sentences = [text] if preserve_line else sent_tokenize(text)
    return [
        token for sent in sentences for token in _treebank_word_tokenizer.tokenize(sent)
    ]
        
def pad_sequence(
    sequence,
    n,
    pad_left=False,
    pad_right=False,
    left_pad_symbol=None,
    right_pad_symbol=None,
):
    """
    Returns a padded sequence of items before ngram extraction.

        >>> list(pad_sequence([1,2,3,4,5], 2, pad_left=True, pad_right=True, left_pad_symbol='<s>', right_pad_symbol='</s>'))
        ['<s>', 1, 2, 3, 4, 5, '</s>']
        >>> list(pad_sequence([1,2,3,4,5], 2, pad_left=True, left_pad_symbol='<s>'))
        ['<s>', 1, 2, 3, 4, 5]
        >>> list(pad_sequence([1,2,3,4,5], 2, pad_right=True, right_pad_symbol='</s>'))
        [1, 2, 3, 4, 5, '</s>']

    :param sequence: the source data to be padded
    :type sequence: sequence or iter
    :param n: the degree of the ngrams
    :type n: int
    :param pad_left: whether the ngrams should be left-padded
    :type pad_left: bool
    :param pad_right: whether the ngrams should be right-padded
    :type pad_right: bool
    :param left_pad_symbol: the symbol to use for left padding (default is None)
    :type left_pad_symbol: any
    :param right_pad_symbol: the symbol to use for right padding (default is None)
    :type right_pad_symbol: any
    :rtype: sequence or iter
    """
    sequence=iter(sequence)
    if pad_left:
        sequence=chain((left_pad_symbol,) * (n - 1), sequence)
    if pad_right:
        sequence=chain(sequence, (right_pad_symbol,) * (n - 1))
    return sequence

# add a flag to pad the sequence so we get peripheral ngrams?
def ngrams(
    sequence,
    n,
    pad_left=False,
    pad_right=False,
    left_pad_symbol=None,
    right_pad_symbol=None,
):
    """
    Return the ngrams generated from a sequence of items, as an iterator.
    For example:

        >>> from nltk.util import ngrams
        >>> list(ngrams([1,2,3,4,5], 3))
        [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

    Wrap with list for a list version of this function.  Set pad_left
    or pad_right to true in order to get additional ngrams:

        >>> list(ngrams([1,2,3,4,5], 2, pad_right=True))
        [(1, 2), (2, 3), (3, 4), (4, 5), (5, None)]
        >>> list(ngrams([1,2,3,4,5], 2, pad_right=True, right_pad_symbol='</s>'))
        [(1, 2), (2, 3), (3, 4), (4, 5), (5, '</s>')]
        >>> list(ngrams([1,2,3,4,5], 2, pad_left=True, left_pad_symbol='<s>'))
        [('<s>', 1), (1, 2), (2, 3), (3, 4), (4, 5)]
        >>> list(ngrams([1,2,3,4,5], 2, pad_left=True, pad_right=True, left_pad_symbol='<s>', right_pad_symbol='</s>'))
        [('<s>', 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, '</s>')]


    :param sequence: the source data to be converted into ngrams
    :type sequence: sequence or iter
    :param n: the degree of the ngrams
    :type n: int
    :param pad_left: whether the ngrams should be left-padded
    :type pad_left: bool
    :param pad_right: whether the ngrams should be right-padded
    :type pad_right: bool
    :param left_pad_symbol: the symbol to use for left padding (default is None)
    :type left_pad_symbol: any
    :param right_pad_symbol: the symbol to use for right padding (default is None)
    :type right_pad_symbol: any
    :rtype: sequence or iter
    """
    sequence=pad_sequence(
        sequence, n, pad_left, pad_right, left_pad_symbol, right_pad_symbol
    )

    history=[]
    while n > 1:
        # PEP 479, prevent RuntimeError from being raised when StopIteration bubbles out of generator
        try:
            next_item=next(sequence)
        except StopIteration:
            # no more data, terminate the generator
            return
        history.append(next_item)
        n -= 1
    for item in sequence:
        history.append(item)
        yield tuple(history)
        del history[0]

def bigrams(sequence, **kwargs):
    """
    Return the bigrams generated from a sequence of items, as an iterator.
    For example:

        >>> from nltk.util import bigrams
        >>> list(bigrams([1,2,3,4,5]))
        [(1, 2), (2, 3), (3, 4), (4, 5)]

    Use bigrams for a list version of this function.

    :param sequence: the source data to be converted into bigrams
    :type sequence: sequence or iter
    :rtype: iter(tuple)
    """

    for item in ngrams(sequence, 2, **kwargs):
        yield item

def trigrams(sequence, **kwargs):
    """
    Return the trigrams generated from a sequence of items, as an iterator.
    For example:

        >>> from nltk.util import trigrams
        >>> list(trigrams([1,2,3,4,5]))
        [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

    Use trigrams for a list version of this function.

    :param sequence: the source data to be converted into trigrams
    :type sequence: sequence or iter
    :rtype: iter(tuple)
    """

    for item in ngrams(sequence, 3, **kwargs):
        yield item

def everygrams(sequence, min_len=1, max_len=-1, **kwargs):
    """
    Returns all possible ngrams generated from a sequence of items, as an iterator.

        >>> sent='a b c'.split()
        >>> list(everygrams(sent))
        [('a',), ('b',), ('c',), ('a', 'b'), ('b', 'c'), ('a', 'b', 'c')]
        >>> list(everygrams(sent, max_len=2))
        [('a',), ('b',), ('c',), ('a', 'b'), ('b', 'c')]

    :param sequence: the source data to be converted into trigrams
    :type sequence: sequence or iter
    :param min_len: minimum length of the ngrams, aka. n-gram order/degree of ngram
    :type  min_len: int
    :param max_len: maximum length of the ngrams (set to length of sequence by default)
    :type  max_len: int
    :rtype: iter(tuple)
    """

    if max_len==-1:
        max_len=len(sequence)
    for n in range(min_len, max_len + 1):
        for ng in ngrams(sequence, n, **kwargs):
            yield ng

def strQ2B_raw(ustring):
           ss=[]
           for s in ustring:
                      rstring=""
                      for uchar in s:
                                 inside_code=ord(uchar)
                                 if inside_code==12288:
                                            inside_code==32
                                 elif (inside_code>=65281 and inside_code<=65374):
                                            inside_code-=65248
                                 rstring+=chr(inside_code)
                      ss.append(rstring)          
           return "".join(ss) #字符间是否需要空格

def strQ2B_words(ustring): #分词后使用
           ss=[]
           for s in ustring:
                      rstring=""
                      for uchar in s:
                                 inside_code=ord(uchar)
                                 if inside_code==12288:
                                            inside_code==32
                                 elif (inside_code>=65281 and inside_code<=65374):
                                            inside_code-=65248
                                 rstring+=chr(inside_code)
                      ss.append(rstring)          
           return " ".join(ss) #字符间是否需要空格
       
def replace_chinese_punctuation_with_english(text):
    import re
    # 定义中文标点和对应的英文标点的映射关系
    punctuation_mapping={
        '，': ',',
        '。': '.',
        '？': '?',
        '！': '!',
        '；': ';',
        '：': ':',
        '（': '(',
        '）': ')',
        '【': '[',
        '】': ']',
        '｛': '{',
        '｝': '}',
        '《': '<',
        '》': '>',
        '“': '"',
        '”': '"',
        '‘': '\'',
        '’': '\''}
    # 使用正则表达式替换中文标点符号
    for chi_punct, eng_punct in punctuation_mapping.items():
        text=re.sub(re.escape(chi_punct), eng_punct, text)
    return text    

def replace_english_punctuation_with_chinese(text):
    import re
    # 定义英文标点和对应的中文标点的映射关系
    punctuation_mapping={
        ',': '，',
        # '.': '。', # 去掉！
        '?': '？',
        '!': '！',
        ';': '；',
        ':': '：',
        '(': '（',
        ')': '）',
        '[': '【',
        ']': '】',
        '{': '｛',
        '}': '｝',
        '<': '《',
        '>': '》'}
    # 使用正则表达式替换英文标点符号
    for eng_punct, chi_punct in punctuation_mapping.items():
        text=re.sub(re.escape(eng_punct), chi_punct, text)
    return text         

def extract_misspelled_words_from_docx(file_path, mode=None):
    '''
    Parameters
    ----------
    file_path : TYPE string
        DESCRIPTION. r"DocsMetrics for Translation Quality Assessment_A Case for Standardising Error Typologies.docx"
    mode : TYPE, optional string
        DESCRIPTION. 
        1. The default is None, which means extracting all words with double underlines and wavy lines. 
        2. The "spell" mode means extracting all words with wavy red lines.
        3. The "gram" mode means extracting all words with double underlines.
        
    Returns
    -------
    matches : TYPE list
        DESCRIPTION. 
        ['Standardising', 'centring', 'categorise', 'standardisation', 'characterised']
    '''
    import docx # pip install python-docx
    import re
    document=docx.Document(file_path)
    document_xml=document.element.xml
    # Save the XML string as an txt file
    # from PgsFile import write_to_txt as wt
    # wt(output_path,document_xml)
    if mode is None: # double underlines & wavy lines
        pattern=r'<w:proofErr.*?/>.*?<w:t>(.*?)</w:t>.*?<w:proofErr.*?/>' 
    elif mode=="spell": #wavy red lines
        pattern=r'<w:proofErr w:type="spellStart"/>.*?<w:t>(.*?)</w:t>.*?<w:proofErr w:type="spellEnd"/>' 
    elif mode=="gram": #double underlines
        pattern=r'<w:proofErr w:type="gramStart"/>.*?<w:t>(.*?)</w:t>.*?<w:proofErr w:type="gramEnd"/>' 
    matches=re.findall(pattern, document_xml, re.DOTALL)
    return matches

def install_package(package_name: str):
    """Install a Python package using pip.
    Args:
        package_name: The name of the package to install.
    """
    import pip
    pip.main(['install', package_name])

def uninstall_package(package_name: str):
    """Uninstall a Python package using pip.
    Args:
        package_name: The name of the package to uninstall.
    """
    import pip
    pip.main(['uninstall', package_name, '-y'])

# A list of conda configuration commands.
conda_mirror_commands=[
    "pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple", # Windows recommended
    "conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/", # MacOS recommended
    "conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/",
    "conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/",
    "conda config --append channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/fastai/",
    "conda config --append channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/",
    "conda config --append channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/",
    "pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/"
]

def DirList(root_dir: str) -> tuple: 
    """
    List the contents of a directory and return two lists containing the names of the directories and files in the directory.

    Args:
        root_dir (str): The path to the directory whose contents should be listed.

    Returns:
        tuple: A tuple containing two lists: the first list contains the names of the directories in the root directory, and the second list contains the names of the files in the root directory.
    """    
    import os
    dirct=root_dir
    dirList=[]
    fileList=[]
    files=os.listdir(dirct)  # Get a list of all the files and directories in the root directory

    for f in files:
        if os.path.isdir(dirct + '/'+f): # If the item is a directory, add its name to the directory list
            dirList.append(f)
        elif os.path.isfile(dirct + '/'+f): # Get a list of all the files and directories in the root directory
            fileList.append(f)
    return dirList, fileList

def get_text_length_kb(text: str) -> str:
    """
    Get the length of a text string in KB (kilobytes, eg.26.5 KB).
    """
    # Get the length of the text in bytes
    text_bytes=len(text.encode('utf-8'))

    # Convert the length to KB
    text_kb=text_bytes / 1024
    rounded_num=round(text_kb, 2)
    
    text_kb=f'{rounded_num} KB'
    print(type(text_kb))

    return text_kb

def run_script(py_path: str):
    """
    Open a Python script in the Python interactive command line.

    Args:
        py_path (str): The file path of the Python script to open.
    """
    from builtins import open
    exec(get_data_text(py_path))    

def generate_password(length: int) -> str:
    """
    Generate a random password of a specified length.
    
    Args:
        length (int): The length of the random string to generate.

    Returns:
        str: A random string of the specified length.
    """
    import random
    # Define the set of characters to choose from
    character_set="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    random_password=''.join(random.choice(character_set) for _ in range(length))

    return random_password

def extract_numbers(string: str) -> list:
    """
    Extract numbers from a string and convert them to integers.

    Args:
        string (str): The input string containing numbers.

    Returns:
        list: A list of the extracted numbers as integers, interspersed with the original string fragments.
    """
    import re
    # Define a regular expression to match one or more digits
    digit_pattern=re.compile(r'(\d+)')

    # Split the input string using the regular expression
    fragments=digit_pattern.split(string)

    # Convert every other fragment to an integer (the ones that match the digit pattern)
    for i in range(1, len(fragments), 2):
        fragments[i]=int(fragments[i])
        
    return fragments

def sort_strings_with_embedded_numbers(strings: list) -> list:
    """
    Sort a list of strings containing embedded numbers.

    The strings are sorted based on the embedded numbers, with earlier numbers taking precedence over later ones.

    Args:
        strings (list): The list of strings to sort.

    Returns:
        list: A new list containing the sorted strings.
    """
    # Sort the strings using the extract_numbers() function as the key
    sorted_strings=sorted(strings, key=extract_numbers)
    return sorted_strings

def run_command(command: str) -> str:
    """
    Run a command and return its output as a string.

    Args:
        command (str): The command to run.

    Returns:
        str: The output of the command.
    """
    import subprocess
    # Run the command and capture the output
    output=subprocess.check_output(command, shell=True)

    # Decode the output from bytes to string
    output_str=output.decode()

    return output_str

# Import the urllib.parse module to handle URL encoding
import urllib.parse
# Define a function to URL-encode a Chinese keyword
def encode_chinese_keyword_for_url(chinese_keyword):
    # Use urllib.parse.quote to encode the Chinese keyword
    encoded_keyword = urllib.parse.quote(chinese_keyword)
    # Return the encoded keyword
    return encoded_keyword

import random
import requests
from lxml import html, etree
import pandas as pd
my_headers={"User-Agent": random.choice(yhd)} 

from fake_useragent import UserAgent
ua = UserAgent()
headers = {"User-Agent": ua.random}

class PGScraper(object): 
    def __init__(self): 
        self.pattern=[] 
        self.urls=[]
        self.show_url=None

    def get_initial_text(self, url, want_list, show_url=False, timeout=None, headers=None, cookies=None, params=None, proxies=None):
        all_want_list=[]
        valid_xpath=[]
        valid_span=[]
        # Example HTML content
        if timeout is None:
            real_timeout=24.0
        else:
            real_timeout=timeout
        
        r=requests.get(url,timeout=real_timeout,headers=headers, cookies=cookies, params=params, proxies=proxies)
        if r.status_code==200:
            r.encoding="utf-8"
            html_content=r.content
            # Parse HTML content
            tree=html.fromstring(html_content)
            relative_xpaths=[]
            for text in want_list:
                # Find elements containing the text
                elements=tree.xpath(f"//*[contains(text(), '{text}')]")
                if not elements:
                    return None
                
                # Assume we want the first matching element
                element=elements[0]
                absolute_xpath=tree.getroottree().getpath(element)
                relative_xpaths.append(absolute_xpath)
            
            path1=relative_xpaths[0]
            path2=relative_xpaths[1]
            
            common_pat=[]
            for i,j in zip(path1.split("/"), path2.split("/")):
                if i==j:
                    common_pat.append(i)
                else:
                    rs=i.split("[")[0]+"[id_holder]"
                    common_pat.append(rs)
                    valid_span=[int(i.split("[")[1].strip("]")), int(j.split("[")[1].strip("]"))]
            general_path="/".join(common_pat)
            
            minspan=min(valid_span)
            maxspan=max(valid_span)
            if show_url==False:
                for n in range(1,1000):
                    if n<minspan:
                        try:
                            my_path=general_path.replace("id_holder", str(n))+"/text()"
                            target_eles=tree.xpath(my_path)
                            if len(target_eles)>0:
                                all_want_list.append(clean_list(target_eles))                    
                                valid_xpath.append(my_path)
                        except:
                            error_type, value, traceback=sys.exc_info()
                            error_info=f'{error_type}\n{value}\n{traceback}'                            
                            print(error_info)
        
                    elif minspan<=n<=maxspan:
                        my_path=general_path.replace("id_holder", str(n))+"/text()"
                        target_eles=tree.xpath(my_path)
                        all_want_list.append(clean_list(target_eles))
                        valid_xpath.append(my_path)
                    elif maxspan<n:
                        my_path=general_path.replace("id_holder", str(n))+"/text()"
                        target_eles=tree.xpath(my_path)
                        if len(target_eles)>0:
                            all_want_list.append(clean_list(target_eles))
                            valid_xpath.append(my_path)
                        else:
                            break
                self.pattern=valid_xpath
                self.show_url=False
                return all_want_list     
               
            else: #with title's url
                for n in range(1,1000):
                    if n<minspan:
                        try:
                            my_path=general_path.replace("id_holder", str(n))+"/text()"
                            my_path_url=general_path.replace("id_holder", str(n))+"/@href"
                            target_eles=tree.xpath(my_path)
                            target_url_eles=tree.xpath(my_path_url)
                            if len(target_eles)>0:
                                all_want_list.append((clean_list(target_eles),clean_list(target_url_eles)))                    
                                valid_xpath.append((my_path,my_path_url))
                        except:
                            error_type, value, traceback=sys.exc_info()
                            error_info=f'{error_type}\n{value}\n{traceback}'                            
                            print(error_info)
        
                    elif minspan<=n<=maxspan:
                        my_path=general_path.replace("id_holder", str(n))+"/text()"
                        my_path_url=general_path.replace("id_holder", str(n))+"/@href"
                        target_eles=tree.xpath(my_path)
                        target_url_eles=tree.xpath(my_path_url)
                        all_want_list.append((clean_list(target_eles),clean_list(target_url_eles)))          
                        valid_xpath.append((my_path,my_path_url))
                    elif maxspan<n:
                        my_path=general_path.replace("id_holder", str(n))+"/text()"
                        my_path_url=general_path.replace("id_holder", str(n))+"/@href"
                        target_eles=tree.xpath(my_path)
                        target_url_eles=tree.xpath(my_path_url)
                        if len(target_eles)>0:
                            all_want_list.append((clean_list(target_eles),clean_list(target_url_eles)))          
                            valid_xpath.append((my_path,my_path_url))
                        else:
                            break
                self.pattern=valid_xpath
                self.show_url=True
                return all_want_list     
        
        else:
            print(r.status_code,"invalid url",url)            
            self.pattern=valid_xpath
            return all_want_list                 
    
    def get_similar_text(self, url, timeout=None, headers=None, cookies=None, params=None, proxies=None):
        all_want_list=[]
        # Example HTML content
        if timeout is None:
            real_timeout=24.0
        else:
            real_timeout=timeout
            
        r=requests.get(url, timeout=real_timeout, headers=headers, cookies=cookies, params=params, proxies=proxies)
        if r.status_code==200:
            r.encoding="utf-8"
            html_content=r.content
            # Parse HTML content
            tree=html.fromstring(html_content)
            if self.show_url==True:
                for pat,url in self.pattern:
                    target_eles=tree.xpath(pat)
                    target_url_eles=tree.xpath(url)
                    all_want_list.append((clean_list(target_eles), clean_list(target_url_eles)))
            else:     
                for pat in self.pattern:
                    target_eles=tree.xpath(pat)
                    all_want_list.append(clean_list(target_eles))                    
            return all_want_list
        else:
            print(r.status_code,"invalid url",url)            
            return all_want_list   


    
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:11:45 2020
Showing download progress and speed when audio-visual files like MP4, MP3, JPG etc are downloading!
@author: Petercusin
"""

import time
from contextlib import closing 

def audiovisual_downloader(url, path, headers=None, params=None, cookies=None):
    with closing(requests.get(url, stream=True, headers=headers, params=params, cookies=cookies)) as r:
        chunk_size=1024*10
        content_size=int(r.headers['content-length'])
        print('Initiating download...')
        with open(path, "wb") as f:
            p=ProgressData(size=content_size, unit='Kb', block=chunk_size)
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                p.output()
                
class ProgressData(object):
    def __init__(self, block, size, unit, file_name='', ):
        self.file_name=file_name
        self.block=block/1000.0
        self.size=size/1000.0
        self.unit=unit
        self.count=0
        self.start=time.time()
    def output(self):
        self.end=time.time()
        self.count += 1
        speed=self.block/(self.end-self.start) if (self.end-self.start)>0 else 0
        self.start=time.time()
        loaded=self.count*self.block
        progress=round(loaded/self.size, 4)
        if loaded >= self.size:
            print(u'%sYour download has finished successfully.\r\n'%self.file_name)
        else:
            print(u'{0}Download Progress: {1:.2f}{2}/{3:.2f}{4} {5:.2%} Download Speed: {6:.2f}{7}/s'.\
                  format(self.file_name, loaded, self.unit,\
                  self.size, self.unit, progress, speed, self.unit))
            print('%50s'%('/'*int((1-progress)*50)))

def levenshtein_distance(s, t):
	m, n=len(s), len(t)
	if m < n:
		s, t=t, s
		m, n=n, m
	d=[list(range(n + 1))] + [[i] + [0] * n for i in range(1, m + 1)]
	for j in range(1, n + 1):
		for i in range(1, m + 1):
			if s[i - 1]==t[j - 1]:
				d[i][j]=d[i - 1][j - 1]
			else:
				d[i][j]=min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1
	return d[m][n]

def compute_similarity(input_string, reference_string):
	distance=levenshtein_distance(input_string, reference_string)
	max_length=max(len(input_string), len(reference_string))
	similarity=1 - (distance / max_length)
	return similarity

pgs_abbres_words=['A.B.','A.D.','A.G.','A.I.','A.M.','A.P.','A.V.','AFP.','Ala.','Alta.','Apr.','Ariz.','Ark.','Assn.','Aug.','Ave.','B.A.','B.C','B.C.','B.Ed.','B.I.G','B.R.','B.S.','Blvd.','Brig.','Brig.-Gen.','Bros.','C.D.','C.E.O','C.I.A.','C.M.','C.V.','Calif.','Capt.','Cf.','Ch.','Cie.','Cir.','Cllr.','Cmdr.','Co.','Co.Design','Col.','Colo.','Conn.','Corp.','Cos.','Coun.','Cpl.','Cres.','D.C.','D.D.S.','D.J.','D.K.','D.S.','Dec.','Del.','Dept.','Det.','Dr.','E.B.','E.C.','E.ON','E.U.','E.coli','E.g.','Ed.','Esq.','F.C.','Feb.','Fig.','Fla.','Fri.','G.K.','G.M.','G.Skill','Ga.','Gen.','Gov.','Govt.','H.E.','H.L.','H.S.','Hon.','Hwy.','I.T.','I.e.','Ill.','Inc.','Ind.','J.Crew','J.D.','J.G.','J.P','J.R.R.','Jan.','Jr.','Jul.','Jun.','K.C.','K.J.','K.M.','K.N.','K.P.','K.R.','Kan.','Ky.','L.A.','L.L.','L.S.','LLC.','La.','Lieut.','Lt.','Lt.-Cmdr.','Lt.-Col.','Lt.-Gen.','Ltd.','M.A.','M.B.','M.B.A.','M.D.','M.E.N','M.I.A.','M.J.','M.M.','M.P.','M.S.','Maj.','Maj.-Gen.','Man.','Mar.','Mass.','Md.','Messrs.','Mfg.','Mfrs.','Mich.','Minn.','Miss.','Mmes.','Mo.','Mon.','Mr.','Mrs.','Ms.','Msgr.','Mss.','N.A.','N.B.','N.C.','N.D.','N.H.','N.J.','N.L.','N.M.','N.S.','N.W.A.','N.W.T.','N.Y.','Neb.','Nev.','No.','Nos.','Nov.','O.C.','O.K.','O.S.','Oct.','Okla.','Ont.','Op.','Ore.','P.C.','P.E.','P.E.I.','P.K.','P.M.','P.O.','P.R.','P.S.','Pa.','Ph.D','Ph.D.','Plc.','Pres.','Prof.','Psy.D.','Pte.','Que.','R.E.M.','R.I.','R.I.P.','R.M','R.R.','Rd.','Rep.','Rev.','Rs.','Rt.','S.A.','S.C.','S.D.','S.F.','S.H.I.E.L.D.','S.K.','S.League','S.M.','S.P.','Sask.','Sat.','Sec.','Sen.','Sep.','Sgt.','Sr.','St.','Ste.','Sub-Lieut.','Sun.','Supt.','T.A.','T.R.','T.V.','TV.','Tenn.','Tex.','Thu.','Tue.','Twp.','U.A.E.','U.K.','U.N','U.P.','U.S','U.S.','U.S.A.','U.S.C.','UK.','US.','V.P.','Va.','Vol.','Vt.','W.H.O.','W.Va.','Wash.','Wed.','Wis.','Y.T.','a.m.','abr.','anon.','bk.','bks.','bull.','c.','ca.','cf.','ch.','def.','e.g.','ed.','eds.','et al.','etc.','fig.','ft.','fwd.','gal.','i.e.','ibid.','illus.','in.','jour.','lb.','mag.','mi.','ms.','mss.','no.','oz.','p.','p.m.','pg.','pgs.','pp.','pseud.','pt.','pts.','pub.','qt.','qtd.','ser.','supp.','trans.','viz.','vol.','vols.','vs.','yd.']

def clean_text(text): #清洗除了句号以外的其他标点符号问题
    # 在标点符号右边邻接单词前添加空格
    import re
    # text=replace_chinese_punctuation_with_english(text) 
    text=re.sub(r'(?<=[\?\!\,\;\:\)\]\}])\s*(?=\w)', ' ', text)
    # 删除标点符号与左边单词之间的空格
    text=re.sub(r'\s*([\?\!\,\;\:\)\]\}\>])', r'\1', text)
    # 删除标点符号与右边单词之间的空格
    text=re.sub(r'\s*\(\s*', r' (', text)
    text=re.sub(r'\s*\[\s*', r' [', text)
    text=re.sub(r'\s*\{\s*', r' {', text)
    text=re.sub(r'\s*\<\s*', r' <', text)
    # 处理多余的空格
    text=re.sub(r'\s{2,}', ' ', text)
    text=re.sub(r'-{2,}', '-', text)
    return text

def clean_text_with_abbreviations(text):
    import re

    # 按行分割文本
    lines = text.splitlines()

    # 清洗每一行
    cleaned_lines = []
    for line in lines:
        cleaned_line = clean_line_with_abbreviations(line)
        cleaned_lines.append(cleaned_line)

    # 将清洗后的行重新组合成文本
    cleaned_text = '\n'.join(cleaned_lines)
    return cleaned_text

def clean_line_with_abbreviations(line):
    import re

    # 清洗除了句号以外的其他标点符号问题
    line = clean_text(line)

    matches = []
    for seg in line.split():
        if "." in seg:
            if not seg.endswith("."):
                matches.append(seg)
            elif seg.endswith("..") and "..." not in seg:
                line = line.replace("..", ".")

    for match in matches:
        if any(word in match for word in pgs_abbres_words):
            inter = match.split(".")
            new_match = "".join([w + "." for w in inter[0:-1]]) + " " + inter[-1]
            line = line.replace(match, new_match)
        else:
            line = line.replace(match, match.replace(".", ". "))

    line = re.sub(r'\s+\.', '.', line)
    return line


import shutil
def move_file(source_file, destination_folder, new_file_name=None):
    """
    Move/cut a file to another folder.

    Parameters:
    source_file (str): The path to the source file.
    destination_folder (str): The path to the destination folder.
    new_file_name (str, optional): The new name for the file in the destination folder. Defaults to None.
    """
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Construct the destination file path
    if new_file_name:
        destination_file=os.path.join(destination_folder, new_file_name)
    else:
        destination_file=os.path.join(destination_folder, os.path.basename(source_file))

    # Move the file to the destination folder
    shutil.move(source_file, destination_file)

    print(f"File moved from {source_file} to {destination_file}")

def copy_file(source_file, destination_folder, new_file_name=None):
    """
    Copy a file to another folder.

    Parameters:
    source_file (str): The path to the source file.
    destination_folder (str): The path to the destination folder.
    new_file_name (str, optional): The new name for the file in the destination folder. Defaults to None.
    """
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Construct the destination file path
    if new_file_name:
        destination_file = os.path.join(destination_folder, new_file_name)
    else:
        destination_file = os.path.join(destination_folder, os.path.basename(source_file))

    # Copy the file to the destination folder
    shutil.copy2(source_file, destination_file)
    
def check_empty_cells(file_path):
    """
    Check for any empty cells in an Excel file and return their exact positions.

    Parameters:
    file_path (str): The path to the Excel file.

    Returns:
    list of tuples: A list of tuples where each tuple contains the column ID and row ID of an empty cell. If no empty cells are found, an empty list is returned.

    Example:
    empty_cells=check_empty_cells('your_file.xlsx')
    if empty_cells:
        print(f"Empty cells found at positions: {empty_cells}")
    else:
        print("No empty cells found.")
    """
    # Read the Excel file
    df=pd.read_excel(file_path)

    # Initialize a list to store the positions of empty cells
    empty_cells=[]

    # Iterate over the DataFrame to find empty cells
    for row_id, row in df.iterrows():
        for col_id, value in row.items():
            if pd.isnull(value):
                empty_cells.append((col_id, row_id))

    return empty_cells

def makefile(file_path):
    if os.path.exists(file_path):
        pass
    else:
        write_to_txt(file_path, "")
        
def save_dict_to_excel(data, output_file, headers=None):
    """
    Save Python dictionary data into an Excel .xlsx file with custom headers.

    Parameters:
    data (dict): The dictionary containing the data to be saved.
    output_file (str): The path to the output Excel file.
    headers (list of str, optional): A list of strings representing the headers for the Excel file. Defaults to ['Key', 'Value'] if not provided.

    Returns:
    None

    Example:
    data={'key1': 'value1', 'key2': 'value2'}
    output_file='output.xlsx'
    save_dict_to_excel(data, output_file)  # Uses default headers
    save_dict_to_excel(data, output_file, headers=['Source Text', 'Target Text'])  # Uses custom headers
    """
    if headers is None:
        headers=['Key', 'Value']
    elif len(headers) != 2:
        raise ValueError("Headers list must contain exactly 2 elements.")

    # Convert the dictionary to a DataFrame
    df=pd.DataFrame(list(data.items()), columns=headers)

    # Save the DataFrame to an Excel file
    df.to_excel(output_file, index=False)

def len_rows(file_path):
    """
    Calculate the number of rows in an Excel file based on the largest row number of any possible columns.

    Parameters:
    file_path (str): The path to the Excel file.

    Returns:
    int: The number of rows in the Excel file.
    """
    # Read the Excel file
    df=pd.read_excel(file_path)

    # Get the number of rows
    row_count=df.shape[0]

    return row_count

def format_float(number, decimal_places=2):
    """
    Format a float to a specified number of decimal places.

    Parameters:
    number (float): The float number to be formatted.
    decimal_places (int, optional): The number of decimal places to format the number to. Defaults to 2.

    Returns:
    str: The formatted number as a string with the specified number of decimal places.

    Example:
    formatted_number=format_float(3.1415926535)
    print(formatted_number)  # Output: 3.14

    formatted_number=format_float(3.1415926535, 4)
    print(formatted_number)  # Output: 3.1416
    """
    formatted_number="{:.{precision}f}".format(number, precision=decimal_places)
    return formatted_number


def mhtml2html(input_file_path, output_file_path=None):
    """
    Extracts HTML content from an MHTML file. Optionally saves it to an HTML file and returns the HTML string.

    Parameters:
    input_file_path (str): The path to the MHTML file.
    output_file_path (str, optional): The path to the output HTML file. If None, the HTML content will not be saved.

    Returns:
    str: The extracted HTML content.
    """
    import pimht
    mhtml = pimht.from_filename(input_file_path)
    longest_length = 0
    html_content = ""

    for mhtml_part in mhtml:
        if "text/html" in mhtml_part.content_type:
            possible_html = mhtml_part.text
            current_length = len(possible_html)
            if current_length > longest_length:
                longest_length = current_length
                html_content = possible_html

    if output_file_path:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"HTML content successfully saved to {output_file_path}\n")
            
    return html_content
    

def get_data_html_offline(file_path):
    """
    Reads a local HTML/XML file and extracts specific elements.
    Parameters:
    file_path (str): The path to the local HTML file. my_html="Top 5 Web Scraping Methods_ Including Using LLMs - Comet.mhtml"
    
    Returns: html/xml
    
    XPath common usages:
    rst = html.xpath('//div[@class="image-caption"]/text()')  # Get the text content of the specified tag
    rst = html.xpath('//div[@class="image-caption"]/text()')  # Get the text content of the specified tag
    rst1 = html.xpath('//div[@class="_16zCst"]/h1/text()')
    rst2 = html.xpath('//p[1]/text()')  # Get the text content of the first p node
    rst3 = html.xpath('//p[position()<3]/text()')  # Get the text content of the first two p nodes
    rst4 = html.xpath('//p[last()]/text()')  # Get the text content of the last p node
    rst5 = html.xpath('//a[2]/@href')  # Get the href attribute of the second a node
    
    """
    if file_path.endswith(".mhtml"):
        import pimht
        mhtml = pimht.from_filename(file_path)
        longest_length = 0
        html_content = ""
        for mhtml_part in mhtml:
            if "text/html" in mhtml_part.content_type:
                possible_html=mhtml_part.text
                current_length = len(possible_html)
                if current_length > longest_length:
                    longest_length = current_length
                    html_content = possible_html
        # Parse the HTML content
        html = etree.HTML(html_content)
        return html
    elif file_path.endswith(".html"): #.html
        html=etree.parse(file_path,etree.HTMLParser())
        return html
    elif file_path.endswith(".xml"):
        xml=etree.parse(file_path, etree.XMLParser())   
        return xml
    else:
        print("Only supports mhtml, html, and xml file format!")

def get_data_html_online(url, html=True, timeout=None, headers=None, cookies=None, params=None, proxies=None):
    '''
    rst = html.xpath('//div[@class="image-caption"]/text()')  # Get the text content of the specified tag
    rst = html.xpath('//div[@class="image-caption"]/text()')  # Get the text content of the specified tag
    rst1 = html.xpath('//div[@class="_16zCst"]/h1/text()')
    rst2 = html.xpath('//p[1]/text()')  # Get the text content of the first p node
    rst3 = html.xpath('//p[position()<3]/text()')  # Get the text content of the first two p nodes
    rst4 = html.xpath('//p[last()]/text()')  # Get the text content of the last p node
    rst5 = html.xpath('//a[2]/@href')  # Get the href attribute of the second a node
    '''
    # Example HTML content
    if timeout is None:
        real_timeout=24.0
    else:
        real_timeout=timeout    
    try:
        time.sleep(round(random.uniform(1.0, 3.9), 19)) 
        r=requests.get(url, timeout=real_timeout, headers=headers, cookies=cookies, params=params, proxies=proxies)
        print(r.status_code) # print the reponse status code
        if r.status_code==200:
            if html==False:
                return r
            else:
                r.encoding="utf-8"
                data=r.text
                html=etree.HTML(data)
                return html, data
        else:
            print(r.status_code, "Can not find the page!")
            return None
    except Exception as err:
        print(err)

def find_table_with_most_rows(tables): 
    max_rows=0
    max_table_index=-1
    for i, table in enumerate(tables):
        if isinstance(table, pd.DataFrame) and len(str(table.shape[0])) > max_rows:
            max_rows=len(str(table.shape[0]))
            max_table_index=i
    return max_table_index, max_rows if max_table_index!= -1 else None

def get_data_table_url(url, output_file, most_rows=True):
    try:
        # Wrap the HTML string in a StringIO object
        tables=pd.read_html(url)
        if most_rows==False:
            # 1. default: the first table
            df=tables[0]  
        else:
            # 2. get the table with most rows
            target_table=find_table_with_most_rows(tables)[0] #  (1, 32)
            df=tables[target_table]        
        
        df.to_excel(output_file, index=False)
        print(f"Data has been saved to {output_file}")
    except Exception as err:
        print(f"Errors found! {err}")
        return None

def get_data_table_html_string(html_string, output_file, most_rows=True):
    try:
        # Wrap the HTML string in a StringIO object
        from io import StringIO
        html_io = StringIO(html_string)
        tables=pd.read_html(html_io)
        if most_rows==False:
            # 1. default: the first table
            df=tables[0]  
        else:
            # 2. get the table with most rows
            target_table=find_table_with_most_rows(tables)[1] #  (1, 32)
            df=tables[target_table]        
        
        df.to_excel(output_file, index=False)
        print(f"Data has been saved to {output_file}")
    except Exception as err:
        print(f"Errors found! {err}")
        return None

import importlib.metadata
def get_library_location(library_name):
    distribution = importlib.metadata.distribution(library_name)
    return str(distribution.locate_file(''))

def get_stopwords(language=None):
    '''
    Parameters
    ----------
    language : TYPE, string: like 'english', 'chinese', etc.
        DESCRIPTION. The default is None.

    Returns
    -------
    TYPE, list: like ["'ll", "'tis", "'twas", "'ve", '10', '39', 'a', "a's", 'able', 'ableabout', 'about', 'above', 'abroad', 'abst']
        DESCRIPTION. The default will return a list of English stopwords.

    '''
    stopwords_path=get_library_location("PgsFile")+"/PgsFile/Corpora/Stopwords"
    if language is None:
        en_stopwords=get_data_lines(find_txt_files_with_keyword(stopwords_path, "english")[0])
        return en_stopwords
    else:
        lang_stopwords=get_data_lines(find_txt_files_with_keyword(stopwords_path, language)[0])
        return lang_stopwords    

from PIL import Image
def replace_white_with_transparency(input_path, output_path):
    """
    This function opens an image, replaces all white pixels with transparent pixels.

    Parameters:
    input_path (str): The path to the input image file.
    output_path (str): The path to save the output image file.
    """
    # 从RGB（24位）模式转成RGBA（32位）模式
    img = Image.open(input_path).convert('RGBA')
    W, L = img.size
    white_pixel = (0, 0, 0, 0)  # white
    for h in range(W):
      for i in range(L):
        if img.getpixel((h, i)) == white_pixel:
          img.putpixel((h, i), (255, 255, 255, 0))   # make it transparent
    img.save(output_path)

def get_font_path(font_name=None):
    '''
    Retrieves the file path of a specified font.

    Parameters
    ----------
    font_name : str, optional
        The name of the font file (must end with ".ttf"). If provided, it should match one of the available fonts in the library, such as:
        - 'DejaVuSans.ttf'
        - '书体坊赵九江钢笔行书体.ttf'
        - '全新硬笔楷书简.ttf'
        - '全新硬笔行书简.ttf'
        - '博洋行书3500.TTF'
        - '陆柬之行书字体.ttf'
        The default is None, which will return the path for 'DejaVuSans.ttf'.

    Returns
    -------
    font_path : str
        The full file path of the specified font. If no font name is provided, the default path for 'DejaVuSans.ttf' will be returned.
        Example: "C:/Windows/Fonts/simhei.ttf"
    '''
    
    font_folder = get_library_location("PgsFile") + "/PgsFile/models/fonts"
    if font_name is None:
        font_path = get_full_path(font_folder, "DejaVuSans.ttf")
    else:
        font_path = get_full_path(font_folder, font_name)
    return font_path

simhei_default_font_path_MacOS_Windows=["/System/Library/Fonts/STHeiti Medium.ttc",
                   r"C:\Windows\Fonts\simhei.ttf",  # Use a font that supports Chinese characters
                   ]


def get_env_variable(variable_name):
    # Get the value of the specified environment variable
    value = os.getenv(variable_name)
    return value

def get_all_env_variables():
    # Get all environment variables
    env_vars = os.environ
    
    # Print all user environment variables
    return dict(env_vars)

import subprocess
def set_permanent_environment_variable(variable_name, variable_value, system_wide=False):
    """
    Sets a permanent environment variable on Windows using the `setx` command.

    Args:
        variable_name (str): The name of the environment variable.
        variable_value (str): The value to set for the environment variable.
        system_wide (bool): If True, sets the variable system-wide (requires admin privileges).
                            If False, sets the variable for the current user only.
    """
    try:
        # Construct the setx command
        command = ['setx', variable_name, variable_value]
        if system_wide:
            command.append('/M')  # Add /M flag for system-wide variables

        # Run the command
        subprocess.run(command, shell=True, check=True)

        print(f'Permanent environment variable {variable_name} set to {variable_value} '
              f'({"system-wide" if system_wide else "user-level"}).')
    except subprocess.CalledProcessError as e:
        print(f'Failed to set environment variable: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

def delete_permanent_environment_variable(variable_name, system_wide=False):
    """
    Deletes a permanent environment variable on Windows using the `reg` command.

    Args:
        variable_name (str): The name of the environment variable to delete.
        system_wide (bool): If True, deletes the variable system-wide (requires admin privileges).
                            If False, deletes the variable for the current user only.
    """
    try:
        # Determine the registry key based on the scope
        if system_wide:
            reg_key = r'HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
        else:
            reg_key = r'HKCU\Environment'

        # Run the `reg delete` command to remove the variable
        subprocess.run(
            ['reg', 'delete', reg_key, '/v', variable_name, '/f'],
            shell=True,
            check=True
        )

        print(f'Permanent environment variable {variable_name} deleted '
              f'({"system-wide" if system_wide else "user-level"}).')
    except subprocess.CalledProcessError as e:
        print(f'Failed to delete environment variable: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')


def calculate_mean_dependency_distance(spacy_doc):
    """
    Calculate the mean dependency distance for tokens in a spaCy Doc object.

    The dependency distance is the absolute difference in positions between a token
    and its syntactic head. This function computes the average of these distances
    for all tokens in the Doc object, excluding punctuation and the root token.

    Parameters:
    spacy_doc (spacy.tokens.Doc): The spaCy Doc object to analyze.

    Returns:
    float: The mean dependency distance. Returns 0 if there are no valid tokens to analyze.
    """
    
    doc=spacy_doc
    total_distance = 0
    count = 0

    for token in doc:
        if token.dep_ not in ("punct", "ROOT"):
            distance = abs(list(doc).index(token.head) - list(doc).index(token))
            total_distance += distance
            count += 1

    if count == 0:
        return 0

    mean_distance = total_distance / count
    return mean_distance

def word_lemmatize(spacy_doc):
    """
    Lemmatize the words in a spaCy Doc object and return the lemmatized text.

    This function processes each token in the Doc object, replacing it with its lemma
    unless the lemma is '-PRON-', in which case the original text of the token is used.
    The resulting lemmatized words are joined into a single string.

    Parameters:
    spacy_doc (spacy.tokens.Doc): The spaCy Doc object to lemmatize.

    Returns:
    str: The lemmatized text as a single string.
    """
    doc = spacy_doc
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in doc])
    return text

def word_NER(spacy_doc):
    """
    Extract Named Entities from a spaCy Doc object.

    This function processes the Doc object to identify and extract named entities,
    returning a list of tuples where each tuple contains the entity text and its label.

    Parameters:
    spacy_doc (spacy.tokens.Doc): The spaCy Doc object to analyze.

    Returns:
    list of tuples: A list of tuples where each tuple contains the entity text and its label.
    """
    doc = spacy_doc
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def word_POS(spacy_doc):
    """
    Extract Part-Of-Speech (POS) tags from a spaCy Doc object.

    This function processes the Doc object to identify and extract the POS tags for each token,
    returning a list of tuples where each tuple contains the token text and its corresponding POS tag.

    Parameters:
    spacy_doc (spacy.tokens.Doc): The spaCy Doc object to analyze.

    Returns:
    list of tuples: A list of tuples where each tuple contains the token text and its POS tag.
    """
    doc = spacy_doc
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags

def extract_noun_phrases(spacy_doc):
    """
    Extract noun phrases from a spaCy Doc object.

    This function processes the Doc object to identify and extract noun phrases,
    returning a list of strings where each string is a noun phrase.

    Parameters:
    spacy_doc (spacy.tokens.Doc): The spaCy Doc object to analyze.

    Returns:
    list of str: A list of noun phrases extracted from the Doc object.
    """
    doc = spacy_doc
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    return noun_phrases

def extract_dependency_relations(spacy_doc):
    """
    Extract the dependency relations for each word in a spaCy Doc object.

    This function processes the Doc object to identify and extract the dependency relations
    for each token, returning a list of tuples where each tuple contains the token text,
    its dependency relation, and the text of its syntactic head.

    Parameters:
    spacy_doc (spacy.tokens.Doc): The spaCy Doc object to analyze.

    Returns:
    list of tuples: A list of tuples where each tuple contains the token text,
                    its dependency relation, and the text of its syntactic head.
    """
    doc = spacy_doc
    dependency_relations = [(token.text, token.dep_, token.head.text) for token in doc]
    return dependency_relations

def extract_dependency_relations_full(spacy_doc):
    """
    Extract comprehensive dependency relations for each word in a spaCy Doc object.

    This function processes the Doc object to identify and extract detailed dependency relations
    for each token. It returns a list of tuples where each tuple contains the token text,
    its lemmatized form, its part-of-speech (POS) tag, its dependency relation, the text of its
    syntactic head, and a list of its child tokens.

    Parameters:
    spacy_doc (spacy.tokens.Doc): The spaCy Doc object to analyze.

    Returns:
    list of tuples: A list of tuples where each tuple contains:
                    - The token text
                    - The lemmatized form of the token
                    - The POS tag of the token
                    - The dependency relation of the token
                    - The text of the token's syntactic head
                    - A list of the text of the token's child tokens
    """
    doc = spacy_doc
    dependency_relations = [(token.text, token.lemma_, token.pos_, token.dep_, token.head.text, [child.text for child in token.children]) for token in doc]
    return dependency_relations

usua_tag_set = {
    "A": "General & Abstract Terms",
    "B": "The Body & the Individual",
    "C": "Arts & Crafts",
    "E": "Emotional Actions, States & Processes",
    "F": "Food & Farming",
    "G": "Government & the Public Domain",
    "H": "Architecture, Building, Houses & the Home",
    "I": "Money & Commerce",
    "K": "Entertainment, Sports & Games",
    "L": "Life & Living Things",
    "M": "Movement, Location, Travel & Transport",
    "N": "Numbers & Measurement",
    "O": "Substances, Materials, Objects & Equipment",
    "P": "Education",
    "Q": "Linguistic Actions, States & Processes",
    "S": "Social Actions, States & Processes",
    "T": "Time",
    "W": "The World & Our Environment",
    "X": "Psychological Actions, States & Processes",
    "Y": "Science & Technology",
    "Z": "Names & Grammatical Words"
}


def get_CET_dics(name=None):
    '''
    Parameters
    ----------
    name : TYPE, string: like 'CET-4', 'CET-6', etc.
        DESCRIPTION. The default is None.

    Returns
    -------
    TYPE, list: like ['a', 'an', 'abandon', 'able', 'ability', 'aboard', 'abolish', 'abolition', 'about', 'above', 'abroad', 'absent', 'absence', 'absolute', 'absorb']
        DESCRIPTION. The default will return a list of English CET (China's College English Test band 4 & 6) words.
    '''
    
    dic_path=get_library_location("PgsFile")+"/PgsFile/models/dics"
    if name is None:
        cet_words=get_data_lines(find_txt_files_with_keyword(dic_path, "cet-4")[0])
        return cet_words
    else:
        cet_words=get_data_lines(find_txt_files_with_keyword(dic_path, name)[0])
        return cet_words   

def get_BNC_dic():
    '''
    Returns
    -------
    TYPE, pandas dataframe: 
              List   ... Total frequency
        0        1k  ...         2525253
        1        1k  ...           47760
        2        1k  ...          192168
        3        1k  ...           25370
        4        1k  ...            9284
            ...  ...             ...
        24997   25k  ...               0
        24998   25k  ...               0
        24999   25k  ...               9
        25000   25k  ...               4
        25001   25k  ...               9
        
        [25002 rows x 4 columns]        
        DESCRIPTION. The default will return a dataframe of the most commonly used English word list based on the BNC-COCA corpus.
    '''
    import pandas as pd
    inter=get_library_location("PgsFile")+"/PgsFile/models/dics"
    dic_path=get_full_path(inter, "BNC_COCA_lists.xlsx")
    print(dic_path)
    df=pd.read_excel(dic_path)
    return df
    
def get_LLMs_prompt(task=None):
    '''
    Parameters
    ----------
    task : TYPE, string: like 'MIP', 'WSD', etc.
        DESCRIPTION. The default is None.

    Returns
    -------
    TYPE, string: like LLM Prompt for Metaphor Analysis Task:
        Identify all metaphorical expressions in the provided text using MIP (Metaphor Identification Procedure).
        Categorize each metaphor into one of the following CDA sub-types (with brief justification).
        DESCRIPTION. The default will return a text promt for specific LLM task.
    '''
    
    dic_path=get_library_location("PgsFile")+"/PgsFile/models/prompts"
    if task is None:
        user_prompt=get_data_text(find_txt_files_with_keyword(dic_path, "mip")[0])
        return user_prompt
    else:
        user_prompt=get_data_text(find_txt_files_with_keyword(dic_path, task)[0])
        return user_prompt   
    
def predict_category(model, new_title, description=""):
    """
    Predict the news category for a new title (and optional description).
    # Load the trained model
    model_path = "PGS_news_classifier.bin"
    
    Args:
        model = fasttext.load_model(model_path)
        new_title (str): New news headline to classify
        description (str): Optional short description to include with the title
    Returns:
        tuple: (predicted_label, confidence_score)
    """
    text = f"{new_title} {description}".strip()
    labels, scores = model.predict(text, k=1)  # k=1 returns only the top prediction
    predicted_label = labels[0].replace('__label__', '')
    confidence_score = scores[0]
    return predicted_label, confidence_score   

import platform
import sys

def get_system_info():
    """
    Determine the computer's system architecture and operating system type.

    Returns:
        dict: A dictionary containing:
            - 'os_type': The general OS type (e.g., 'Windows', 'Linux', 'macOS').
            - 'os_name': The detailed OS name (e.g., 'Windows 10', 'Ubuntu').
            - 'os_version': The OS version (e.g., '10.0.19041').
            - 'architecture': The system architecture (e.g., '64bit', '32bit').
            - 'processor': The processor type (e.g., 'x86_64', 'ARM64').
    """
    system_info = {
        'os_type': None,
        'os_name': None,
        'os_version': None,
        'architecture': None,
        'processor': None
    }

    # Get OS type (Windows/Linux/macOS)
    os_type = platform.system()
    system_info['os_type'] = os_type

    # Get detailed OS name and version
    if os_type == "Windows":
        system_info['os_name'] = platform.win32_ver()[0]
        system_info['os_version'] = platform.win32_ver()[1]
    elif os_type == "Linux":
        system_info['os_name'] = ' '.join(platform.linux_distribution()[:2])
        system_info['os_version'] = platform.release()
    elif os_type == "Darwin":
        system_info['os_name'] = 'macOS'
        system_info['os_version'] = platform.mac_ver()[0]

    # Get architecture (32bit/64bit)
    is_64bit = sys.maxsize > 2**32
    system_info['architecture'] = '64bit' if is_64bit else '32bit'

    # Get processor information
    system_info['processor'] = platform.machine()

    return system_info


import time
from functools import wraps

def timeit(func):
    """Decorator to measure execution time of a function or script."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        if elapsed_time > 60:
            # Convert elapsed time to days, hours, minutes, and seconds
            days = int(elapsed_time // (24 * 3600))
            hours = int((elapsed_time % (24 * 3600)) // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = elapsed_time % 60

            # Format the time string according to the rules
            parts = []
            if days > 0:
                parts.append(f"{days} days")
            if days > 0 or hours > 0:
                parts.append(f"{hours:02}:{minutes:02}:{seconds:06.4f}")
            elif minutes > 0:
                parts.append(f"{minutes:02}:{seconds:06.4f}")
            else:
                parts.append(f"{seconds:06.4f} seconds")

            time_str = ", ".join(parts)
        else:
            time_str = f"{elapsed_time:.4f} seconds"

        print(f"'{func.__name__}' executed in {time_str}")
        return result
    return wrapper

def file_to_list_of_dicts(input_path, output_path):
    """
    Convert a CSV or XLSX file into a JSON file, where each line in the JSON file is a dictionary representing a row from the input file.
    The keys of each dictionary are formatted as "column1, column2, column3, etc."

    Args:
        input_path (str): Path to the CSV or XLSX file.
        output_path (str): Path to the output JSON file.

    Returns:
        None: The function writes the dictionaries to a JSON file specified by output_path.
    """
    # Determine the file type based on the file extension
    import pandas as pd
    if input_path.endswith('.csv'):
        df = pd.read_csv(input_path)
    elif input_path.endswith('.xlsx'):
        df = pd.read_excel(input_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or XLSX file.")

    # Use default keys "col1, col2, etc."
    total = len(list(df.iterrows()))
    for index, row in df.iterrows():
        row_dict = {f"col{i+1}": value for i, value in enumerate(row)}
        append_dict_to_json(output_path, row_dict)
        print(f'Converting {decimal_to_percent(index/total)}')

    print("Conversion complete!")
    

import liwc
import json
def perform_liwc_en(dic_path, file_path, output_excel_path):
    '''
    Parameters
    ----------
    dic_path : str
        Path to the LIWC dictionary file.
    file_path : str
        Path to the raw text file.
    output_excel_path : str
        Path to the output Excel file.
    '''
    parse, category_names = liwc.load_token_parser(dic_path)
    test = get_data_text(file_path)
    test_tokens = [w.lower() for w in word_tokenize2(test)]
    my_word_list = dict(word_list(test_tokens))
    corpus_scale = sum(my_word_list.values())

    labels = {'function': '1', 'pronoun': '2', 'ppron': '3', 'i': '4', 'we': '5', 'you': '6', 'shehe': '7', 'they': '8', 'ipron': '9', 'article': '10', 'prep': '11', 'auxverb': '12', 'adverb': '13', 'conj': '14', 'negate': '15', 'verb': '20', 'adj': '21', 'compare': '22', 'interrog': '23', 'number': '24', 'quant': '25', 'affect': '30', 'posemo': '31', 'negemo': '32', 'anx': '33', 'anger': '34', 'sad': '35', 'social': '40', 'family': '41', 'friend': '42', 'female': '43', 'male': '44', 'cogproc': '50', 'insight': '51', 'cause': '52', 'discrep': '53', 'tentat': '54', 'certain': '55', 'differ': '56', 'percept': '60', 'see': '61', 'hear': '62', 'feel': '63', 'bio': '70', 'body': '71', 'health': '72', 'sexual': '73', 'ingest': '74', 'drives': '80', 'affiliation': '81', 'achiev': '82', 'power': '83', 'reward': '84', 'risk': '85', 'focuspast': '90', 'focuspresent': '91', 'focusfuture': '92', 'relativ': '100', 'motion': '101', 'space': '102', 'time': '103', 'work': '110', 'leisure': '111', 'home': '112', 'money': '113', 'relig': '114', 'death': '115', 'informal': '120', 'swear': '121', 'netspeak': '122', 'assent': '123', 'nonflu': '124', 'filler': '125', 'punctuation':'126'}

    # 第一列：类别标签
    # 第二列：某类别出现的词种数
    # 第三列：某类别出现的词次数
    # 第四列：考察文本语料库的总词次数
    # 第五列：覆盖率
    # 第六列：例词，包含某个词的频次降序排列
    
    def get_category_info(x):
        category_words = []
        category_words_freq = 0
        for w in my_word_list:
            categories = parse(w)
            if x in categories:
                category_words.append([w, my_word_list[w]])
                category_words_freq += my_word_list[w]

        final = sorted(category_words, key=lambda x: x[1], reverse=True)
        json_string = json.dumps(final)
        return [len(category_words), category_words_freq, corpus_scale, decimal_to_percent(category_words_freq / corpus_scale), json_string]

    data = []
    labels_list = list(labels.keys())
    for i in labels_list:
        rs = get_category_info(i)
        data.append([i] + rs)

    import pandas as pd
    df = pd.DataFrame(data, columns=[u'类别', u'出现词种数', u'出现词次', u'总词次', u'覆盖率', u'例词'])
    df.to_excel(output_excel_path, 'sheet1', index=False)


def perform_liwc_zh(dic_path, file_path, output_excel_path):
    '''
    Parameters
    ----------
    dic_path : str
        Path to the LIWC dictionary json file.
    file_path : str
        Path to the raw text file.
    output_excel_path : str
        Path to the output Excel file.
    '''        
    
    f=open(dic_path,"r")
    dicx=json.load(f)    
    
    test = get_data_text(file_path)
    test_tokens = word_tokenize(test)
    my_word_list=dict(word_list(test_tokens))
    corpus_scale=sum(my_word_list.values())
    
    labels=['Entry:词条','function:功能词','pronoun:代名词','ppron:特定人称代名词','i:第一人称单数代名词','we:第一人称复数代名词','you:第二人称代名词','shehe:第三人称单数代名词','they:第三人称复数代名词','youpl:第二人称复数代名词','ipron:非特定人称代名词','prep:介系词','auxverb:助动词','adverb:副词','conj:连接词','negate:否定词','quanunit:量词','prepend:后置词','specart:特指定词','particle:小品词','modal_pa:语气词','general_pa','compare:比较词','interrog:疑问词','number:数字','quant:概数词','affect:情感历程词','posemo:正向情绪词','negemo:负向情绪词','anx:焦虑词','anger:生气词','sad:悲伤词','social:社会历程词','family:家族词','friend:朋友词','female:女性词','male:男性词','cogproc','insight:洞察词','cause:因果词','discrep:差距词','tentat:暂定词','certain:确切词','differ','percept:感知历程词','see:视觉词','hear:听觉词','feel:感觉词','bio:生理历程词','body:身体词','health:健康词','sexual:性词','ingest:摄食词','drives','affiliation','achieve:成就词','power','reward','risk','tensem:时态标定词','focuspast:过去时态标定词','focuspresent:现在时态标定词','focusfuture:未来时态标定词','progm:延续时态标定词','relativ:相对词','motion:移动词','space:空间词','time:时间词','work:工作词','leisure:休闲词','home:家庭词','money:金钱词','relig:宗教词','death:死亡词','informal','swear:脏话','netspeak:网络用语','assent:应和词','nonflu:停顿赘词','filler:填充赘词','punctuation:标点符号']
    # target_index=labels.index("swear") #75
    
    def get_category_info(x):
        category_words=[]
        category_words_indicx=[]
        category_words_freq=0
        for w in dicx:
            if dicx[w][x]=="1":
                category_words_indicx.append(w)
                if w in my_word_list:
                    category_words_freq+=my_word_list[w]
                    category_words.append([w,my_word_list[w]])
        final=sorted(category_words,key=lambda x: x[1],reverse=True)
        json_string = json.dumps(final, ensure_ascii=False)
        return [len(category_words),decimal_to_percent(len(category_words)/len(category_words_indicx)),category_words_freq,corpus_scale, decimal_to_percent(category_words_freq/corpus_scale), json_string]
    
    data=[]
    for i in labels[1::]:
        rs=get_category_info(labels[1::].index(i)) 
        data.append([i]+rs)
    
    
    import pandas as pd
    df = pd.DataFrame(data,columns=[u'类别', u'出现词种数', u'占词表百分比', u'出现词次', u'总词次', u'覆盖率', u'例词'])
    df.to_excel(output_excel_path,'sheet1',index=False)
    
    
import math
from collections import defaultdict
def calculate_log_likelihood(target_count, reference_count, total_target, total_reference):
    """Calculate the log-likelihood of a word being a keyword using absolute frequencies."""
    # Calculate expected frequencies
    total_combined = total_target + total_reference
    expected_target = (target_count + reference_count) * (total_target / total_combined)
    expected_reference = (target_count + reference_count) * (total_reference / total_combined)

    # Calculate log-likelihood
    ll = 0.0
    if target_count > 0:
        ll += target_count * math.log(target_count / expected_target)
    if reference_count > 0:
        ll += reference_count * math.log(reference_count / expected_reference)

    return ll * 2  # Return G^2 statistic

def extract_keywords_en(target_text, top_n=10):
    """Extract keywords from target text using log-likelihood with absolute reference frequencies."""
    # Example usage
    my_dic_path = get_library_location("PgsFile")+"/PgsFile/models/dics/unigram_freq_only.json" # BNC_wordlist
    reference_freq = get_data_json(my_dic_path)
    # Tokenize target text and preserve original case
    original_words = word_tokenize2(target_text)
    lower_words = [w.lower() for w in original_words if w.lower() not in BigPunctuation and w.lower() not in get_stopwords()]
    total_target = len(lower_words)

    # Calculate target word frequencies
    target_word_freq = defaultdict(int)
    word_case_mapping = {}
    for orig_word, lower_word in zip(original_words, [w.lower() for w in original_words]):
        if lower_word in lower_words:
            target_word_freq[lower_word] += 1
            if lower_word not in word_case_mapping:
                word_case_mapping[lower_word] = orig_word

    # Calculate total reference frequency
    total_reference = sum(reference_freq.values())

    # Calculate log-likelihood for each word
    keyword_scores = []
    for word, target_count in target_word_freq.items():
        reference_count = reference_freq.get(word, 0)
        ll = calculate_log_likelihood(target_count, reference_count, total_target, total_reference)
        relative_freq = target_count / total_target
        original_word = word_case_mapping.get(word, word)
        keyword_scores.append((original_word, target_count, relative_freq, ll))

    # Sort keywords by log-likelihood score
    keyword_scores.sort(key=lambda x: x[3], reverse=True)

    # Return top N keywords
    return keyword_scores[:top_n]

def extract_keywords_en_be21(target_text, top_n=10):
    """Extract keywords from target text using log-likelihood with absolute reference frequencies."""
    # Example usage
    my_dic_path = get_library_location("PgsFile")+"/PgsFile/models/dics/BE21.json" # BE21_wordlist
    reference_freq = get_data_json(my_dic_path)
    # Tokenize target text and preserve original case
    original_words = word_tokenize2(target_text)
    lower_words = [w.lower() for w in original_words if w.lower() not in BigPunctuation and w.lower() not in get_stopwords()]
    total_target = len(lower_words)

    # Calculate target word frequencies
    target_word_freq = defaultdict(int)
    word_case_mapping = {}
    for orig_word, lower_word in zip(original_words, [w.lower() for w in original_words]):
        if lower_word in lower_words:
            target_word_freq[lower_word] += 1
            if lower_word not in word_case_mapping:
                word_case_mapping[lower_word] = orig_word

    # Calculate total reference frequency
    total_reference = sum(reference_freq.values())

    # Calculate log-likelihood for each word
    keyword_scores = []
    for word, target_count in target_word_freq.items():
        reference_count = reference_freq.get(word, 0)
        ll = calculate_log_likelihood(target_count, reference_count, total_target, total_reference)
        relative_freq = target_count / total_target
        original_word = word_case_mapping.get(word, word)
        keyword_scores.append((original_word, target_count, relative_freq, ll))

    # Sort keywords by log-likelihood score
    keyword_scores.sort(key=lambda x: x[3], reverse=True)

    # Return top N keywords
    return keyword_scores[:top_n]

def resize_image(input_image_path, output_image_path, max_size_kb):
    '''
    # Example 1: Resizing a JPG image
    input_image_path_jpg = 'example_input.jpg'
    output_image_path_jpg = 'example_output_resized.jpg'
    resize_image(input_image_path_jpg, output_image_path_jpg, max_size_kb=2048)

    # Example 2: Resizing a PNG image
    input_image_path_png = 'example_input.png'
    output_image_path_png = 'example_output_resized.png'
    resize_image(input_image_path_png, output_image_path_png, max_size_kb=2048)
    '''
    # Open the image file
    with Image.open(input_image_path) as img:
        # Function to save the image and check its size
        def save_image(img, output_path, quality=95):
            if output_path.lower().endswith('.jpg'):
                img.save(output_path, 'JPEG', quality=quality)
            else:
                img.save(output_path, 'PNG', optimize=True)

        # Initial save to check the size
        save_image(img, output_image_path)

        # Check the size and reduce quality/dimensions if necessary
        size = os.path.getsize(output_image_path) // 1024  # Size in KB

        # Reduce quality for JPG or optimize PNG
        quality = 95
        while size > max_size_kb:
            # Reduce dimensions
            width, height = img.size
            img = img.resize((int(width * 0.9), int(height * 0.9)), Image.LANCZOS)

            # Save the image
            save_image(img, output_image_path, quality)
            size = os.path.getsize(output_image_path) // 1024

            # Reduce quality for JPG
            if output_image_path.lower().endswith('.jpg'):
                quality -= 5
                if quality < 10:  # Prevent quality from going too low
                    break

        if size <= max_size_kb:
            print(f"Image resized successfully to {size} KB.")
        else:
            print("Could not reduce the image size below 2MB.")

import base64
def convert_image_to_url(image_path: str) -> str:
    """
    Convert an image file to a base64 encoded URL format.

    :param image_path: Path to the image file.
    :return: A string representing the image in the required URL format.
    """
    # Check if the file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"The file {image_path} does not exist.")

    # Open and read the image file in binary mode
    with open(image_path, "rb") as f:
        image_data = f.read()

    # Extract the file extension and convert it to base64
    file_extension = os.path.splitext(image_path)[1][1:]
    base64_image_data = base64.b64encode(image_data).decode('utf-8')

    # Create the image URL
    image_url = f"data:image/{file_extension};base64,{base64_image_data}"

    return image_url

import ast
def markdown_to_python_object(data):
    """
    If `data` is already a Python object (list, dict, tuple, str, etc.), return it.
    If it's a Markdown code block, try to parse it into the equivalent Python object.
    """
    # If already a Python object (but not a string), return as is
    if not isinstance(data, str):
        return data

    # Match Markdown code block (with or without `python`)
    code_block = re.search(r"```(?:python)?\s*(.*?)\s*```", data, re.DOTALL)
    if not code_block:
        # If there's no triple backticks, try parsing the string directly
        try:
            return ast.literal_eval(data)
        except Exception:
            return data.strip()
    
    code_str = code_block.group(1)

    # Try safe parsing
    try:
        return ast.literal_eval(code_str)
    except Exception:
        return code_str.strip()


import math
from collections import defaultdict, Counter

def tfidf_keyword_extraction(documents, top_percent=(0.0, 0.10)):
    """
    Extract keywords from a small set of tokenized documents using TF-IDF.

    Parameters
    ----------
    documents : list of list of str
        Corpus represented as tokenized documents.
    top_percent : tuple of float
        Range of percentage (low, high) to select top keyword candidates.

    Returns
    -------
    full_list : list of tuple
        All (term, tf-idf_score) sorted by score in descending order.
    candidates : list of tuple
        Keyword candidates from top_10% range.
    """
    log = math.log  # local reference for speed

    # Step 1: Compute IDF
    total_docs = len(documents)
    doc_freq = defaultdict(int)
    for doc in documents:
        for term in set(doc):
            doc_freq[term] += 1
    idf = {term: log((total_docs + 1) / (df + 1)) + 1 for term, df in doc_freq.items()}

    # Step 2: Compute TF-IDF
    tfidf_scores = {}
    for doc in documents:
        total_terms = len(doc)
        term_counts = Counter(doc)
        for term, count in term_counts.items():
            tfidf_scores[term] = (count / total_terms) * idf[term]  # overwrite as before

    # Step 3: Sort full list
    full_list = sorted(tfidf_scores.items(), key=lambda x: x[1], reverse=True)

    # Step 4: Extract candidates based on percentage range
    n_terms = len(full_list)
    low_cut = int(n_terms * top_percent[0])
    high_cut = int(n_terms * top_percent[1])
    candidates = full_list[low_cut:high_cut]  # slice range

    return full_list, candidates


from xml.dom.minidom import Document
from datetime import datetime
def maketmx(
    tmx_path,
    source_list,
    target_list,
    source_lang="zh-CN",
    target_lang="en-US",
    author="Petercusin",
    client_name=None,
    project_id=None,
    domain=None,
    status="Final"
):
    """
    Generate a TMX (Translation Memory eXchange) file for any two language pairs, with optional metadata.

    Parameters
    ----------
    tmx_path : str
        Path to save the TMX file, e.g., "translation_memory.tmx".
    source_list : list of str
        List of source language segments, e.g., ["你好", "再见"].
    target_list : list of str
        List of target language segments, e.g., ["Hello", "Goodbye"].
        **Must have the same number of elements as `source_list`.**
    source_lang : str, optional
        Source language code, e.g., "zh-CN" (default), "fr-FR", "de-DE".
    target_lang : str, optional
        Target language code, e.g., "en-US" (default), "es-ES", "ja-JP".
    author : str, optional
        Author of the TMX file, e.g., "Petercusin" (default).
    client_name : str, optional
        Name of the client or company, e.g., "Acme Corp".
    project_id : str, optional
        Project identifier, e.g., "Project_XYZ_2025".
    domain : str, optional
        Domain or subject field, e.g., "Medical", "Legal", "Technical".
    status : str, optional
        Translation status, e.g., "Draft", "Reviewed", "Final" (default).

    Returns
    -------
    None
        Writes the TMX file to the specified path.

    Raises
    ------
    ValueError
        If `source_list` and `target_list` have different lengths.

    Example
    -------
    # Chinese to English, with metadata
    maketmx(
        "zh_en.tmx",
        ["你好", "再见"],
        ["Hello", "Goodbye"],
        "zh-CN",
        "en-US",
        author="Dr. Guisheng PAN",
        client_name="Acme Corp",
        project_id="Project_XYZ_2025",
        domain="Technical",
        status="Final"
    )
    """
    if len(source_list) != len(target_list):
        raise ValueError("source_list and target_list must have the same number of elements.")

    doc = Document()
    tmx = doc.createElement("tmx")
    tmx.setAttribute("version", "1.4")
    doc.appendChild(tmx)

    header = doc.createElement("header")
    header.setAttribute("creationtool", "PgsFile")
    header.setAttribute("creationtoolversion", "0.5.1")
    header.setAttribute("creationtooldeveloper", author)
    header.setAttribute("creationdate", datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"))
    header.setAttribute("srclang", source_lang)
    header.setAttribute("trtlang", target_lang)
    header.setAttribute("datatype", "plaintext")
    header.setAttribute("segtype", "sentence")
    header.setAttribute("adminlang", "en-US")
    header.setAttribute("o-tmf", "PgsFile_TM")
    tmx.appendChild(header)

    # Add optional metadata as <prop> elements
    if client_name:
        prop = doc.createElement("prop")
        prop.setAttribute("type", "x-Client")
        prop.appendChild(doc.createTextNode(client_name))
        header.appendChild(prop)
    if project_id:
        prop = doc.createElement("prop")
        prop.setAttribute("type", "x-Project")
        prop.appendChild(doc.createTextNode(project_id))
        header.appendChild(prop)
    if domain:
        prop = doc.createElement("prop")
        prop.setAttribute("type", "x-Domain")
        prop.appendChild(doc.createTextNode(domain))
        header.appendChild(prop)
    if status:
        prop = doc.createElement("prop")
        prop.setAttribute("type", "x-Status")
        prop.appendChild(doc.createTextNode(status))
        header.appendChild(prop)

    body = doc.createElement("body")
    tmx.appendChild(body)

    for i in range(len(source_list)):
        tu = doc.createElement("tu")
        body.appendChild(tu)

        # Source language segment
        tuv = doc.createElement("tuv")
        tuv.setAttribute("xml:lang", source_lang)
        tu.appendChild(tuv)
        seg = doc.createElement("seg")
        seg_text = doc.createTextNode(source_list[i])
        seg.appendChild(seg_text)
        tuv.appendChild(seg)

        # Target language segment
        tuv = doc.createElement("tuv")
        tuv.setAttribute("xml:lang", target_lang)
        tu.appendChild(tuv)
        seg = doc.createElement("seg")
        seg_text = doc.createTextNode(target_list[i])
        seg.appendChild(seg_text)
        tuv.appendChild(seg)

    with open(tmx_path, 'w', encoding='utf-8') as f:
        doc.writexml(f, indent='\t', newl='\n', addindent='\t')

