import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import darkdetect
from tkinter.font import Font
from ttkbootstrap.scrolled import ScrolledText
from tkinter import filedialog
from tkinter import Listbox
from tkinter import Entry
from threading import Thread
from plyer import notification
import json
import os

from tools.Translatorcode import Trans

import datetime
import webbrowser
from tkinter import messagebox
from time import sleep

from time import time

print(time())

#设置
settings = {}
if not os.path.exists("./settings.json"):
    with open("settings.json","w",encoding="utf-8") as j:
        json.dump({"theme":"none","font":"Microsoft YaHei","april_fools":False,"Tr:rmcache":True,"Tr:count":4,"Tr:fromlang":"en","Tr:tolang":"zh"},j,indent=4)
with open("settings.json","r",encoding="utf-8") as r:
    settings = json.load(r)

if darkdetect.isDark() == True and settings["theme"] == "none":
    kind = "darkly"
elif settings["theme"] == "none":
    kind = "litera"
else:
    kind = settings["theme"]

def refont(side):
    returnfont = Font(family=settings["font"],size=side)
    return returnfont

root = ttk.Window(themename=kind,title="Minecraft tools")
root.geometry("1000x650")

nt = ttk.Notebook(root)
nt.pack(fill="both",expand=True)

#主页
p0 = ttk.Frame()
nt.add(p0,text="主页")

title = ttk.Label(p0,text="你好\n欢迎使用\n🛠功能建设中👈🤓👍",font=refont(30))
title.pack()
title = ttk.Label(p0,text="欢迎使用",font=refont(25))

print(time())

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

startbuttun1 = ttk.Button(start_frame,bootstyle="info-outline",width=7,text="翻译单个",command=lambda:translate_only())
startbuttun1.pack(side=LEFT,padx=2)
def translate_only():
    startbuttun1.config(state="disabled")
    def completetask():
        startbuttun1.config(state="normal")
    thread = Thread(target= lambda:(mian_code.translate(fromlang=settings["Tr:fromlang"],tolang=settings["Tr:tolang"],count=settings["Tr:count"],translator="local",kind="only"), completetask()))
    thread.start()

startbuttun2 = ttk.Button(start_frame,bootstyle="info-outline",width=7,text="翻译多个")
startbuttun2.config(state="disabled")
startbuttun2.pack(side=LEFT,padx=2)


"""
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
"""
#文件操作
text = ttk.Label(tools,text="————文件————",foreground="gray")
text.pack(side=TOP,anchor="w")

fileframe = ttk.Frame(tools,)
fileframe.pack(side=TOP,pady=10,anchor='w')

input_buttun = ttk.Button(fileframe,bootstyle="info-outline",width=7,text="选择文件",command=lambda:jointask())
input_buttun.pack(side=LEFT,padx=2)
def jointask():
    input_buttun.config(state="disabled")
    def completetask():
        input_buttun.config(state="normal")
    thread = Thread(target=lambda: (mian_code.joincache(), completetask()))
    thread.start()

del_buttun = ttk.Button(fileframe,bootstyle="danger-outline",width=7,text="删除文件",command=lambda:mian_code.delfile())
del_buttun.pack(side=LEFT,padx=2)

##settings&list
text = ttk.Label(tools,text="————设置————",foreground="gray")
text.pack(side=TOP,anchor="w")

def Tr_setting():
    window_set = ttk.Toplevel(root)
    window_set.title("设置")
    window_set.geometry("300x500")
    window_set.transient(root)
    window_set.grab_set()

    bgcanvas = ttk.Canvas(window_set)
    scroll = ttk.Scrollbar(window_set,orient="vertical",command=bgcanvas.yview)
    bgcanvas.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right",fill="y")
    bgcanvas.pack(side="left",fill="both",expand=True)

    main_frame = ttk.Frame(bgcanvas)
    bgcanvas.create_window((0,0),window=main_frame,anchor="nw")
    def update_scrollregion(event):
        bgcanvas.configure(scrollregion=bgcanvas.bbox("all"))
    main_frame.bind("<Configure>",update_scrollregion)

    def _on_mousewheel(event):
        if event.delta:
            bgcanvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            pass
    bgcanvas.bind_all("<MouseWheel>", _on_mousewheel)

    text = ttk.Label(main_frame,text="使用翻译库:")
    text.pack(side="top",anchor="w",padx=5)
    combobox_ta = ttk.Combobox(main_frame,values=["translators(联网)","argostranslate(本地模型)"],state="readonly")
    combobox_ta.current(1)
    combobox_ta.pack(side=TOP,anchor="w",padx=5)
    def comboboxchange(event):
        pass

    text = ttk.Label(main_frame,text="输入语言")
    text.pack(side="top",anchor="w",padx=5)
    e1 = ttk.StringVar()
    entry1 = Entry(main_frame,width=10,textvariable=e1)
    entry1.pack(side="top",anchor="w",padx=5)
    e1.set(settings["Tr:fromlang"])

    text = ttk.Label(main_frame,text="输出语言")
    text.pack(side="top",anchor="w",padx=5)
    e2 = ttk.StringVar()
    entry2 = Entry(main_frame,width=10,textvariable=e2)
    entry2.pack(side="top",anchor="w",padx=5)
    e2.set(settings["Tr:tolang"])

    text = ttk.Label(main_frame,text="最大线程数")
    text.pack(side="top",anchor="w",padx=5)
    e3 = ttk.StringVar()
    entry3 = Entry(main_frame,width=10,textvariable=e3)
    entry3.pack(side="top",anchor="w",padx=5)
    e3.set(settings["Tr:count"])

    #translators
    text = ttk.Label(main_frame,text="translators库相关:",font=refont(15))
    text.pack(side="top",anchor="w",padx=5)
    trframe = ttk.Frame(main_frame)
    trframe.pack(side="top",anchor="w",padx=10)

    ###
    text = ttk.Label(trframe,text="md给我气傻了暂时不写",foreground="red")
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

    text = ttk.Label(trframe,text="*注意,请使用\"-\"而不是\"_\"",foreground="gray")
    text.pack(side="top",anchor="w",padx=5)

    #argostranslate
    text = ttk.Label(main_frame,text="argostranslate库相关:",font=refont(15))
    text.pack(side="top",anchor="w",padx=5)
    argframe = ttk.Frame(main_frame)
    argframe.pack(side="top",anchor="w",padx=5)

    
setbuttun = ttk.Button(tools,bootstyle="info-outline",width=7,text="设置",command=Tr_setting)
setbuttun.pack(side=TOP,pady=10,anchor='w')

print(time())


#函数/主程序
Tr_set = {}
Tr_set["Tr:rmcache"]=settings["Tr:rmcache"]

mian_code = Trans(mes=logs_text,settings=Tr_set)
joincache_tr = Thread(target=mian_code.joincache)

print(time())

#小彩蛋~

if datetime.datetime.now().month == 4 and datetime.datetime.now().day == 1:
    root.withdraw()
    if messagebox.askyesno("Minecraft Tools","程序出了些问题,但可以继续启动"):
        webbrowser.open("https://www.bilibili.com/video/BV1GJ411x7h7")
        messagebox.showerror("你被骗了","今天是愚人节哦🤣~")
    else:
        sleep(10)
        messagebox.showwarning("Minecraft Tools","不是哥们，还在等呢，看日期吧bro")
    root.deiconify()

print(time())

root.mainloop()

with open("settings.json","w",encoding="utf-8") as j:
    json.dump(settings,j,indent=4)