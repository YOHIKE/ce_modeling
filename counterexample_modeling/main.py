import sys, os, hashlib
from get_output_from_NuSMV import*
from parse_output import*
from result_organization import*
from create_counterexample_model import*
from antlr import antlr_parser
from trace import*
from antlr import antlr_parser_for_spec
from operate_files import*

class Main:
    def __init__(self):
        #引数を確認し，行う処理を決定
        self.check_args()
        #NuSMVでモデル検査
        self.get_output_from_NuSMV = Get_Output_From_NuSMV(self.smvFile)
        self.spec = self.get_output_from_NuSMV.specification
        self.result = self.get_output_from_NuSMV.result
        if self.result[0] == "Error":
            "NuSMVでsmvファイルを実行した際にエラーが出力されました"
        #検査結果を整理
        self.parseOutput = Parse_Output(self.result,  self.spec)
        #print(self.parseOutput.results)
        #for i in self.parseOutput.results[0]["state_variables"][0]:
          #  print(i)
        self.results = Result_Organization(self.parseOutput.results).results  
        #antlrで作成したパーサ・レクサを用いてパース
        self.antlr_parser = antlr_parser.Antlr_Parser(self.smvFile)
        #解析
        self.analyze()

    
    def analyze(self):
        #反例が出力されなかった場合処理を終了
        if len(self.result)==0:
            print("出力された反例はありませんでした")
            return
        #解析に使用する検査式を入力するファイルを8桁のハッシュと紐付けて生成
        elif self.create_formula_files:
            self.hash_dict = {}
            
            for i, result in enumerate(self.results):
               
                if result["inspection_result"] == True:
                    continue
                non_space_spec = result["specification"].replace(" ", "").encode()
                spec_hash = str(int(hashlib.sha1(non_space_spec).hexdigest(), 16) % (10**8)).zfill(8)
                path = "./"+self.dir_name+"/"+"formulas-"+str(spec_hash)+".txt"
                self.hash_dict[spec_hash] = result["specification"]
                
                if os.path.isfile(path):
                    continue
                if self.auto_write_formulas:
                    self.formulas= self.antlr_parser.listener.formulas
                    
                    self.formulas = sorted(set(self.formulas), key = self.formulas.index)
                else:
                    self.formulas=None
                
                Create_File("formulas-"+str(spec_hash), result["specification"], self.dir_name, self.auto_write_formulas, self.formulas)

            hash_table_txt = ""
            for i in self.hash_dict.keys():
                hash_table_txt += i + " : " + self.hash_dict[i] + os.linesep
            
            with open("./"+self.dir_name+"/hash_table.txt", mode="w") as f:
                f.write(hash_table_txt)
            return
       #ハッシュで紐付けた各ファイルの検査式などを利用して解析
        elif self.use_each_formulas:
            
            for i, result in enumerate(self.results):
                
                non_space_spec = result["specification"].replace(" ", "").encode()
                spec_hash = str(int(hashlib.sha1(non_space_spec).hexdigest(), 16) % (10**8)).zfill(8)
                
                path = "./"+self.dir_name+"/"+"formulas-"+spec_hash+".txt"
                if result["inspection_result"] == True or os.path.isfile(path) == False:
                    continue
                
                self.formulas = Read_Txtfile(path).formulas
                
                self.create_counterexample_model = CreateCounterexampleModel(result, i, self.antlr_parser.listener.var_dec_par_module)
                self.trace = Trace(self.create_counterexample_model , self.formulas,result, i, path)
            for i, result in enumerate(self.results):
                if result["inspection_result"] == True:
                    continue
                self.output_tabular = OutputTabular(result, i)
            return 
        #各検査式の部分式を用いて解析
        if self.auto_specification_create:
            self.formulas= self.antlr_parser.formulas_li
            self.formulas = sorted(set(self.formulas), key = self.formulas.index)
            
        #各検査式の変数を用いて解析
        elif self.auto_output_var:
            self.formulas = self.antlr_parser.var_li
        #各検査式の変数を用いて解析
        elif self.auto_output_formula:
            self.formulas = self.antlr_parser.formula_li
        #formulas.txtのファイルの検査式などを用いて解析
        else:
            self.formulas = None
        
        for i, result in enumerate(self.results):
            if result["inspection_result"] == True:
                continue

            
            self.create_counterexample_model = CreateCounterexampleModel(result, i, self.antlr_parser.listener.var_dec_par_module)
            self.trace = Trace(self.create_counterexample_model , self.formulas,result, i, "formulas.txt")
        #解析結果の出力
        for i, result in enumerate(self.results):
            if result["inspection_result"] == True:
                continue
            self.output_tabular = OutputTabular(result, i)

    #引数を確認し，行う処理を決定する変数をTrueにする，また，検査に使用するファイル名を取得
    def check_args(self):
        args = sys.argv
        self.smvFile = None
        self.counterexample_model_name = None
        self.excel_file_name = None
        self.auto_specification_create = False
        self.create_formula_files = False
        self.use_each_formulas = False
        self.auto_write_formulas = False
        self.auto_output_var = False
        self.auto_output_formula = False
        for i in args:
            if ".smv" in i:
                self.smvFile = i
            #elif i == "-x":
              #  print("保存するエクセルファイル名を入力してください")
              #  self.excel_file_name = input()
               # if  ".xlsx" not in self.excel_file_name:
              #      self.excel_file_name+=".xlsx"
              #  print(self.excel_file_name)
            elif i == "-c":
                print("作成するディレクトリ名を指定してください(入力がない場合デフォルトのディレクトリ名になります)")
                self.dir_name = input()
                if self.dir_name =="":
                    self.dir_name = "formulas-dir"
                print("検査式から自動で式を作成しますか？  y/n")
                self.temp_input = input()
                if self.temp_input=="y":
                     self.auto_write_formulas = True

                elif self.temp_input != "n":
                    print("不正な入力を受け付けたためファイルを作成できませんでした")
                    sys.exit(0)
                self.create_formula_files = True

            elif i == "-e":
                print("使用するディレクトリファイル名を指定してください(入力がない場合デフォルトのディレクトリ名になります)")
                self.dir_name = input()
                if self.dir_name =="":
                    self.dir_name = "formulas-dir"
                if not os.path.isdir:
                    print("指定されたディレクトリが見つかりませんでした")
                else:
                    self.use_each_formulas = True
            
            elif i == "-v":
                self.auto_output_var = True
            elif i == "-f":
                self.auto_output_formula = True
            elif i == "-a":
                self.auto_specification_create= True
        if self.smvFile == None:
            print("検査するsmvファイル名を入力してください")
            self.smvFile = input()
            
        print('used smv file :', self.smvFile)
if __name__ == '__main__':
    Main()