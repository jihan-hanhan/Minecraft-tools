import os
import shutil
import zipfile as zf
from tkinter import filedialog
from datetime import datetime
from tkinter import END
from tkinter import messagebox
import argostranslate.package
import argostranslate.translate
import json
from threading import Thread
from threading import Lock

#import translators as ts

minecraft_lang_map = {
    "en": ["en_us.json"],
    "zh": ["zh_cn.json", "zh_tw.json"],
    "es": ["es_es.json", "es_mx.json"],
    "fr": ["fr_fr.json"],
    "de": ["de_de.json"],
    "ja": ["ja_jp.json"],
    "ko": ["ko_kr.json"],
    "ru": ["ru_ru.json"],
    "pt": ["pt_br.json", "pt_pt.json"],
    "it": ["it_it.json"],
    "nl": ["nl_nl.json"],
    "pl": ["pl_pl.json"],
    "tr": ["tr_tr.json"],
    "sv": ["sv_se.json"],
    "uk": ["uk_ua.json"],
    "ar": ["ar_sa.json"],
    "hu": ["hu_hu.json"],
    "cs": ["cs_cz.json"],
    "th": ["th_th.json"],
    "vi": ["vi_vn.json"],
    "el": ["el_gr.json"],
    "id": ["id_id.json"],
    "no": ["nb_no.json"],
    "fi": ["fi_fi.json"],
    "da": ["da_dk.json"]
}
class Trans():
    def __init__(self,mes):
        self.filepath=[]
        self.filelist=[]
        self.mes = mes
        self.rmcache()
        self.det_models_dir()
        self.mk_outputsdir()
        argostranslate.package.update_package_index()
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
        if os.path.exists("./cache/translator"):
            shutil.rmtree("./cache/translator")
        os.makedirs("./cache/translator")
        self.cutin("旧的缓存已清空\n")

    def det_models_dir(self):
        if not os.path.exists("./models"):
            os.makedirs("./models")
            self.cutin("首次使用,创建models目录\n")
    
    def mk_outputsdir(self):
        if not os.path.exists("./cache/outputs"):
            os.makedirs("./cache/outputs")
            self.cutin("首次使用,创建outputs目录\n")
    
    def joincache(self):
        self.filepath.append(filedialog.askopenfilename(title="选择文件",filetypes=[("jar文件","*.jar"),("json文件","*.json")]))
        if not self.filepath[-1]=="":
            self.cutin(f"新的文件{os.path.basename(self.filepath[-1])}加入队列\n")
            file_n , file_e = os.path.splitext(self.filepath[-1])
            if file_e == ".jar":
                back = "_jar"
            elif file_e == ".json":
                back = "_jn"
            path_s = (f"./cache/translator/"+os.path.basename(self.filepath[-1])+back)
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
        self.filepath = os.listdir("./cache/translator")
        if self.filepath == []:
            self.cutin("没有缓存文件\n")
            return
        file = filedialog.askdirectory(initialdir="./cache/translator",title="选择缓存文件夹")
        if file == "":
            self.cutin("用户没有选择文件\n")
            return
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
    
    def clean_folder_name(self,folder_name:str):
        suffixes = ["_jar", "_jn"]
        for suffix in suffixes:
            if folder_name.endswith(suffix):
                return folder_name[:-len(suffix)]
        return folder_name
    
    def trans_ts(self,dic,forml,tol,trantor): #在线版
        traned_dic = dic
        for i1,i2 in dic.items():
            pass
    
    def trans_ts_retdic(self,text_L,fromlang,tolang,trantor):
        traned_dic = {}
        for dic in text_L:
            pass
    
    def trans_local_detcet_installedpackage(self,fromlang,tolang):
        installed_package = argostranslate.package.get_installed_packages()
        return any(
            pkg.from_code == fromlang and pkg.to_code == tolang
            for pkg in installed_package
        )
    
    def trans_local_installpackages(self,fromlang:str,tolang:str):
        try:
            self.cutin(f"尝试安装{fromlang}-{tolang}\n")
            available_packages = argostranslate.package.get_available_packages()
            install = next(
                filter(
                    lambda x: x.from_code == fromlang and x.to_code == tolang,
                    available_packages
                )
            )
            argostranslate.package.install_from_path(install.download())
            self.cutin("安装成功")
        except Exception as e:
            self.cutin(e)
            self.cutin("\n")
            self.cutin("包下载时发生错误,请确认网络连接,或使用VPN")


    def trans_local(self,text,fromlang,tolang,count=4):
        #检测部分
        if not self.trans_local_detcet_installedpackage(fromlang,tolang):
            if messagebox.askyesno("MT",f"未发现{fromlang}-{tolang}语言包，确定安装吗?") == "yes":
                self.trans_local_installpackages(fromlang,tolang)
            else:
                self.cutin("未能满足翻译条件\n")
                return
        #翻译部分
        return argostranslate.translate(text,fromlang,tolang)
        """暂时放弃部分
        if type(text) is str:
            return argostranslate.translate.translate(text,fromlang,tolang)
        elif type(text) is list:
            for i in text:
                return_t = []
                return_t.append(argostranslate.translate.translate(i,fromlang,tolang))
                return return_t
        elif type(text) is dict:
            text2 = self.spdic(text,count)
            for dict1 in text2:
                for key in dict1:
                    v = argostranslate.translate.translate(dict1[key],fromlang,tolang)
                    text[key] = v
            return text
        """
        
    def translate(self,fromlang,tolang,count,translator,kind,text=None):
        if translator == "local":
            if kind == "only":
                path = filedialog.askdirectory(title="选择文件夹",initialdir="./cache/translator")
                if path.endswith("_jar"):
                    self.cutin(f"选择 {path} \n")
                    #文件夹操作
                    path2 = path + "/assets"

                    dirs = os.listdir(path2)
                    if "minecraft" in dirs:
                        dirs.remove("minecraft")
                    path2 = path2 + "/" +dirs[0] +"/lang"
                    ##寻找fromlang
                    paths = []
                    try:
                        for i in minecraft_lang_map[fromlang]:
                            paths.append(path2+"/"+i)
                    except Ellipsis as e:
                        self.cutin(e+"\n")
                        self.cutin("未发现目标语言文件,请确认lang目录存在并包含目标语言文件\n")
                        return
                    ##翻译
                    for i in paths:
                        with open(i,"r") as f:
                            data = json.load(f)
                        sdata = self.spdic(data,count)
                        data = {}
                        lock = Lock()
                        #循环翻译
                        def work_translate(dict1):
                            cache = {}
                            for key in dict1:
                                v = self.trans_local(dict1[key],fromlang,tolang,count)
                                self.cutin(f"{dict1[key]}-->{v}\n")
                                cache[key] = v
                            with lock:
                                data.update(cache)
                            self.cutin(f"完成线程{cache}\n")
                        threads = []
                        for dict1 in sdata:
                            work = Thread(target=work_translate,args=(dict1,))
                            work.start()
                            threads.append(work)

                        for t in threads:
                            t.join()
                        #写入
                        with open(i,"w") as f:
                            json.dump(data,f)
                        self.cutin("将翻译语言文件写入中\n")
                    ##输出
                    filename = self.clean_folder_name(os.path.basename(path))
                    filedir = filedialog.asksaveasfilename(title="保存",initialdir="./cache/outputs",
                                                           initialfile=filename,defaultextension=".jar",filetypes=[("jar文件","*.jar"),("所有文件", "*.*")])
                    if not filedir:
                        self.cutin("取消保存\n")
                        return
                    self.cutin(f"完成{path}模组翻译")


        
                
                    








    
    


        
        