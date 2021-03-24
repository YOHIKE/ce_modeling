import subprocess
import re

class Get_Output_From_NuSMV:
    def __init__(self, smvFile):
        self.smvFile = smvFile
        #NuSMVで検査
        try:

            self.outputFromNuSMV = subprocess.check_output("NuSMV {}".format(smvFile),  shell=True, stderr=subprocess.STDOUT).decode()
        except subprocess.CalledProcessError as e:
            self.result = ["Error"]
            return
        #検査結果，検査にしようした検査式をリストに整理
        self.analyzeOutput()
    
    def analyzeOutput(self):
        self.temp = re.split(r"-- specification (.*)  is true", self.outputFromNuSMV)
        
        #検査結果のリスト
        self.outputFromNuSMV = []
    
        for i in self.temp: 
            self.outputFromNuSMV.extend(re.split(r"-- specification (.*)  is false", i))
        self.outputFromNuSMV.pop(0)
        #出力結果の何番目が反例なのかを保存するリスト
        self.result = []
        self.specification = []
        

        for i in range(len(self.outputFromNuSMV)):
            if i % 2:
                if ("State" in self.outputFromNuSMV[i]):
                    self.result.append(self.outputFromNuSMV[i])
                else:

                    self.result.append(True)
            else:
                self.specification.append(self.outputFromNuSMV[i])
        
