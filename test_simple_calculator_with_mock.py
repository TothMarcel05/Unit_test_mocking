def test_add_with_mock_history_service():
        if self.validation_service:
            self.validation_service.validate_numbers(1, 2)
        
        result = 1 + 2
        
        if self.logger:
            self.logger.log_operation("add", 1, 2, result)
        
        if self.history_service:
            self.history_service.save_operation("add", 1, 2, result)
        
        return result

def test_multiply_with_multiple_mocks():
        if self.validation_service:
        self.validation_service.validate_numbers(1, 2)
        
        result = 1 * 2
        
        if self.logger:
            self.logger.log_operation("multiply", 1, 2, result)
        
        if self.history_service:
            self.history_service.save_operation("multiply", 1, 2, result)
        
        return result

def test_get_history_count_with_mock():
        if self.history_service:
        return self.history_service.get_operation_count()
        return 0