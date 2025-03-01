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
thulac_tags={'n': '名词', 'np': '人名', 'ns': '地名', 'ni': '机构名', 'nz': '其它专名', 'm': '数词', 'q': '量词', 'mq': '数量词', 't': '时间词', 'f': '方位词', 's': '处所词', 'v': '动词', 'a': '形容词', 'd': '副词', 'h': '前接成分', 'k': '后接成分', 'i': '习语', 'j': '简称', 'r': '代词', 'c': '连词', 'p': '介词', 'u': '助词', 'y': '语气助词', 'e': '叹词', 'o': '拟声词', 'g': '语素', 'w': '标点', 'x': '其它'}

LangCodes={'AA': ['阿法尔语', 'Afar'], 'AB': ['阿布哈兹语', 'Abkhaz'], 'AE': ['阿维斯陀语', 'Avestan'], 'AF': ['阿非利堪斯语', 'Afrikaans'], 'AK': ['阿坎语', 'Akan, Twi-Fante'], 'AM': ['阿姆哈拉语', 'Amharic'], 'AN': ['阿拉贡语', 'Aragonese'], 'AR': ['阿拉伯语', 'Arabic'], 'AS': ['阿萨姆语', 'Assamese'], 'AV': ['阿瓦尔语', 'Avaric'], 'AY': ['艾马拉语', 'Aymara'], 'AZ': ['阿塞拜疆语', 'Azerbaijani'], 'BA': ['巴什基尔语', 'Bashkir'], 'BE': ['白俄罗斯语', 'Belarusian'], 'BG': ['保加利亚语', 'Bulgarian'], 'BH': ['比哈尔语', 'Bihari'], 'BI': ['比斯拉玛语', 'Bislama'], 'BM': ['班巴拉语', 'Bambara'], 'BN': ['孟加拉语', 'Bengali'], 'BO': ['藏语', 'Tibetan Standard, Central Tibetan'], 'BR': ['布列塔尼语', 'Breton'], 'BS': ['波斯尼亚语', 'Bosnian'], 'CA': ['加泰隆语', 'Catalan;\xa0Valencian'], 'CE': ['车臣语', 'Chechen'], 'CH': ['查莫罗语', 'Chamorro'], 'CO': ['科西嘉语', 'Corsican'], 'CR': ['克里语', 'Cree'], 'CS': ['捷克语', 'Czech'], 'CU': ['教会斯拉夫语', 'Old Church Slavonic, Church Slavic, Church Slavonic, Old Bulgarian, Old Slavonic'], 'CV': ['楚瓦什语', 'Chuvash'], 'CY': ['威尔士语', 'Welsh'], 'DA': ['丹麦语', 'Danish'], 'DE': ['德语', 'German'], 'DV': ['迪维希语', 'Divehi; Dhivehi; Maldivian;'], 'DZ': ['不丹语', 'Dzongkha'], 'EE': ['埃维语', 'Ewe'], 'EL': ['现代希腊语', 'Greek, Modern'], 'EN': ['英语', 'English'], 'EO': ['世界语', 'Esperanto'], 'ES': ['西班牙语', 'Spanish; Castilian'], 'ET': ['爱沙尼亚语', 'Estonian'], 'EU': ['巴斯克语', 'Basque'], 'FA': ['波斯语', 'Persian'], 'FF': ['富拉语', 'Fula; Fulah; Pulaar; Pular'], 'FI': ['芬兰语', 'Finnish'], 'FJ': ['斐济语', 'Fijian'], 'FO': ['法罗斯语', 'Faroese'], 'FR': ['法语', 'French'], 'FY': ['弗里西亚语', 'Western Frisian'], 'GA': ['爱尔兰语', 'Irish'], 'GD': ['盖尔语（苏格兰语）', 'Scottish Gaelic; Gaelic'], 'GL': ['加利西亚语', 'Galician'], 'GN': ['瓜拉尼语', 'Guaraní'], 'GU': ['古吉拉特语', 'Gujarati'], 'GV': ['马恩岛语', 'Manx'], 'HA': ['豪萨语', 'Hausa'], 'HE': ['希伯来语', 'Hebrew\xa0(modern)'], 'HI': ['印地语', 'Hindi'], 'HO': ['希里莫图语', 'Hiri Motu'], 'HR': ['克罗地亚语', 'Croatian'], 'HT': ['海地克里奥尔语', 'Haitian; Haitian Creole'], 'HU': ['匈牙利语', 'Hungarian'], 'HY': ['亚美尼亚语', 'Armenian'], 'HZ': ['赫雷罗语', 'Herero'], 'I.E.': ['国际语E', 'Interlingue'], 'IA': ['国际语A', 'Interlingua'], 'ID': ['印尼语', 'Indonesian'], 'IG': ['伊博语', 'Igbo'], 'II': ['四川彝语（诺苏语）', 'Nuosu'], 'IK': ['依努庇克语', 'Inupiaq'], 'IO': ['伊多语', 'Ido'], 'IS': ['冰岛语', 'Icelandic'], 'IT': ['意大利语', 'Italian'], 'IU': ['伊努伊特语', 'Inuktitut'], 'JA': ['日语', 'Japanese'], 'JV': ['爪哇语', 'Javanese'], 'KA': ['格鲁吉亚语', 'Georgian'], 'KG': ['刚果语', 'Kongo'], 'KI': ['基库尤语', 'Kikuyu, Gikuyu'], 'KJ': ['夸尼亚玛语', 'Kwanyama, Kuanyama'], 'KK': ['哈萨克语', 'Kazakh'], 'KL': ['格陵兰语', 'Kalaallisut, Greenlandic'], 'KM': ['高棉语', 'Khmer, Cambodian'], 'KN': ['坎纳达语', 'Kannada'], 'KO': ['朝鲜语', 'Korean'], 'KR': ['卡努里语', 'Kanuri'], 'KS': ['克什米尔语', 'Kashmiri'], 'KU': ['库尔德语', 'Kurdish'], 'KV': ['科米语', 'Komi'], 'KW': ['康沃尔语', 'Cornish'], 'KY': ['吉尔吉斯语', 'Kirghiz, Kyrgyz'], 'LA': ['拉丁语', 'Latin'], 'LB': ['卢森堡语', 'Luxembourgish, Letzeburgesch'], 'LG': ['干达语', 'Luganda'], 'LI': ['林堡语', 'Limburgish, Limburgan, Limburger'], 'LN': ['林加拉语', 'Lingala'], 'LO': ['老挝语', 'Lao'], 'LT': ['立陶宛语', 'Lithuanian'], 'LU': ['卢巴—加丹加语', 'Luba-Katanga'], 'LV': ['拉脱维亚语', 'Latvian'], 'MG': ['马达加斯加语', 'Malagasy'], 'MH': ['马绍尔语', 'Marshallese'], 'MI': ['毛利语', 'Māori'], 'MK': ['马其顿语', 'Macedonian'], 'ML': ['马拉亚拉姆语', 'Malayalam'], 'MN': ['蒙古语', 'Mongolian'], 'MR': ['马拉提语', 'Marathi (Marāṭhī)'], 'MS': ['马来语', 'Malay'], 'MT': ['马耳他语', 'Maltese'], 'MY': ['缅甸语', 'Burmese'], 'NA': ['瑙鲁语', 'Nauru'], 'NB': ['挪威布克摩尔语', 'Norwegian Bokmål'], 'ND': ['北恩德贝勒语', 'North Ndebele'], 'NE': ['尼泊尔语', 'Nepali'], 'NG': ['恩敦加语', 'Ndonga'], 'NL': ['荷兰语', 'Dutch'], 'NN': ['尼诺斯克挪威语', 'Norwegian Nynorsk'], 'NO': ['挪威语', 'Norwegian'], 'NR': ['南恩德贝勒语', 'South Ndebele'], 'NV': ['纳瓦霍语', 'Navajo, Navaho'], 'NY': ['尼扬贾语', 'Chichewa; Chewa; Nyanja'], 'OC': ['普罗旺斯语', 'Occitan'], 'OJ': ['奥吉布瓦语', 'Ojibwe, Ojibwa'], 'OM': ['阿芳•奥洛莫语', 'Oromo'], 'OR': ['奥利亚语', 'Oriya'], 'OS': ['奥塞梯语', 'Ossetian, Ossetic'], 'PA': ['旁遮普语', 'Panjabi, Punjabi'], 'PI': ['巴利语', 'Pāli'], 'PL': ['波兰语', 'Polish'], 'PS': ['普什图语', 'Pashto, Pushto'], 'PT': ['葡萄牙语', 'Portuguese'], 'QU': ['凯楚亚语', 'Quechua'], 'RM': ['罗曼语', 'Romansh'], 'RN': ['基隆迪语', 'Kirundi'], 'RO': ['罗马尼亚语', 'Romanian,\xa0Moldavian, Moldovan'], 'RU': ['俄语', 'Russian'], 'RW': ['基尼阿万达语', 'Kinyarwanda'], 'SA': ['梵语', 'Sanskrit (Saṁskṛta)'], 'SC': ['撒丁语', 'Sardinian'], 'SD': ['信德语', 'Sindhi'], 'SE': ['北萨摩斯语', 'Northern Sami'], 'SG': ['桑戈语', 'Sango'], 'SI': ['僧加罗语', 'Sinhala, Sinhalese'], 'SK': ['斯洛伐克语', 'Slovak'], 'SL': ['斯洛文尼亚语', 'Slovene'], 'SM': ['萨摩亚语', 'Samoan'], 'SN': ['绍纳语', 'Shona'], 'SO': ['索马里语', 'Somali'], 'SQ': ['阿尔巴尼亚语', 'Albanian'], 'SR': ['塞尔维亚语', 'Serbian'], 'SS': ['塞斯瓦特语', 'Swati'], 'ST': ['南索托语', 'Southern Sotho'], 'SU': ['巽他语', 'Sundanese'], 'SV': ['瑞典语', 'Swedish'], 'SW': ['斯瓦希里语', 'Swahili'], 'TA': ['泰米尔语', 'Tamil'], 'TE': ['泰卢固语', 'Telugu'], 'TG': ['塔吉克语', 'Tajik'], 'TH': ['泰语', 'Thai'], 'TI': ['提格里尼亚语', 'Tigrinya'], 'TK': ['土库曼语', 'Turkmen'], 'TL': ['他加禄语', 'Tagalog'], 'TN': ['塞茨瓦纳语', 'Tswana'], 'TO': ['汤加语', 'Tongan'], 'TR': ['土耳其语', 'Turkish'], 'TS': ['宗加语', 'Tsonga'], 'TT': ['塔塔尔语', 'Tatar'], 'TW': ['特威语', 'Twi'], 'TY': ['塔希提语', 'Tahitian'], 'UG': ['维吾尔语', 'Uighur, Uyghur'], 'UK': ['乌克兰语', 'Ukrainian'], 'UR': ['乌尔都语', 'Urdu'], 'UZ': ['乌兹别克语', 'Uzbek'], 'VE': ['文达语', 'Venda'], 'VI': ['越南语', 'Vietnamese'], 'VO': ['沃拉普克语', 'Volapük'], 'WA': ['瓦隆语', 'Walloon'], 'WO': ['沃洛夫语', 'Wolof'], 'XH': ['科萨语', 'Xhosa'], 'YI': ['依地语', 'Yiddish'], 'YO': ['约鲁巴语', 'Yoruba'], 'ZA': ['壮语', 'Zhuang, Chuang'], 'ZH': ['汉语（中文）', 'Chinese'], 'ZU': ['祖鲁语', 'Zulu']}

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

def audiovisual_downloader(url, path, headers=None):
    with closing(requests.get(url, stream=True, headers=headers)) as r:
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

def get_data_html_offline(file_path):
    """
    Reads a local HTML file and extracts specific elements.
    Parameters:
    file_path (str): The path to the local HTML file. my_html="Top 5 Web Scraping Methods_ Including Using LLMs - Comet.mhtml"
    
    Returns: html
    
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
    else: #.html
        html=etree.parse(file_path,etree.HTMLParser())
    return html

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
        if isinstance(table, pd.DataFrame) and table.shape[0] > max_rows:
            max_rows=table.shape[0]
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
            target_table=find_table_with_most_rows(tables)[0] #  (1, 32)
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