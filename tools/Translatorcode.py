import os
import shutil
import zipfile as zf
from tkinter import filedialog
from datetime import datetime
from tkinter import END
from tkinter import messagebox
#import translators as ts

class Trans():
    def __init__(self,mes):
        self.filepath=[]
        self.filelist=[]
        self.mes = mes
        self.rmcache()
        pass

    def cutin(self,str,kind=None,):
        self.mes.text.configure(state='normal')
        timenow = datetime.now()
        timenow = timenow.strftime("%H:%M:%S")
        self.mes.insert(END,f"[{timenow}]:")
        if kind == None:
            self.mes.insert(END,str)
        elif kind == 1:
            self.mes.insert(END,str,"warn")
        self.mes.text.configure(state='disabled')

    def rmcache(self):
        if os.path.exists("./cache/trans"):
            shutil.rmtree("./cache/trans")
        os.makedirs("./cache/trans")
        self.cutin("旧的缓存已清空\n")
    
    def joincache(self):
        self.filepath.append(filedialog.askopenfilename(title="选择文件",filetypes=[("jar文件","*.jar"),("json文件","*.json")]))
        if not self.filepath[-1]=="":
            self.cutin(f"新的文件{os.path.basename(self.filepath[-1])}加入队列\n")
            file_n , file_e = os.path.splitext(self.filepath[-1])
            if file_e == ".jar":
                back = "_jar"
            elif file_e == ".json":
                back = "_jn"
            path_s = (f"./cache/trans/"+os.path.basename(self.filepath[-1])+back)
            path_s = os.path.join(path_s)
            
            
            if back == "_jar":
                with zf.ZipFile(self.filepath[-1],"r") as z:
                    z.extractall(path_s)
            elif back == "_jn":
                os.mkdir(path_s)
                shutil.copy(self.filepath[-1],path_s)
            self.cutin(f"文件{os.path.basename(self.filepath[-1])}加入缓存\n")
        else:
            self.cutin("没有选择文件\n")
            del self.filepath[-1]
    
    def delfile(self):
        self.filepath = os.listdir("./cache/trans")
        if self.filepath == []:
            self.cutin("没有缓存文件\n")
            return
        file = filedialog.askdirectory(initialdir="./cache/trans",title="选择缓存文件夹")
        if file == "":
            self.cutin("用户没有选择文件\n")
        return_d = messagebox.askquestion("确认","是否删除该缓存")
        if return_d == "no":
            self.cutin("用户取消删除\n")
            return
        shutil.rmtree(file)
        self.cutin(f"删除{file}成功\n")
    
    def spdic(self,dic,count):
        sub_dicts = []
        keys = list(dic.keys())
        to_keys = len(keys)

        for i in range(0, to_keys, count):
            sub_dict = {k: dic[k] for k in keys[i:i + count]}
            print(i)
            sub_dicts.append(sub_dict)

        return sub_dicts
    
    def trans_ts(self,dic,forml,tol,trantor):
        traned_dic = dic
        for i1,i2 in dic.items():
            pass
    
    def trans_ts_retdic(self,text_L,fromlang,tolang,trantor):
        traned_dic = {}
        for dic in text_L:
            pass



    
    


        
        