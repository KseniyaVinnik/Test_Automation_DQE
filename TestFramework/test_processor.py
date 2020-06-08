import glob


class TestProcessor:
    def __init__(self, config, connector, logger):
        self.config = config
        self.connector = connector
        self.logger = logger

    def process(self):
        test_data_files = self.check_test_folder()

        for f in test_data_files:
            self.do_testing(f)

    def check_test_folder(self):
        test_data_folder = self.config.get_test_data_folder()
        return [f for f in glob.glob(test_data_folder + '/*.json', recursive=True)]

    def do_testing(self, file_name):
        self.logger.start_test(file_name)

        with open(file_name, encoding='utf8') as f:
            test_data = eval(f.read())
        for test in test_data['tests']:
            self.logger.start_case(test['name'])
            query = test['query']
            try:
                query2 = test['query2']
                result1 = self.connector.execute(query)
                result2 = self.connector.execute(query2)
                if result1 == result2:
                    actual_result = "The result of the 1st query is equal to the result of the 2nd query"
                elif result1 > result2:
                    actual_result = "The result of the 1st query is more than the result of the 2nd query"
                else:
                    actual_result = "The result of the 1st query is less than the result of the 2nd query"
                expected_result = test['expected']
                queries = query + "\n\tAND \n\tQuery2: " + query2
                if actual_result in expected_result:
                    self.logger.add_pass(queries, actual_result)
                else:
                    self.logger.add_fail(queries, actual_result, expected_result)
            except KeyError:
                expected_result = test['expected']
                actual_result = self.connector.execute(query)
                if actual_result == expected_result:
                    self.logger.add_pass(query, actual_result)
                else:
                    self.logger.add_fail(query, actual_result, expected_result)
