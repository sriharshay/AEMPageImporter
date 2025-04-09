# README
1. Install below packages
    ```
    pip install requests pandas openpyxl pyyaml bs4
    ```
2. Update the [config.yaml](config.yaml), if needed
3. Start the import process 
    ```
    python init_import.py config.yaml
    ```
4. Import process executes for the initial 5 entries from the excel. Update the 'data[:5]' in [init_import.py](init_import.py)
5. Excel file data is processed in [excel_data.py](excel_data.py)
4. If there is any issue in conncting to the microservice endpoint, troubleshoot [response_from_ms.py](response_from_ms.py) module.
7. Respense from the micro service endpoint is processed in [process_ms_response.py](process_ms_response.py) module.
8. Processed miscro service endpoint is fed to AEM in [create_pages.py](create_pages.py) module.
