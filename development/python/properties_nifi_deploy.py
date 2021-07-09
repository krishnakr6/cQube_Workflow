NIFI_IP = 'http://localhost' # Nifi url
NIFI_PORT = 8080             # Nifi Port number
NIFI_TEMPLATE_PATH = '/home/krishna/Downloads/' # Nifi templates local directory path ending with /
NIFI_PARAMETER_DIRECTORY_PATH = '/home/krishna/KR/Tibil/nifi_dir/parameters/'  # Nifi parameters[created by ansible using config file] local directory path ending with /
NIFI_INPUT_OUTPUT_PORTS = {
    'static_data_transformer': [
                              {'OUTPUT_PORT': 'static_split_file_wait', 'INPUT_PORT': 'split_wait'},
                              {'OUTPUT_PORT': 'static_split_success','INPUT_PORT': 'split_file_process_success'},
                              {'OUTPUT_PORT': 'static_split_failure','INPUT_PORT': 'split_file_failure'},
                              
                              {'OUTPUT_PORT': 'store_s3_output_port','INPUT_PORT': 'store_s3_input_port'},
                              {'OUTPUT_PORT': 'store_school_mgt_s3_output_port','INPUT_PORT': 'store_school_mgt_s3_input_port'},
                              {'OUTPUT_PORT': 'store_school_mgt_s3_output_port2','INPUT_PORT': 'store_school_mgt_s3_input_port2'},
                              {'OUTPUT_PORT': 'static_store_output_dir_output_port','INPUT_PORT': 'static_store_output_dir_input_port'},
                              {'OUTPUT_PORT': 'static_s3_school_management_output_port','INPUT_PORT': 'static_s3_school_management_output_port'},
                              
                              
                              ],
    
    'cQube_data_storage': {'static_data_transformer': [{'OUTPUT_PORT': 'static_files', 'INPUT_PORT': 'static_data_input'}]}


}
