class Result_Organization:
    def __init__(self, results):
        #反例を状態番号，使用した変数名，各変数の状態遷移のすべてを記述した辞書形式形式の変数を生成
        self.results = []
        self.result_organization(results)
        
    def result_organization(self, results):

        for index, result in enumerate(results):
            if result['inspection_result'] == False:
                self.results.append({'state_num':results[index]['state_num'], 'input_num':results[index]['input_num'], 'specification': results[index]['specification'], 'inspection_result':results[index]['inspection_result'],  'loop_start_pos':results[index]['loop_start_pos']})
                self.results[index]['state_variables'] = self.variables_organization(results[index]['state_variables'])
                if results[index]['input_variables'] != None:
                    self.results[index]['input_variables'] = self.variables_organization(results[index]['input_variables'])
            else:
                self.results.append(result)
    
    def variables_organization(self, variables):
        organized_variables = []
        template = {}
        for var, value in variables[0]:
            template[var] = value 
        for index, item in enumerate(variables):
            if index > 0:
                template=organized_variables[-1]
            organized_variables.append(template.copy())
            for var, value in item:
                organized_variables[index][var] = value

        return  organized_variables