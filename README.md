# Normalizeit

Normalizeit is a simple tool to normalize your data given an input schema and an output schema.

## Example
    ```
     python3 normalizeit.py normalize '{"helloworld" : "helloworld"}' --input-scheme='{"helloworld" : "%%key"}' --output-scheme='{"helloworld" : "%%key"}' --value-id-str="%%"
     ```

## Installation
    
        ```
        pip3 install -r requirements.txt
        ```
        
