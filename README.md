# README
1. Install python packages
    ```
    pip install requests pandas openpyxl pyyaml bs4
    ```
2. Update the [config.yaml](config.yaml), if needed update the [config_loader.py](config_loader.py)
3. Start the import process 
    ```
    python init_import.py 
    ```
4. Import process can be limited to only few excel entries with by updating the for loop 
   ``` data to 'data[:5]' ``` in [init_import.py](init_import.py)
5. Excel file data is processed in [excel_data.py](excel_data.py)
6. If there is any issue in conncting to the microservice endpoint, troubleshoot [response_from_ms.py](response_from_ms.py) module.
7. Respense from the micro service endpoint is validated in [process_ms_response.py](process_ms_response.py) module.
8. Validated miscro service endpoint response is fed to AEM [aem_connector.py](aem_connector.py) module.
