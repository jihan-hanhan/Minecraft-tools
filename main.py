import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import darkdetect
from tkinter.font import Font
from ttkbootstrap.scrolled import ScrolledText
from tkinter import filedialog
from tkinter import Listbox
from tkinter import Entry
from threading import Thread

from Translatorcode import Trans


if darkdetect.isDark() == True:
    kind = "darkly"
else:
    kind = "litera"

def refont(side):
    returnfont = Font(family="Microsoft YaHei",size=side)
    return returnfont

root = ttk.Window(themename=kind,title="Minecraft tools")
root.geometry("1000x650")

nt = ttk.Notebook(root)
nt.pack(fill="both",expand=True)

#翻译器页面小组件
p1 = ttk.Frame()
nt.add(p1,text="翻译器")

title = ttk.Label(p1,text="Minecraft 模组翻译器",font=refont(30))
title.pack(side=TOP,anchor="w",padx=10)

text_ref = ttk.Label(p1,text="*翻译输出不代表mod创作团队品质",foreground="gray")
text_ref.pack(side=TOP,anchor="e")

flood = ttk.Progressbar(p1,length=1115,bootstyle="success")
flood.pack(side=TOP,anchor="w",padx=13,pady=10,fill="x")

logs_text = ScrolledText(p1,vbar=True,width=60, height=28,font=refont(10))
logs_text.pack(side=LEFT,anchor="nw",padx=11,pady=10)
logs_text.text.configure(state='disabled')
logs_text.tag_configure("warn", foreground="#ffc107")

tools = ttk.Frame(p1,width=380,height=680)
tools.pack(side=LEFT,anchor="n",padx=10,pady=10,fill="y")
tools.pack_propagate(False)



##start框架
text = ttk.Label(tools,text="————开始————",foreground="gray")
text.pack(side=TOP,anchor="w")

start_frame = ttk.Frame(tools,width=100,height=130)
start_frame.pack(side=TOP,pady=10,anchor="w")

startbuttun1 = ttk.Button(start_frame,bootstyle="info-outline",width=7,text="翻译单个")
startbuttun1.pack(side=LEFT,padx=2)

startbuttun2 = ttk.Button(start_frame,bootstyle="info-outline",width=7,text="翻译所有")
startbuttun2.pack(side=LEFT,padx=2)

startbuttun3 = ttk.Button(start_frame,bootstyle="info-outline",width=7,text="翻译json")
startbuttun3.pack(side=LEFT,padx=2)


##output框架
text = ttk.Label(tools,text="————输出————",foreground="gray")
text.pack(side=TOP,anchor="w")

output_frame = ttk.Frame(tools,width=100,height=130)
output_frame.pack(side=TOP,pady=10,anchor='w')


opbuttun1 = ttk.Button(output_frame,bootstyle="success-outline",width=7,text="jar")
opbuttun1.pack(side=LEFT,padx=2)

opbuttun2 = ttk.Button(output_frame,bootstyle="success-outline",width=7,text="json")
opbuttun2.pack(side=LEFT,padx=2)

opbuttun3 = ttk.Button(output_frame,bootstyle="success-outline",width=7,text="材质包")
opbuttun3.pack(side=LEFT,padx=2)

#文件操作
text = ttk.Label(tools,text="————文件————",foreground="gray")
text.pack(side=TOP,anchor="w")

fileframe = ttk.Frame(tools,)
fileframe.pack(side=TOP,pady=10,anchor='w')

input_buttun = ttk.Button(fileframe,bootstyle="info-outline",width=7,text="选择文件",command=lambda:joincache_tr.start())
input_buttun.pack(side=LEFT,padx=2)

del_buttun = ttk.Button(fileframe,bootstyle="danger-outline",width=7,text="删除文件",command=lambda:mian_code.delfile())
del_buttun.pack(side=LEFT,padx=2)

##settings&list
text = ttk.Label(tools,text="————设置————",foreground="gray")
text.pack(side=TOP,anchor="w")

fromlanguage = "en"
tolanguage = "zh-cn"

def setting():
    window_set = ttk.Toplevel(root)
    window_set.title("设置")
    window_set.geometry("300x500")

    text = ttk.Label(window_set,text="使用翻译库:")
    text.pack(side="top",anchor="w",padx=5)
    combobox_ta = ttk.Combobox(window_set,values=["translators(联网)","argostranslate(本地模型)"],state="readonly")
    combobox_ta.current(0)
    combobox_ta.pack(side=TOP,anchor="w",padx=5)

    #translators
    text = ttk.Label(window_set,text="translators库相关:")
    text.pack(side="top",anchor="w",padx=5)
    trframe = ttk.Frame(window_set)
    trframe.pack(side="top",anchor="w",padx=10)

    ###
    text = ttk.Label(trframe,text="md给我气傻了暂时不写")
    text.pack(side="top",anchor="w",padx=5)
    ###

    text = ttk.Label(trframe,text="翻译引擎")
    text.pack(side="top",anchor="w",padx=5)
    combobox = ttk.Combobox(trframe,values=["Niutrans", "MyMemory", "Alibaba", "Baidu", "ModernMt", "VolcEngine"
                                            , "Iciba", "Iflytek", "Google", "Bing", "Lingvanex", "Yandex", "Itranslate",
                                              "SysTran", "Argos", "Apertium", "Reverso", "Deepl", "CloudTranslation",
                                            "QQTranSmart", "TranslateCom", "Sogou", "Tilde", "Caiyun", "QQFanyi",
                                              "TranslateMe", "Papago", "Mirai", "Youdao", "Iflyrec", "Hujiang", "Yeekit",
                                                "LanguageWire", "Elia", "Judic", "Mglip", "Utibet"],state="readonly")
    combobox.current(9)
    combobox.pack(side="top",anchor="w",padx=5)
    text = ttk.Label(trframe,text="*更多请访问 https://github.\ncom/UlionTse/translators/ \n了解",foreground="gray")
    text.pack(side="top",anchor="w",padx=5)
    
    text = ttk.Label(trframe,text="输入语言")
    text.pack(side="top",anchor="w",padx=5)
    e1 = ttk.StringVar()
    entry1 = Entry(trframe,width=10,textvariable=e1)
    entry1.pack(side="top",anchor="w",padx=5)
    e1.set(fromlanguage)

    text = ttk.Label(trframe,text="输出语言")
    text.pack(side="top",anchor="w",padx=5)
    e2 = ttk.StringVar()
    entry2 = Entry(trframe,width=10,textvariable=e2)
    entry2.pack(side="top",anchor="w",padx=5)
    e2.set(tolanguage)

    text = ttk.Label(trframe,text="*注意,请使用\"-\"而不是\"_\"",foreground="gray")
    text.pack(side="top",anchor="w",padx=5)

    #argostranslate
    text = ttk.Label(window_set,text="argostranslate库相关:")
    text.pack(side="top",anchor="w",padx=5)
    argframe = ttk.Frame(window_set)
    argframe.pack(side="top",anchor="w",padx=5)

    


setbuttun = ttk.Button(tools,bootstyle="info-outline",width=7,text="设置",command=setting)
setbuttun.pack(side=TOP,pady=10,anchor='w')





#函数/主程序
mian_code = Trans(mes=logs_text)
joincache_tr = Thread(target=mian_code.joincache)
root.mainloop()