import re
import os
class Create_File:
    #検査に使用する検査式などを入力するファイルを生成
    def __init__(self, file_name, txt, dir_name, auto_write_tf, formulas):
        self.dir_name = dir_name
        self.create_dir()
        self.file_name = file_name+".txt"
        self.txt = txt
        self.path = "./"+self.dir_name+"/"+self.file_name
        with open(self.path, mode="w") as f:
            f.write("--"+txt+os.linesep)
            if auto_write_tf:
                li = self.create_formula_list(formulas)
                li = sorted(set(li), key = li.index)
                
                for i in li:
                    f.write(i+os.linesep)
    #ディレクトリを生成
    def create_dir(self):
        if not os.path.isdir(self.dir_name):
            os.mkdir(self.dir_name)
    #検査式ごとに検査に使用する変数などを入力するためのテキストファイルを生成
    def create_formula_list(self, formulas):
        li = []
        skip_tf = False
        if type(formulas[0]) is str:
            return formulas
        for index, item in enumerate(formulas): 
            
            if skip_tf == True:
                skip_tf = False
                continue
            ltl_tf = False
            temp_formula = "( " + item.formula
            temp_ltl_ope_li = list(dict.fromkeys(item.ltl_ope_li))
            for i in reversed(temp_ltl_ope_li):
                if i == "G" or i=="F" or i=="X":
                    ltl_tf = True
                if  "G" in i or "F" in i or "X" in i :
                    temp_formula = i + " " + temp_formula
            
            if item.ltl_ope_li[-1] == "U" and index+1 <= len(formulas) :
                skip_tf = True
                temp_formula = temp_formula + " U " + formulas[index+1].formula +  " )"
            else:
                temp_formula +=  " )"
            temp_formula =  "SPEC " + temp_formula
            if ltl_tf:
                temp_formula = "LTL" + temp_formula 
            li.append(temp_formula)
            

        return li

#検査に使用するテキストファイルの読み込み
class Read_Txtfile:
    def __init__(self, path):
        self.path = path
        
        with open(self.path) as f:
            self.txts = f.readlines()
            if self.txts != 0:
                self.first_txt = re.sub("[\r\n]+$",'', self.txts[0] )
                if self.first_txt[0:2] !="--":
                    self.first_txt = self.first_txt[2:]
        
        self.formulas = self.parse_txt_data()

    def  parse_txt_data(self):
        li = []
        with open(self.path) as f:
            li = f.readlines()
            li = [re.sub("[\r\n]+$",'', i )for i in li[1:]]
            temp =[]
            for i in li:
                if "SPEC" in i:
                    temp.append(i)
                else:
                    temp.append(i.replace(" ", ""))
            li=temp
            li = [i for i in li if i != "" ]
            return li


#Create_File("test_file", "LTLSPEC A = B", "formulas-dir")
#Read_Txtfile("./formulas-dir/test_file.txt")
