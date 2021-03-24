import os
class CreateCounterexampleModel:
    
    def __init__(self, result, num, var_dec_par_module):
        self.result = result
        self.var_dec_par_module = var_dec_par_module
        #for  i in self.var_dec_par_module.keys():
          #  print(i)
          #  print(self.var_dec_par_module[i])
        self.path = "counterexample_model_"+str(num)+".smv"
        self.define = None
        self.var = None
        self.assign = None
        self.specification = None
        self.create_counter_example()
        #self.create_DEFINE()
        #self.create_VAR()
        #self.create_ASSIGN(4)
        
    def create_counter_example(self):
        #反例モデルの生成
        #path = "counterexample_model.smv"
        if self.result["inspection_result"] == True:
            return
        self.variables = {i: [] for i in self.result["state_variables"][0].keys()}
        for i in self.result["state_variables"]:
            for j in self.result["state_variables"][0].keys():
                self.variables[j].append(i[j]) 
        self.variables = {i: list(set(self.variables[i])) for i in self.variables.keys()}

        self.model = "MODULE main"+os.linesep + os.linesep
        
        self.var = self.create_VAR()
        self.define = self.create_DEFINE()
        self.assign = self.create_ASSIGN(1)
        self.spec = (self.result["specification"].replace(".", "_"))
        if  "EX"  in self.spec or  "AX"  in self.spec or "EG"  in self.spec or "AG"  in self.spec or "AF"  in self.spec or "EF"  in self.spec:
            self.spec ="SPEC" + self.spec
        else:
            self.spec = "LTLSPEC " +  self.spec
        self.write_counterexample_model(self.path)
    #反例モデルをファイルに書き込み
    def write_counterexample_model(self,path):
        model = self.model 
        
        if self.define != None:
            model += self.define
        model = model + self.var + self.assign + self.spec
        with open(path, mode="w") as f:
            f.write(model)
    
    #定数定義部を生成
    def create_DEFINE(self):
        template_DEFINE ="DEFINE"+ os.linesep
        
        for i in self.variables.keys():
            if len(self.variables[i]) == 1 and self.variables[i][0].isdecimal():
                if self.var_list != [] and str(i).replace(".", "_") not in self.var_list:

                    template_DEFINE+=("    "+str(i).replace(".", "_") + " := " + self.variables[i][0] + ";"+os.linesep)

        if template_DEFINE == "DEFINE"+os.linesep:
            return None
        return template_DEFINE
    #変数定義部を生成
    def create_VAR(self):
        template_VAR = ("VAR"+os.linesep+os.linesep+"    next_state : 2.." + str(len(self.result["state_num"])+1) + ";"+os.linesep)
        self.var_list = []
        for i in self.var_dec_par_module["main"].keys():
            
            if type(self.var_dec_par_module["main"][i]) is dict:
                
                temp_dict = self.var_dec_par_module[self.var_dec_par_module["main"][i]["module"]]
                for j in temp_dict.keys():
                    template_VAR += "    " + i + "_" +  j + " : " + temp_dict[j]+ ";" +os.linesep
                    self.var_list.append(i + "_" +  j)
            else:
                template_VAR+="    " + i + " : " + self.var_dec_par_module["main"][i] + ";" +os.linesep
                self.var_list.append(i)
        #defineとvar定義
        #for i in self.variables.keys():
         #   if "FALSE" in self.variables[i] or "TRUE" in self.variables[i]:
          #      template_VAR+=("    "+str(i).replace(".", "_") + " : boolean;"+os.linesep)
          #      continue
           # elif len(self.variables[i]) == 1 and self.variables[i][0].isdecimal():
           #     continue
          #  value = ",".join(sorted(self.variables[i],))
           # template_VAR+=("    "+str(i).replace(".", "_") + " : {" + value + "}"+";"+os.linesep)
        
        return template_VAR
    #init_stateはNuSMVにおけるstate
    #状態遷移定義部を生成
    def create_ASSIGN(self, init_state):
        self.max_state = len(self.result["state_num"])
        if init_state +1 > self.max_state and len(self.result["loop_start_pos"]) != 0:
            template_ASSIGN = "ASSIGN"+os.linesep+os.linesep+"    init(next_state) := " + str(self.result["loop_start_pos"][0]) + ";"+os.linesep
        else:
            template_ASSIGN = "ASSIGN"+os.linesep+os.linesep+"    init(next_state) := " + str(init_state+1) + ";"+os.linesep
        for i in self.result["state_variables"][0].keys():
            if len(self.variables[i]) ==1 and self.variables[i]!= "TRUE" and self.variables[i] != "FALSE":
                continue
            template_ASSIGN += ("    init(" + i.replace(".", "_") +") := "+self.result["state_variables"][init_state-1][i] + ";"+os.linesep)
        template_ASSIGN+=os.linesep
        template_ASSIGN+="    next(next_state) := case"+os.linesep
        for i in range(1,len(self.result["state_num"])-1):
            template_ASSIGN+=("        next_state = "+str(i+1) +" : " + str(i+2) + ";"+os.linesep)
        
        if len(self.result["loop_start_pos"]) != 0:
            self.loop_start_pos = self.result["loop_start_pos"][0]
            template_ASSIGN+=("        next_state = "+str(i+2) +" : " + str(self.result["loop_start_pos"][0]+1) + ";"+os.linesep)
        else:
            self.loop_start_pos = None
        template_ASSIGN+=("        TRUE : next_state;"+os.linesep)
        template_ASSIGN+="        esac;"+os.linesep+os.linesep

        for i in self.result["state_variables"][0].keys():
            if len(self.variables[i]) ==1:
                continue
            template_ASSIGN+="    next(" + i.replace(".", "_") +") := case"+os.linesep
            for index, li in enumerate(self.result["state_variables"]):
                if index == 0:
                    continue
                template_ASSIGN+=("        next_state = "+str(index+1) +" : " + li[i] + ";"+os.linesep)


            template_ASSIGN+=("        TRUE:" + i.replace(".", "_") +";"+os.linesep)
            template_ASSIGN+="        esac;"+os.linesep+os.linesep

        return template_ASSIGN

