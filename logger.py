import logging
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import json
from datetime import datetime

class AlgorithmLogger:
    def __init__(self, log_dir='logs', app_log_file='app.log', transaction_log_file='transactions.log'):
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        self.app_log_path = os.path.join(log_dir, app_log_file)
        self.transaction_log_path = os.path.join(log_dir, transaction_log_file)

        self.app_logger = logging.getLogger('algorithm_app')
        self.app_logger.setLevel(logging.INFO)
        

        app_handler = RotatingFileHandler(
            self.app_log_path, 
            maxBytes=10485760,
            backupCount=5
        )
        app_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        app_handler.setFormatter(app_formatter)
        self.app_logger.addHandler(app_handler)

        self.transaction_logger = logging.getLogger('algorithm_transactions')
        self.transaction_logger.setLevel(logging.INFO)

        transaction_handler = TimedRotatingFileHandler(
            self.transaction_log_path,
            when='midnight',
            interval=1,
            backupCount=30  
        )
        transaction_formatter = logging.Formatter('%(message)s')
        transaction_handler.setFormatter(transaction_formatter)
        self.transaction_logger.addHandler(transaction_handler)
    
    def log_algorithm_call(self, algorithm_name, request_data, response_data, execution_time=None):
        """
        Log an algorithm API call with request and response details
        
        Args:
            algorithm_name: Name of the algorithm that was called
            request_data: The input payload
            response_data: The response sent back
            execution_time: Execution time in milliseconds (optional)
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        log_entry = {
            'timestamp': timestamp,
            'algorithm': algorithm_name,
            'request': request_data,
            'response': response_data
        }
        
        if execution_time is not None:
            log_entry['execution_time_ms'] = execution_time

        self.app_logger.info(f"API Call: {algorithm_name} - Execution time: {execution_time}ms")

        self.transaction_logger.info(json.dumps(log_entry))
        
    def log_error(self, message, error=None):
        """
        Log an error message
        
        Args:
            message: Error message
            error: Exception object (optional)
        """
        if error:
            self.app_logger.error(f"{message}: {str(error)}")
        else:
            self.app_logger.error(message)