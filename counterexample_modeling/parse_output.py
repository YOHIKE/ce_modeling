import re
import regex
import os
class Parse_Output:
    #検査結果を辞書形式で各情報ごとに整理
    def __init__(self, outputs, specifications):
        self.outputs = outputs
        self.results = []
        for index, item in enumerate(self.outputs):
            if item != True:
                temp = self.parseOutput(item)
                self.results.append({'specification':specifications[index], 'inspection_result':False, 'state_num':temp[0], 'input_num':temp[1], 'state_variables':temp[2], 'input_variables':temp[3], 'loop_start_pos':temp[4]})
            else:
                self.results.append({'specification':specifications[index], 'inspection_result':True})
    
    def parseOutput(self, result):
        #--specification (...) is Falseから検査結果までを分析したリスト
        output = re.split(r"-> (.*) <-",  result)
        #検査結果の中のstateとinputのリスト
        state_num = [output[i] for i in range(len(output)) if i % 2 == 1]
        input_num = None
        #各状態の変数と値の変動のリスト
        state_variables = [output[i].replace(" ", "") for i in range(len(output)) if i % 2 == 0 ]
        input_variables = None
        #最初からループしているかを調べてから最初の検査結果の部分を削除する
        loop_start_pos = []
        if "--Loopstartshere" in state_variables[0]:
            #ループが開始している場所のリスト
            loop_start_pos.append(1)  
        state_variables.pop(0)

        if len(state_num) >= 2 and 'Input' in state_num[1] :
            input_num = [state_num[i] for i in range(len(state_num)) if i %2 == 1]
            state_num = [state_num[i] for i in range(len(state_num)) if i %2 == 0]
            input_variables = [state_variables[i] for i in range(len(state_variables)) if i %2 == 1]
            state_variables = [state_variables[i] for i in range(len(state_variables)) if i %2 == 0]
        
        if "\r\n" in output:
            linesep = "\r\n"
        elif "\r" in output:
            linesep = "\r"
        elif "\n" in output:
            linesep = "\n"
        else:
            linesep =os.linesep
        
        
        for i in range(len(state_variables)):
            state_variables[i] = state_variables[i].split(linesep)
            
            state_variables[i].pop(0)
            state_variables[i].pop(-1)
            #loop start hereの場所を見つけそれをloop start pos に保存する
            for j in range(len(state_variables[i])):   
                state_variables[i][j] = state_variables[i][j].split("=")
            if state_variables[i]:
                if len(state_variables[i][-1]) == 1:
                    loop_start_pos.append(i+2)
                    state_variables[i].pop(-1)
        
        if input_variables != None:
            for i in range(len(input_variables)):
                input_variables[i] = input_variables[i].split(linesep)
                input_variables[i].pop(0)
                input_variables[i].pop(-1)
                for j in range(len(input_variables[i])):
                    input_variables[i][j] = input_variables[i][j].split("=")
                    if input_variables[i][j][0] == 'running':
                        input_variables[i][j][0] = 'main.running'

                if input_variables[i]:

                    if len(input_variables[i][-1]) == 1:
                        loop_start_pos.append(i+2)
                        input_variables[i].pop(-1)    
        return state_num, input_num, state_variables, input_variables, loop_start_pos